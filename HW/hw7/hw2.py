def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)
def main():
    print("********** Игра Крестики-нолики для двух игроков **********")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = 'X'
    winner = None

    while True:
        print_board(board)
        move = int(input(f"Куда поставим {player_turn}? "))
        if board[(move - 1) // 3][(move - 1) % 3] == ' ':
            board[(move - 1) // 3][(move - 1) % 3] = player_turn
            if check_winner(board, player_turn):
                winner = player_turn
                break
            elif is_board_full(board):
                break
            else:
                player_turn = 'O' if player_turn == 'X' else 'X'
        else:
            print("Эта клетка уже занята. Выберите другую.")
    print_board(board)
    if winner:
        print(f"{winner} выиграл!")
    else:
        print("Ничья!")

if __name__ == "__main__":
    main()