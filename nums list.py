Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fruit_tuple=("apple","banana","strawberry","orange")
print(fruit_tuple.index("strawberry"))
2
print(fruit_tuple[2])
strawberry

names_list=["John","Tim","Sam"]

del names_list[1]
print(names_list)
['John', 'Sam']
names_list.append(input("Please add a name: "))
Please add a name: Jared
print(names_list)
['John', 'Sam', 'Jared']
names_list.sort()
print(sorted(names_list))
['Jared', 'John', 'Sam']
colors={1:"Red",2:"Blue",3:"Green"}
colour[2]="Yellow"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    colour[2]="Yellow"
NameError: name 'colour' is not defined. Did you mean: 'colors'?
colors[2]="Yellow"
print(colors)
{1: 'Red', 2: 'Yellow', 3: 'Green'}
x=[123,675,874,906,503]
print(len(x))
5
print(x[1:4])
[675, 874, 906]
for i in x:
    print(i)

    
123
675
874
906
503
num=int(input("Enter a number: "))
Enter a number: 12
if num in x:
    print(num,"is in list")
else:
    print("Not in list")

    
Not in list
x.insert(2,420)
print(x)
[123, 675, 420, 874, 906, 503]
x.remove(906)
print(x)
[123, 675, 420, 874, 503]
x.append(876)
print(x)
[123, 675, 420, 874, 503, 876]
fruit_tuple=("apple","Mango","Cherry","Strawberry","Guava")
print(fruit_tuple.index("Strawberry"))
3
print(fruit_tuple[2])
Cherry
names_list=["Adam","Bungei","Moses","Abraham"]
print(names_list.append(input("Please enter a name : ")))
Please enter a name : Joy
None
print(names_list)
['Adam', 'Bungei', 'Moses', 'Abraham', 'Joy']
print(names_list.append(input("Please enter a name: ")))
Please enter a name: Chuck
None
print(names_list)
['Adam', 'Bungei', 'Moses', 'Abraham', 'Joy', 'Chuck']
del names_list("Chuck")
SyntaxError: cannot delete function call
del names_list[1]
print(names_list)
['Adam', 'Moses', 'Abraham', 'Joy', 'Chuck']
names_list.sort()
print(sorted(names_list))
['Abraham', 'Adam', 'Chuck', 'Joy', 'Moses']
colors={1:"Blue",2:"Red",3:"Black",4:"Purple"}
colors[2]="Orange"
print(colors)
{1: 'Blue', 2: 'Orange', 3: 'Black', 4: 'Purple'}
x=[156,764,806,045,767]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
x=[145,897,56,98,909,456]
for i in x:
    print(i)

    
145
897
56
98
909
456
print(len(x))
6
print(x[1:4])
[897, 56, 98]
num=int(input("Please enter a number: "))
Please enter a number: 90
if num in x:
    print(num," is in list")
else:
    print("Not in the list.")

    
Not in the list.
x.insert(2,420)
print(x)
[145, 897, 420, 56, 98, 909, 456]
x.remove(897)
print(x)
[145, 420, 56, 98, 909, 456]
x.append(988)
print(x)
[145, 420, 56, 98, 909, 456, 988]
countries_tuple=("Cameroon","Japan","Canada","Ghana","Guinea","Syria")
print(countries_tuple)
('Cameroon', 'Japan', 'Canada', 'Ghana', 'Guinea', 'Syria')
print()

country=input("Please enter a country of your choice : ")
Please enter a country of your choice : Canada
print(countries_tuple.index(country))
2
num=int(input("Please enter a number : "))
Please enter a number : 3
print(countries_tuple[num])
Ghana
sports=("Tennis","Football")
fav=input("Please enter your favourite sport : ")
Please enter your favourite sport : Rugby
sports.append(fav)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    sports.append(fav)
AttributeError: 'tuple' object has no attribute 'append'
sports=["Tennis","Football"]
sports.append(input("Enter your favourite sport: "))
Enter your favourite sport: Rugby
print(sports)
['Tennis', 'Football', 'Rugby']
sports.sort()
print(sports)
['Football', 'Rugby', 'Tennis']
subjects=["Maths","English","Geography","Algebra","Calculus","Physics"]
fav=input("Please enter a subject that you dont like")
Please enter a subject that you dont like Algebra
subjects.remove(fav)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    subjects.remove(fav)
ValueError: list.remove(x): x not in list
print(fav)
 Algebra
