class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # construct graph and start with black color and all neibors with it should be
        # red color, keep labeling, if we found a neighbor with the same color as self
        # it is not bipartite

        graphs = {}
        n = len(graph)
        for idx, arr in enumerate(graph):
            graphs[idx] = arr

        visited = set()
        colors = {}
        def dfs(node):
            if node in visited: return True
            visited.add(node)
            color = colors[node]
            for nei in graphs[node]:
                if nei in colors and colors[nei] == color: return False
                colors[nei] = -color
                if not dfs(nei): return False
            return True

        for node in range(n):
            if node not in visited:
                if node not in colors: colors[node] = 1
                if not dfs(node): return False
        return True
