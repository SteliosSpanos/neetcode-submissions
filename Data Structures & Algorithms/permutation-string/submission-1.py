class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1) - 1

        s1_dict = {}
        for c in s1:
            s1_dict[c] = 1 + s1_dict.get(c, 0)

        while j < len(s2):
            s2_dict = {}
            for c in s2[i:j+1]:
                s2_dict[c] = 1 + s2_dict.get(c, 0)

            if s2_dict == s1_dict:
                return True
            else:
                j += 1
                i += 1
        return False
        