class Solution:
    def replaceFirstNonValElement(self, val, current_pointer, nums):
        elem_found = False
        found_idx = -1
        for i in range(current_pointer + 1, len(nums)):
            if nums[i] == -1000:
                continue

            if nums[i] != val:
                elem_found = True
                found_idx = i
                break
        if elem_found:
            return found_idx
        else:
            return current_pointer

    def removeElement1(self, nums, val):
        print(nums)
        newLegth = 0
        for i in range(0, len(nums)):
            print("running for idx", i)
            if nums[i] == val:
                idx = self.replaceFirstNonValElement(val, i, nums)
                print("will be replacing", nums[i], "with index", idx, "value ", nums[idx])
                nums[i] = nums[idx]
                nums[idx] = -1000
                print("new nums", nums, "new lenght", newLegth)
                continue
            if nums[i] == -1000:
                idx = self.replaceFirstNonValElement(val, i, nums)
                print("will be replacing", nums[i], "with index", idx, "value ", nums[idx])
                nums[i] = nums[idx]
                nums[idx] = -1000
            newLegth += 1
            print("new nums", nums, "new lenght", newLegth)
        return newLegth

    def removeElement(self, nums, val):
        # print(nums)
        newLegth = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums.remove(nums[i])
                continue
            newLegth += 1

        return newLegth


def testing():
    solve = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    # assert solve.removeElement(nums, val) == 2
    print("test passed")

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert solve.removeElement(nums, val) == 5
    print("test passed")


testing()
