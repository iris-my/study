while True:
    numbers = input("Please input a number,and it must be posttive integer:")

    if numbers.isdigit():
        num = int(numbers)
        print('*' * num)
        break
    else:
        print("Your input is not a positive integer!")

