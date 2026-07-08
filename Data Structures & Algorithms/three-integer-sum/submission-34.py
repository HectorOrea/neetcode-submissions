class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        # is O(n)
        sorted_nums = sorted(nums) # nlogn
        def twoSum(i, target): # returns list of lists of non-duplicate indices
            res = []
            l = i + 1
            r = len(sorted_nums) - 1
            while (l < r):
                L = sorted_nums[l]
                R = sorted_nums[r]
                if (L + R < target):
                    l += 1
                elif (L + R > target):
                    r -= 1
                else: # l+r==target
                    res.append([L, R])
                    print((i, l, r))
                    # update to avoid duplicate triplets
                    while l < r and L == sorted_nums[l]:
                        l += 1
            return res
                    
        res = []
        i = 0
        while i < len(sorted_nums) - 1:
            n = sorted_nums[i]
            tuples = twoSum(i, -n)
            for t in tuples:
                [b, c] = t
                res.append([n, b, c])
            while (i < len(sorted_nums) - 1 and n == sorted_nums[i]):
                i += 1
        return res
        