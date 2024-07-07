#write a python program that accepts numbers from a user and translate them to words

phone = input("Phone: ")
mapping_digits = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
output = ""
for ch in phone:
    output += mapping_digits.get(ch, "!") + " "
print(output)