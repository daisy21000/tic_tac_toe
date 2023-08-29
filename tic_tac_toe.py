import random


class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.choices = ['X', 'O']
        self.player_1 = None
        self.player_2 = None
        self.computer = None
        self.turn = None
        self.start()

    def start(self):
        self.start_players()
        self.turn = self.player_1
        is_game_on = True
        while is_game_on:
            self.start_turn()
            winner = self.check_winner()
            if winner:
                self.print_board()
                if winner == 'Draw':
                    print('It\'s a draw!')
                else:
                    print(f'Winner is {winner}!')
                is_game_on = False
            if self.turn == self.player_1:
                self.turn = self.player_2
            else:
                self.turn = self.player_1

    def start_players(self):
        user_choice = input("Do you want to play against a computer or play 2 player?\n"
                            "Type '0' for 2 player and 1 for computer\n")
        if user_choice == '0':
            has_game_started = False
            while not has_game_started:
                try:
                    one_choice = int(input("Choose which one Player 1 would like:\n0 for 'X'\n1 for 'O'\n"))
                except ValueError:
                    print('Invalid Input. Please type \'0\' or \'1\'')
                else:
                    self.player_1 = self.choices[one_choice]
                    if self.player_1 == 'X':
                        self.player_2 = self.choices[1]
                    else:
                        self.player_2 = self.choices[0]
                    has_game_started = True
        elif user_choice == '1':
            has_game_started = False
            while not has_game_started:
                try:
                    one_choice = int(input("Choose which one you would like:\n0 for 'X'\n1 for 'O'\n"))
                except ValueError:
                    print('Invalid Input. Please type \'0\' or \'1\'')
                else:
                    self.player_1 = self.choices[one_choice]
                    if self.player_1 == 'X':
                        self.player_2 = self.choices[1]
                    else:
                        self.player_2 = self.choices[0]
                    self.computer = self.player_2
                    has_game_started = True
        print(f'Player 1 is {self.player_1}\nPlayer 2 is {self.player_2}')

    def start_turn(self):
        self.print_board()
        self.input_in_board(self.turn)

    def print_board(self):
        for row in self.board:
            pretty_row = "  ".join([row[0], '|', row[1], '|', row[2]])
            print(pretty_row)

    def input_in_board(self, player):
        if player == self.computer:
            is_number_valid = False
            while not is_number_valid:
                computer_choice = random.randint(0, 8)
                choice = computer_choice + 1
                if computer_choice > 2:
                    if computer_choice > 5:
                        input_row_index = 2
                        computer_choice -= 6
                    else:
                        input_row_index = 1
                        computer_choice -= 3
                else:
                    input_row_index = 0
                position = self.board[input_row_index][computer_choice]
                if position == ' ':
                    self.board[input_row_index][computer_choice] = self.computer
                    print(f'The computer chose {choice}')
                    is_number_valid = True
        else:
            is_input_valid = False
            while not is_input_valid:
                try:
                    player_input = int(input('Choose where you want to go (1 - 9) ')) - 1
                except ValueError:
                    print("Invalid Input. Please type a number from 1 to 9")
                else:
                    if player_input > 2:
                        if player_input > 5:
                            input_row_index = 2
                            player_input -= 6
                        else:
                            input_row_index = 1
                            player_input -= 3
                    else:
                        input_row_index = 0

                    position = self.board[input_row_index][player_input]
                    if position == ' ':
                        self.board[input_row_index][player_input] = player
                        is_input_valid = True
                    else:
                        print('That position already has an input. Please use another value.')

    def check_winner(self):
        for choice in self.choices:
            if self.board[0][0] == choice and self.board[0][1] == choice and self.board[0][2] == choice or\
               self.board[1][0] == choice and self.board[1][1] == choice and self.board[1][2] == choice or\
               self.board[2][0] == choice and self.board[2][1] == choice and self.board[2][2] == choice or\
               self.board[0][0] == choice and self.board[1][0] == choice and self.board[2][0] == choice or \
               self.board[0][1] == choice and self.board[1][1] == choice and self.board[2][1] == choice or \
               self.board[0][2] == choice and self.board[1][2] == choice and self.board[2][2] == choice or\
               self.board[0][0] == choice and self.board[1][1] == choice and self.board[2][2] == choice or\
               self.board[0][2] == choice and self.board[1][1] == choice and self.board[2][0] == choice:
                return choice
            elif ' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]:
                return 'Draw'
        return None
