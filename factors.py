def print_factors(number):
    print("the factor of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
number = int(input("enter your number to fund its factors:"))
print_factors(number)