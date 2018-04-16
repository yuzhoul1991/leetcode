class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # This a tricky math problem
        # a/(b/c/d) == a/b * c * d
        # x1/x2/x3/x4/x5 no matter how you add parens, x1 will divide x2
        # then we need to make items starting with x3 to be multiplies instead of divide
        # So only one way to add parens x1/(x2/../x5) = x1/x2 * x3...*x5
        if not nums: return ""
        if len(nums) < 3: return "/".join(list(map(str, nums)))
        ret = []
        for idx, num in enumerate(nums):
            term = str(num)
            if idx == len(nums)-1:
                term += ')'
            else:
                term += '/'
            if idx == 0:
                term += '('
            ret.append(term)
        return "".join(ret)
