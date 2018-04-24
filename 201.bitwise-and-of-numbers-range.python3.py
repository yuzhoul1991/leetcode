class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m = 11001 n = 11110 then the result is 11000
        # we need to find the bits from MSB from m and n are the same
        def using_mask(m, n):
            mask = 0xffffffff
            while m & mask != n & mask:
                # shift the mask to left to remove the LSB
                mask <<= 1
            return m & mask
        
        def no_mask(m, n):
            count = 0
            while m != n:
                m >>= 1
                n >>= 1
                count += 1
            return m << count
        return no_mask(m, n)
