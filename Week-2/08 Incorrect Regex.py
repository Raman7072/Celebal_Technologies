import re

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the string
    regex_str = input()
    
    try:
        # Attempt to compile the regex
        re.compile(regex_str)
        print("True")
    except re.error:
        # If compilation fails, print False
        print("False")
