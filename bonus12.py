# understanding functions and decoupling
feet_inches = input("Enter feet and inches: ").split(" ")


def convert(feet_inches):
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
