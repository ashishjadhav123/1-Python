
list_1 = ['apple', 'banana', 'cherry']
print(list_1)

list_2 = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(f"First element: {list_2[0]}")
print(f"Last element: {list_2[-1]}")
print(f"Middel element: {list_2[len(list_2)//2]}")

print(f"Length: {len(list_2)}")
print(f"3rd element: {list_2[2]}")

list_2.append("chiku")
print(list_2)

list_2.insert(3, "mango")
print(list_2)

print("*"*50)

nums = [10, 20, 30, 40, 50]

print(nums[:3])

print(nums[-2:])

print(nums[1:3])

nums.extend([60, 70, 80, 10, 20, 30, 40, 50])
print(nums)

# nums.remove(40)
# print(nums)
#
# nums.pop()
# print(nums)

print("*"*50)

print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Sum: {sum(nums)}")

print(sorted(nums))
print(sorted(nums, reverse=True))

dig = nums[0]
list1 = []
for i in nums:
    if i >= dig:
        list1.append(i)
        dig = i
print(list1)

occ_dic = {}

for num in nums:
    if num in occ_dic:
        occ_dic[num] += 1
    else:
        occ_dic[num] = 1

print(occ_dic)

print(f"Index element: {nums.index(40)}")

print("*"*50)

# Write a program to remove duplicates from a list.
frsh_list = []

for num in nums:
    if num not in frsh_list:
        frsh_list.append(num)

print(frsh_list)

# Write a program to square every number in a list.
# for num in frsh_list:
#     print(num**2)

max_val = max(nums)
temp_val = nums[0]
for num in nums:
    if num >= temp_val and num < max_val:
        temp_val = num

print(temp_val)

# Rotate a list:
print(nums)
print(nums[::-1])

print("*"*50)

nested_list = [[1, 2, 3], [4], [5, 6, 7], [8, 9], 'Ashish', 28]
single_list = []

for element in nested_list:
    if type(element) == list:
        single_list.extend(element)
    else:
        single_list.append(element)


print(single_list)

print("*"*50)

list_sqr = [i**2 for i in nums]
print(list_sqr)