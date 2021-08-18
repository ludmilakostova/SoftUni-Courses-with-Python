n = int(input())
fulfill = 0
for i in range(1, n + 1):
    water_per_line = int(input())
    fulfill += water_per_line
    if fulfill >= 255:
        print(f'Insufficient capacity!')
        fulfill -= water_per_line
if fulfill <= 255:
    print(fulfill)
else:
    print(0)
