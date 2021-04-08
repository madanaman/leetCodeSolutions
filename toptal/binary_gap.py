def solution(N):
    bin_representation = bin(N).replace("0b", "")
    # print(bin_representation)
    longest_sequence = 0
    first_1 = False
    temp_sequence = 0
    for i in bin_representation:
        # print("staring", i, "first1", first_1)
        if int(i) == 1 and first_1 is False:
            # print("first_1 initialized")
            first_1 = True
        elif int(i) == 0 and first_1 is True:
            # print("temp sequence increased")
            temp_sequence += 1
        elif int(i) == 1 and first_1 is True:
            # print("figuring out if replacing or not")
            if temp_sequence >= longest_sequence:
                # print("temp replaced")
                longest_sequence = temp_sequence
            temp_sequence = 0
        # print(temp_sequence)
    return longest_sequence


assert solution(1041) == 5
print("test passed")
assert solution(9) == 2
print("test passed")
assert solution(529) == 4
print("test 3 passed")
assert solution(20) == 1
print("test 4 passed")
assert solution(15) == 0
print("test 5 passed")