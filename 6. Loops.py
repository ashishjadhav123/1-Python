
for i in range(10):
    print(i, end=" ")

print()

print("*"*50)

num = int(input("Enter a number: "))
temp = num
val = 0
for i in range(len(str(num))):
    dig = num % 10
    num = num // 10
    val = val * 10 + dig

print(f"{temp} is Palindrome" if val == temp else f"{temp} is not Palindrome")

print("*"*50)

for i in range(5):
    print("*"*5)

print("*"*50)

for i in range(5):
    print("*"*(int(i)+1))

print("*"*50)

counter = 5
for i in range(counter):
    print("*"*counter)
    counter -= 1

print("*"*50)
# Print a star pyramid pattern.
row = 10

for i in range(row):
    print(' ' * (row - 1 - i), end='')
    print('*' * (2 * i + 1))
