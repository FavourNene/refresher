import random

winning_rules = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}
choices = list(winning_rules.keys())
user_history = {"Rock": 0, "Paper": 0, "Scissors": 0}

turns = 0
ai_win = 0
your_win = 0

def determine_winner(user_choice, ai_choice, your_win, ai_win):
    if ai_choice == user_choice:
        return "It's a tie", your_win, ai_win
    elif winning_rules[user_choice] == ai_choice:
        your_win += 1
        return "You win!", your_win, ai_win
    else:
        ai_win += 1
        return "AI wins!", your_win, ai_win

print("Welcome to Nene's Rock, Paper, Scissors!")

while True:
    user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to stop and see your score): ").capitalize()
    if user_choice == "Quit":
        print(f"AI won {ai_win} times and you won {your_win} times in {turns} turns.")
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue


    user_history[user_choice] += 1
    turns += 1

    ai_choice = random.choice(choices)
    print(f"AI chose: {ai_choice}")

    result, your_win, ai_win = determine_winner(user_choice, ai_choice, your_win, ai_win)
    print(result)
