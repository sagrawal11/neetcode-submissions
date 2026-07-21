class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # it's my understanding that O(1) extra memory means I can't just 
        # create a new array and traverse through the initial one backward
        # and then set that one equal to s, I have to do it another way

        # let's do this with two pointers
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        