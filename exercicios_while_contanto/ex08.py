num = 1

while num <= 20:
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
        num = num + 1
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
        num = num + 1
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        num = num + 1
    else:
        print(num)
        num = num + 1
print("Fim")