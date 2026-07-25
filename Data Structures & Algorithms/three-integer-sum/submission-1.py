class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3sum is just 2sum in disguise
        # since we're looking at summing to 0, we can reframe it as
        # nums[i] + nums[j] = -nums[k]

        final = []

        # we should first sort the array, that'll make things faster
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    final.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                if total < 0:
                    left += 1
                if total > 0:
                    right -= 1
        return final
