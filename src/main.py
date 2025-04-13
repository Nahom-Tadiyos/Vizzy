import pandas as pd
import customtkinter as ct

selected_graph_type = None
filename = "No file uploaded"
insert = "None"
data = "None"

app = ct.CTk()
app.title("Vizzy")
app.geometry("900x700")

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)

def load_csv():
    global filename, data
    filename = ct.filedialog.askopenfilename()
    if filename.endswith('.csv'):
        data = pd.read_csv(filename)
        filename_text.configure(text=filename if filename else "No file uploaded")
        preview_box.delete("0.0", "end") #Delete everything inside the box
        preview_box.insert("0.0", data.head().to_string()) #Prints the df.head
        no_data_label.configure(text="")
    else:
        filename_text.configure(text="Please upload a CSV file.")
        preview_box.delete("0.0", "end")
        no_data_label.configure(text="No data to visualize")

def selectGraphCombo(choice):
    global selected_graph_type
    selected_graph_type = choice
    print("Selected graph type:", selected_graph_type)

nav_frame = ct.CTkFrame(app, height=40)
nav_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

home_button = ct.CTkButton(nav_frame, text="Home", width=80)
home_button.grid(row=0, column=0, padx=5, pady=5)

visualize_button = ct.CTkButton(nav_frame, text="Visualize", width=80)
visualize_button.grid(row=0, column=1, padx=5, pady=5)

predict_button = ct.CTkButton(nav_frame, text="Predict", width=80)
predict_button.grid(row=0, column=2, padx=5, pady=5)

export_button = ct.CTkButton(nav_frame, text="Export", width=80)
export_button.grid(row=0, column=3, padx=5, pady=5)

left_frame = ct.CTkFrame(app, width=200)
left_frame.grid(row=1, column=0, sticky="ns")

upload_file_label = ct.CTkLabel(left_frame, text="Upload CSV File", anchor="w")
upload_file_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

upload_file_btn = ct.CTkButton(left_frame, text="Choose file", command=lambda: load_csv())
upload_file_btn.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

filename_text = ct.CTkLabel(left_frame, text=filename, text_color="black", fg_color="transparent", anchor="w")
filename_text.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

chart_type_label = ct.CTkLabel(left_frame, text="Chart Type", anchor="w")
chart_type_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

select_graph_combo = ct.CTkComboBox(left_frame, values=["Line", "Bar", "Scatter", "Pie"], command=selectGraphCombo)
select_graph_combo.grid(row=4, column=0, padx=10, pady=(5, 10), sticky="ew")

right_frame = ct.CTkFrame(app)
right_frame.grid(row=1, column=1, rowspan=2, sticky="nsew")
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_rowconfigure(1, weight=1)

data_preview_label = ct.CTkLabel(right_frame, text="Data Preview", font=ct.CTkFont(size=20, weight="bold"), anchor="w")
data_preview_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

preview_box = ct.CTkTextbox(right_frame, width=800, height=200)
preview_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

visualization_label = ct.CTkLabel(right_frame, text="Visualization", font=ct.CTkFont(size=20, weight="bold"), anchor="w")
visualization_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

visualization_frame = ct.CTkFrame(right_frame)
visualization_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

no_data_label = ct.CTkLabel(visualization_frame, text="No data to visualize", text_color="gray")
no_data_label.pack(expand=True)

export_visualization_button = ct.CTkButton(visualization_frame, text="Export", width=80, anchor="e")
export_visualization_button.pack(side="right", padx=5, pady=5)

app.mainloop()