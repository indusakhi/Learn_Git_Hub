import tkinter as tk
from tkinter import filedialog
import webbrowser

# Create the main window
root = tk.Tk()
# Window size
root.geometry("300x300")

def on_click():
    print("Button clicked!")
def show_text():
    print("You typed:", entry.get())
def choose_file():
    file_path = filedialog.askopenfilename()
    print("Selected File:", file_path)  
def choose_config_file():
    file_path = filedialog.askopenfilename()
    print("Selected config File:", file_path)      
def open_url():
    webbrowser.open("https://www.google.com")    

# Title of the window
root.title("ENNA")
#label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
#label.pack()
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=20)
entry = tk.Entry(root, width=30)
entry.pack()
btn = tk.Button(root, text="Submit", command=show_text)
btn.pack(pady=10)
btn1 = tk.Button(root, text="Select_Campiagns", command=choose_file)
btn1.pack(pady=20)
#link = tk.Label(root, text="Open Google", fg="green", cursor="hand2")
#link.pack(pady=20)
button_config = tk.Button(root, text="Select_Config", command=choose_config_file, fg="black")
button_config.pack(pady=20)
#link.bind("<Button-1>", open_url)


# Run the window loop
root.mainloop()
