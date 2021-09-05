import os
by_extension = {}
for file in os.listdir(input()):
    ext = file.split(".")[-1]
    if ext not in by_extension:
        by_extension[ext] = []
    by_extension[ext].append(file)
sorted_by_extension = sorted(by_extension.items(), key=lambda x: (x[0], x[1]))

with open(os.path.expanduser("~/Desktop/report.txt"), "w") as out_file:
    for key, value in sorted_by_extension:
       out_file.write(f'{key}\n')
       for val in value:
           out_file.write(f'___{val}\n')


