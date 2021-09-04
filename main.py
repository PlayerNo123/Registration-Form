from tkinter import *
root = Tk()
root.geometry("600x400")

def getvals():
    print("Accepted")


Label(root, text="Registration Form by PlayerNo123", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
age = Label(root, text="Age")
gender = Label(root, text="Gender")
email = Label(root, text="Email")
phone = Label(root, text="Phone")

name.grid(row=1, column=2)
age.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
phone.grid(row=5, column=2)

namevalue = StringVar
agevalue = StringVar
gendervalue = StringVar
emailvalue = StringVar
phonevalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
ageentry = Entry(root, textvariable=agevalue)
genderentry = Entry(root, textvariable=gendervalue)
emailentry = Entry(root, textvariable=emailvalue)
phoneentry = Entry(root, textvariable=phonevalue)

nameentry.grid(row=1, column=3)
ageentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
phoneentry.grid(row=5, column=3)

#
checkbtn = Checkbutton(text="Remember me", variable = checkvalue)
checkbtn.grid(row=6, column= 3)

#
Button(text="Sumbit", command=getvals).grid(row=7, column=3)

root.mainloop()