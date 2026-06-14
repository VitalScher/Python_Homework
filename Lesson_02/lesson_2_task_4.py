num = int(input("Введите любое целое число: "))

def fizz_buzz(num):
    for n in range(1, num+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else: 
            print(n)

fizz_buzz(num)

