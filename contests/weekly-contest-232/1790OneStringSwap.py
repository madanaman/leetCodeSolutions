class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        diff_count = 0
        prev_mismatched = []
        for i in range(0, len(s1)):
            if diff_count > 2:
                #more than one switch will be required
                return False
            if s1[i] != s2[i]:
                diff_count += 1
                prev_mismatched.append((s1[i], s2[i]))
        if len(prev_mismatched) == 2:
            k1, v1 = prev_mismatched[0]
            k2, v2 = prev_mismatched[1]
            if k1 == v2 and k2 == v1:
                return True
            else:
                return False
        else:
            return False

solve = Solution()
assert (solve.areAlmostEqual("abc", "def")) is False
print("test passed")
assert (solve.areAlmostEqual("bank", "kanb")) is True
print("test passed")
assert (solve.areAlmostEqual("attack", "defend")) is False
print("test passed")
assert (solve.areAlmostEqual("kelb", "kelb")) is True
print("test passed")
assert (solve.areAlmostEqual("abcd", "dcba")) is False
print("test passed")
assert (solve.areAlmostEqual("aa", "ac")) is False
print("test passed")