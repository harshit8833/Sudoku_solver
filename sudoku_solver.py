board = [                                          ## PUT ANY SUDOKU VALUE
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board_):                             ## Making seperation lines
    for i in range(len(board_)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board_[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board_[i][j])
            else:
                print(str(board_[i][j]) + " ", end="")


def find_empty(board_):                                ## Recognising blank boxes
    for i in range(len(board_)):
        for j in range(len(board_[0])):
            if board_[i][j] == 0:
                return (i, j)  # row, col

    return None


def solve(board_):
    find = find_empty(board_)
    if not find:
        return True                               ## BASE CASE OF RECURSION
    else:
        row, col = find

    for i in range(1,10):
        if valid(board_, i, (row, col)):
            board_[row][col] = i

            if solve(board_):                         ## RECURSIVE CALL
                return True

            board_[row][col] = 0                      ## RESETING IF PARTICULAR NUMBER NOT VALID

    return False


def valid(board_, num, pos):

    # Check row
    for i in range(len(board_[0])):
        if board_[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board_)):
        if board_[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board_[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(board_):
    for i in range(len(board_)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board_[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board_[i][j])
            else:
                print(str(board_[i][j]) + " ", end="")


def find_empty(board_):
    for i in range(len(board_)):
        for j in range(len(board_[0])):
            if board_[i][j] == 0:
                return (i, j)  # row, col

    return None
print('''
            _---~~(~~-_.
     _{        )   )
   ,   ) -~~- ( ,-' )_
  (  `-,_..`., )-- '_,)
 ( ` _)  (  -~( -_ `,  }
 (_-  _  ~_-~~~~`,  ,' )
   `~ -^(    __;-,((()))
         ~~~~ {_ -_(())
                `\  }
                  { }
''')
print("            SUDOKU SOLVER")
print("______________________________________")
print_board(board)
solve(board)
print("______________________________________")
print("SOLUTION")
print("______________________________________")
print_board(board)