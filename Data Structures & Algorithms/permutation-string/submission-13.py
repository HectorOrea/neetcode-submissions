class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_freq_map = {chr(ord('a') + i): 0 for i in range(26)}
        for c in s1:
            target_freq_map[c] += 1

        window_freq_map = {chr(ord('a') + i): 0 for i in range(26)}        
        for c in s2[:len(s1)]:
            window_freq_map[c] += 1

        if target_freq_map == window_freq_map:
                return True

        l, r = 0, len(s1)
        while (r < len(s2)): # New window will include s2[r]

            # shift window and update state
            window_freq_map[s2[l]] -= 1
            l += 1

            window_freq_map[s2[r]] += 1
            r += 1

            # check validity of new window
            if target_freq_map == window_freq_map:
                return True
        return False


        