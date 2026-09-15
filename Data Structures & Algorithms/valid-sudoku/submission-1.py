class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = {}
            for j in range(9):
                num = board[i][j]
                if num == ".": continue
                if num in seen:
                    return False
                seen[num] = 1
        for i in range(9):
            seen = {}
            for j in range(9):
                num = board[j][i]
                if num == ".": continue
                if num in seen:
                    return False
                seen[num] = 1
        sector = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".": continue
                sec = int(j / 3) + (int(i / 3) * 3)
                if num in sector[sec]:
                    return False
                sector[sec][num] = 1
        return True