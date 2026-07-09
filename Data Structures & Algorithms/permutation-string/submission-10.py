class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # have a sliding window that is len(s1)
        # state map that tracks how many of each char are in our window
        # and we can check that these numbers match up the count of our target

        target_freq_map = {} # takes O(n) to generate for n = len(s1)
        for c in s1:
            target_freq_map[c] = target_freq_map.get(c, 0) + 1
      
        if len(s1) > len(s2):
            return False

        # init window and check if it's a solution
        window_freq_map = {}
        for c in s2[:len(s1)]:
            window_freq_map[c] = window_freq_map.get(c, 0) + 1
        if set(target_freq_map.items()) == set(window_freq_map.items()):
                return True

        l, r = 0, len(s1) - 1
        while (r < len(s2)):

            window = s2[l:r+1]
            # if (window == "ab"):
            #     print(target_freq_map.items())
            #     print(window_freq_map.items())

            if set(target_freq_map.items()) <= set(window_freq_map.items()):
                return True

            # shift window
            l += 1
            r += 1

            # update state
            window_freq_map[s2[l-1]] = window_freq_map.get(s2[l-1], 0) - 1
            if (r < len(s2)):
                 window_freq_map[s2[r]] = window_freq_map.get(s2[r], 0) + 1      
        return False


        