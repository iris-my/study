import math
import sys
numbers=input("Please input a number,and it must be posttive integer:")
#num=int(numbers)

while numbers.isdigit():
    count=1
    while (count<=int(numbers)):
        print('*',end=' ')
        count=count+1
else:
    print("Your input is not a positive integer!")

