
tup1 = (1, 2, 3, 4, 5)
print(tup1)

tup2 = ('Ashish', 28, 96.85, True)

for i in tup2:
    print(i)

print(tup2[0])
print(tup2[-1])
print(len(tup2))

print("*"*50)

t = (10, 20, 30, 40, 50, 10, 20, 30, 60)

dic = {}
for i in t:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
print("*"*50)

t3 = tup1 + t
print(t3)

print(max(t3))
print(min(t3))

print(sum(t3))

t4 = set(t3)
print(t4)
t4 = tuple(t4)
print(t4)
