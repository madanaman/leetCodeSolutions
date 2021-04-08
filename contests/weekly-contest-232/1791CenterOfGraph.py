class Solution:
    def findCenter(self, edges):
        n1, n2 = edges[0]
        if n1 in edges[1]:
            return n1
        else:
            return n2

solve = Solution()
assert solve.findCenter([[1,2],[2,3],[4,2]]) == 2
print("test passed")
assert solve.findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1
print("test passed")
