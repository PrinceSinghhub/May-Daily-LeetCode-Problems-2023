class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums = sorted(((b, a) for a, b in zip(nums1, nums2)), reverse=True)

        heap = [num[1] for num in nums[:k]]
        ksum = sum(heap)
        heapq.heapify(heap)

        maxResult = ksum * nums[k - 1][0]

        for num2, num1 in nums[k:]:
            ksum += num1 - heapq.heappushpop(heap, num1)

            maxResult = max(maxResult, ksum * num2)

        return maxResult