class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for idx, val in enumerate(nums):
            if target - val in num_map:
                return [num_map[target - val], idx]
            num_map[val] = idx
            
