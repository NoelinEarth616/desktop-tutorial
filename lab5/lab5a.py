print("Q1.1")
l1 = [1, 2, 3]
l2 = ["1.0", "Jessa", 3]
l3 = [ ]
print(l1)
print(l2)
print(l3)

print("Q1.2")
list1 = ["M", "na", "i", "ke"]
list2 = ["y", "me", "s", "lly"]
result = [''.join(tup) for tup in zip(list1, list2)]
print(result)

print("Q2.1")
numbers = [1, 2, 3, 4, 5, 6, 7]
squares2 = [num ** 2 for num in numbers]
print(squares2)

print("Q2.2")
list1 = [" Hello ", " take "]
list2 = [" Dear ", " Sir "]

result = []

for word1 in list1:
    for word2 in list2:
        result.append(word1.strip() + " " + word2.strip())

print(result)

print("Q3.1")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

merged_dict = {**dict1, **dict2}

print(merged_dict)

print("Q3.2")
sampleDict = {
    "class": {},
    80: {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict[80]['student']['marks']['history'])

print("Q3.3")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

init_dict = {name.strip(): defaults.copy() for name in employees}

print(init_dict)

print("Q4.1")
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])

print("Q4.2")
tuple1 = (10, 20, 30, 40)
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]
print(a)
print(b)
print(c)
print(d)

print('Q4.3')
tuple1 = (11, 22)
tuple2 = (99, 88)
tem = tuple2
tuple2 = tuple1
tuple1 = tem
print('tuple1: ',tuple1)
print('tuple2: ',tuple2)

print("Q5")
input_line = input("Enter a line: ")

letter_counts = {}

for char in input_line:
    if char.isalpha():
        char = char.lower()
        if char not in letter_counts:
            letter_counts[char] = 0
        letter_counts[char] += 1

for letter, count in letter_counts.items():
    print(f"The letter '{letter}' appears {count} time(s).")

print("Q6")
n = int(input("Enter the number of elements (in the range 1 -> 100): "))

if 1 <= n <= 100:
    elements = []

    print("Enter the elements:")
    for i in range(n):
        elements.append(int(input(f"Ele {i+1}: ")))

    for i in range(len(elements)):
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]

    search_key = int(input("Enter the search key: "))

    found = False
    for i in range(len(elements)):
        if elements[i] == search_key:
            found = True
            break

    if found:
        print(f"Found {search_key} at position {i+1} in the list.")
    else:
        print(f"Not Found!")

else:
    print("Invalid number of elements.")