class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # have a sliding window that is len(s1)
        # Scan all contiguous substrings of s2 of that length and see if they are a permutation or not
        if len(s1) > len(s2):
            return False
        target = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i:i+len(s1)]
            if sorted(sub) == target:
                return True
        return False

        # Time: O(n^2logn) for n = len(s1)


        