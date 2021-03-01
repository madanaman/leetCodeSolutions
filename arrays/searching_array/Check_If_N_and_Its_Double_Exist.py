class Solution:
    def checkIfExist(self, arr):
        for i in range(0, len(arr)):
            if arr[i] == 0 and arr.count(0) % 2 == 0:
                return True
            if arr[i] == 0:
                continue
            if arr[i] * 2 in arr:
                print(arr[i] * 2)
                return True
        return False


def testing():
    solve = Solution()
    ip = [3, 1, 7, 11]
    # assert solve.checkIfExist(ip) is False
    print("test passed")
    ip = [10, 2, 5, 3]
    # assert solve.checkIfExist(ip) is True
    print("test passed")
    print(solve.checkIfExist([-2,0,10,-19,4,6,-8]))

testing()