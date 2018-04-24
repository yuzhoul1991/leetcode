class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # fill the result number by taking 1 bit from LSB of n and shift left
        # then shift n to right for next bit
        ret = 0
        for _ in range(32):
            ret = (ret << 1) | (n & 1)
            n >>= 1
        return ret
        
