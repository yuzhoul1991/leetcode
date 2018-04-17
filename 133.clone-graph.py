# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        if not hasattr(self, 'hsh'):
            self.hsh = {}
        if node.label in self.hsh:
            return self.hsh[node.label]
        dup = UndirectedGraphNode(node.label)
        for neighbor in node.neighbors:
            if neighbor.label == node.label:
                dup.neighbors.append(dup)
            else:
                clone = self.cloneGraph(neighbor)
                self.hsh[neighbor.label] = clone
                dup.neighbors.append(clone)
        return dup
