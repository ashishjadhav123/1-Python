n = 5
print("Positive" if n > 0 else "Negative")

# num = int(input("Enter a number: "))
# print("Even" if num % 2 == 0 else "Odd")
#
# marks = int(input("Enter a Marks: "))
# print("Pass" if marks >= 40 else "Fail")

print("*"*50)

marks = int(input("Enter a Marks: "))
if marks > 90:
    print("A")
elif marks >= 75 and marks < 90:
    print("B")
elif marks >= 50 and marks < 75:
    print("C")
else:
    print("Fail")

print("*"*50)

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num <= 50:
        print("Number is even but less than 50")
    elif num > 50:
        print("Number is even but greater than 50")
else:
    print("Number is odd")

print("*"*50)

num = int(input("Enter a number: "))
temp = num
k = len(str(num))
op_num = 0
for i in range(k):
    dig = num % 10
    op_num += dig ** k
    num //= 10

print(f"Output number: {op_num}")
print(f"{temp} is Armstrong number" if op_num == temp else f"{temp} is not Armstrong number")