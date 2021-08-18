# -	If the number is 88 - "Leo finally won the Oscar! Leo is happy".
# -	If the number is 86 - "Not even for Wolf of Wall Street?!"
# -	If the number is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
# -	If the number is over 88 - "Leo got one already!"

num = int(input())
text = ''
if num == 88:
    text = 'Leo finally won the Oscar! Leo is happy'
elif num == 86:
    text = 'Not even for Wolf of Wall Street?!'
elif num > 88:
    text = 'Leo got one already!'
else:
    text = 'When will you give Leo an Oscar?'
print(text)