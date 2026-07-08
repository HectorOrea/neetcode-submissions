class Solution:    

    # for n len of strs, for m max(len(s))
    # Time: O(nm)
    # Space: O(nm)
    def encode(self, strs: List[str]) -> str:
        char_list = []
        for s in strs:
            if len(s) == 0:
                char_list.extend(["/", "e"])
                continue
            for c in s:
                if c == "/":
                    char_list.append("//")
                else:
                    char_list.append(c)
            char_list.extend(["/", "w"])
        res = "".join(char_list)
        print(res)
        return res

    # for n = len(s), m = len(max_word)
    # O(n)
    def decode(self, s: str) -> List[str]:
        res = []
        cur_word = []
        i = 0
        while i < len(s):
            if s[i] == "/":
                if i < len(s) - 1 and s[i+1] == "w":
                    res.append("".join(cur_word))
                    cur_word = []
                    i += 1
                elif i < len(s) - 1 and s[i+1] == "e":
                    res.append("")
                    i += 1
                    cur_word = []
                else: # i < len(s) - 1 and s[i+1] == "/"
                    cur_word.append("/")
                    i += 1
            else:
                cur_word.append(s[i])
            i += 1
        return res
