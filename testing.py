import sys
from collections import defaultdict


def Solution(number):
    total_count = 0
    for i in range(0, len(number) - 1):
        print("loop i", i)
        j_ptr = i+1
        for j in range(j_ptr, len(number) - 1):
            # print("printing j", j)
            if int(number[i]) != int(number[j]):
                continue
            print("loop j", j)
            k_ptr=j+1
            for k in range(k_ptr, len(number) - 1):
                if int(number[i]) + 1 != int(number[k]):
                    continue
                print("loop k", k)
                l_ptr=k+1
                for l in range(l_ptr, len(number) - 1):
                    if int(number[k]) != int(number[l]):
                        continue
                    else:
                        print("loop l", l)
                        total_count += 1

    return total_count


line = sys.stdin.readline()
print(Solution(line))



