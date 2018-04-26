class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # If we minus then when dividend is large compared to divisor, it will be overtime
        # each time we shift divisor to left by 1 to multiply it by 2 until it is larger than dividend
        # minus it from the dividend, repeat the process
        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        while dividend >= divisor:
            temp = divisor << 1
            count = 0
            while dividend >= temp:
                temp <<= 1
                count += 1
            ret += 2**count
            if not is_negative and ret > 2**31 -1: 
                ret = 2**31 - 1
                break
            elif is_negative and ret > 2**31:
                ret = 2**31
                break
            dividend -= (temp >> 1)
        return ret if not is_negative else -ret
        
