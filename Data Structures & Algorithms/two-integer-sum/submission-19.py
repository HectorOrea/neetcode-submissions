class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        # forgot edge case of having same number
        # assumes a, b in nums 

        def get_indices(a, b):
            i_prime = 0
            j_prime = 0
            for i in range(len(nums)):
                if nums[i] == a:
                    i_prime = i
                    break
            for j in range(len(nums) - 1, 0, -1):
                if nums[j] == b:
                    j_prime = j
                    break
            if i_prime == j_prime:
                return [-1, -1]
            return [min(i_prime, j_prime), max(i_prime, j_prime)]

        s = set(nums)
        for num in s: # What happens when num = rest, 
            rest = target - num
            if rest in s:
                [i, j] = get_indices(num, rest)
                if i == -1:
                    continue
                return [i, j]

    # time: O(n)
    # space: O(n)