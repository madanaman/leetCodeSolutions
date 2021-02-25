class Solution:
    # def duplicateZeros(self, arr):
    #     """
    #     Do not return anything, modify arr in-place instead.
    #     """
    #     new_array = arr
    #     arr = []
    #     i = 0
    #     while i < len(new_array):
    #         if len(arr) >= len(new_array):
    #             break
    #         if new_array[i] == 0:
    #             arr.append(0)
    #             arr.append(0)
    #         else:
    #             arr.append(new_array[i])
    #         i += 1
    #
    #     # arr = new_array
    #     print(arr)
    #     return arr
    # def duplicateZeros(self, arr):
    #     count_of_zeros = sum([1 if elem == 0 else 0 for elem in arr[0:len(arr) - 1]])
    #     print(count_of_zeros, "count of zeros")
    #     left_ptr = len(arr) - count_of_zeros - 1
    #     right_ptr = len(arr) - 1
    #     while left_ptr > 0:
    #         print("left pointer", left_ptr)
    #         print("right pointer", right_ptr)
    #         print("pre state", arr)
    #         if arr[left_ptr] == 0 and left_ptr == right_ptr and right_ptr == len(arr) - 1:
    #             print("inside first ")
    #             left_ptr -= 1
    #             right_ptr -= 1
    #         elif arr[left_ptr] == 0:
    #             print("inside second")
    #             arr[right_ptr] = 0
    #             arr[right_ptr - 1] = 0
    #             left_ptr -= 1
    #             right_ptr -= 2
    #         else:
    #             print("inside else")
    #             arr[right_ptr] = arr[left_ptr]
    #             left_ptr -= 1
    #             right_ptr -= 1
    #         print("post state", arr)
    #
    #     # print(arr)
    # def duplicateZeros(self, arr):
    #     right_pointer = len(arr) - 1
    #     final_length = len(arr)
    #     while right_pointer >= 0:
    #         if arr[right_pointer] == 0:
    #             arr = arr[0:right_pointer] + [0] + arr[right_pointer:final_length]
    #             # print(right_pointer, "temp", arr)
    #             arr = arr[:final_length]
    #             # print("final of the iteration", arr)
    #         right_pointer -= 1
    #     return arr
    def duplicateZeros(self, arr):
        # find actual array:
        # print("input", arr)
        final_length = len(arr)
        right_pointer = len(arr) - 1
        left_pointer = -1
        zero_found = 0
        ignore_last = False
        temp_len = 0
        for i in range(0, len(arr) - 1):
            if arr[i] == 0:
                zero_found += 1
                temp_len = temp_len + 1
                if temp_len >= final_length:
                    ignore_last = True
                if ignore_last is False:
                    arr[right_pointer] = ""
                right_pointer -= 1
            if arr[i] == "":
                break
            left_pointer += 1
            temp_len = temp_len + 1
        # print(arr, left_pointer)
        right_pointer = len(arr) - 1
        while left_pointer >= 0 and zero_found > 0:
            if arr[left_pointer] == 0 and ignore_last is False:
                arr[right_pointer] = 0
                arr[right_pointer - 1] = 0
                right_pointer -= 2
                left_pointer -= 1
            else:
                if ignore_last == True:
                    ignore_last = False
                arr[right_pointer] = arr[left_pointer]
                right_pointer -= 1
                left_pointer -= 1

        # print("final", arr)
        return arr

    # print(arr)


def test():
    ip1 = [0, 1, 7, 6, 0, 2, 0, 7]
    ip2 = [1, 0, 2, 3, 0, 4, 5, 0]
    ip3 = [1, 2, 3]
    ip4 = [8, 4, 5, 0, 0, 0, 0, 7]
    solve = Solution()
    # solve.duplicateZeros(ip1)
    # solve.duplicateZeros(ip3)
    assert solve.duplicateZeros(ip1) == [0, 0, 1, 7, 6, 0, 0, 2]
    print("test case passed")
    assert solve.duplicateZeros(ip2) == [1, 0, 0, 2, 3, 0, 0, 4]
    print("test case passed")
    assert solve.duplicateZeros(ip3) == [1, 2, 3]
    print("test case passed")
    assert solve.duplicateZeros(ip4) == [8, 4, 5, 0, 0, 0, 0, 0]
    print("test case passed")


# ip1 = [0, 1, 7, 6, 0, 2, 0, 7]
# ip2 = [1,0,2,3,0,4,5,0]
# solve = Solution()
# solve.duplicateZeros(ip)

# print(solve)
test()
