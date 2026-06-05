class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #create an adj list
        #set source node in the min heap
        #get the node from the heap
        #perform relaxation on the edges of the node
        graph = defaultdict(list)
        for s,d,w in edges:
            graph[s].append((w,d))
        shortest = {}
        q = [(0,src)]
        while q:
            w1,node1 = heapq.heappop(q)
            if node1 in shortest: continue
            shortest[node1] = w1
            #check the neighbors
            for w,d in graph[node1]:
                heapq.heappush(q,(w1+w,d))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
