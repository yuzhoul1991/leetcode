class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Use divide and conquer, if index 0 and len(s)-1 is equal
        # then remove these two ends and test inner substring
        # Note cannot use recursion, otherwise it exceeds max recursive depth
        def range_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        for i in range(len(s)//2):
            # Notice how ~i gets the corresponding index on the other end
            if s[i] != s[~i]:
                j = len(s) -1 -i
                # try deleting from both ends 
                return range_palindrome(i+1, j) or range_palindrome(i, j-1)
        return True
