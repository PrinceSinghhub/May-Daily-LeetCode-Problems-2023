class Solution:
    def arraySign(self, nums):

        prod = 1
        for i in nums:
            prod *= i

        if prod > 0:
            return 1

        if prod < 0:
            return -1
        return 0


