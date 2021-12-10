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

def check_bingo(boards, draws, win_idx):
    # win_idx is a list containing the winning board index
    # and its score
    # list is sorted such that the first entry contains the
    # first winning board
    # if board already in the list, dont add again
    # return an updated win_idx

    for b in range(len(boards)):
        alread_won = [x[0] for x in win_idx]
        if b in alread_won:
            continue

        board = boards[b]
        for row in board:
            c = [x for x in row if x in draws]
            if len(c) == 5:
                score = calculate_bingo_score(board, draws)
                win_idx.append([b, score])
        for i in range(5):
            c_x = [n for n in board if n[i] in draws ]
            if len(c_x) == 5:
                score = calculate_bingo_score(board, draws)
                win_idx.append([b, score])

    return win_idx

def calculate_bingo_score(original_board:List, draws:List):
    score_nums = []
    for r in range(len(original_board)):
        row = original_board[r]
        for n in range(len(row)):
            if row[n] not in drawed:
                score_nums.append(original_board[r][n])
    
    return sum(score_nums)*drawed[-1]


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
    
    win_boards_idx_score = []
    drawed = []
    for lucky_number in draws:
        drawed.append(lucky_number)
        win_boards_idx_score = check_bingo(boards, drawed, win_boards_idx_score)
    
    # Solution for Part A
    print(f"First board to win final score: {win_boards_idx_score[0][1]}")

    # Solution for Part B
    print(f"Last board to win final score: {win_boards_idx_score[-1][1]}")
