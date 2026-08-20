class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle, visited = set(), set()
        adjList = defaultdict(list)
        output = list()
        for crs, preq in prerequisites:
            adjList[crs].append(preq)
        
        def dfs(crs):
            # cycle detected
            if crs in cycle:
                return False
            # already handled
            if crs in visited:
                return True

            cycle.add(crs)

            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            visited.add(crs)
            output.append(crs)
            cycle.remove(crs)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
