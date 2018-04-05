class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        if len(nums) == 1: return 0
        hsh = {}
        for idx, num in enumerate(nums): hsh[num] = idx
        nums.sort(reverse=True)
        if 2 * nums[1] <= nums[0]:
            return hsh[nums[0]]
        else:
            return -1

