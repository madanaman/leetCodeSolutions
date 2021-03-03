class Solution:
    def thirdMax(self, nums):
        nums = sorted(set(nums), reverse=True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]

def testing():
    solve = Solution()
    assert solve.thirdMax([3,2,1]) == 1
    print("test passed")
    assert solve.thirdMax([1,2]) == 2
    print("test passed")
    assert solve.thirdMax([2,2,3,1]) == 1
    print("test passed")

testing()