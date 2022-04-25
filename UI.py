from tkinter import *
from rac_req import Recommender

root = Tk()
root.geometry("600x600")

def callback(input):
    if input.isdigit() or input == "" or input == ".":
        return True
    else:
        return False

def save_inputs():
    for field in INPUT_FIELDS:
        field_text = field.cget("text")
        if field_text != "weight distribution":
            inputs[field_text] = float(field.get())
        else:
            inputs[field_text] = field.get()
        #error = Label(root, text=(field.cget("text") + " is empty or is not a number. Please re-enter."))
        #if field.get().isdecimal() is False and field.get().isnumeric() is False:
        #    error.pack()
    recc = Recommender(inputs["head size"], inputs["length"], inputs["strung weight"], inputs["weight distribution"], inputs["balance point"])
    print(recc.get_recs())
    print(inputs)

# App text
APP_TITLE = Label(root, text="Racquet Recommender", font=("Calibri", 40))
INSTRUCTIONS = Label(root, text="Enter your preferred:", font=("Calibri", 25))
HEAD_SIZE = Label(root, text="Head size (sq. in.):", font=("Calibri", 15))
LENGTH = Label(root, text="Length (in.):", font=("Calibri", 15))
STRUNG_WEIGHT = Label(root, text="Strung weight (g):", font=("Calibri", 15))
WEIGHT_DISTRIBUTION = Label(root, text="Weight distribution:", font=("Calibri", 15))
BALANCE_POINT = Label(root, text="Balance point:", font=("Calibri", 15))
INPUT_TEXT = [APP_TITLE, INSTRUCTIONS, HEAD_SIZE, LENGTH, STRUNG_WEIGHT, WEIGHT_DISTRIBUTION, BALANCE_POINT]

# App buttons
SUBMIT_B = Button(root, text="SUBMIT", bg="#3c9a12", fg="white", font=("Calibri", 25), command=save_inputs)

# Input fields
reg = root.register(callback)
HEAD_SIZE_I = Entry(root, text="head size", font=("Calibri", 15), width=5)
LENGTH_I = Entry(root, text="length", font=("Calibri", 15), width=5)
STRUNG_WEIGHT_I = Entry(root, text="strung weight", font=("Calibri", 15), width=5)
WEIGHT_DISTRIBUTION_I = Entry(root, text="weight distribution", font=("Calibri", 15), width=5)
BALANCE_POINT_I = Entry(root, text="balance point", font=("Calibri", 15), width=5)
INPUT_FIELDS = [HEAD_SIZE_I, LENGTH_I, STRUNG_WEIGHT_I, WEIGHT_DISTRIBUTION_I, BALANCE_POINT_I]
inputs = {}
#for field in INPUT_FIELDS:
#    field.config(validate="key", validatecommand=(reg, '%P'))

# Retrieve recommendations


# Display GUI
APP_TITLE.pack()
INSTRUCTIONS.pack()
for idx in range(2, len(INPUT_TEXT)):
    INPUT_TEXT[idx].pack()
    INPUT_FIELDS[idx-2].pack()
SUBMIT_B.pack(pady=(20,0))

root.mainloop()