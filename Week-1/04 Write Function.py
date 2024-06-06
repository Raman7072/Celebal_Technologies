def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        # If year is divisible by 100, check further
        if year % 100 == 0:
            # If year is divisible by 400, it is a leap year
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            # If year is not divisible by 100, but divisible by 4, it is a leap year
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))