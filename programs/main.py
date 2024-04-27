import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create a label
label = tk.Label(window, text="Hello, GUI!")
label.pack()

# Create a button
button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

# Start the main event loop
window.mainloop()
