
str_val = "Python"

for i in str_val:
    print(i)

print(f"Length: {len(str_val)}")

print("*"*50)

word = "Programming"

print(f"First 3 letters: {word[:3]}")

print(f"Last 4 letters: {word[-4:]}")

print(f"4-6 letters: {word[2:6]}")

print(f"Reversed word: {word[::-1]}")

x = "DataScience"

print(x[:4])
print(x[4:])

print("*"*50)

print(x.upper())

print(x.lower())

print(x.title())

text = "   Python Programming   "

print(text.strip())

print(text.replace("Python", "Java").strip())

sentence = "banana"

print(sentence.count("a"))

print("*"*50)

str_val = input("Enter a string: ")

print("String is palindrome" if str_val == str_val[::-1] else "String not palindrome")

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

count_vowels = 0
count_consonants = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

print(count_vowels, count_consonants)

word_list = sentence.split(" ")
print(f"Word List: {word_list}")

print(sentence.replace(" ", ""))

print(f"First char of string: {str_val[0]}")
print(f"Last char of string: {str_val[-1]}")
print(f"Middel char of string: {str_val[len(str_val)//2]}")

print("*"*50)

sentence = input("Enter a sentence: ")
frequency = {}

for char in sentence:
    if char.lower() in frequency:
        frequency[char.lower()] += 1
    else:
        frequency[char.lower()] = 1

print(frequency)

print("*"*50)

Input= "Py3th0n9"

for char in Input:
    if char.isdigit():
        Input = Input.replace(char, "")


print(Input)