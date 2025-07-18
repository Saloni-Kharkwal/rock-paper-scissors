import random

print("\033[1m\033[96m\n===== 🎮 WELCOME TO ROCK, PAPER, SCISSORS 🎮 =====\n\033[0m")

options = ["rock", "paper", "scissors"]

rock_ascii = """
\033[96m🪨 ROCK
    _______
---'   ____)
      (_____ )
      (_____ )
      (____ )
---.__(___)\033[0m
"""

paper_ascii = """
\033[93m📄 PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)\033[0m
"""

scissors_ascii = """
\033[95m✂️ SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\033[0m
"""

you_won_ascii = """
\033[92m
__   __            _    _ _       _ 
\\ \\ / /           | |  | (_)     | |
 \\ V /___  _   _  | |  | |_ _ __ | |
  \\ // _ \\| | | | | |/\\| | | '_ \\| |
  | | (_) | |_| | \\  /\\  / | | | |_|
  \\_/\\___/ \\__,_|  \\/  \\/|_|_| |_(_)
\033[0m
"""

you_lose_ascii = """
\033[91m
__   __            _                    _ 
\\ \\ / /           | |                  | |
 \\ V /___  _   _  | |     ___  ___  ___| |
  \\ // _ \\| | | | | |    / _ \\/ __|/ _ \\ |
  | | (_) | |_| | | |___| (_) \\__ \\  __/_|
  \\_/\\___/ \\__,_| \\_____/ \\___/|___/\\___(_)
\033[0m
"""

tie_ascii = """
 _______ _____ ______ 
|__   __|_   _|  ____|
   | |    | | | |__   
   | |    | | |  __|  
   | |   _| |_| |____ 
   |_|  |_____|______|
"""

game_over_ascii = """
\033[95m
   ____    _    __  __ _____    _____     _______ ____  
  / ___|  / \\  |  \\/  | ____|  / _ \\ \\   / / ____|  _ \\ 
 | |  _  / _ \\ | |\\/| |  _|   | | | \\ \\ / /|  _| | |_) |
 | |_| |/ ___ \\| |  | | |___  | |_| |\\ V / | |___|  _ < 
  \\____/_/   \\_\\_|  |_|_____|  \\___/  \\_/  |_____|_| \\_\\
\033[0m
"""

player_score = 0
computer_score = 0
round_number = 1

while player_score < 3 and computer_score < 3:
    print(f"\n🎯 \033[96mRound {round_number}\033[0m")
    player = input("\033[93m👉 Choose rock, paper, or scissors: \033[0m").lower()

    if player not in options:
        print("\033[91m❌ Invalid choice. Please choose rock, paper, or scissors.\033[0m")
        continue

    computer = random.choice(options)
    print(f"\n🤖 \033[93mComputer chose:\033[0m \033[96m{computer.capitalize()}\033[0m")

    if player == "rock":
        print(rock_ascii)
    elif player == "paper":
        print(paper_ascii)
    else:
        print(scissors_ascii)

    if computer == "rock":
        print(rock_ascii)
    elif computer == "paper":
        print(paper_ascii)
    else:
        print(scissors_ascii)

    if player == computer:
        print("🤝 It's a tie!")
        print(tie_ascii)
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("\033[92m✅ You win this round!\033[0m")
        print(you_won_ascii)
        player_score += 1
    else:
        print("\033[91m❌ Computer wins this round!\033[0m")
        print(you_lose_ascii)
        computer_score += 1

    print(f"\033[96m📊 Score — You: {player_score} | Computer: {computer_score}\033[0m")
    round_number += 1

print("\n" + game_over_ascii)
if player_score > computer_score:
    print("\033[92m🏆 You won the game!\033[0m")
    print(you_won_ascii)
else:
    print("\033[91m😞 You lost the game.\033[0m")
    print(you_lose_ascii)

print("\033[95m🙌 Thanks for playing! See you next time!\033[0m")
