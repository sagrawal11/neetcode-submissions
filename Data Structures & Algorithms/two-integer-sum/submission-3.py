class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # using enumerate, you can get both the index and the value
        for i, val in enumerate(nums):
            complement = target - val

            # now that we have the complement, if it exists in our dictionary
            # then we've found the sum
            if complement in seen:
                return [seen[complement], i]
            
            # if the complement isn't in the dictionary, add it
            seen[val] = i
        return []