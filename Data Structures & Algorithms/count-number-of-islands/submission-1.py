class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        row,col = len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]!="1":
                return False
            #mark current location as visited by setting it as -1
            grid[r][c] = "-1"
            #search in the immediate neighbourhood
            neighbors = [[1,0],[-1,0],[0,-1],[0,1]]
            for _r,_c in neighbors:
                dfs(r+_r,c+_c)
            return True
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and dfs(r,c):
                    result+=1
        return result
        