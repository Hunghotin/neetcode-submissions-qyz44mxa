class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m>=1:
            n = len(matrix[0])
        else:
            return False
        
        i = 0
        while True:
            if i+1<m:
                a = matrix[i+1][0]
                b = matrix[i][-1]
                if target>=a:
                    i+=1
                    continue
                elif target<=b:
                    for j in range(n):
                        if matrix[i][j]==target:
                            return True
                    return False
                else:
                    return False
            else:
                for j in range(n):
                    if matrix[i][j]==target:
                        return True
                return False