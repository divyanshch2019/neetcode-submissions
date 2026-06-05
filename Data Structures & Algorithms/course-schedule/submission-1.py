
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph,visited = {}, set()
        def preReqToList():
            for course,dependsOn in prerequisites:
                if course not in graph:
                    graph[course] = []
                if dependsOn not in graph:
                    graph[dependsOn] = []
                graph[course].append(dependsOn)
        # this will give the AL for the course
        preReqToList()
        #now explore the graph and look for cycle, if the cycle is found return false
        #if numCourse is not 0 then return False
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            # traverse the neighbors
            for n in graph[node]:
                if not dfs(n):
                    #this will handle any of the cycle
                    return False
            visited.remove(node)
            return True
        for key in graph.keys():
            if not dfs(key):
                return False               
        return True