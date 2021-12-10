from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Dimenciones")
root.geometry("800x500")

my_pic = Image.open("GUI/icons/multimedia.png")
resized = my_pic.resize((300,225), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
my_label = Label(root, image = new_pic)
my_label.pack(pady = 20)
root.mainloop()