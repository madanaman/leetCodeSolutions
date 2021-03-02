class Solution:
    def replaceElements(self, arr):
        prev_max = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > prev_max:
                new_max = arr[i]
            else:
                new_max = prev_max
            arr[i] = prev_max
            prev_max = new_max
            # print(arr)
        # print("final array", arr)
        return arr



def testing():
    solve = Solution()
    ip = [17,18,5,4,6,1]
    assert solve.replaceElements(ip) == [18,6,6,6,1,-1]
    print('test passed')
    ip = [400]
    assert solve.replaceElements(ip) == [-1]
    print('test passed')

testing()