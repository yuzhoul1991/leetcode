#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (34.52%)
# Total Accepted:    70.1K
# Total Submissions: 203K
# Testcase Example:  '[]'
#
# Note: This is an extension of House Robber.
# 
# After robbing those houses on that street, the thief has found himself a new
# place for his thievery so that he will not get too much attention. This time,
# all houses at this place are arranged in a circle. That means the first house
# is the neighbor of the last one. Meanwhile, the security system for these
# houses remain the same as for those in the previous street. 
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # recursive solution with cache
        n = len(nums)
        cache = {}
        def helper(house_index, picked_first):
            if house_index == n-1:
                if picked_first: return 0
                else: return nums[house_index]
            if (house_index, picked_first) in cache: return cache[(house_index, picked_first)]
            if house_index + 2 < n:
                max_reward = max(helper(house_index+1, picked_first), nums[house_index] + helper(house_index+2, picked_first))
            else:
                max_reward = max(helper(house_index+1, picked_first), nums[house_index])
            cache[(house_index, picked_first)] = max_reward
            return max_reward
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(helper(0, True), helper(1, False))
        
"""
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.func = Solution().rob

    def test_empty(self):
        self.assertEqual(self.func([]), 0)

    def test_one(self):
        self.assertEqual(self.func([1]), 1)

    def test_two(self):
        self.assertEqual(self.func([1,2]), 2)
        
    def test_sanity(self):
        self.assertEqual(self.func([1,3,1]), 3)

    def test_lc_failed(self):
        self.assertEqual(self.func([2,7,9,3,1]), 11)

if __name__ == '__main__':
    unittest.main()

"""
