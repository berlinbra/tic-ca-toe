class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Check for draw
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Draw'

        return None

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

def main():
    game = TicTacToe()
    print('Welcome to Tic Tac Toe!')
    print('Enter row (0-2) and column (0-2) to make a move.')

    while True:
        game.display_board()
        print(f"Player {game.current_player}'s turn")

        try:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game.make_move(row, col):
                    winner = game.check_winner()
                    if winner:
                        game.display_board()
                        if winner == 'Draw':
                            print('Game Over! It\'s a draw!')
                        else:
                            print(f'Game Over! Player {winner} wins!')
                        break
                else:
                    print('That position is already taken!')
            else:
                print('Invalid input! Row and column must be between 0 and 2')
        except ValueError:
            print('Invalid input! Please enter numbers')

if __name__ == '__main__':
    main()