fruits = ["apple ","oranges","banana","mango"]
animals = ("cat","rat","monkey")
states:{"AP","TS","DL","KA","TN"}

print(fruits[1])
fruits.append("kiwvi")
print(fruits)
fruits.remove("mango")
print(fruits)
fruits.reverse()
print(fruits)
"""count of list"""
print(fruits.count('banana')) 
print(len(fruits))

for x in fruits:
    print(x)
    print('a',x.isalnum())
    print('b',x.isalpha())
    checkapple = "apple" in x; """check value """
    print(x[2:4]); """split the postion"""
    print(x.strip())
    print(x.split(','))
   
    print(checkapple)
    checknotapple = "mango" not in x
    print(checknotapple)
    print(x)
