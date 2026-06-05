from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        def edgeToGraph():
            for first,second in edges:
                graph[first].append(second)
                graph[second].append(first)
        # fill the graph
        edgeToGraph();
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            # vist node neighbors
            for n in graph[node]:
                if n == prev:
                    continue
                if not dfs(n,node):
                    # this will detect any cycle and do an early return
                    return False
            return True
        return dfs(0,-1) and len(visited) == n