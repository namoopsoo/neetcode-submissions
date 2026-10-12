from typing import List


def valid_row(row):
    if chars := set(row) - ({(str(i)) for i in range(1, 10)}.union({"."})):
        print("illegal characters", chars)
        return False

    # no dupes 
    nums = [x for x in row if x != "."]
    if len(nums) > len(set(nums)):
        print("dupes not allowed")
        return False

    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if not validate_rows(board):
            return False

        if not validate_columns(board):
            return False
        
        if not validate_boxes(board):
            return False

        return True

def validate_rows(grid):
    for i in range(9):
        if not valid_row(grid[i]):
            print(
                "row invalid", i, grid[i]
            )
            return False

    return True

def validate_columns(grid):
    for j in range(9):
        column = [grid[i][j] for i in range(9)]
        if not valid_row(column):
            print("col ", j, "invalid", column)
            return False

    return True
    
def validate_boxes(grid):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [
                grid[i][j], grid[i][j+1], grid[i][j+2],
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2],
                ]
            if not valid_row(box):
                print("box invalid", i, j)
                print(box[:3])
                print(box[3:6])
                print(box[6:])
                return False

    return True

