class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # If there is an answer then the answer substring must have a length that
        # is divisible of len(s)
        if not s: return True
        n = len(s)
        # Test every possible substring length from 2 to n//2
        for i in range(1, n//2+1):
            if n % i == 0:
                substr = s[:i]
                if s == substr * (n//i): return True
        return False
        
