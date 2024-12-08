import random

stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

#Function kung unsay pilion sa player
def player_choice():
    choices = ("rock", "paper", "scissors")
    while True:
        player = input("Choose your tool [rock/paper/scissors]: ").strip().lower()
        if player in choices:
            return player
        print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")

#Function kung kinsa ang nidaog
def winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    return "loss"

#Function update sa stats
def update_stats(result):
    if result == "win":
        stats["wins"] += 1
    elif result == "loss":
        stats["losses"] += 1
    elif result == "tie":
        stats["ties"] += 1

#Function para display sa stats
def display_stats():
    print("\nGame Statistics:")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Ties: {stats['ties']}\n")

#Main game loop
def play_game():
    while True:
        player = player_choice()
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")

        result = winner(player, computer)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")
        
        update_stats(result)
        display_stats()

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
