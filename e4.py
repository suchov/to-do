import webbrowser

user_term = input("Enter a search term: ")

webbrowser.open_new("https://google.com/search?q=" + user_term)
