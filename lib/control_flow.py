#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
# username = input("Enter username: ")
# password = input("Enter password: ")
# result = admin_login(username, password)
# print(result)

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65 :
        return "It's a little chilly out there!"
    elif temperature == 75:
         return "It's perfect out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


# temperature = int(input("Enter temperature: "))
# result = hows_the_weather(temperature)
# print(result)


 

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


# for i in range(1, 16):
#     result = fizzbuzz(i)
#     print(result)
  

# def calculator(operation, num1, num2):
def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Cannot divide by zero!")
            return None
    else:
        print("Invalid operation!")
        return None


# operation = input("Enter an operation (+, -, *, /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = calculator(operation, num1, num2)
# print("Result:", result)






