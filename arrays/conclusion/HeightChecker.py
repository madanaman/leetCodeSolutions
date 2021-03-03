class Solution:
    def heightChecker(self, heights):
        new_heights = sorted(heights)
        diff_count = 0
        for i in range(0,len(heights)):
            if heights[i] != new_heights[i]:
                diff_count += 1
        return diff_count

def testing():
    solve = Solution()
    ip = [1,1,4,2,1,3]
    assert solve.heightChecker(ip) == 3
    print("test passed")
    assert solve.heightChecker([5,1,2,3,4]) == 5
    print("test passed")
    assert solve.heightChecker([1,2,3,4,5]) == 0
    print("test passed")

testing()