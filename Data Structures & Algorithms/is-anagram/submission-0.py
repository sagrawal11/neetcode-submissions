class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        # print(s_sorted)
        # print(t_sorted)

        s_map = {}
        t_map = {}

        for char in s_sorted:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1

        for char in t_sorted:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1

        # print(s_map)
        # print(t_map)

        # now we need to compare our maps
        if s_map == t_map:
            return True
        return False




