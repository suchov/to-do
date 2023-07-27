# the ptorgram that will count the number of char in the prompt

prompt = "Enter the text here: "
user_input = input(prompt)

count = 0
for item in user_input:
    count = count + 1

print(f'The count of the string provided: {count}')
