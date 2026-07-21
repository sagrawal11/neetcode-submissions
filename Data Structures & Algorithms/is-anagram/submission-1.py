class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # originally I had sorted the two strings but that's not needed
        # since == compares the maps keys and values automatically, we 
        # don't need the map to be in order per say, so no sorting needed

        s_map = {}
        t_map = {}

        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1

        for char in t:
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




