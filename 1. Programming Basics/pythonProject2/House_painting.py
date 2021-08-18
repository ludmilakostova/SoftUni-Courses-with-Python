x = float(input())
y = float(input())
h = float(input())
side_wall = x * y
total_side_wall = 2 * side_wall - 2 * 2.25
front_wall = x * x
total_front_wall = 2 * front_wall - 2.4
total_perimeter1 = total_side_wall + total_front_wall
total_roof = 2 * (x * y) + 2 * (x * h / 2)
green_color = total_perimeter1 / 3.4
red_color = total_roof / 4.3
green_color_f = "{:.2f}".format(green_color)
red_color_f = "{:.2f}".format(red_color)
print(green_color_f)
print(red_color_f)