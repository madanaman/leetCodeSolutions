class Solution:
    def twoSum(self, nums, target):
        diff_dict = {}  # value: Index
        for key, value in enumerate(nums):
            if target - value in diff_dict.keys():
                return [diff_dict[target - value], key]
            else:
                diff_dict[value] = key
            print(diff_dict)
        return False


def testing():
    solve = Solution()
    assert solve.twoSum([3, 3], 6) == [0, 1]
    print("test passed")
    assert solve.twoSum([2,7,11,15], 9) == [0, 1]
    print("test passed")


testing()