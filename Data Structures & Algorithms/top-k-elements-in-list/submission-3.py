class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make a histogram dict w num -> freq
        # Get (n, f) tuples and sort w respect to f
        # Get the first k
        # Time: O(n) + O(nlogn) + O(k) = O(n)
        # Space: O(n) 

        h = defaultdict(int)
        for n in nums:
            h[n] += 1
        l = []
        for (n, freq) in h.items():
            l.append((freq, n))
        res = []
        for (f, n) in sorted(l)[-k:]:
            res.append(n)
        return res

        # example: [1, 3, 1]

