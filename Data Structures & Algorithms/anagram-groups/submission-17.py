class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            a = "".join(sorted(s))
            l = d.get(a, [])
            l.append(s)
            d[a] = l
        
        res = []
        for val in d.values():
            res.append(val)
        return res

        
    # we can map everything to it's sorted version
    # Store those maps in hashmaps
    # more particularly an array