class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Use divide and conquer otherwise it will timeout
        # calcuate tmp = myPow(x, n/2) first and the answer is tmp * tmp if n is even
        # otherwise is tmp * tmp * x since there is 1 remainder
        
        # terminal cases to terminate the recursion
        if n == 0: return 1 
        if n == 1: return x

        # In python -3//2 is -2 not -1 so it's better to always do this in positive numbers
        if n < 0: 
            n = -n
            x = 1.0/x
        temp = self.myPow(x, n//2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp
