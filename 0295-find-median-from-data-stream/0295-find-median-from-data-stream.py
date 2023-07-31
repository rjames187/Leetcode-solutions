from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.smaller = [] # max heap
        self.larger = [] # min heap
        

    def addNum(self, num: int) -> None:
        if self.larger and self.larger[0] > num:
            heappush(self.smaller, -num)
        else:
            heappush(self.larger, num)
        self.balance()
            
    def balance(self):
        if len(self.larger) > len(self.smaller) + 1:
            val = heappop(self.larger)
            heappush(self.smaller, -val)
        elif len(self.smaller) > len(self.larger) + 1:
            val = -heappop(self.smaller)
            heappush(self.larger, val)

    def findMedian(self) -> float:
        small = -self.smaller[0] if self.smaller else None
        large = self.larger[0] if self.larger else None
        if len(self.larger) > len(self.smaller):
            return large
        elif len(self.smaller) > len(self.larger):
            return small
        else:
            return (large + small) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()