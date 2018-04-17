class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 1. All Os on the boarder and the ones connected with them cannot be turned into X
        # 2. find all of them and mark as 'S'
        # 3. turn all O to X
        # 4. turn all S to O
        if not board: return 
        n, m = len(board), len(board[0])
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O': return
            board[i][j] = 'S'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for j in range(m):
            if board[0][j] == 'O': dfs(0, j)
            if board[n-1][j] == 'O': dfs(n-1, j)

        for i in range(n):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][m-1] == 'O': dfs(i, m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'S': board[i][j] = 'O'
