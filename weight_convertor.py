# Ask a user for their weight and unit
weight = int(input("Enter your weight: "))
unit = input("L (lbs) or K (kgs): ").lower()

# convert the weight from one unit to another based on the unit input 
# using match cases 
match unit:
    case "l":
        converted = weight * 0.45
        print(f"You are {round(converted, 2)} kilos")
    case "k":
        converted = weight / 0.45
        print(f"You are {round(converted, 2)} pounds")
    case _:
        print("Enter a valid weight and unit")

# using if statememts 
# if unit == "l":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# elif unit == "k":
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

