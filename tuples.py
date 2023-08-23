# It looks like there will be no tuples in here, just play with the list
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)
