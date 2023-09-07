# understanding functions and decoupling
feet_inches = input("Enter feet and inches: ").split(" ")


def parse(feet_inches):
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
