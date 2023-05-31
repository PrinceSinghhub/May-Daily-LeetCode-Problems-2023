class Solution(object):
    def findDifference(self, nums1, nums2):

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        temp = nums1.copy()

        for i in nums1:
            if i in nums2:
                temp.remove(i)
                nums2.remove(i)

        return [temp, nums2]
