
set1 = {1, 2, 3, 4, 5, 3, 2, 1}
print(type(set1))
print(set1)

set1.add(6)
set1.add(7)
print(set1)

print("*"*50)

set2 = set()
set2.add(1)
set2.add(2)
set2.add(3)

print(set2)

print("*"*50)

liset1 = [1, 2, 3, 4, 5, 3, 2, 1]
print(liset1)

set3 = set(liset1)
set3.add(6)
print(set3)

print("*"*50)

set4 = frozenset([1, 2, 3, 4, 5, 3, 2, 1])
print(set4)

try:
    set4.add(7)
except Exception as exp:
    print(exp)
    print(type(exp).__name__)

print("*"*50)

set3.update([7, 8, 9, 10, 5])
print(set3)

print("*"*50)

set3.remove(7)
print(set3)

print("*"*50)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Union: {A | B}")

print(f"Intersection: {A & B}")

print(f"Difference: {A ^ B}")

print(f"Symmetric difference: {A ^ B - A}")

print(f"Min: {min(A)}", f"Maxx: {max(A)} from set A")

print("*"*50)

C = {5, 6, 7, 8}
print("Find elements present in set A but not in B and C.")
print((A - B - C))

print("*"*50)