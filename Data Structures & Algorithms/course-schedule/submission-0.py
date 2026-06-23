class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visit_state = [0] * numCourses 
        
        def dfs(crs):
            if visit_state[crs] == 1: return False
            if visit_state[crs] == 2: return True
            
            visit_state[crs] = 1
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit_state[crs] = 2
            return True
        
        # Now the loop only calls dfs()
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True