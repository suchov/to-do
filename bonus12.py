# understanding functions and decoupling
feet_inches = input("Enter feet and inches: ").split(" ")


def convert(feet_inches):
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    meters = feet * 0.3048 + inches * 0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters."


print(convert(feet_inches))
