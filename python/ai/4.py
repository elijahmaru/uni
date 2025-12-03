import math
from copy import deepcopy

BOARD_SIZE = 4
WIN_LENGTH = 3
HUMAN = "X"
AI = "O"
EMPTY = "."
# Создание пустого поля


def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


# Вывод в консоль игрового поля


def print_board(board):
    print("\n " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()


# Проверка победы


def is_win(board, player):
    # Проверка горизонталей
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE - WIN_LENGTH + 1):
            if all(board[r][c + i] == player for i in range(WIN_LENGTH)):
                return True
    # Проверка вертикалей
    for c in range(BOARD_SIZE):
        for r in range(BOARD_SIZE - WIN_LENGTH + 1):
            if all(board[r + i][c] == player for i in range(WIN_LENGTH)):
                return True
        # Проверка диагоналей
    for r in range(BOARD_SIZE - WIN_LENGTH + 1):
        for c in range(BOARD_SIZE - WIN_LENGTH + 1):
            if all(board[r + i][c + i] == player for i in range(WIN_LENGTH)):
                return True
    # Проверка обратных диагоналей
    for r in range(BOARD_SIZE - WIN_LENGTH + 1):
        for c in range(WIN_LENGTH - 1, BOARD_SIZE):
            if all(board[r + i][c - i] == player for i in range(WIN_LENGTH)):
                return True
    return False


# Проверка ничьей


def is_draw(board):
    return all(
        board[r][c] != EMPTY for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)
    )


# Генерация всех возможных ходов


def get_valid_moves(board):
    moves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY:
                moves.append((r, c))
    return moves


def heuristic(board):
    score = 0
    lines = []
    # Горизонтали
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE - WIN_LENGTH + 1):
            lines.append([board[r][c + i] for i in range(WIN_LENGTH)])
    # Вертикали
    for c in range(BOARD_SIZE):
        for r in range(BOARD_SIZE - WIN_LENGTH + 1):
            lines.append([board[r + i][c] for i in range(WIN_LENGTH)])
    # Диагонали
    for r in range(BOARD_SIZE - WIN_LENGTH + 1):
        for c in range(BOARD_SIZE - WIN_LENGTH + 1):
            lines.append([board[r + i][c + i] for i in range(WIN_LENGTH)])
    # Обратные диагонали
    for r in range(BOARD_SIZE - WIN_LENGTH + 1):
        for c in range(WIN_LENGTH - 1, BOARD_SIZE):
            lines.append([board[r + i][c - i] for i in range(WIN_LENGTH)])
    # Подсчёт
    for line in lines:
        xCount = line.count(HUMAN)
        oCount = line.count(AI)
        if xCount == 3:
            score += 100
        if oCount == 3:
            score -= 100
        if xCount == 2 and oCount == 0:
            score += 10
        if oCount == 2 and xCount == 0:
            score -= 10
        if xCount >= 1 and oCount == 0:
            score += 1
        if oCount >= 1 and xCount == 0:
            score -= 1

    return score


def minimax(board, depth, isMaxTurn, maxDepth):
    # board — текущее поле
    # depth — текущая глубина
    # is_max_turn — True, если ход Maximizer (X)
    # max_depth — ограничение глубины
    # Возвращает: (оценка, (row, col))
    # Проверка терминальных состояний
    if is_win(board, HUMAN):
        return 100, None
    if is_win(board, AI):
        return -100, None
    if is_draw(board):
        return 0, None
    # Ограничение глубины
    if depth == maxDepth:
        return heuristic(board), None
    validMoves = get_valid_moves(board)
    if isMaxTurn:
        worstValue = -math.inf
        bestMove = None
        for r, c in validMoves:
            newBoard = deepcopy(board)
            newBoard[r][c] = HUMAN
            value, move = minimax(newBoard, depth + 1, False, maxDepth)
            if value > worstValue:
                worstValue = value
                bestMove = (r, c)
        return worstValue, bestMove
    else:
        worstValue = math.inf
        bestMove = None
        for r, c in validMoves:
            newBoard = deepcopy(board)
            newBoard[r][c] = AI
            value, move = minimax(newBoard, depth + 1, True, maxDepth)
            if value < worstValue:
                worstValue = value
                bestMove = (r, c)
        return worstValue, bestMove


# ХОД ИИ (ToDo)


def ai_move(board, maxDepth):
    # Делает ход ИИ, возвращает обновлённое поле.
    print("ИИ думает...")
    value, move = minimax(board, depth=0, isMaxTurn=False, maxDepth=maxDepth)
    print(f"Оценка позиции для ИИ: {value}")
    print(f"ИИ выбирает ход: {move}")
    # print(f"На глубине: {depth}")
    if move is not None:
        r, c = move
        board[r][c] = AI
    return board


# ХОД ЧЕЛОВЕКА


def human_move(board):
    while True:
        try:
            r = int(input("Введите номер строки: "))
            c = int(input("Введите номер столбца: "))
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == EMPTY:
                board[r][c] = HUMAN
                return board
            else:
                print("Некорректный ход.")
        except:
            print("Ошибка ввода.")
    # ИГРОВОЙ ЦИКЛ


def play_game(maxDepth: int = 1):
    board = create_board()
    print("Игра начинается! Вы играете за X.")
    print_board(board)
    while True:
        # Ход человека
        board = human_move(board)
        print_board(board)
        if is_win(board, HUMAN):
            print("Вы победили!")
            break
        if is_draw(board):
            print("Ничья!")
            break
        # Ход ИИ
        board = ai_move(board, maxDepth=maxDepth)
        print_board(board)
        if is_win(board, AI):
            print("ИИ победил!")
            break
        if is_draw(board):
            print("Ничья!")
            break


if __name__ == "__main__":
    for depth in range(1, 4):
        print(f"Игра с ИИ с глибиной {depth}")
        play_game(maxDepth=depth)
        print("=" * 40)
