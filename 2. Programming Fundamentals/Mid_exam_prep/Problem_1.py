experience_amount_target = float(input())
count_battles = int(input())
experience_cumulated = 0
battles = 0
while count_battles > 0:
    experience_earned_per_battle = float(input())
    if battles % 3 == 0:
        experience_earned_per_battle = experience_earned_per_battle * 1.15
    if battles % 5 == 0:
        experience_earned_per_battle = experience_earned_per_battle * 0.9
    if battles % 15 == 0:
        experience_earned_per_battle = experience_earned_per_battle * 1.05
    experience_cumulated += experience_earned_per_battle
    if experience_amount_target - experience_cumulated <= 0:
        break
    count_battles -= 1
    battles += 1

needed_experience = experience_amount_target - experience_cumulated
if needed_experience <= 0:
    print(f'Player successfully collected his needed experience for {battles} battles.')
else:
    print(f'Player was not able to collect the needed experience, {needed_experience:.2f} more needed')


