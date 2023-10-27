import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    number_players = input("Enter the number of players : ")
    if not number_players.isdigit():
        print('Please enter a valid integer')
        continue
    if not (1 < int(number_players) <= 4):
        print("enter a digit between 2 and 4")
        continue
    else:
        break

max_score = 50
player_scores = [0 for _ in range(int(number_players))]

while max(player_scores) < max_score:
    for player_idx in range(int(number_players)):
        print("\nPlayers ",player_idx + 1, "is starting !\n")
        current_score = 0
        
        while True:
            if_roll = input("Would u like to roll ? (y) : ")
            if if_roll.lower() != "y":
                player_scores[player_idx] += current_score
                break

            value = roll()
            if int(value) == 1:
                print("You rolled a 1 your score is now 0 :( !)")
                current_score = 0
                break
            else:
                current_score += value
                print("Your rolled a ",value)
                print("your current score is now ", current_score,"\n")

        print("Your total score is ",player_scores[player_idx])
    
winning_player_idx = player_scores.index(max(player_scores)) 

print("Player ",winning_player_idx + 1 ," has won win a score of ",max(player_scores) , " !")