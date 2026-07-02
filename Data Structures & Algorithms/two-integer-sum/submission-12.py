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
            return [min(i_prime, j_prime), max(i_prime, j_prime)]

        def are_valid(a, b):
            if a != b:
                return True
            else:
                return Counter(nums)[a] > 1

        s = set(nums)
        for num in s: # What happens when num = rest, 
            rest = target - num
            if rest in s and are_valid(num, rest):
                return get_indices(num, rest)

    # time: O(n)
    # space: O(n)