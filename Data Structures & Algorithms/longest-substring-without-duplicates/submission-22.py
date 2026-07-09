class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # oawhoaibwuiii
        max_length = 0
        cur_length = 0
        l = 0
        r = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                seen.remove(s[l])
                l += 1
                cur_length -= 1
        return max_length
            

            
        


