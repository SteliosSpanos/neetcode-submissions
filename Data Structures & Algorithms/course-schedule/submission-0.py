class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list  = defaultdict(list)
        for pair in prerequisites:
            adj_list[pair[0]].append(pair[1])

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False # Cycle detected
            if adj_list[crs] == []:
                return True
            
            visited.add(crs)
            for course in adj_list[crs]:
                if not dfs(course):
                    return False

            visited.remove(crs)
            adj_list[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True        