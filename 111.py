Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
file=open("Bookz.csv","w")
newrecord="To Kill a Mockingbird, Harper Lee, 1960"
file.write(str(newrecord))
39
newrecord="A Brief History of Time,Stephen Hawking, 1988"
file.write(str(newrecord))
45
newrecord="The Great Gatsby,F.Scott Fitzgerald, 1922"
file.write(str(newrecord))
41
newrecord="The Man Who Mistook His Wife For a Hat, Oliver Sacks, 1985"
file.write(str(newrecord))
58
newrecord="Pride and Prejudice, Jane Austen, 1813"
file.write(str(newrecord))
38
file.close()
