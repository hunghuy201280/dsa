from typing import List

from twisted.python.util import println


class Solution1:
    def checkStraight(self, row: List[str]) -> bool:
        l = set()
        for s in row:
            if s == ".":
                continue
            if s in l:
                return False
            else:
                l.add(s)
        return True

    def getBoxIndex(self, x: int, y: int) -> int:
        temp = int(x / 3) * 3 + int(y / 3)

        return temp

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [[] for i in range(9)]
        boxes = [[] for i in range(9)]
        colCount = 0
        for nRow, row in enumerate(board):
            isValid = self.checkStraight(row)
            if not isValid:
                return False
            for i, x in enumerate(row):
                cols[i].append(x)
                boxIdx = self.getBoxIndex(i, nRow)
                boxes[boxIdx].append(x)

        for i, col in enumerate(cols):
            isValid = self.checkStraight(col)
            if not isValid:
                return False
            isValid = self.checkStraight(boxes[i])
            if not isValid:
                return False

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[False for x in range(9)] for x in range(9)]
        rows = [[False for x in range(9)] for x in range(9)]
        boxes = [[False for x in range(9)] for x in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1

                boxIndex = int(i / 3) * 3 + int(j / 3)
                if cols[j][num] or rows[i][num] or boxes[boxIndex][num]:
                    return False
                cols[j][num] = True
                rows[i][num] = True
                boxes[boxIndex][num] = True
        return True


if __name__ == "__main__":
    s = Solution()
    res = s.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    println(res)

    res = s.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    println(res)
