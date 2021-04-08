import itertools


class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []
        digit_map = {"2": ['a', 'b', 'c'],
                     "3": ['d', 'e', 'f'],
                     "4": ['g', 'h', 'i'],
                     "5": ['j', 'k', 'l'],
                     "6": ['m', 'n', 'o'],
                     "7": ['p', 'q', 'r', 's'],
                     "8": ['t', 'u', 'v'],
                     "9": ['w', 'x', 'y', 'z']
                     }
        str_digits = digits
        new_list = []
        for digit in str_digits:
            new_list.append(digit_map[digit])

        all_combinations = list(itertools.product(*new_list))
        final_list = []
        for comb in all_combinations:
            temp = ""
            for elem in comb:
                temp += elem
            final_list.append(temp)

        return final_list


solve = Solution()
print(solve.letterCombinations("23"))
