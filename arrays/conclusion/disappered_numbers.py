class Solution:
    def findDisappearedNumbers(self, nums):
        arr = set(range(1, len(nums) + 1))
        for num in nums:
            if num in arr:
                arr.remove(num)
        return list(arr)

def testing():
    solve = Solution()
    assert solve.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
    print("test passed")

testing()