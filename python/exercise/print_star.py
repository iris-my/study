while True:
    numbers=input("Please input a number,and it must be posttive integer:")
    if numbers.isdigit():
        num=int(numbers)
        for i in range(num):
            print('*'*num)
        break
    else:
        print("Your input is not a positive integer!")

