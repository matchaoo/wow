import tkinter as tk
def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='ศูนย์ทุกค่าจ้า')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'        # \n ไว้ใช้ขึ้นบรรืัดใหม่

    output_label.configure(text=output)

window = tk.Tk()
window_title = ('Multiplication')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='แม่สูตรคูณ')
title_label.pack(pady=20)                               #padx pady ไว้สร้างที่ว่างมาแทรก

number_input = tk.Entry(master=window)
number_input.pack()

go_button = tk.Button(master=window, text='ได้แก่', command=show_output, width=15, height=1)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop()
