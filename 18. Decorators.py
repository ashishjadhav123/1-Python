import time

def time_this(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} take {(end - start)*10000} mil seconds" )
        return result
    return wrapper

@time_this
def square(list_num):
    result = []
    for i in list_num:
        result.append(i**2)
    return result

@time_this
def cube(list_num):
    result = []
    for i in list_num:
        result.append(i**3)
    return result


array = range(1, 10000)
square(array)
cube(array)


print("*"*50)


def chk_number(func):
    def wrapper(*args, **kwargs):
        all_val = list(args) + list(kwargs.values())

        for i in all_val:
            if i < 0:
                raise ValueError(f"{i} is Negative value")
        result = func(*args, **kwargs)
        return result
    return wrapper


@chk_number
def square1(num):
    return num**2


num = 5
print(square1(num))

print("*"*50)

# Multiple Decorators

def first_decor(func):
    def wrapper(*args, **kwargs):
        print(f"Before line from first decorator")
        result = func(*args, **kwargs)
        print(f"After line from first decorator")
        return result
    return wrapper


def second_decor(func):
    def wrapper(*args, **kwargs):
        print(f"Before line from second decorator")
        result = func(*args, **kwargs)
        print(f"After line from second decorator")
        return result
    return wrapper


@first_decor
@second_decor
def square2(num):
    print(num**2)
    return num**2

square2(5)

print("*"*50)

@first_decor
def cube1(num):
    return num**3

print(cube1(5))

print("*"*50)

def repeat(num):
    def decor_fun(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(f"iteration {i+1}")
                print(f"Before line from decorator")
                result = func(*args, **kwargs)
                print(f"After line from decorator")
            return result
        return wrapper
    return decor_fun


@repeat(5)
def cube2(num):
    print(num**3)

cube2(5)

