mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)
#ordered
#immutable
#allow duplicate

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Access Tuple Elements
print(mytuple[1])
print(mytuple[2:5])


#Tuple Methods
#1.Tuple Length
print(len(mytuple))

#2.count()
#thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(mytuple.count("apple"))

#3.index()
print(mytuple.index("apple")) #returns first occurence of the value
