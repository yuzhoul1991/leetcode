class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Use DFS and keep a global visited for the outer loop
        # inside dfs function use a per dfs visited set. If during one dfs
        # next id is already in the per dfs visited set, it has a cycle
        graph = collections.defaultdict(list)
        for id, pre, in prerequisites:
            graph[id].append(pre)
        assert(len(graph) <= numCourses)
        visited = set()

        def dfs(id, current_visit):
            if id in visited: return True
            current_visit.add(id)
            visited.add(id)
            for next_id in graph[id]:
                if next_id in current_visit or not dfs(next_id, current_visit):
                    return False
            # Till here, we are sure from current id onward, there is no loop
            # so remove self id from the current_visit set
            current_visit.discard(id)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, set()):
                    return False
        return True


        
