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

        # color can be used as visited too
        colors = {}
        for node in range(n):
            if node not in colors:
                stack = [node]
                colors[node] = 1
                while stack:
                    node = stack.pop()
                    for nei in graphs[node]:
                        if nei not in colors:
                            stack.append(nei)
                            colors[nei] = -colors[node]
                        elif colors[nei] == colors[node]:
                            return False
        return True

