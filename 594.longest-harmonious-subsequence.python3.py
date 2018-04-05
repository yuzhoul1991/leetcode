class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        ret = 0
        for digit, count in counter.items():
            if digit+1 in counter:
                ret = max(ret, count + counter[digit+1])
            if digit-1 in counter:
                ret = max(ret, count + counter[digit-1])
        return ret
        
