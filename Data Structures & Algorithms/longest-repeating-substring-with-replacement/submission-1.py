class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # our two bounds
        left = 0
        counts = {} # this is our frequency map
        max_frequency = 0
        max_length = 0

        # now, let's add everything in this window to a dictionary
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_frequency = max(max_frequency, counts[s[right]])

            while (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length


