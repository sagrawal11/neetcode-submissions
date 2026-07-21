class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can go through the list and figure out all the anagrams
        # so we would order the characters in each word, then add them to a hashmap
        # this gives us all the anagrams
        # then, we can compare each element of the input array with the hashmap and see
        # at which indices the words are anagrams
        # from there we grab the indices whcih are anagrams and put them in lists, and
        # append that to a final larger list. 

        # There's a much more elegant way of doing this, shown below
        
        # defaultdict(list) automatically creates a new list if a key is missing
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
