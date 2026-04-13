class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    a = board[i][j]
                    for m in range(9):
                        if board[i][m]==a and m!=j:
                            print(1)
                            return False
                        if board[m][j]==a and m!=i:
                            print(2)
                            return False
        
        for i in range(1,9,3):
            for j in range(1,9,3):
                record = []
                for m in range(-1,2):
                    for n in range(-1,2):
                        if board[i+m][j+n]!=".":
                            if board[i+m][j+n] in record:
                                print(3)
                                return False
                            else:
                                record.append(board[i+m][j+n])
        return True
