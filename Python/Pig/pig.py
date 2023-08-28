"""pig notes:


- multiplayer game
- Each turn: roll a die from 1 - 6.
- Anything outside of 1 is added to your score (e.g. you get a 5, your score is now 5, your next roll is a 3, your score is now 8).
- The player can decide how many times they can roll the device, BUT:
- If they roll a 1, the score that was going to be added to their total is now 0 (e.g. you roll 5 times, 
you have 20 points. your sixth role is a 1. The points that were going to be added to your total score is null, and your round ends. 
Your score stays the same tho, doesn't reset, just the points that were going to be added).
- A set score is agreed upon before playing which is the win criteria for the game.


pythonr requirements: 
- allow user to roll a dice, i.e. rng 

- ask the user if they wish to continue to roll.

- if they stop their turn, add their current round total to their total score.

- if they get a 1, dont allow them to continue and add nothing to their score 

- constantly need to check if one of the players has the targeted score, and end the game accordingly with who won."""


import random


def roll():
    MinimumValue = 1
    MaximumValue = 6
    roll = random.randint(MinimumValue, MaximumValue)

    return roll


while True:
    players = input("Enter the number of players. 2 -4.")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Between 2 and 4 players.")
    else:
        print("Invalid! try again.")



max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for player_idx in range(players):
        current_score = 0
        print("\nplayer number", player_idx + 1, "turn has just started\n")

        while True:
            shouldRoll = input("Would you like to roll? (y)")
            if shouldRoll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            

        print("Your score is:", current_score)
    
    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])






