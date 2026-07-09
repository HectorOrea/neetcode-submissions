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


        l, r = 0, len(s1) - 1
        while (r < len(s2)):

            # check if it's a valid solution
            if target_freq_map == window_freq_map:
                return True

            # shift window
            l += 1
            r += 1

            # update state
            window_freq_map[s2[l-1]] -= 1
            if (r < len(s2)): # be careful to not do an index error
                 window_freq_map[s2[r]] += 1      
        return False


        