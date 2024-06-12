def task(s, arr):
    for case in arr:
        if case[0] == "pop":
            s.discard(next(iter(s)))
        elif case[0] == "remove" or case[0] == "discard":
            s.discard(int(case[1]))
        else:
            continue
    return sum(s)

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    arr = []
    cases = int(input())
    for _ in range(cases):
        arr.append(list(input().split()))
    result = task(s, arr)
    print(result)