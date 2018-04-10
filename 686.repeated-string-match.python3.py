class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if any(x not in A for x in B): return -1
        if B in A: return 1
        ret = 1
        string = A
        while len(string) <= 2 * len(B):
            string += A
            ret += 1
            if B in string: return ret
        return -1
        
