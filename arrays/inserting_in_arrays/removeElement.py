def removeElement(nums, val):
    lpointer = 0
    for rpointer in range(0, len(nums)):
        if nums[rpointer] == val:
            nums[rpointer], nums[lpointer] = nums[lpointer], nums[lpointer]
            lpointer += 1
        print(nums)
    return lpointer


def testing():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert removeElement(nums=nums, val=val) == 5
    print("pass")


testing()
