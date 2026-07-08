class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pres = [1 for _ in range(n)]
        pre_p = 1
        for i in range(len(nums)):
            if i == 0:
                pres[i] = 1
                continue
            pre_p *= nums[i-1]
            pres[i] = pre_p
        
        posts = [1 for _ in range(n)]
        post_p = 1
        for i in range(n-1, -1, -1):
            if i == n-1:
                posts[i] = 1
                continue
            post_p *= nums[i + 1] # the one after
            posts[i] = post_p
        print(pres)
        print(posts)
        res = [pres[i] * posts[i] for i in range(n)]
        return res


    
        