from typing import List

def create_boards(lines: List):
    c = 0
    boards = []
    board = []
    for i in range(len(lines)):
        l = lines[i]
        if l == '\n':
            boards.append(board)
            c = 0
            board = []
        elif i == len(lines)-1: # last board
            row = l.strip('\n').split()
            int_row = [int(x) for x in row]
            board.append(int_row)
            boards.append(board)
        else:
            c += 1
            row = l.strip('\n').split()
            int_row = [int(x) for x in row]
            board.append(int_row)
    return boards

def mark_boards(boards: List, number: int):
    marked_boards = []
    for board in boards:
        marked_board = []
        for row in board:
            marked_row = ['x' if n == number else n for n in row]
            marked_board.append(marked_row)
        marked_boards.append(marked_board)
    return marked_boards

def check_bingo(boards):
    for b in range(len(boards)):
        board = boards[b]
        for row in board:
            c = row.count('x')
            if c == 5:
                return board, b
        for i in range(5):
            c_x = ['x' for n in board if n[i] == 'x' ]
            if len(c_x) == 5:
                return board, b
    return None

def calculate_bingo_score(marked_board:List, original_board:List, last_num:int):
    score_nums = []
    for r in range(len(marked_board)):
        row = marked_board[r]
        for n in range(len(row)):
            if row[n] != 'x':
                score_nums.append(original_board[r][n])
    
    return sum(score_nums)*last_num


if __name__ == "__main__":
    draws = [17,11,37,7,89,48,99,28,56,55,
        57,27,83,59,53,72,6,87,33,82,
        13,23,35,40,71,47,78,2,39,4,
        51,1,67,31,79,69,15,73,80,22,
        92,95,91,43,26,97,36,34,12,96,
        86,52,66,94,61,76,64,77,85,98,
        42,68,84,63,60,30,65,19,54,58,
        24,20,25,75,93,16,18,44,14,88,
        45,10,9,3,70,74,81,90,46,38,21,
        49,29,50,0,5,8,32,62,41]

    with open("boards_input", 'r') as inF:
        lines = inF.readlines()
        boards = create_boards(lines)
    
    marked_boards = boards.copy()
    for lucky_number in draws:
        marked_boards = mark_boards(marked_boards, lucky_number)
        if check_bingo(marked_boards) == None:
            continue
        else:
            win_board, b = check_bingo(marked_boards)
            final_score = calculate_bingo_score(win_board, boards[b], lucky_number)
            print("Bingo!")
            print("Final score: ", final_score)
            break

