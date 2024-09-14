from typing import List

from twisted.python.util import println


class Solution:
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
        temp = int(x / 3) + int(y / 3)
        extra = 0
        if y > 2:
            if y < 6:
                extra = 2
            else:
                extra = 4
        res = temp + extra
        return res

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
