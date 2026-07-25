class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        substring = set()
        left = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(s[i])
            max_count = max(max_count, i - left + 1)

        return max_count
