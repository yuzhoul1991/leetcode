#
# [256] Paint House
#
# https://leetcode.com/problems/paint-house/description/
#
# algorithms
# Easy (46.37%)
# Total Accepted:    31.6K
# Total Submissions: 68.1K
# Testcase Example:  '[]'
#
# 
# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no two
# adjacent houses have the same color.
# 
# 
# The cost of painting each house with a certain color is represented by a n x
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and
# so on... Find the minimum cost to paint all houses.
# 
# 
# Note:
# All costs are positive integers.
#
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Recursive solution with cache
        if not costs: return 0
        n = len(costs)
        cache = {}
        def helper(house_index, color_index):
            #print(house_index, " ", color_index)
            if house_index == n: return 0
            if (house_index, color_index) in cache: return cache[(house_index, color_index)]
            color_index_next_house = [i for i in range(3) if i != color_index]
            min_cost = float('+inf')
            for color_idx in color_index_next_house:
                min_cost = min(min_cost, costs[house_index][color_index] + helper(house_index+1, color_idx))
            cache[(house_index, color_index)] = min_cost
            return min_cost 
        return min([helper(0, i) for i in range(3)])

"""
import unittest

class TestMinCost(unittest.TestCase):
    def setUp(self):
        self.func = Solution()
        self.empty_input = []
        self.regular_inputs = [
            [[2, 2, 3],
            [2, 0, 3]]
        ]
        self.answers = [2]

    def test_empty_input(self):
        self.assertEqual(self.func.minCost(self.empty_input), 0)

    def test_reg_input(self):
        for i, stimulus in enumerate(self.regular_inputs):
            answer = self.answers[i]
            self.assertEqual(self.func.minCost(stimulus), answer)
        

if __name__ == '__main__':
    unittest.main()

"""
