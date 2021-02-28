"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough space
to hold additional elements from nums2.

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_write_pointer = len(nums1) - 1
        startm = m - 1
        startn = n - 1
        # print("input", nums1, nums2)
        while num1_write_pointer >= 0:
            # print("nums1", nums1, "nums2", nums2)
            # print(num1_write_pointer, startm, startn, nums1[startm], nums2[startn])
            if startm >= 0 and startn >= 0:
                if nums2[startn] >= nums1[startm]:
                    # print("inside first if")
                    nums1[num1_write_pointer] = nums2[startn]
                    startn -= 1
                else:
                    # print("inside else")
                    nums1[num1_write_pointer] = nums1[startm]
                    startm -= 1
            elif startm >= 0:
                break
            elif startn >= 0:
                nums1[num1_write_pointer] = nums2[startn]
                startn -= 1
            num1_write_pointer -= 1
        # print(nums1)
        return nums1


def testing():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solve = Solution()
    assert solve.merge(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]
    print("test successful")

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    assert solve.merge(nums1, m, nums2, n) == [1]
    print("test successful")


testing()


def test():
    pass


# ip1 = [0, 1, 7, 6, 0, 2, 0, 7]
# ip2 = [1,0,2,3,0,4,5,0]
# solve = Solution()
# solve.duplicateZeros(ip)

# print(solve)
test()
