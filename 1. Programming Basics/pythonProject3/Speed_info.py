speed = float(input())
speed_info = 0
if speed <= 10:
    speed_info = "slow"
elif 10 < speed <= 50:
    speed_info = "average"
elif 50 < speed <= 150:
    speed_info = "fast"
elif 150 < speed <= 1000:
    speed_info = "ultra fast"
elif speed > 1000:
    speed_info = "extremely fast"
print(speed_info)