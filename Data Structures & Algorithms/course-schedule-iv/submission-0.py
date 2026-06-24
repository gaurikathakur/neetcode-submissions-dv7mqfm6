class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = {i: [] for i in range(numCourses)}
        for pre, crr in prerequisites:
            pre_map[pre].append(crr)
        reachable=[set() for _ in range(numCourses)]
        def dfs(start_node,curr):
            for neighbor in pre_map[curr]:
                if neighbor not in reachable[start_node]:
                    reachable[start_node].add(neighbor)
                    dfs(start_node,neighbor)
        for i in range(numCourses):
            dfs(i,i)
        return [v in reachable[u] for u, v in queries]

        
        