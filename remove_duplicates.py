#write a program to remove the duplicates in a list
numbers = [8, 7, 10, 1, 2, 3, 5, 6, 3, 5, 2]

#method 1
for num in numbers:
    if numbers.count(num) > 1:
        numbers.remove(num)
print(numbers)

#method 2
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)