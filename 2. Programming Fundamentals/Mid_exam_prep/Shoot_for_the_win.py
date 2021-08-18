shoot_target = [int(target) for target in input().split()]
command = input()
count_shoot_target = 0
while not command == 'End':
    index = int(command)
    if index < len(shoot_target) and shoot_target[index] != -1:
        initial_value_shoot_target = shoot_target[index]
        shoot_target[index] = -1
        count_shoot_target += 1
        for target in shoot_target:
            if target != -1 and target > initial_value_shoot_target:
                index = shoot_target.index(target)
                target -= initial_value_shoot_target
                shoot_target[index] = target
            elif target != -1 and target <= initial_value_shoot_target:
                index = shoot_target.index(target)
                target += initial_value_shoot_target
                shoot_target[index] = target
    command = input()
shoot_target = [str(target) for target in shoot_target]
print(f'Shot targets: {count_shoot_target} -> {" ".join(shoot_target)}')