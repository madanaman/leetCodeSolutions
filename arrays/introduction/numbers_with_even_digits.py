class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total_even_count = 0
        # if nums is None:
        #     return total_even_count
        for num in nums:
            if len(str(num)) % 2 == 0:
                total_even_count += 1
        return total_even_count