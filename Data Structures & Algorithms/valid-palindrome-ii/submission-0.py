class Solution:
    def validPalindrome(self, s: str) -> bool:
        # let's start by formatting the string so we can parse it easier
        cleaned_s = [char.lower() for char in s if char.isalnum()]
        # print(cleaned_s)

        left = 0
        right = len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                # MISTMATCH
                check_left = cleaned_s[left+1 : right+1]
                check_right = cleaned_s[left : right]

                # now need to check if each check is a palindrome itself
                return check_left == check_left[::-1] or  check_right == check_right[::-1]

            left += 1
            right -= 1
        return True
        