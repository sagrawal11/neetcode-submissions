class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # I could use a map for this one. Basically, add everything to a 
        # map and then compare the size of the map to the size of the array
        # maps get rid of duplicates so if they're the same length, then no duplicates

        # or even better, I can count the number of items in each array and if
        # a count in the dictionary is larger than 1, immediately know it's true

        array_map = {}
        for num in nums:
            if num in array_map:
                array_map[num] += 1
            else:
                array_map[num] = 1
        
        for counts in array_map.values():
            if counts != 1:
                return True
        return False


