from tkinter import *
import backend

def viewCommand():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def searchEntry():
    list1.delete(0, END)
    for row in backend.search(titleText.get(), authorText.get(), yearText.get(), isbnText.get()):
        list1.insert(END, row)

def addEntry():
    backend.insert(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    list1.delete(0, END)
    list1.insert(END, (titleText.get(), authorText.get(), yearText.get(), isbnText.get()))

window = Tk()

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

titleText = StringVar()
e1 = Entry(window, textvariable = titleText)
e1.grid(row = 0, column = 1)


authorText = StringVar()
e2 = Entry(window, textvariable = authorText)
e2.grid(row = 0, column = 3)


yearText = StringVar()
e2 = Entry(window, textvariable = yearText)
e2.grid(row = 1, column = 1)


isbnText = StringVar()
e2 = Entry(window, textvariable = isbnText)
e2.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "View All", width = 12, command = viewCommand)
b1.grid(row = 2, column = 3)


b2 = Button(window, text = "Search Entry", width = 12, command = searchEntry)
b2.grid(row = 3, column = 3)


b3 = Button(window, text = "Add Entry", width = 12, command = addEntry)
b3.grid(row = 4, column = 3)


b4 = Button(window, text = "Update Selected", width = 12)
b4.grid(row = 5, column = 3)


b5 = Button(window, text = "Delete Selected", width = 12)
b5.grid(row = 6, column = 3)


b6 = Button(window, text = "Close", width = 12)
b6.grid(row = 7, column = 3)


window.mainloop()