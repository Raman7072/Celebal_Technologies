from collections import Counter

# Read inputs
X = int(input())
shoe_sizes = Counter(map(int, input().split()))
N = int(input())

# Initialize total earnings
total_earnings = 0

# Process each customer
for _ in range(N):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        total_earnings += price
        shoe_sizes[size] -= 1

# Print total earnings
print(total_earnings)
