waiting_list = int(input())
lift_situation = [int(el) for el in input().split()]
while waiting_list > 0 and sum(lift_situation) < len(lift_situation) * 4:
    for i in range(len(lift_situation)):
        available_space = 4 - lift_situation[i]
        if waiting_list >= available_space:
            lift_situation[i] += available_space
            waiting_list -= available_space
        else:
            available_space = waiting_list
            lift_situation[i] += available_space
            waiting_list -= available_space
lift_situation_str = [str(el) for el in lift_situation]
if waiting_list == 0 and sum(lift_situation) < len(lift_situation) * 4:
    print(f'The lift has empty spots!\n{" ".join(lift_situation_str)}')
elif waiting_list == 0 and sum(lift_situation) == len(lift_situation) * 4:
    print(" ".join(lift_situation_str))
elif waiting_list > 0:
    print(f'There isn\'t enough space! {waiting_list} people in a queue!\n{" ".join(lift_situation_str)}')

