

dic = {'Name': 'Ashish', 'Age': 28, 'City': 'Mumbai'}
print(dic)

dic['Area'] = 'Bhandup'
print(dic)

del dic['Area']
print(dic)

print("*"*50)

for i in dic:
    print(i, dic[i])

for i in dic.items():
    print(i)

print("*" * 50)

dic1 = {'val1': 10, 'val2': 20, 'val3': 30, 'val4': 40, 'val5': 20, 'val6': 30}

max_val_key = ''
max = dic1['val1']
for k, v in dic1.items():
    if v > max:
        max_val_key = k
        max = v

print(max_val_key)

print("*" * 50)

keys = ["name", "age", "city"]
values = ["Ashish", 28, "Mumbai"]
dic_val = {}
for val1, val2 in zip(keys, values):
    dic_val[val1] = val2

print(dic_val)

print("*" * 50)

d = { 'a': 10, 'b': 20, 'c': 30 }
lis1 = []
for i in d.items():
    lis1.append(i)

print(lis1)