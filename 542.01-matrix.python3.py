class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        n, m = len(matrix), len(matrix[0])
        # Use dp to do two pass to solve the problem
        # the first pass updates from top left to bottom right, the 2nd pass is the reverse
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: continue
                num = float('+inf')
                if i > 0:
                    num = min(num, matrix[i-1][j]+1)
                if j > 0:
                    num = min(num, matrix[i][j-1]+1)
                matrix[i][j] = num

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if matrix[i][j] == 0: continue
                # Notice on the 2nd round, num cannot be +inf because we are only doing a partial update, ie. only looking at proceeding elements, should not overwrite the results of previous round
                num = matrix[i][j]
                if i+1 < n:
                    num = min(num, matrix[i+1][j]+1)
                if j+1 < m:
                    num = min(num, matrix[i][j+1]+1)
                matrix[i][j] = num
        return matrix
