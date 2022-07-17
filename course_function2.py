def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "1" and passwordInput == "1":
        return showMenu()
    else:
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        totalPrice = int(input("total price : "))
        print(vatCalculate(totalPrice))
    elif userSelected == 2:
        print(priceCalculate())
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result  #ค่าจากการ return จะส่งกลับไปยังตัวที่เรียก function มันมา
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    result = price1+price2
    print("total price : ",result)
    return print(vatCalculate(result))




login()