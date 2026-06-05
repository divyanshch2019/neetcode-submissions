class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l,r,mid = 0, ROWS*COLS-1,0
        while l < r:
            mid = l + (r-l)//2
            #express in terms of row,col
            row,col = mid//COLS,mid%COLS
            if matrix[row][col]>=target:
                #move left
                r= mid
            else:
                #move right
                l = mid+1
        row,col = l//COLS,l%COLS
        return matrix[row][col] ==  target
        