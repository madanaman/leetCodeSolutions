def solution(A):
    my_dict = {}
    for i in A:
        if i not in my_dict:
            my_dict[i] = i
        else:
            my_dict.pop(i)
    for key in my_dict.keys():
        return key

print(solution([9, 3, 9, 3, 9, 7, 9]))