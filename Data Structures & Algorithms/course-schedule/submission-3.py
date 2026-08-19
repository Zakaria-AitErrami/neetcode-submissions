class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course: preq
        adjList = defaultdict(list)

        for course, preq in prerequisites:
            adjList[course].append(preq)
        

        # visit all the courses along the curr DFS path
        visitedSet = set()

        def dfs(course):
            if course in visitedSet:
                return False
            # The course doen't have any preq
            if adjList[course] == []:
                return True
            visitedSet.add(course)

            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            visitedSet.remove(course)
            # if we run DFS on the node again we will return True immedialtely
            adjList[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
            
                