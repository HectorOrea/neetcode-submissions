class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            counter = [0] * 26
            for c in s:
                i = ord(c) - ord("a")
                counter[i] += 1
            k = tuple(counter)
            v = d.get(k, [])
            v.append(s)
            d[k] = v
        res = []
        for val in d.values():
            res.append(val)
        return res

        
        
        
        # d = dict()
        # for s in strs:
        #     a = "".join(sorted(s))
        #     l = d.get(a, [])
        #     l.append(s)
        #     d[a] = l
        
        # res = []
        # for val in d.values():
        #     res.append(val)
        # return res

        
    # Time: O(n*slogs)
    # Space: O(n)

    # 