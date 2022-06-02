# backtracking
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# pick empty square "0" -> try number -> check valid -> if valid repeat / if not backtrack

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True  # base case: if no more empty space means we found solution we done
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):  # check if num(i for now) is valid
            bo[row][col] = i  # if valid plug in the board

            if solve(bo):  # recursively call solve on the new board until, we get find_empty solution
                return True  # else if we gone through whole loop and no find_empty solution return False

            bo[row][col] = 0  # meaning it will backtrack the last element we added and reset
    return False


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:  # after every 3 rows
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):  # every position in the row
            if j % 3 == 0 and j != 0:  # every third position
                print(" | ", end="")  # print " | " and end with "" so it stays on same line

            if j == 8:  # check if last position
                print(bo[i][j])  # print number and go back to top of loop for next line/row
            else:
                print(str(bo[i][j]) + " ", end="")  # print the number and add space, stay on same line


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # pos = (row, col)
    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):  # so we already inserted the num in pos(the empty space)
        if bo[pos[0]][i] == num and pos[1] != i:  # now check if the num shows up in the row and/while ignoring pos,
            # which was the empty space we just put the num in. Ultimately, checking if num shows up twice in a row
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:  # go down the column of where pos is and check if num appears while
            # ignoring the place pos[0] which is the empty space we put the num in
            return False

    # Check box if num is already there
    box_x = pos[1] // 3  # coordinate of box (0,0)|(0,1)|(0,2)
    box_y = pos[0] // 3  # (1,0)|(1,1)|(1,2) ... etc.

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


print_board(board)
solve(board)
print("_______________________")
print_board(board)
