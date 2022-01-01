import numpy

chunks = []
numbers = []


class BingoNumber:
    def __init__(self, value):
        self.marked = False
        self.value = value

    def mark(self):
        self.marked = True

    def __repr__(self):
        return str((self.value, self.marked))


with open('input.txt') as f:
    chunk_count = 0
    chunk = []
    for i, line in enumerate(f):
        if i == 0:
            numbers = [int(x) for x in line.strip().split(',')]
        else:
            if line != '\n':
                chunk.append(line.strip().split())
                if len(chunk) == 5:
                    chunks.append(chunk)
                    chunk = []


def convert_chunk_to_bingo_numbers(chunks):
    ret = []
    for chunk in chunks:
        converted_chunk = []
        for a in chunk:
            temp = []
            for val in a:
                temp.append(BingoNumber(int(val)))
            converted_chunk.append(temp)
        ret.append(converted_chunk)
    return ret


def build_boards(bingo_number_chunks):
    boards = []
    for chunk in bingo_number_chunks:
        boards.append(numpy.array(chunk))
    return boards


def play_number(boards, number):
    print(f"Playing number: {number}...")
    for board in boards:
        for row in board:
            for board_num in row:
                if board_num.value == number:
                    board_num.mark()


def process_winner(board, play):
    total = 0
    print('The Winning Board:')
    print(board)
    for row in board:
        for val in row:
            if not val.marked:
                total += val.value
    return total * play


def check_winner(boards):
    for board in boards:
        # Columns
        for i in range(0, len(board)):
            col = board[:, i]
            marked = True
            for val in col:
                if not val.marked:
                    marked = False
            if marked:
                # We have a winner
                print('We have a winning column!')
                return board, col
        # Check rows
        for row in board:
            marked = True
            for val in row:
                if not val.marked:
                    marked = False
            if marked:
                # We have a winner
                print('We have a winning row!')
                return board, row

    return False


def play(boards, plays):
    for play in plays:
        play_number(boards, play)
        result = check_winner(boards)
        if result:
            return process_winner(result[0], play)


boards = build_boards(convert_chunk_to_bingo_numbers(chunks))
final_score = play(boards, numbers)
print(f"The Final Score is {final_score}")
