class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # For each bit of the 32 bit, count the number of numbers in nums
        # that has 1 in that position if there are k number and total is n
        # then the contribution to the total hamming distance is k*(n-k)
        ret = 0
        n = len(nums)
        for i in range(32):
            k = sum(1 for num in nums if num&(1<<i))
            ret += k * (n-k)
        return ret
