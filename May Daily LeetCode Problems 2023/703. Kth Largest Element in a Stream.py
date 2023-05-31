import heapq


class KthLargest:

    def __init__(self, k, nums):

        self.heap = []
        self.k = k

        for i in nums:
            heapq.heappush(self.heap, i)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val):

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

    # Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)