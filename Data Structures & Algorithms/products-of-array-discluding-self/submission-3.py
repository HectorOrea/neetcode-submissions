class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # assuming total product fits in 32 bit integer
        p = 1
        num_zeros, zi = 0, -1

        # Tracking num_zeros and returning when >1 zeros in nums
        for i, n in enumerate(nums):
            if n == 0 and zi == -1:
                zi = i
                num_zeros += 1
                continue
            elif n == 0 and zi != -1:
                res = [0] * len(nums)
                return res
            else:
                p *= n
        
        if num_zeros == 1:
            res = [0 for _ in range(len(nums))]
            res[zi] = p
            return res

        res = [0 for _ in range(len(nums))]
        for i, n in enumerate(nums):
            res[i] = p // n

        return res
        