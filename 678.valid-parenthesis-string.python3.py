class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # DP top down solution
        # helper function is_valid returns true if s[i:j+1] is valid
        memo = {}
        left = '(*'
        right = '*)'
        def is_valid(i, j):
            # when two pointers cross, all previous examination passed return true
            if i > j: return True
            # When it's only one character it is a valid string only 
            # when the char is *
            if i == j: return s[i] == '*'
            key = (i, j)
            if key in memo: return memo[key]
            # Case 1: outer two char is valid, whole thing is valid as long
            # as inner is valid, like a russian doll
            if s[i] in left and s[j] in right and is_valid(i+1, j-1):
                memo[key] = True
                return True

            # Case 2: s[i:j+1] can be separated to segments each of them needs
            # to be valid
            # Notice this cannot be inclusive for j, otherwise infinite recursion
            for k in range(i, j):
                if is_valid(i, k) and is_valid(k+1, j):
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        if not len(s): return True
        return is_valid(0, len(s)-1)
