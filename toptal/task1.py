import re


def solution(A, B, P):
    # write your code in Python 3.6
    regex_expr = r"*"+P+"*"
    # r = re.compile(regex_expr)
    newlist = []
    new_B = enumerate(B)
    # print(new_B)
    for idx, elem in new_B:
        print(elem)
        if re.search(regex_expr, elem):
            newlist.append(elem)  # Read Note
    if len(newlist) == 0:
        return "NO CONTACT"
    elif len(newlist) == 1:
        return A[newlist[0].split(",")[0]]
    elif len(newlist) > 1:
        names_list = []
        for i in range(0, len(newlist)):
            names_list.append(A[newlist[0].split(",")[0]])
        return min(names_list)

A = ['pim','pom']
B = ["999999999", "777888999"]
P = "88999"

print(solution(A, B, P))
