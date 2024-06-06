import itertools

def calculate_probability_of_a(N, letters, K):
    # Generate all combinations of indices of length K
    indices = list(range(N))
    all_combinations = list(itertools.combinations(indices, K))
    
    count_combinations_with_a = 0
    
    # Check each combination
    for combination in all_combinations:
        if any(letters[i] == 'a' for i in combination):
            count_combinations_with_a += 1
    
    # Calculate total number of combinations
    total_combinations = len(all_combinations)
    
    # Calculate the probability
    probability = count_combinations_with_a / total_combinations
    
    # Print the result rounded to 3 decimal places
    print(f"{probability:.3f}")

if __name__ == '__main__':
    # Read input
    N = int(input().strip())
    letters = input().strip().split()
    K = int(input().strip())
    
    calculate_probability_of_a(N, letters, K)
