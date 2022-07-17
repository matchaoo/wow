from tkinter import *

def sayHelloWorld():
    print("Say Hello World")

mainWindow = Tk()
mainWindow.title("Test Py")
mainWindow.minsize(width=400, height=400)
mainWindow.maxsize(width=800, height=800)

button = Button(mainWindow, text="Click me", command=sayHelloWorld, width=20)
button.place(x = 50, y = 20)

button = Button(mainWindow, text="Click me", command=sayHelloWorld).grid(row=1)

label = Label(mainWindow, text="Hello World", width=20, fg= "red", bg= "blue", font=("Helvetica", 24)).grid(row=0, column=1)


mainWindow.mainloop()
