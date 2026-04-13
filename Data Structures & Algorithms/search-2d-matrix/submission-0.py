class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m>=1:
            n = len(matrix[0])
        else:
            return False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                    return True
        return False