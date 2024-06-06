import sys

def encode_string(S):
    result = []
    count = 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            result.append((count, int(S[i - 1])))
            count = 1
    result.append((count, int(S[-1])))  # Adding the last character
    return result

# Read input from STDIN
S = sys.stdin.readline().strip()

# Encode the string
encoded_string = encode_string(S)

# Output
output = ' '.join(['({}, {})'.format(count, char) for count, char in encoded_string])
print(output)
