waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, waiting in enumerate(waiting_list):
    print(f"{index + 1}.{waiting.capitalize()}")
