# prompts the user to enter a new memeber
# adds that member to member.txt at the end of the existing memebers.

user_input = input("Add a new memeber: ")

file = open("files/member.txt", "r")
members = file.readlines()
file.close()

file = open("files/member.txt", "w")
members.append(user_input + "\n")
file.writelines(members)
file.close()
