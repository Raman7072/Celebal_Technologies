def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        decimal_representation = str(i).rjust(width)
        octal_representation = oct(i)[2:].rjust(width)
        hexadecimal_representation = hex(i)[2:].upper().rjust(width)
        binary_representation = bin(i)[2:].rjust(width)
        
        print(f"{decimal_representation} {octal_representation} {hexadecimal_representation} {binary_representation}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)