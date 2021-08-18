juries_number = int(input())
presentation_name = input()
counter_presentation = 0
sum_average_presentation = 0

while presentation_name != "Finish":
    total_per_presentation = 0
    average_presentation = 0
    for i in range(juries_number):
        mark = float(input())
        total_per_presentation += mark
    average_presentation = total_per_presentation / juries_number
    counter_presentation += 1
    sum_average_presentation += average_presentation
    print(f'{presentation_name} - {average_presentation:.2f}.')
    presentation_name = input()

final_average = sum_average_presentation / counter_presentation
print(f'Student\'s final assessment is {final_average:.2f}.')


