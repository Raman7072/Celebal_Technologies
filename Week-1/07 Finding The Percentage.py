if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    
    # Calculate the average of the queried student's marks
    query_scores = student_marks[query_name]
    average_score = sum(query_scores) / len(query_scores)
    
    # Print the average score rounded to 2 decimal places
    print(f"{average_score:.2f}")
