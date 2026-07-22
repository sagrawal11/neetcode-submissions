class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # so we will build this from the back, starting from nums1[m] and nums2[n]
        # at each point we'll compare the element at nums2 and nums1. Whichever is larger
        # we'll put in the next available slot and then increment that array one down as we grab from it

        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
        
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1

  


