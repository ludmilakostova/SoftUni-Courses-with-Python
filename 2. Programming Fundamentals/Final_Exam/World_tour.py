stops = input()
command = input()
while not command == "Travel":
    instruction = command.split(":")
    key_word = instruction[0]
    if key_word == "Add Stop":
        start_index = int(instruction[1])
        string = instruction[2]
        if 0 <= start_index < (len(stops)):
            new_stops = stops[:start_index] + string + stops[start_index:]
            stops = new_stops
        print(stops)
    elif key_word == "Remove Stop":
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            new_stops = stops[:start_index] + stops[end_index+1:]
            stops = new_stops
        print(stops)
    elif key_word == "Switch":
        old_string = instruction[1]
        new_string = instruction[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()

print(f'Ready for world tour! Planned stops: {stops}')