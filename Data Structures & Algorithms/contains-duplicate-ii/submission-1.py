class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            # first check if the number is in the sliding window
            if nums[i] in window:
                return True
            
            # if it's not, then add it to the window
            window.add(nums[i])

            # if the window has grown larger than k, remove the first item
            if len(window) > k:
                window.remove(nums[i-k])
        return False

        # I didn't really know how to use sets for this one so I used AI