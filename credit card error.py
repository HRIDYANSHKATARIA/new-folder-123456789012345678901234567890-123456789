from tkinter import *

root = Tk()
root.title("Error of credit card")
root.geometry("600x200")

input_box = Entry(root)
input_box.pack()

def ():
   
    get_input = input_box.get()
    try:
        print(get_input)
    except(type_error):
        message.showinfo("error","can't verify number")
        
button = Button(root,text="Verify",command=addition)
button.pack()        
root.mainloop()