import pandas as pd
from customtkinter import *
import customtkinter as ct
import tktable as tb

selected_graph_type = None
filename = "No file uploaded"
insert = "None"
data = "None"

app = ct.CTk()
app.title("Vizzy")
app.geometry("900x700")

def load_csv():
     global filename, data
     filename = ct.filedialog.askopenfilename()
     if filename.endswith('.csv'):
          data = pd.read_csv(filename)
          filenameText.configure(text=filename if filename else "No file uploaded")

          previewBox.delete("0.0", "end")
          previewBox.insert("0.0", data.head().to_string()) #Inserts the df.head into the textbox

     else:
          filenameText.configure(text="Please upload a CSV file.")


def selectGraphCombo(choice):
    global selected_graph_type
    selected_graph_type = choice
    print("Selected graph type:", selected_graph_type)

def previewData():
     tb.Table()


uploadFilebtn = ct.CTkButton(app, text="Upload CSV", command=load_csv)
uploadFilebtn.pack()

filenameText = ct.CTkLabel(app, text_color="black", fg_color="transparent", text=filename)
filenameText.pack()

selectGraphComboBox = ct.CTkComboBox(app, values=["Line", "Bar", "Scatter", "Pie"], command=selectGraphCombo)
selectGraphComboBox.pack()

previewBox = ct.CTkTextbox(app, width=800, height=200)
previewBox.pack()








app.mainloop()