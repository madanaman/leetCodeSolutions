from collections import deque
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0 | len(nums) == 1:
            return len(nums)
        write_ptr = 0
        for curr_ptr in range(0, len(nums)):
            if nums[curr_ptr] != nums[write_ptr]:
                write_ptr += 1
                nums[write_ptr] = nums[curr_ptr]
        print(nums)
        return write_ptr + 1




def testing():
    solve = Solution()
    ip = [1, 1, 2]
    assert solve.removeDuplicates(ip) == 2
    print("test passed")
    ip = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert solve.removeDuplicates(ip) == 5
    print("test passed")

testing()
