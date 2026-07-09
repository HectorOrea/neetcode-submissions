class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # initialize matches for s1 and initial window. Return True if it's a solution
        s1count, win_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            win_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1count[i] == win_count[i]:
                matches += 1
        
        if matches == 26:
            return True

        for r in range(len(s1), len(s2)): # loop over 'next addition' to our window. The window at the end of this contains s2[r]
            
            l_remove = r - len(s1)

            # start computing the delta in matches
            affected = {s2[l_remove], s2[r]}
            matches_before = 0
            for c in affected:
                if win_count[ord(c) - ord('a')] == s1count[ord(c) - ord('a')]:
                    matches_before += 1
                    
            # update state for new window
            win_count[ord(s2[l_remove]) - ord('a')] -= 1
            win_count[ord(s2[r]) - ord('a')] += 1

            matches_after = 0
            for c in affected:
                if win_count[ord(c) - ord('a')] == s1count[ord(c) - ord('a')]:
                    matches_after += 1
            
            # update matches
            delta = matches_after - matches_before
            matches += delta
            
            # check if solution
            if matches == 26:
                return True
        return False
        
        


        