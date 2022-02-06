# https://www.hackerrank.com/challenges/find-the-running-median/problem
# Solution: https://www.youtube.com/watch?v=VmogG01IjYc
import bisect
import heapq
import unittest

class Solution:
    
    def runningMedian(self,a):
        # Write your code 
        L = [] # arrays of median
        
        
        # 1st attempt with sort
        # run time error (failing some test cases)
        
        # subL = []
        # for i in range(len(a)):
            
        #     subL.append(a[i])
        #     subL.sort()
            
        #     midp = float((len(subL)))/2
            
        #     if len(subL) % 2 != 0:
        #         L.append(float(subL[int(midp)]))
        #     else:
        #         result = (subL[int(midp)] +  subL[int(midp-1)]) / 2
        #         L.append(float(result))
        # return L
        
        # 2nd attempt with Heap
        lower = [] # max_heap for lower numbers
        higher = [] # min_heap for higher numbers
        for i in range(len(a)):
            self.addtoHeap(a[i], lower, higher)
            
            self.rebalance(lower, higher)
            L.append(float(round(self.getMedian(lower,higher),1)))
            
        return L
    
    def addtoHeap(self,number,lower,higher):
        if not lower or number < -lower[0]:
            heapq.heappush(lower,-number)
        else:
            heapq.heappush(higher,number)
            

    def rebalance(self,lower,higher):
        if len(lower) - len(higher) >= 2:
            heapq.heappush(higher,-heapq.heappop(lower))
        elif len(higher) - len(lower) >= 2:
            heapq.heappush(lower,-heapq.heappop(higher))
            
    def getMedian(self,lower,higher):
        if len(lower) == len(higher): # heap with same length
            return (-lower[0] + higher[0]) / 2 # get average 
        if len(lower) > len(higher):
            return float(-lower[0])
        else:
            return float(higher[0])
        
        # 3rd solution using Bisect 
        # p = [] # new sorted list
        # l = 0 
        
        # for i in range(len(a)):
        #     l = l + 1
        #     bisect.insort(p,a[i])
        #     print(p)
        #     if(l % 2 == 1):
        #         print('Here')
        #         L.append(float(p[l//2]))
        #     else:
        #         L.append(float(p[l//2] + p[l//2-1])/2)
        # return L 

    
    
class testGetMedians(unittest.TestCase):
    listOfArrays = [
        ([12, 4, 5, 3, 8, 7],[12.0,8.0,5.0,4.5,5.0,6.0]),
        ([7, 3, 5, 2],[7.0,5.0,5.0,4.0])
    ]
    def testGetMedians(self):
        for i, expected in self.listOfArrays:
            actual = Solution().runningMedian(i)
            self.assertEqual(actual,expected)
        
if __name__ == '__main__':
    unittest.main()