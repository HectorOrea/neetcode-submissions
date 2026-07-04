class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1st soln) Make a histogram dict w num -> freq
        # Get (n, f) tuples and sort w respect to f
        # Get the first k
        # Time: O(n) + O(nlogn) + O(k) = O(nlogn)
        # Space: O(n) 

        # 2ns soln) Make freq list
        # Heapify to get max heap
        # Pop k times
        # Time: O(n) + O(k*logn) 
        # Space: O(n)
        # freq = defaultdict(int)
        # for n in nums:
        #     freq[n] += 1
        # h = [(-f, n) for (n, f) in freq.items()]
        # heapq.heapify(h)
        # res = []
        # for _ in range(k):
        #     f, n = heapq.heappop(h)
        #     res.append(n)
        # return res

        # 3rd soln)
        # Make empty heap and push everything from freq on there keeping it no 
        # bigger than k
        # Copy info from heap into a list we return
        # Time: O(n) + O(nlogk) + O((n - k) * logk) + O(n) = O(nlogk)
        # Space: O(n + k)
        # freq = defaultdict(int)
        # for n in nums:
        #     freq[n] += 1

        # h = []
        # for (n, f) in freq.items():
        #     heapq.heappush(h, (f, n))
        #     if len(h) > k:
        #         heapq.heappop(h)

        # res = []
        # for (f, n) in h:
        #     res.append(n)
        
        # return res

        # 4th soln)
        # make list freq where freq[i] is list of nums that appear i times
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for (n, f) in count.items():
            freq[f].append(n)
        
        print(freq)
        res = []
        i = len(nums)
        while len(res) < k:
            res.extend(freq[i])
            i -= 1
        return res[:k]
            
    # nums=[1,2,2,3,3,3]
    # count = {1 : 1, 2:2, 3:3}
    # freq = [[], [1], [2], [3]]
            

            




        

            


        
