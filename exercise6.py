filenames = ['ddoc.txt', 'rreport.txt', 'ppresentation.txt']

#program that generat multipe text files by iterating over filenames
#and writes Hello in each generated file

for file in filenames:
    fn = open(f"files/{file}", "w")
    fn.writelines("Hello")
    fn.close()
