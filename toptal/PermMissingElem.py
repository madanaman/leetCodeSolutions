def solution(A):
    # write your code in Python 3.6
    sorted_array = sorted(A)
    if len(A) == 0:
        return 1

    for i in range(0, len(A)):
        if sorted_array[i] != i + 1:
            return i + 1

    return len(A)+1

assert solution([]) == 1
print("test 1 passed")
assert solution([2,3]) == 1
print('test 2 passed')
print(solution([1]))
print('test 3 passed')