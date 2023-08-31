date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
jornal = input("Let your thoughts flow: \n")

with open(f"journal/{date}.txt", "w") as fl:
    fl.write(mood + "\n")
    fl.write(jornal)
