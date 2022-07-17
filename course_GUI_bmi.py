from tkinter import *
import math

def leftClickButton(event):
    labelResult.configure(text=format(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2), '.2f'))

    bmi = format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), '.2f')  #แสดงทศนิยม 2 ตำแหน่ง

    bmiList = ["ผอมเกินไป", "ปกติ", "ท้วม", "อ้วน", "อ้วนมาก"]
    bmiShow = 0

    if float(bmi) <= 18.5:
        bmiShow = bmiList[0]

    elif float(bmi) > 18.5 and float(bmi) <= 22.9:
        bmiShow = bmiList[1]

    elif float(bmi) >= 23 and float(bmi) <= 24.9:
        bmiShow = bmiList[2]

    elif float(bmi) >= 25 and float(bmi) <= 29.9:
        bmiShow = bmiList[3]

    elif float(bmi) >= 30:
        bmiShow = bmiList[4]

    labelBmi.configure(text=bmiShow)

MainWindow = Tk()
MainWindow.title = "BMI"
MainWindow.minsize(width=400, height=400)
MainWindow.maxsize(width=800, height=800)

labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)                 #click แล้วให้ทำตามฟังก์ชัน
calculateButton.grid(row=2)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

labelBmi = Label(MainWindow, text="BMI")
labelBmi.grid(row=3, column=1)

MainWindow.mainloop()