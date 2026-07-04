class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1st soln) Make a histogram dict w num -> freq
        # Get (n, f) tuples and sort w respect to f
        # Get the first k
        # Time: O(n) + O(nlogn) + O(k) = O(nlogn)
        # Space: O(n) 

        # Make freq list
        # Heapify to get max heap
        # Pop k times
        # Time: O(n) + O(k*logn) 
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        h = [(-f, n) for (n, f) in freq.items()]
        heapq.heapify(h)
        res = []
        for _ in range(k):
            f, n = heapq.heappop(h)
            res.append(n)
        return res




        

            


        
