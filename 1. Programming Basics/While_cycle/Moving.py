width = int(input())
length = int(input())
high = int(input())
carton = input()
house_area = width * length * high
total_boxes = 0
while carton != 'Done':
    total_boxes += int(carton)
    if total_boxes <= house_area:
        free_space = house_area - total_boxes
        carton = input()
        continue
    else:
        break

if total_boxes <= house_area:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(total_boxes-house_area)} Cubic meters more.')
