# reads each text file and
# prints out the content of each file in the command line
# a,b,c .txt

files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    fn = open(f"files/{file}", "r")
    text = fn.read()
    fn.close()
    print(text)
    print("END OF THE FILE HERE, LET'S GET RUMBA!")
