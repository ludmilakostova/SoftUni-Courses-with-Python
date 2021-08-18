import sys
n = int(input())
max_value = -sys.maxsize
for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow/snowball_time)**snowball_quality
    if snowball_value >= max_value:
        max_value = int(snowball_value)
        snowball_snow_final = snowball_snow
        snowball_time_final = snowball_time
        snowball_quality_final = snowball_quality
print(f'{snowball_snow_final} : {snowball_time_final} = {max_value} ({snowball_quality_final})')

