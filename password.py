import random

upper_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
lower_letter=upper_letter.lower() 
digits= "1234567890"
symbols= "()[]{}>.<,/?:|\//*+@#$%^&~"

upper, lower, nums, syms= True, True, True, True

ap = ""
if upper:
    ap += upper_letter

if lower:
    ap += lower_letter
if digits:
    ap += digits
if symbols:
    ap += symbols

length=30
count=26

for x in range(count):
    password= "".join(random.sample(ap, length))
    print(password)

