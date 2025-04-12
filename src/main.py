import pandas as pd
import customtkinter as ct

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
     else:
          filenameText.configure(text="Please upload a CSV file.")

uploadFilebtn = ct.CTkButton(app, text="Upload CSV", command=load_csv)
uploadFilebtn.pack()

filenameText = ct.CTkLabel(app, text_color="black", fg_color="transparent", text=filename)
filenameText.pack()








app.mainloop()