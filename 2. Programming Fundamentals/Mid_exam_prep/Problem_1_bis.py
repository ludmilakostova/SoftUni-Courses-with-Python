experience_amount_target = float(input())
count_battles = int(input())
experience_cumulated = 0
for i in range(1, count_battles+1):
    experience_earned_per_battle = float(input())
    if i % 3 == 0:
        experience_earned_per_battle = experience_earned_per_battle * 1.15
    if i % 5 == 0:
        experience_earned_per_battle = experience_earned_per_battle * 0.9
    if i % 15 == 0:
        experience_earned_per_battle = experience_earned_per_battle * 1.05
    experience_cumulated += experience_earned_per_battle
    if experience_amount_target - experience_cumulated <= 0:
        print(f'Player successfully collected his needed experience for {i} battles.')
        exit()

needed_experience = experience_amount_target - experience_cumulated
print(f'Player was not able to collect the needed experience, {needed_experience:.2f} more needed.')

