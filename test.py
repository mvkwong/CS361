from tkinter import *
from PIL import Image, ImageTk

root = Tk()
path = "microservice/1.jpg"
image_file = ImageTk.PhotoImage(Image.open(path))
image_label = Label(root, image = image_file)
image_label.pack()

root.mainloop()