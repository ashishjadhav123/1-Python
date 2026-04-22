
print("Custom Iterator")

class RemoteControl:
    def __init__(self):
        self.channels = ['AAj Tak', 'Zee News', 'BBC', 'CNN']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            raise StopIteration

        return self.channels[self.index]


r = RemoteControl()
itr = iter(r)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


print("*"*50)

print("Normal Iterator")

list1 = [1, 2, 3, 4, 5]

itr = iter(list1)

print(next(itr))
print(next(itr))

print("*"*50)

print("Reverse Iterators")

reverse_itr = reversed(list1)
print(next(reverse_itr))
print(next(reverse_itr))
print(next(reverse_itr))

print("*"*50)

dec1 = {1:"Ashish", 2:"Ram", 3:"Laxman"}

key_itr = iter(dec1.keys())
val_itr = iter(dec1.values())

print(next(key_itr))
print(next(val_itr))

print(next(key_itr))
print(next(val_itr))

print("*"*50)

class EverNumber:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n % 2 == 0:
            return f"Even Number: {self.n}"

for n in range(1, 20+1):
    print(next(EverNumber(n)))
