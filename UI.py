from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from rac_req import Recommender
from idlelib.tooltip import Hovertip
import pandas as pd
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x800")

def retrieve_pic():
    instruct_file = open("microservice/instructions.txt", "w")
    instruct_file.write("run")
    instruct_file.close()
    path_file = open("microservice/img_url.txt", "r")
    path = path_file.readline().strip()
    path_file.close()
    image = Image.open(path)
    resize_image = image.resize((135,231))
    img = ImageTk.PhotoImage(resize_image)
    image_label.configure(image = img)
    image_label.image = img
    return image_label

def display_inputs():
    APP_TITLE.pack()
    INSTRUCTIONS.pack()
    for idx in range(2, len(INPUT_TEXT)):
        INPUT_TEXT[idx].pack()
        INPUT_FIELDS[idx-2].pack()
    SUBMIT_B.pack(pady=(20,0))
    input_frame.pack()

def callback(input):
    if input.isdigit() or input == "" or input == ".":
        return True
    else:
        return False

def save_inputs():
    inputs["head size"] = float(input_entries[0].get())
    inputs["length"] = float(input_entries[1].get())
    inputs["strung weight"] = float(input_entries[2].get())
    inputs["weight distribution"] = input_entries[3].get()
    inputs["balance point"] = float(input_entries[4].get())
    inputs["brand"] = input_entries[5].get()
    recc = get_recommendation(inputs)
    #recc = Recommender(inputs["head size"], inputs["length"], inputs["strung weight"], inputs["weight distribution"], inputs["balance point"], inputs["brand"])
    display_results_frame(recc.get_recs())

def get_recommendation(inputs):
    recc = Recommender(inputs["head size"], inputs["length"], inputs["strung weight"], inputs["weight distribution"], inputs["balance point"], inputs["brand"])
    
    return recc

def display_results_frame(recommendations):
    input_frame.pack_forget()
    image_label = retrieve_pic()
    RESULTS.pack()
    for idx in range(5):
        result_text[idx].set(recommendations[idx])
    for result in results_arr:
        result.pack()
    image_label.pack()
    INPUT_AGAIN_B.pack(pady=(20,0))
    EXCEL_EXPORT_B.pack(pady=(20,0))
    EXIT_B.pack(pady=(20,0))
    results_frame.pack()

def clear_results():
    results_frame.pack_forget()
    input_frame.pack()

def presence_check(*args):
    if input_entries[0].get() and input_entries[1].get() and input_entries[2].get() and input_entries[3].get() and input_entries[4].get() and input_entries[5].get():
        SUBMIT_B.config(state='normal')
    else:
        SUBMIT_B.config(state='disabled')
    if weight_distribution.get() == "Balanced":
        BALANCE_POINT_I.delete(0,5)
        BALANCE_POINT_I.insert(0,"0")
        BALANCE_POINT_I.config(state='readonly')
    else:
        BALANCE_POINT_I.config(state='normal')

def export():
    recc = get_recommendation(inputs)
    recc.get_recs()
    recc.export_csv()

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
BRAND = Label(input_frame, text="Brand:", font=("Calibri", 15))
INPUT_TEXT = [APP_TITLE, INSTRUCTIONS, HEAD_SIZE, LENGTH, STRUNG_WEIGHT, WEIGHT_DISTRIBUTION, BALANCE_POINT, BRAND]
RESULTS = Label(results_frame, text="Recommendations based on your preferences:", font=("Calibri", 25))

# App buttons
SUBMIT_B = Button(input_frame, text="Submit", bg="#3c9a12", fg="white", font=("Calibri", 25), state='disabled', command=save_inputs)
INPUT_AGAIN_B = Button(results_frame, text="Input Again", bg="#3c9a12", fg="white", font=("Calibri", 25), command=clear_results)
EXCEL_EXPORT_B = Button(results_frame, text="Export racquet data as CSV", bg="#3c9a12", fg="white", font=("Calibri", 25), command=export)
EXCEL_TIP = Hovertip(EXCEL_EXPORT_B, "Export recommended racquet specs to an Excel-compatible format for spec comparison\nMust have a spreadsheet program")
EXIT_B = Button(results_frame, text="Exit", bg="#3c9a12", fg="white", font=("Calibri", 25), command=close)

# Input storage
head_size = StringVar()
length = StringVar()
strung_weight = StringVar()
weight_distribution = StringVar()
balance_point = StringVar()
brand = StringVar()
head_size.trace("w", presence_check)
length.trace("w", presence_check)
strung_weight.trace("w", presence_check)
weight_distribution.trace("w", presence_check)
balance_point.trace("w", presence_check)
brand.trace("w",  presence_check)
input_entries = [head_size, length, strung_weight, weight_distribution, balance_point, brand]

# Input fields
reg = root.register(callback)
HEAD_SIZE_I = Entry(input_frame, text="head size", textvariable=head_size , font=("Calibri", 15), width=5)
LENGTH_I = Entry(input_frame, text="length", textvariable=length, font=("Calibri", 15), width=5)
STRUNG_WEIGHT_I = Entry(input_frame, text="strung weight", textvariable=strung_weight, font=("Calibri", 15), width=5)
WEIGHT_DISTRIBUTION_I = Entry(input_frame, text="weight distribution", font=("Calibri", 15), width=12)
WEIGHT_DISTRIBUTION_D = ttk.Combobox(input_frame, text="weight distribution", textvariable=weight_distribution, font=("Calibri", 15), state="readonly", values=["Head light", "Balanced", "Head heavy"], width=12)
BALANCE_POINT_I = Entry(input_frame, text="balance point", textvariable=balance_point, font=("Calibri", 15), width=5)
BRAND_D = ttk.Combobox(input_frame, text="brand", textvariable=brand, font=("Calibri", 15), state="readonly", values=["Any Brand", "Babolat", "Dunlop", "Head", "Prince", "Technifibre", "Volkl", "Wilson", "Yonex"], width=10)
INPUT_FIELDS = [HEAD_SIZE_I, LENGTH_I, STRUNG_WEIGHT_I, WEIGHT_DISTRIBUTION_D, BALANCE_POINT_I, BRAND_D]
inputs = {}
first_result_text = StringVar()
second_result_text = StringVar()
third_result_text = StringVar()
fourth_result_text = StringVar()
fifth_result_text = StringVar()
first_result = Label(results_frame, textvariable=first_result_text, font=("Calibri", 15))
second_result = Label(results_frame, textvariable=second_result_text, font=("Calibri", 15))
third_result = Label(results_frame, textvariable=third_result_text, font=("Calibri", 15))
fourth_result = Label(results_frame, textvariable=fourth_result_text, font=("Calibri", 15))
fifth_result = Label(results_frame, textvariable=fifth_result_text, font=("Calibri", 15))
results_arr = [first_result, second_result, third_result, fourth_result, fifth_result]
result_text = [first_result_text, second_result_text, third_result_text, fourth_result_text, fifth_result_text]
image_label = Label(results_frame)

display_inputs()
root.mainloop()