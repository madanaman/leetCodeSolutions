from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    my_deque = deque(A)
    for i in range(K):
        elem = my_deque.pop()
        my_deque.appendleft(elem)

    return list(my_deque)