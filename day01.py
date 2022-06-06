import sys

print("Day 1 - String Manipulation")
print("String Concatenation is done with the", '"+"', "sign.")
print("e.g. print('Hello' + 'World')")
print("New lines can be created witht a backslash and n.")
print("-------------------------------------------------")

print("Hello",input("What is you name: "))
print("-------------------------------------------------")

var = input("Enter you name to get the wordcount: ").replace(" ",'')
print('Word Count: ',len(var))
print('Size in bytes: ',sys.getsizeof(var))
print("-------------------------------------------------")

a = input("a: ")
b = input("b: ")
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)
print("-------------------------------------------------") 

print("Welcome to BAND NAME GENERATOR!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What was the name of your first pet?\n")
print("The name of your band could be: ", city, pet)