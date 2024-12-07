class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print('\n')
        for i, row in enumerate(self.board):
            print(f' {row[0]} | {row[1]} | {row[2]} ')
            if i < 2:
                print('-----------')

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
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

        # Check for tie
        if all(cell != ' ' for row in self.board for cell in row):
            return 'Tie'

        return None

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

def main():
    game = TicTacToe()
    print('Welcome to Tic Tac Toe!')
    print('Enter moves using row (0-2) and column (0-2)')
    
    while True:
        game.print_board()
        print(f"\nPlayer {game.current_player}'s turn")
        
        try:
            row = int(input('Enter row (0-2): '))
            col = int(input('Enter column (0-2): '))
            
            if game.make_move(row, col):
                winner = game.check_winner()
                if winner:
                    game.print_board()
                    if winner == 'Tie':
                        print('\nGame Over! It\'s a tie!')
                    else:
                        print(f'\nGame Over! Player {winner} wins!')
                    break
                game.switch_player()
            else:
                print('\nInvalid move! Try again.')
        except ValueError:
            print('\nPlease enter valid numbers!')

if __name__ == '__main__':
    main()