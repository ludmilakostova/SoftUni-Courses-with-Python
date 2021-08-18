# text = input()
# emojis_str = ""
# for i in range(len(text)):
#     if text[i] == ":" and i < len(text) - 1:
#         emojis_str += (text[i] + text[i + 1]) + ", "
#
# emojis_list = emojis_str.split(", ")
# emojis_list = [emojis for emojis in emojis_list if len(emojis) == 2]
# print("\n".join(emojis_list))

text = input()
emojis = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":" and i < len(text) - 1]
print("\n".join(emojis))
