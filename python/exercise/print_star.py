while True:
    numbers=input("Please input a number,and it must be posttive integer:")
    if numbers.isdigit():
        num=int(numbers)
        for i in range(num):
            print(' '*(num-i)+'*'*(2*i+1))
        print('*'*(2*num+1))
        for i in range(num):
            print(' '*(i+1) + '*'*(2*(num-i-1)+1))
        break
    else:
        print("Your input is not a positive integer!")

