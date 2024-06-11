def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    # Initialize a list to hold each line of the rangoli
    lines = []
    
    for i in range(size):
        # Create the pattern for the current line
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        # Center the pattern to the required width
        lines.append(s.center(4*size - 3, '-'))
    
    # Print the full rangoli by combining the top and bottom parts
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)