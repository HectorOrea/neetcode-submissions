class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # go through our set
        # do set membership to see how high up and down we can go
        # remove these members and repeat until the list is empty


    # Time: O(n) + O(n) + O(n)
    # Space: O(n)

        # ns = set(nums)
        # max_len = 0
        # cur_len = 0

        # def check_up(x) -> int:
        #     res = 0
        #     while (x + 1) in ns:
        #         res += 1
        #         x += 1
        #     return res, x
        
        # def check_down(x) -> int:
        #     res = 0
        #     while (x - 1) in ns:
        #         res +=1 
        #         x -= 1
        #     return res, x
                
        # l = len(ns)
        # while l > 0:
        #     n = next(iter(ns))

        #     # remove contiguous seq found
        #     # update max_len id necessary
        #     l = len(ns)
        #     a, A = check_down(n)
        #     b, B = check_up(n)
        #     cur_len = 1 + a + b
        #     if cur_len > max_len:
        #         max_len = cur_len
        #     for m in range(A, B + 1):
        #         ns.remove(m)
        #     l = len(ns)
        # return max_len

        # Soln 2)
        # Make the set, iterate through and make the seq. beginnings keys to a dict
        ns = set(nums)
        seqs = set()
        for n in ns:
            if (n-1) not in ns:
                seqs.add(n)

        max_len = 0
        for k in seqs:
            cur_len = 1
            while (k + 1) in ns:
                k += 1
                cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len

            

        