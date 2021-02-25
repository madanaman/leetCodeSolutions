class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_max_len_seq = 0
        curr_max_len_seq = 0
        for num in nums:
            if num == 1:
                curr_max_len_seq += 1
            else:
                if curr_max_len_seq > prev_max_len_seq:
                    prev_max_len_seq = curr_max_len_seq
                curr_max_len_seq = 0
        if curr_max_len_seq > prev_max_len_seq:
            prev_max_len_seq = curr_max_len_seq
        return prev_max_len_seq


