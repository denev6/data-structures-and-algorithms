# Ref: velog.io/@y7y1h13/알고리즘leetcode-Valid-Sudokupython

class Solution:
    def isValidSudoku(self, board):
        N = 9
        row_dict = collections.defaultdict(list)
        col_dict = collections.defaultdict(list)
        box_dict = collections.defaultdict(list)

        for row in range(N):
            for col in range(N):
                val = board[row][col]

                if val == '.':
                    continue

                if val in row_dict[row]:
                    return False
                row_dict[row].append(val)

                if val in col_dict[col]:
                    return False
                col_dict[col].append(val)

                idx = (row // 3) * 3 + col // 3
                if val in box_dict[idx]:
                    return False
                box_dict[idx].append(val)

        return True