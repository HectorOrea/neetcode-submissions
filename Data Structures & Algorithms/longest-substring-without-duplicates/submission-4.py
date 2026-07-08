class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # (length, members, b) = elm
       # "ahoawceha" 
       # what if we tracked longest subseq that STARTS at a given char
       # [3, 6, 6, 5, ]
        if s == "":
            return 0
        l = 0
        max_length = 0
        max_subseqs = {}
        while (l + max_length - 1 < len(s)): # while we can have a string bigger than max_length start at l
           # compute max subseq len that starts at l

           # init as single seq
            max_subseqs[l] = 1
            seq_elms = set(s[l])

            # look ahead as far as we can
            r = l + 1
            seq_elms = set(s[l])
            while (r < len(s)):
                if s[r] in seq_elms:
                    break
                seq_elms.add(s[r])
                max_subseqs[l] += 1
                r += 1

            # update max_length 
            max_length = max(max_length, max_subseqs[l])      
            l += 1
        return max_length

