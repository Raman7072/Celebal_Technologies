To implement **Slowly Changing Dimension (SCD) Type-2** on the `CustomerDim` table, we need to create a trigger that handles inserts by updating the existing records and inserting new ones with the correct start and end dates. Here’s how you can create the `trg_dim` trigger in SQL Server:
## 1. Create the Trigger

```
%sql
CREATE TRIGGER trg_dim
ON CustomerDim
INSTEAD OF INSERT
AS
BEGIN
    -- Declare variables to store current and new dates
    DECLARE @CurrentDate DATE = CAST(GETDATE() AS DATE);

    -- Iterate over the inserted rows
    DECLARE @CustomerID INT, @CustomerName NVARCHAR(100), @Address NVARCHAR(255);

    DECLARE insert_cursor CURSOR FOR 
    SELECT CustomerID, CustomerName, Address
    FROM inserted;

    OPEN insert_cursor;

    FETCH NEXT FROM insert_cursor INTO @CustomerID, @CustomerName, @Address;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Check if a record with the same CustomerID already exists and is current
        IF EXISTS (SELECT 1 FROM CustomerDim WHERE CustomerID = @CustomerID AND IsCurrent = 1)
        BEGIN
            -- Update the existing current record to set it as historical
            UPDATE CustomerDim
            SET EffectiveEndDate = DATEADD(DAY, -1, @CurrentDate), IsCurrent = 0
            WHERE CustomerID = @CustomerID AND IsCurrent = 1;
        END

        -- Insert the new record as the current record
        INSERT INTO CustomerDim (CustomerID, CustomerName, Address, EffectiveStartDate, EffectiveEndDate, IsCurrent)
        VALUES (@CustomerID, @CustomerName, @Address, @CurrentDate, '9999-12-31', 1);

        FETCH NEXT FROM insert_cursor INTO @CustomerID, @CustomerName, @Address;
    END;

    CLOSE insert_cursor;
    DEALLOCATE insert_cursor;
END;
GO
```

## 2. Insert the New Records

Now,
when you insert new records into the `CustomerDim` table, the trigger will automatically handle the *SCD Type-2* logic:

```
%sql
INSERT INTO CustomerDim (CustomerID, CustomerName, Address)
VALUES
    (1, 'John Doe', 'Ajmer'),
    (4, 'David Richard', 'Mumbai'),
    (3, 'Bob Smith', 'Chennai'),
    (5, 'Eva Dsouza', 'Mumbai');
```

## Expected Output
After running the insert statements, the `CustomerDim` table will look like this:

```
 ______________________________________________________________________________________________
| CustomerID | CustomerName  | Address     | EffectiveStartDate | EffectiveEndDate | IsCurrent |
|------------|---------------|-------------|--------------------|------------------|-----------|
| 1          | John Doe      | 123 Main St | 2023-01-01         | 2023-09-10       | 0         |
| 1          | John Doe      | Ajmer       | 2023-09-11         | 9999-12-31       | 1         |
| 2          | Alice Johnson | 456 Elm St  | 2023-01-01         | 9999-12-31       | 1         |
| 3          | Bob Smith     | 789 Oak St  | 2023-01-01         | 2023-09-10       | 0         |
| 3          | Bob Smith     | Chennai     | 2023-09-11         | 9999-12-31       | 1         |
| 4          | David Richard | Mumbai      | 2023-09-11         | 9999-12-31       | 1         |
| 5          | Eva Dsouza    | Mumbai      | 2023-09-11         | 9999-12-31       | 1         |
```
<sup>______________________________________________________________________</sup>
