import re
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first_half = s[:int(len(s)/2)]
        second_half = s[int(len(s)/2):]
        vowels = "aeiou"
        no_of_vowels_1 = sum([1 for elem in first_half.lower() if elem in vowels])
        no_of_vowels_2 = sum([1 for elem in second_half.lower() if elem in vowels])
        if no_of_vowels_1 == no_of_vowels_2:
            return True
        else:
            return False

# solve = Solution()
# assert solve.halvesAreAlike('book') is True
# print('test1 passed') 
# assert solve.halvesAreAlike('textbook') is False
# print('test2 passed')
# assert solve.halvesAreAlike('MerryChristmas') is False
# print('test3 passed')
# assert solve.halvesAreAlike('AbCdEfGh') is True
# print('test4 passed')