rid=subjects.index(fav)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    rid=subjects.index(fav)
ValueError: ' Algebra' is not in list
rid=subjects.index(fav)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    rid=subjects.index(fav)
ValueError: ' Algebra' is not in list
subjects=["English","Algebra","Calculus","Physics","Geography","Hydrology"]
dis=input("Which subject do you like the least?")
Which subject do you like the least? Algebra
ris=subjects.index(dis)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    ris=subjects.index(dis)
ValueError: ' Algebra' is not in list
subjects_list=["English","Algebra","Computing","Calculus","Physics","Geography"]
Dis=input("Which subject do you like the least? ")
Which subject do you like the least? Algebra
Rid=subjects_list.index(Dis)
sujects_list.remove[Rid]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    sujects_list.remove[Rid]
NameError: name 'sujects_list' is not defined. Did you mean: 'subjects_list'?
subjects_list.remove[Rid]
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    subjects_list.remove[Rid]
TypeError: 'builtin_function_or_method' object is not subscriptable
del subjects_list[Rid]
print(subjects_list)
['English', 'Computing', 'Calculus', 'Physics', 'Geography']
subjects_list=["Computing","Physics","Calculus","Survey","Islam","Hydrology"]
dis=input("Which subjects do you like the least ? ")
Which subjects do you like the least ? Islam
rid=subjects_list.index(dis)
del subjects_list[rid]
print(subjects_list)
['Computing', 'Physics', 'Calculus', 'Survey', 'Hydrology']
food_dictionary={}
food1=input("Enter a food you like : ")
Enter a food you like : Githeri
food_dictionary[1]=food1
food2=input("Enter a food you like: ")
Enter a food you like: Pilau
food_dictionary[2]=food2
food3=input("Enter a foood you like : ")
Enter a foood you like : Shawarma
food_dictionary[3]=food3
food4=input("Enter a food you like: ")
Enter a food you like: Ugali
print(food_dictionary)
{1: 'Githeri', 2: 'Pilau', 3: 'Shawarma'}
food_dictionary[4]=food4
print(food_dictionary)
{1: 'Githeri', 2: 'Pilau', 3: 'Shawarma', 4: 'Ugali'}
dis=input("Which food do you like the least ? ")
Which food do you like the least ? Githeri
rid=food_dictionary.index(dis)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    rid=food_dictionary.index(dis)
AttributeError: 'dict' object has no attribute 'index'
rid=int(input("Which food do you want to get rid of ? "))
Which food do you want to get rid of ? Githeri
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    rid=int(input("Which food do you want to get rid of ? "))
ValueError: invalid literal for int() with base 10: 'Githeri'
rid=int(input("Which food do you want to get rid of : "))
Which food do you want to get rid of : 1
del food_dictionary[rid]
sort.food_dictionary()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    sort.food_dictionary()
NameError: name 'sort' is not defined. Did you mean: 'sports'?
food_dictionary.sort()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    food_dictionary.sort()
AttributeError: 'dict' object has no attribute 'sort'
print(food_dictionary)
{2: 'Pilau', 3: 'Shawarma', 4: 'Ugali'}
colors_list=["Red","Blue","Pink","Green","Orange","Cream","Black","Maroon","Yellow","Brown"]
start=int(input("Please enter a start number: "))
Please enter a start number: 0
end=int(input("Please enter an end number: "))
Please enter an end number: 9
print(colors_list[start:end])
['Red', 'Blue', 'Pink', 'Green', 'Orange', 'Cream', 'Black', 'Maroon', 'Yellow']
numbers_list=[563,925,398,409]
for i in numbers_list:
    print(i)

    
563
925
398
409
num=int(input("Please enter a number : "))
Please enter a number : 234
if num in numbers_list:
    print(num,"Is in position",numbers_list.index(num))
else:
    print(num,"is not in the list.")

    
