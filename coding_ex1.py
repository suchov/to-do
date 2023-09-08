# Your task is to creat a program that generates a random whole
# number. Here is how the program should behave:
# Enter the lower bound: 1
# Enter the upper bound: 10
# 7
import random

user_lower = int(input("Enter the lower bound: "))
user_upper = int(input("Enter the lower bound: "))

print(random.randrange(user_lower, user_upper, 1))
