class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for crs, preq in prerequisites:
            adjList[crs].append(preq)

        # unvisited 0
        # visiting 1
        # visited 2
        visit = [0] * numCourses
        def dfs(crs):
            if visit[crs] == 1:
                return False
            if visit[crs] == 2:
                return True
            visit[crs] = 1
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
                
            visit[crs] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True