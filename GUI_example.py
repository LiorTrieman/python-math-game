from tkinter import *

root = Tk()
root.title("Tip & Bill Calculator")

totaltxt = Label(root, text="Total", font=("Helvitca", 16))
tiptxt = Label(root, text="Tip (%)", font=("Helvitca", 16))
peopletxt = Label(root, text="people", font=("Helvitca", 16))

totaltxt.grid(row=0, sticky=E)
tiptxt.grid(row=1, sticky=E)
peopletxt.grid(row=2, sticky=E)

totalentry = Entry(root)
tipentry = Entry(root)
peopleentry = Entry(root)

totalentry.grid(row=0, column=2)
tipentry.grid(row=1, column=2)
peopleentry.grid(row=2, column=2)

ans = Label(root, text = "ANS")
ans.grid(row=4)

def answer(event):
    data1 = totalentry.get()
    data2 = tipentry.get()
    data3 = peopleentry.get()
    if tipentry.get() == 0:
        ans.configure(str((data1/data3)), text="per person")
        return
    elif data1 == 0:
        ans.configure(text="Specify the total")
        return
    elif data3 == 0 or data3 ==1:
        ans.configure(str(data1*(data2/100+1)))
        return
    elif data1 == 0 and data2 == 0 and data3 ==0:
        ans.configure(text = "Specify the values")
        return
    else:
        ans.configure(str((data1*(data2/100+1)/data3)), text="per person")
        return

bf = Frame(root)
bf.grid(row=3, columnspan=3)
calc = Button(bf, text ="Calculate", fg = "black", command = answer)
calc.bind("<Button-1>", answer)
calc.grid(row=3, column=2)
mainloop()