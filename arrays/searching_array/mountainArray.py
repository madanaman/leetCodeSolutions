class Solution:
    def validMountainArray(self, arr):
        current_flow = "inc"
        previous_flow = []
        prev_elem = -1000000
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False
        for elem in arr:
            if current_flow == 'inc' and elem > prev_elem:
                prev_elem = elem
            elif current_flow == 'inc' and elem < prev_elem:
                previous_flow.append(current_flow)
                current_flow = 'dec'
                prev_elem = elem
            elif current_flow == 'inc' and elem == prev_elem:
                return False
            elif current_flow == 'dec' and elem >= prev_elem:
                return False
            else:
                prev_elem = elem
        if current_flow == 'inc':
            return False
        if len(previous_flow) == 0:
            return False
        return True


def testing():
    solve = Solution()
    ip = [2, 1]
    assert solve.validMountainArray(ip) is False
    print('test1 passed')
    ip = [3, 5, 5]
    assert solve.validMountainArray(ip) is False
    print('test2 passed')
    ip = [0, 3, 2, 1]
    assert solve.validMountainArray(ip) is True
    print('test3 passed')
    ip = [0, 3, 2, 1]
    assert solve.validMountainArray(ip) is True
    print('test4 passed')
    ip = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert solve.validMountainArray(ip) is False
    print('test5 passed')


testing()
