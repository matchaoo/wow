x = int(input("x: "))
y = int(input("y: "))

def plus(x,y):
    print(str(x), "+", str(y), "=", x+y)

def minus(x,y):
    print(str(x), "-", str(y), "=", x-y)

def mulitiply(x,y):
    print(str(x), "x", str(y), "=", x*y)

def divide(x,y):
    print(str(x), "/", str(y), "=", (x/y))

def AddNumber(x,y):
    plus(x,y)
    minus(x,y)
    mulitiply(x,y)
    divide(x,y)

AddNumber(x,y)
