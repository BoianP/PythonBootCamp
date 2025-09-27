import tkinter as tk
from app import App

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("My Password Generator")

app = App(root)
app.pack(fill="both", expand=True)

root.mainloop()