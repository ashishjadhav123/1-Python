
price = 450
quantity = 3

print(f"Cost: {price * quantity}")

print("*"*50)

addition = price + quantity
print(f"Addition: {addition}")

subtraction = price - quantity
print(f"Subtraction: {subtraction}")

multiplication = price * quantity
print(f"Multiplication: {multiplication}")

division = price / quantity
print(f"Division: {division}")

print("*"*50)

float_val = float(20)
print(f"Float: {float_val}")

int_val = int(45.95)
print(f"Int: {int_val}")

print("*"*50)

a = 5
b = 2

print(a/b)

print(a//b)

print(a%b)

print("*"*50)

a = 10
b = 20
print(f"Before swap:{a, b}")
a, b = b, a
print(f"After swap:{a, b}")

print("*"*50)

# number = int(input("Enter a number: "))
#
# print("Even" if number % 2 == 0 else "Odd")

print("*"*50)

# number2 = int(input("Enter a number: "))
#
# print(f"{number} is greater" if number > number2 else f"{number2} is greater")

print("*"*50)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# if num1 <= num2 and num1 <= num3:
#     small = num1
# elif num2 <= num1 and num2 <= num3:
#     small = num2
# else:
#     small = num3
#
# print(f"The smallest number is {small}")

print("*"*50)

num = 450
sum_num = 0
for i in range(len(str(num))):
    sum_num += int(str(num)[i])

print(sum_num)

print("*"*50)

num = int(input("Enter the first number: "))

print(f"Last digit: {num%10}")
print(f"Last digit: {int(str(num)[-1])}")