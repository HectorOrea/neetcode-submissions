class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        mp = {} 
        max_length = 0

        # O(26)
        def most_common_char():
            res, count = "", 0
            for (k, v) in mp.items():
                if v > count:
                    res = k
                    count = v
            return count

        for r in range(len(s)): # At the end of every iteration, [l, r) is valid
            chars_to_change = r - l - most_common_char()
            if chars_to_change <= k:
                mp[s[r]] = mp.get(s[r], 0) + 1
                r += 1
            while (r - l - most_common_char()) > k:
                mp[s[l]] = mp.get(s[l], 0) - 1
                l += 1
            max_length = max(max_length, r - l)
        return max_length


        