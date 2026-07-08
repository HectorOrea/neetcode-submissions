class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make set and track smallest number (x0)
        # init max_len = 0
        # We can see if x0 + 1 in set
        #   if yes max_len += 1
        #   continue until not true
        # Then take another random one:
        #   check if +1 or -1 in set

        import random 

        ns = set(nums)
        max_len = 0
        cur_len = 0

        def check_up(x) -> int:
            res = 0
            while (x + 1) in ns:
                res += 1
                x += 1
            return res, x
        
        def check_down(x) -> int:
            res = 0
            while (x - 1) in ns:
                res +=1 
                x -= 1
            return res, x
                
        l = len(ns)
        while l > 0:
            n = next(iter(ns))

            # remove contiguous seq found
            # update max_len id necessary
            l = len(ns)
            a, A = check_down(n)
            b, B = check_up(n)
            cur_len = 1 + a + b
            if cur_len > max_len:
                max_len = cur_len
            for m in range(A, B + 1):
                ns.remove(m)
            l = len(ns)
        return max_len

        