class Solution:
    def sortByParity(self, nums):
        lpointer = 0
        for rpointer in range(0, len(nums)):
            if nums[rpointer] % 2 == 0:
                nums[lpointer], nums[rpointer] = nums[rpointer], nums[lpointer]
                lpointer += 1
        return nums

def testing():
    solve = Solution()
    ip = [3,1,2,4]
    assert solve.sortByParity(ip) == [2,4,3,1]
    print("test successful")

testing()