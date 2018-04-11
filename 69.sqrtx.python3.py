class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Use binary search to locate the answer
        if x == 0: return 0
        left, right = 1, x
        while left <= right:
            mid = left + (right - left)//2
            square = mid * mid
            if square == x: return mid
            if square > x: right = mid - 1
            else: 
                if (mid+1) * (mid+1) > x: return mid
                else: left = mid + 1
        

