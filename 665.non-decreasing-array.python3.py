class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # when we encounter a violation, fix it by changing either one to the other
        # then compare against sorted array
        if not nums: return False
        if len(nums) == 1: return True
        n = len(nums)
        fix1 = nums[:]
        fix2 = nums[:]
        count = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                fix1[i-1] = fix1[i]
                fix2[i] = fix2[i-1]
                break
        return fix1 == sorted(fix1) or fix2 == sorted(fix2)
