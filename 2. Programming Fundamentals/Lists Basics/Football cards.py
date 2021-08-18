teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_terminated = False
command = input().split(' ')
for cards in command:
    card_info = cards.split('-')
    team_name = card_info[0]
    player_number = int(card_info[1])
    if team_name == 'A' and player_number in teamA:
        teamA.remove(player_number)
    elif team_name == 'B' and player_number in teamB:
        teamB.remove(player_number)
    if len(teamA) < 7 or len(teamB) < 7:
        is_terminated = True
        break
print(f'Team A - {len(teamA)}; Team B - {len(teamB)}')
if is_terminated:
    print(f'Game was terminated')
