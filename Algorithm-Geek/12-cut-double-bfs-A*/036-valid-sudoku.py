# -*- coding: utf-8 -*-

class Solution(object):

    def isValidSudoku(self, board: [[str]]) -> bool:
        m, n = len(board), len(board[0])
        # 行 是否有效
        for i in range(m):
            numbers = set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in numbers:
                        return False
                    numbers.add(board[i][j])
        # 列 是否有效
        for i in range(n):
            numbers = set()
            for j in range(m):
                if board[j][i] != '.':
                    if board[j][i] in numbers:
                        return False
                    numbers.add(board[j][i])
        # 3*3宫格
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                # print('i:', i, 'j:', j)
                numbers = set()
                # 每个宫格
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] != '.':
                            if board[r][c] in numbers:
                                return False
                            numbers.add(board[r][c])
        return True


def main():
    board = [
     ["8","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]
    ]
    result = Solution().isValidSudoku(board=board)
    print(result)


if __name__ == '__main__':
    main()
