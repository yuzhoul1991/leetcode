class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # whenever see a 1, start using the dfs call to extrac the entire island
        # and increment self.cnt
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        seen = set()
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in seen or grid[i][j] != '1': return
            seen.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        ret = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == '1':
                    ret += 1
                    dfs(i, j)
        return ret

        
