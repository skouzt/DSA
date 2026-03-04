from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        boxes = {}
        for r in range(0,9):
            for c in range(0,9):
                value = board[r][c]
                box = (r // 3, c // 3)
                if value == ".":
                    continue
                if value in row[r]:
                    return False
                else:
                    row[r].add(value)
                if value in column[c]:
                    return False
                else:
                    column[c].add(value)
                if box not in boxes:
                    boxes[box] = set()
                if value  in boxes[box]:
                    return False
                else:
                    boxes[box].add(value)
        return True