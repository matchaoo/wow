username_input = input("Username: ")
password_input = input("Password: ")

while username_input != "customer1" or password_input != "1234":
    print("Invalid username or password")
    print("Try again")
    username_input = input("Username: ")
    password_input = input("Password: ")

print("---------------------")
print("Welcome to Aigoo shop")
print("Please select category")
print(">>>")
print("1. Animals Doll")
print("2. Fruit Doll")
print(">>>")

select_category = int(input("Select Category Number: "))

if select_category == 1:
    print("Item list")
    print("1. Rabbit doll   159 THB")
    print("2. Puppy doll    129 THB")
    print("3. Fish doll     109 THB")
    print("4. Tiger doll    169 THB")
    print("5. Parrot doll   169 THB")
    print(">>>")

    doll_select = int(input("Please select your item: "))
    amount = int(input("Amount: "))
    print("------------------------")

    if doll_select == 1:
        total = amount*159
        print("Total", total, "THB")

    elif doll_select == 2:
        total = amount*129
        print("Total", total, "THB")

    elif doll_select == 3:
        total = amount*109
        print("Total", total, "THB")

    elif doll_select == 4:
        total = amount*169
        print("Total", total, "THB")

    elif doll_select == 5:
        total = amount*169
        print("Total", total, "THB")

    else:
        print("Try again")

elif select_category == 2:
    print("Item list")
    print("1. Banana doll    89 THB")
    print("2. Apple doll     99 THB")
    print("3. Cherry doll   109 THB")
    print("4. Coconut doll   89 THB")
    print("5. Grape doll     99 THB")
    print(">>>")

    fruit_select = int(input("Please select your item: "))
    amount = int(input("Amount: "))
    print("------------------------")
    if fruit_select == 1:
        total = amount * 89
        print("Total", total, "THB")

    elif fruit_select == 2:
        total = amount * 99
        print("Total", total, "THB")

    elif fruit_select == 3:
        total = amount * 109
        print("Total", total, "THB")

    elif fruit_select == 4:
        total = amount * 89
        print("Total", total, "THB")

    elif fruit_select == 5:
        total = amount * 99
        print("Total", total, "THB")

    else:
        print("Try agian")


