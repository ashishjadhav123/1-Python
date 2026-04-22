
def area_cal(base, height):
    area = (1/2) * base * height
    return area

base = 10
height = 5
print(area_cal(base, height))


print("*"*50)

def area_cal1(base, height, shape):
    if shape == 'triangle':
        area = (1/2) * base * height
        return f"triangle area: {area}"
    elif shape == 'rectangle':
        area = base * height
        return f"rectangle area: {area}"

shapes = ['triangle', 'rectangle']
for i in shapes:
    print(area_cal1(base, height, i))


print("*"*50)

def row_len(row):
    for i in range(row):
        print("*"*(i + 1), end=" \n")

row_len(5)


print("*"*50)

def armstrong(number):
    power = len(str(number))
    temp = number
    dig = 0
    val = 0
    while number > 0:
        dig = number % 10
        val = val + dig**power
        number //= 10

    print(f"{temp} is Armstrong" if temp == val else f"{temp} is not Armstrong")

armstrong(1634)


print("*"*50)
