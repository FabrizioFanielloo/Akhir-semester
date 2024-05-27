import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, IntVar

# Create the main application window
root = ttk.Window(themename="superhero")

# Set the title of the window
root.title("Crazy ttkbootstrap Example")

# Set the size of the window
root.geometry("400x300")

# Variable to keep track of the selected theme
theme_var = StringVar(value="superhero")

# Function to change the label text when button is clicked
def on_button_click():
    label.config(text="Button Clicked!")
    progress['value'] = 0
    root.after(100, increment_progress)

# Function to increment the progress bar
def increment_progress():
    if progress['value'] < 100:
        progress['value'] += 10
        root.after(100, increment_progress)

# Function to change the theme
def change_theme(event):
    root.style.theme_use(theme_var.get())

# Function to change the label font size
def change_font_size(event):
    label.config(font=("Helvetica", font_size_var.get()))

# Create a label widget
label = ttk.Label(root, text="Hello, ttkbootstrap!", font=("Helvetica", 16))
label.pack(pady=10)

# Create a button widget
button = ttk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Create a progress bar
progress = ttk.Progressbar(root, bootstyle=SUCCESS, maximum=100)
progress.pack(pady=10, fill=X, padx=20)

# Create a dropdown menu for theme selection
theme_label = ttk.Label(root, text="Select Theme:")
theme_label.pack(pady=5)

themes = ["superhero", "darkly", "flatly", "morph", "pulse"]
theme_menu = ttk.Combobox(root, textvariable=theme_var, values=themes)
theme_menu.pack(pady=5)
theme_menu.bind("<<ComboboxSelected>>", change_theme)

# Create a slider to adjust label font size
font_size_var = IntVar(value=16)
font_size_slider = ttk.Scale(root, from_=10, to=30, variable=font_size_var, orient=HORIZONTAL, command=change_font_size)
font_size_slider.pack(pady=10, fill=X, padx=20)

# Run the application
root.mainloop()