class Solution:
    def removeDuplicates(self, nums):
        num_set = list(set(nums))
        for i in range(0, len(num_set)):
            nums[i] = num_set[i]
        return len(num_set)