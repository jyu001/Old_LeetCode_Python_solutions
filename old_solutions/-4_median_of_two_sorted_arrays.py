"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1l = 0
        n1r = len(num1) - 1
        n2l = 0
        n2r = len(num2) - 1
        ans = 0
        plus1 = 0
        while n1r > n1l and n2r > n2l:
            i = (n1r + n1l)/2
            j = (n2r + n2l)/2
            m = min(i, j)/2
            if nums1[i] > nums2[j]:
                n1l = n1l - m
                n1r = i
                n2l = j
                n2r = j + m
            elif nums1[i] < nums2[j]:
                n1l = i
                n2r = j
            elif nums1[i] == nums2[j]:
                if len(nums1)%2 or len(nums2)%2:
                    return nums1[i]
                else: 
                    if i = len(nums1) - 1:
                        plus1 = nums2[j+1]
                    elif j = len(nums2) - 1:
                        plus1 = nums1[i+1]
                    return (nums[i] + plus1)/2
        if n1r == n1l:
            
                
                
        
        
        
        
solution = Solution()


nums1 = [1, 3]
nums2 = [2]
print solution.findMedianSortedArrays(nums1,nums2)


nums1 = [1, 2]
nums2 = [3, 4]
print solution.findMedianSortedArrays(nums1,nums2)
