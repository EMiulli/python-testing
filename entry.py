from tkinter import *

root = Tk()
root.title("Entry Program")
root.geometry("400x400")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)

root.mainloop()

if __name__ == "__main__":
    myClick()
