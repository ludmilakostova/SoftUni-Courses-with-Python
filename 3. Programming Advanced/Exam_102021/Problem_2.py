def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


matrix = []
N = 6
for i in range(N):
    matrix.append(input().split())

collected_point = 0
won = False

prizes = {"Football": 0, "Teddy Bear": 0, "Lego Construction Set": 0}

for _ in range(3):
    row, col = input()[1:-1].split(", ")
    row = int(row)
    col = int(col)
    if is_in_range(row, col, N) and matrix[row][col] == "B":
        for i in range(N):
            if matrix[i][col].isdigit():
                collected_point += int(matrix[i][col])
        matrix[row][col] = 'b'

if 100 <= collected_point <= 199:
    prizes["Football"] += 1
elif 200 <= collected_point <= 299:
    prizes["Teddy Bear"] += 1
elif collected_point >= 300:
    prizes["Lego Construction Set"] += 1

sorted_prizes = sorted(prizes.items(), key=lambda x: -x[1])
if sorted_prizes[0][1] == 1:
    print(f'Good job! You scored {collected_point} points, and you\'ve won {sorted_prizes[0][0]}.')
else:
    print(f'Sorry! You need {100 - collected_point} points more to win a prize.')
