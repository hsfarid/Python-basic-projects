#write a program to find the largest number in a list

numbers  = [3, 2, 7, 120, 89, 56, 45, 90, 32, 78]

#method 1
# numbers.sort()
# print(numbers[-1])

#method 2
largest = 0
for num in numbers:
    if num > largest:
        largest = num
print(f"largest number: {largest}")