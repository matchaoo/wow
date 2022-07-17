fruit = {"apple", "banana", "orange"}
print(fruit)
fruit.add("grape")
print(fruit)
fruit.remove("apple")
print(fruit)
fruit.clear()
print(fruit)

userInput = int(input("Enter Number of Your Favorites Fruits :"))
myFruits = set()
while(len(myFruits)<userInput):
    myFruits.add(input("Fruits : ")) 