class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # For B to be in A, at most A need to be repeated
        # ceil(len(B) / len(A))
        # In case B is integer multiple of A, we need to add 1 to it
        most = math.ceil(len(B) / len(A)) + 1
        ret = 1
        for i in range(most):
            if B in A * (1+i):
                return ret
            ret += 1
        return -1
