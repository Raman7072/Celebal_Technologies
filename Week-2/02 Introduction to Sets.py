def average(array):
    # Convert the list to a set to remove duplicates
    distinct_heights = set(array)
    # Compute the sum of distinct heights
    total_sum = sum(distinct_heights)
    # Compute the number of distinct heights
    number_of_distinct_heights = len(distinct_heights)
    # Calculate the average
    avg = total_sum / number_of_distinct_heights
    # Return the result rounded to 3 decimal places
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)