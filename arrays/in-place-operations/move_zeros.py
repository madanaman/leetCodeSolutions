class Solution:
    def moveZeroes(self, nums):
        write_pointer = 0
        for read_pointer in range(0, len(nums)):
            if nums[read_pointer] != 0:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        # print("updated nums ", nums, "write pointer", write_pointer)
        for i in range(write_pointer, len(nums)):
            nums[i] = 0

        # print("final nums", nums)
        return nums


def testing():
    solve = Solution()
    ip = [0, 1, 0, 3, 12]
    assert solve.moveZeroes(ip) == [1,3,12,0,0]
    print("test passed")

testing()
