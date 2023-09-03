# password quality check program

password = input("Enter a password: ")

result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

result['digit'] = False
for i in password:
    if i.isdigit():
        result['digit'] = True

result['uppercase'] = False
for i in password:
    if i.isupper():
        result['uppercase'] = True

print(result)
if all(result.values()):
    print('Strong Passowrd')
else:
    print('Try more - not a strong Password')
