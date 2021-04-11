from collections import deque


class Solution:
    def prepare_order_map(self, order) -> dict:
        i = 0
        order_map = {}
        for alphabet in order:
            order_map[alphabet] = i
            i += 1
        return order_map

    def isAlienSorted(self, words, order: str) -> bool:
        order_map = self.prepare_order_map(order)
        words_queue = deque(words)
        prev = words_queue.popleft()
        while words_queue:
            new_elem = words_queue.popleft()
            for i in range(len(prev)):
                if i < len(new_elem) and order_map[prev[i]] > order_map[new_elem[i]]:
                    # print("broke because failed order reference", prev[i], new_elem[i])
                    return False
                if i < len(new_elem) and order_map[prev[i]] < order_map[new_elem[i]]:
                    # print("passed order reference", prev[i], new_elem[i])
                    if len(words_queue) == 0:
                        return True
                    else:
                        prev = new_elem
                        continue

            if len(prev) > len(new_elem):
                # print("broke because of length")
                return False
            prev = new_elem

        return True


# solve = Solution()
# assert solve.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") is True
# print("test1 passed")
# assert solve.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz") is False
# print("test2 passed")
# assert solve.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz") is False
# print("test3 passed")
# assert solve.isAlienSorted(words=["apple"], order="abcdefghijklmnopqrstuvwxyz") is True
# print("test4 passed")
# assert solve.isAlienSorted(words=["kuvp","q"], order="ngxlkthsjuoqcpavbfdermiywz") is True
# print("test5 passed")
# assert solve.isAlienSorted(words=["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
#                            , order="zkgwaverfimqxbnctdplsjyohu") is False
# print("test6 passed")
