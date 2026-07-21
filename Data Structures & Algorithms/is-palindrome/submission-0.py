class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we could be given anything, and we only want alphanumerics
        # also it's easier to compare consistently when we lowercase and squish everything together
        cleaned_s = [char.lower() for char in s if char.isalnum()]
        
        # two pointers to go through the phrase
        left = 0
        right = len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
    
        return True