class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap,-num)
        else:
            heapq.heappush(self.minheap,num)
        if  len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-val)
        elif len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-val)

    def findMedian(self) -> float:
        if abs(len(self.maxheap)) > abs(len(self.minheap)):
            median = -self.maxheap[0]
        elif abs(len(self.maxheap)) < abs(len(self.minheap)):
            median = self.minheap[0]
        else:
            median = (-self.maxheap[0] + self.minheap[0]) / 2
        return median

        