class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        d = dict()
        for (i, n) in enumerate(nums):
            if n in d:
                return [d[n], i]
            d[target - n] = i
        return [-1, -1]
            

        # for each num, we want to see if the target is in the array
        # for each num, we can check if it's in our hashmap and if not
        # add the complement to the array. Then if we come across a num
        # that IS in our hashmap, it's a complement