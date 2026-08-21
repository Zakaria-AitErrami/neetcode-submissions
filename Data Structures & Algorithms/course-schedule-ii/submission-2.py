class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        output = list()

        for crs, preq in prerequisites:
            adjList[crs].append(preq)

        # 0 = unvisited
        # 1 = visiting (currently in DFS path)
        # 2 = visited (fully processed)
        visit = [0] * numCourses

        def dfs(crs):
            if visit[crs] == 1:
                return False  # cycle detected

            if visit[crs] == 2:
                return True  # already processed

            visit[crs] = 1

            for nei in adjList[crs]:
                if not dfs(nei):
                    return False

            visit[crs] = 2
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output
