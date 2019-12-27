# Python If-Else



import sys


Num = int(raw_input().strip())

if Num % 2 != 0:
    print("Weird")
else:
    if Num >= 2 and Num <= 5:
        print("Not Weird")
    elif Num >= 6 and Num <= 20:
        print("Weird")
    elif Num > 20:
        print("Not Weird")
