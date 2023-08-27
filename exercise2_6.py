file = open('essay.txt', 'r')

text = file.read()
new_string = ""

for word in text.split():
    new_string += " " + word.capitalize()
print(new_string)
