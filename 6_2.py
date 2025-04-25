import random
class Rock_Paper_Scissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])
    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "user"
        else:
            return "computer"
    def play_round(self, user_choice):
        computer_choice = self.get_computer_choice()
        print(f"Round {self.current_round}:")
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        winner = self.find_winner(user_choice, computer_choice)
        if winner == "user":
            self.user_wins += 1
            print("User wins this round!")
        elif winner == "computer":
            self.computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")
        self.current_round += 1
    def game_over(self):
        return self.current_round > self.total_rounds
    def check_winner(self):
        if self.user_wins > self.computer_wins:
            return "User wins the game!"
        elif self.computer_wins > self.user_wins:
            return "Computer wins the game!"
        else:
            return "It's a draw!"
total_rounds = 3
game = Rock_Paper_Scissors(total_rounds)
while not game.game_over():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid input. Please enter 'rock', 'paper', or 'scissors': ").lower()
    game.play_round(user_choice)
print("\nGame Over!")
print(f"Final Score - User: {game.user_wins}, Computer: {game.computer_wins}")
print(game.check_winner())