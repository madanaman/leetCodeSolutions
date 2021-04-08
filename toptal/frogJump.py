import math
def solution(X, Y, D):
    # write your code in Python 3.6
    number_of_jumps = math.ceil((Y - X)/D)

    return number_of_jumps

print(solution(1, 5, 2))