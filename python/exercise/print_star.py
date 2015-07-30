while True:
    numbers=input("Please input a number,and it must be posttive integer:")
    if numbers.isdigit():
        num=int(numbers)
        for i in range(num):
            print(' '*i + '*'*(2*num-(2*i)-1) + ' '*i)
        break
    else:
        print("Your input is not a positive integer!")

