text = input()
text_list = text.split()
my_dict = {}
for el in text_list:
    for chr in el:
        if chr not in my_dict:
            my_dict[chr] = 1
        else:
            my_dict[chr] += 1
for chr, occurrences in my_dict.items():
    print(f"{chr} -> {occurrences}")

