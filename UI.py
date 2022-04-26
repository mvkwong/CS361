from tkinter import *
from rac_req import Recommender
from idlelib.tooltip import Hovertip

root = Tk()
root.geometry("1200x600")

# Display GUI
def display_inputs():
    #results_frame.destroy()
    APP_TITLE.pack()
    INSTRUCTIONS.pack()
    for idx in range(2, len(INPUT_TEXT)):
        INPUT_TEXT[idx].pack()
        INPUT_FIELDS[idx-2].pack()
    SUBMIT_B.pack(pady=(20,0))
    input_frame.pack()

def clear_results():
    results_frame.destroy()
    display_inputs()

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
    display_results_frame(recc.get_recs())
    print(recc.get_recs())
    print(inputs)

def display_results_frame(recommendations):
    input_frame.destroy()
    RESULTS.pack()
    rec_num = 1
    #rec_labels = []
    for rec in recommendations:
        label_text = str(rec_num) + ". " + recommendations[rec_num-1]
        #rec_labels.append(Label(results_frame, text=label_text, font=("Calibri", 15)))
        Label(results_frame, text=label_text, font=("Calibri", 15)).pack()
        rec_num += 1
    #for rec_label in rec_labels:
    #    rec_label.pack()
    INPUT_AGAIN_B.pack(pady=(20,0))
    EXCEL_EXPORT_B.pack(pady=(20,0))
    EXIT_B.pack(pady=(20,0))
    results_frame.pack()

def close():
    root.quit()

input_frame = Frame(root)
results_frame = Frame(root)

# App text
APP_TITLE = Label(input_frame, text="Racquet Recommender", font=("Calibri", 40))
INSTRUCTIONS = Label(input_frame, text="Enter your preferred:", font=("Calibri", 25))
HEAD_SIZE = Label(input_frame, text="Head size (sq. in.):", font=("Calibri", 15))
LENGTH = Label(input_frame, text="Length (in.):", font=("Calibri", 15))
STRUNG_WEIGHT = Label(input_frame, text="Strung weight (g):", font=("Calibri", 15))
WEIGHT_DISTRIBUTION = Label(input_frame, text="Weight distribution:", font=("Calibri", 15))
BALANCE_POINT = Label(input_frame, text="Balance point:", font=("Calibri", 15))
INPUT_TEXT = [APP_TITLE, INSTRUCTIONS, HEAD_SIZE, LENGTH, STRUNG_WEIGHT, WEIGHT_DISTRIBUTION, BALANCE_POINT]
RESULTS = Label(results_frame, text="Recommendations based on your preferences:", font=("Calibri", 25))
#REC_1 = Label(results_frame, text="1. ", font=("Calibri", 15)))

# App buttons
SUBMIT_B = Button(input_frame, text="Submit", bg="#3c9a12", fg="white", font=("Calibri", 25), command=save_inputs)
INPUT_AGAIN_B = Button(results_frame, text="Input Again", bg="#3c9a12", fg="white", font=("Calibri", 25), command=lambda:display_inputs)
EXCEL_EXPORT_B = Button(results_frame, text="Export to Excel", bg="#3c9a12", fg="white", font=("Calibri", 25))
EXCEL_TIP = Hovertip(EXCEL_EXPORT_B, "Export detailed racquet specs to an Excel-compatible format for data-centric comparison\nMust have a spreadsheet program")
EXIT_B = Button(results_frame, text="Exit", bg="#3c9a12", fg="white", font=("Calibri", 25), command=close)

# Input fields
reg = root.register(callback)
HEAD_SIZE_I = Entry(input_frame, text="head size", font=("Calibri", 15), width=5)
LENGTH_I = Entry(input_frame, text="length", font=("Calibri", 15), width=5)
STRUNG_WEIGHT_I = Entry(input_frame, text="strung weight", font=("Calibri", 15), width=5)
WEIGHT_DISTRIBUTION_I = Entry(input_frame, text="weight distribution", font=("Calibri", 15), width=12)
BALANCE_POINT_I = Entry(input_frame, text="balance point", font=("Calibri", 15), width=5)
INPUT_FIELDS = [HEAD_SIZE_I, LENGTH_I, STRUNG_WEIGHT_I, WEIGHT_DISTRIBUTION_I, BALANCE_POINT_I]
inputs = {}
#for field in INPUT_FIELDS:
#    field.config(validate="key", validatecommand=(reg, '%P'))

display_inputs()
root.mainloop()