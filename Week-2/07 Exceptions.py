# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the input values
    a, b = input().split()
    try:
        # Try to perform integer division
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        # Handle ZeroDivisionError
        print("Error Code:", e)
    except ValueError as e:
        # Handle ValueError
        print("Error Code:", e)
