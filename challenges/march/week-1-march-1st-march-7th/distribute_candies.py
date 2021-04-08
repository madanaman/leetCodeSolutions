class Solution:
    def distributeCandies(self, candyType):
        distinct_candies = len(set(candyType))
        candies_can_be_eaten = int(len(candyType)/2)
        if distinct_candies <= candies_can_be_eaten:
            return distinct_candies
        else:
            return candies_can_be_eaten




solve = Solution()
assert solve.distributeCandies([1,1,2,2,3,3]) == 3
print("test passed")
assert solve.distributeCandies([1,1,2,3]) == 2
print("test passed")
assert solve.distributeCandies([6,6,6,6]) == 1
print("test passed")
