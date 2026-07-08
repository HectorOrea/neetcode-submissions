class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if n is the start of a seq
            if (n - 1) not in numSet:
                # when it is, get length of the sequence
                l = 0
                while (n + l) in numSet:
                    l += 1
                longest = max(longest, l)
        return longest


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


            

        