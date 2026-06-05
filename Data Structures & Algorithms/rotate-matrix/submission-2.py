class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layers = n//2
        for layer in range(layers):
            first,last = layer,n-1-layer
            for i in range(first,last):
                offset = i - first
                temp = matrix[first][i]
                #bottom->top
                matrix[first][i] = matrix[last-offset][first]
                #right->bottom
                matrix[last-offset][first] = matrix[last][last-offset]
                #top-right->bottom-right
                matrix[last][last-offset] = matrix[i][last]
                #top-left->top-right
                matrix[i][last] = temp
        