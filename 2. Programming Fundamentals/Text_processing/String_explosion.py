initial_sequence = input()
new_sequence = ""
bomb_power = 0
i = 0
while i < len(initial_sequence):
    current_ch = initial_sequence[i]

    if not initial_sequence[i] == ">":
        new_sequence += current_ch
    else:
        bomb_power = int(initial_sequence[i+1])
        new_sequence += current_ch

        while bomb_power > 0:
            i += 1

            if i >= len(initial_sequence):
                break

            current_ch = initial_sequence[i]

            if current_ch == ">":
                new_sequence += current_ch
                bomb_power += int(initial_sequence[i+1])
            else:
                bomb_power -= 1

    i += 1

print(new_sequence)


