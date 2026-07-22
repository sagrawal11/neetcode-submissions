class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # first we need to determine which string is shorter
        # that way we can iterate between the two that many times
        output = ''
        if len(word1) < len(word2):
            length = len(word1)
        else:
            length = len(word2)

        # print(length)
        for i in range(length):
            output += word1[i]
            output += word2[i]
        
        if len(word1) < len(word2):
            output += word2[length::]
        else: 
            output += word1[length::]

        return output