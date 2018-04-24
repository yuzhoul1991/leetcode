class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # shift the number to right by 1 and xor with itself
        # all bits should be 1 
        # To test all bits 1, add 1 to the number and AND with itself
        # make sure result is 0
        xor = n ^ (n >> 1)
        return xor & (xor+1) == 0
        