234 is not in the list.
invited_list=[]
name1=input("Whom do you want invited to the party ? ")
Whom do you want invited to the party ? Edmond
name2=input("Whom do you want invited to the party ? ")
Whom do you want invited to the party ? Jared
name3=input("Whom do you want invited to the party ? ")
Whom do you want invited to the party ? Timothy
invited=[name1,name2,name3]
print(invited)
['Edmond', 'Jared', 'Timothy']
more=input("Do you want to invite more persons to the party ? ")
Do you want to invite more persons to the party ? y
while more =="y":
    name=input("Please enter the name of the other person : ")
    more=input("Do you wish to invite more people to the party ? y/n)
               
SyntaxError: unterminated string literal (detected at line 3)
while more =="y":
    name=input("Please enter the name of the other person : ")
    more=input("Do you wish to invite more people to the party ? y/n")
    print("You have
          
SyntaxError: unterminated string literal (detected at line 4)


name1=input("Please enter the name of one you want invited to the party: ")
          
Please enter the name of one you want invited to the party: Jared
name2=input("Please enter the name of one you want invited to the party")
          
Please enter the name of one you want invited to the party Jacinta
name3=input("Please enter the name of the person you want invited to the party : ")
          
Please enter the name of the person you want invited to the party : Jerry
invited=[name1,name2,name3]
          
print(invited)
          
['Jared', ' Jacinta', 'Jerry']
more=input("Do you wish to invite more people to the party ? ")
          
Do you wish to invite more people to the party ? y
while more == "y":
    newname=invited.append(input("Please enter a name : " ))
    more=input("Do you wish to invite more ? " )
    print("You have invited ",len(invited)," People to the party. ")

    
Please enter a name : jared
Do you wish to invite more ? y
You have invited  4  People to the party. 
Please enter a name : Kibett
Do you wish to invite more ? y
You have invited  5  People to the party. 
Please enter a name : Sakaja
Do you wish to invite more ? y
You have invited  6  People to the party. 
Please enter a name : Newton
Do you wish to invite more ? y
You have invited  7  People to the party. 
Please enter a name : Tot
Do you wish to invite more ? y
You have invited  8  People to the party. 
Please enter a name : Livermore
Do you wish to invite more ? y
You have invited  9  People to the party. 
Please enter a name : Assumpta
Do you wish to invite more ? y
You have invited  10  People to the party. 
Please enter a name : Lincoln
Do you wish to invite more ? y
You have invited  11  People to the party. 
Please enter a name : Limo
Do you wish to invite more ? y
You have invited  12  People to the party. 
Please enter a name : Harriet
Do you wish to invite more ? y
You have invited  13  People to the party. 
Please enter a name : Jelimo
Do you wish to invite more ? y
You have invited  14  People to the party. 
Please enter a name : Kobilo
Do you wish to invite more ? h
You have invited  15  People to the party. 

name1=input("Enter a name of a person you want invited to a party: ")
Enter a name of a person you want invited to a party: Karis
name2=input("Enter a name of one you want invited to a party: ")
Enter a name of one you want invited to a party: Lily
name3=input("Enter the name of one you want invited to the party: " )
Enter the name of one you want invited to the party: James
invited=[name1,name2,name3]
print(invited)
['Karis', 'Lily', 'James']
more=input("DO you wish to invite more people to the party ? ")
DO you wish to invite more people to the party ? y
while more == "y":
    newname=invited.append(input("Please enter a name: "))
    more=input("Do you wish to invite more people ? y/n" )
    print("You have invited ",invited," to the party " )
    print("You have invited ",len(invited)," People to the party ")
    print(invited)
    selection=input("Please enter a name in the list")
    print(selection," is in position",invited.index(selection),"in the list. ")
    confirm=input("Do you still want them to come ? y/n")
    if confirm == "n":
        party.remove(selection)
        print(party)

        
Please enter a name: Jose guervo
Do you wish to invite more people ? y/ny
You have invited  ['Karis', 'Lily', 'James', 'Jose guervo']  to the party 
You have invited  4  People to the party 
['Karis', 'Lily', 'James', 'Jose guervo']
Please enter a name in the listLily
Lily  is in position 1 in the list. 
Do you still want them to come ? y/ny
Please enter a name: koros
Do you wish to invite more people ? y/ny
You have invited  ['Karis', 'Lily', 'James', 'Jose guervo', 'koros']  to the party 
You have invited  5  People to the party 
['Karis', 'Lily', 'James', 'Jose guervo', 'koros']
Please enter a name in the listJames
James  is in position 2 in the list. 
Do you still want them to come ? y/ny
Please enter a name: Lotis
Do you wish to invite more people ? y/ny
You have invited  ['Karis', 'Lily', 'James', 'Jose guervo', 'koros', 'Lotis']  to the party 
You have invited  6  People to the party 
['Karis', 'Lily', 'James', 'Jose guervo', 'koros', 'Lotis']
Please enter a name in the listLotis
Lotis  is in position 5 in the list. 
Do you still want them to come ? y/nn
Traceback (most recent call last):
  File "<pyshell#187>", line 11, in <module>
    party.remove(selection)
NameError: name 'party' is not defined



programmes=["Machachari","Inspkta mwala","Tahidi","Grapevine"]
for i in programmes:
    print(i)

    
Machachari
Inspkta mwala
Tahidi
Grapevine
another=input("Please enter another show" )
Please enter another show Patagonia
position=int(input("Please enter a position : "))
Please enter a position : 2
programmes.insert(position,another)
print(programmes)
['Machachari', 'Inspkta mwala', ' Patagonia', 'Tahidi', 'Grapevine']
nums_list=[]
number1=int(input("Please enter a number: "))
Please enter a number: 2
nums_list.append(number1)
print(nums_list)
[2]
num2=int(input("Please enter a number : " ))
Please enter a number : 45
nums_list.append(num2)
print(nums_list)
[2, 45]
num3=int(input("Please enter a number : " ))
Please enter a number : 56
nums_list.append(num3)
print(nums_list)
[2, 45, 56]
num5=int(input("Please enter a number
               
SyntaxError: unterminated string literal (detected at line 1)
;num5=int(input("Please enter a number: "))
               
SyntaxError: invalid syntax
num6=int(input("Please enter a number: "))
               
Please enter a number: 678
nums_list.append(num6)
               
print(nums_list)
               
[2, 45, 56, 678]
num7=int(input("Please enter a number  : "))
               
Please enter a number  : 765
nums_list.append(num7)
               
print(nums_list)
               
[2, 45, 56, 678, 765]
more=input("Do you wish to save the last number : ")
               
Do you wish to save the last number : n
if more == "n":
               nums_list.remove(num7)
               print(nums_list)

               
[2, 45, 56, 678]
