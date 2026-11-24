class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        window_dict = {}
        
        for i in range(len(s1)):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)
            window_dict[s2[i]] = 1 + window_dict.get(s2[i], 0)
        
        if s1_dict == window_dict:
            return True

        i = 0
        for j in range(len(s1), len(s2)):
            incoming_char = s2[j]
            window_dict[incoming_char] = 1 + window_dict.get(incoming_char, 0)

            outgoing_char = s2[i]
            window_dict[outgoing_char] -= 1

            if window_dict[outgoing_char] == 0:
                del window_dict[outgoing_char]

            i += 1

            if s1_dict == window_dict:
                return True
        return False
        