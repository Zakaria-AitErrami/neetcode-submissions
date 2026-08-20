class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for crs, preq in prerequisites:
            adjList[crs].append(preq)
        
        visited = set()

        def dfs(crs):
            if adjList[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)    
            adjList[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        