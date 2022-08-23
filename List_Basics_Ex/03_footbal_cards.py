command = input()

cards = command.split()

team_A = []
team_B = []

game_terminated = False

for i in range(1, 11 + 1):
    team_A.append(i)
    team_B.append(i)

for card in cards:
    card_args = card.split("-")
    team = card_args[0]
    player_number = int(card_args[1])
    if team == "A" and player_number in team_A:
        team_A.remove(player_number)
    elif team == "B" and player_number in team_B:
        team_B.remove(player_number)
    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_terminated:
    print("Game was terminated")
