import tkinter as tk
from tkinter import ttk, messagebox
from password_utils import PasswordGenerator
import pyperclip

DEFAULT_USER = "boian.e.p@gmail.com"
PASSFILE="Day_29_passwd_manager/data.txt"

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master, padx=50, pady=50)
        self.web_var = tk.StringVar(value="")
        self.user_var = tk.StringVar(value=DEFAULT_USER)
        self.pass_var = tk.StringVar(value="")
        self.create_widgets()
        self.layout_widgets()
        self.pgen = PasswordGenerator()
        

    def create_widgets(self):
        #creating the canvas with the logo
        self.canvas = tk.Canvas(self, width=200, height=200)
        self.lock_img = tk.PhotoImage(file=r"Day_29_passwd_manager\logo.png")
        self.canvas.create_image(100, 100, image=self.lock_img, anchor="center")

        #creating the entry labels
        self.web_label = ttk.Label(self, text="Website: ")
        self.user_label = ttk.Label(self, text="Email/Username: ")
        self.pass_label = ttk.Label(self, text="Password: ")

        #creating the entry boxes
        self.web_entry = ttk.Entry(self, textvariable=self.web_var, width=40)
        self.user_entry = ttk.Entry(self, textvariable=self.user_var, width=40)
        self.pass_entry = ttk.Entry(self, textvariable=self.pass_var, width=21)

        #creating the buttons
        self.add_button = ttk.Button(self, text="Add", width=40, command=self._write_password)
        self.generate_button = ttk.Button(self, text="Generate Password", width=17, command=self._generate_password)
 
    def layout_widgets(self):
        #placing the canvas
        self.canvas.grid(row=0, column=0, columnspan=3, pady=10, sticky='n')

        #placing the labels
        self.web_label.grid(row=1, column=0, padx=2, pady=5, sticky="e")
        self.user_label.grid(row=2, column=0, padx=2, pady=5, sticky="e")
        self.pass_label.grid(row=3, column=0, padx=2, pady=5, sticky="e")

        #placing the entry boxes
        self.web_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=5, sticky="w")
        self.web_entry.focus()
        self.user_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=5, sticky="w")
        self.pass_entry.grid(row=3, column=1, padx=2, pady=5, sticky="w")

        #placing the buttons
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="w")
        self.generate_button.grid(row=3, column=2, columnspan=1, sticky='w')
    
    def _write_password(self):
        if self._check_for_blanks() and self._confirm():
            print("confirmed")
            with open(PASSFILE, "a", encoding="utf-8") as f:
                f.write(
                    f"{self.web_var.get()}|{self.user_var.get()}|{self.pass_var.get()}\n"
                )
            self._reset()
    
    def _reset(self):
        self.web_var.set("")
        self.user_var.set(DEFAULT_USER)
        self.pass_var.set("")
    
    def _generate_password(self):
        self.pass_var.set(self.pgen.generate())
        pyperclip.copy(self.pass_var.get())
    
    def _confirm(self) -> bool:
        """Ask the user to confirm the entered credentials before saving."""
        title = self.web_var.get()

        message = (
            "Confirm data:\n\n\n"
            f"Website:         {self.web_var.get()}\n\n"
            f"Email/Username:  {self.user_var.get()}\n\n"
            f"Password:        {self.pass_var.get()}\n\n"
        )
        return messagebox.askyesno(title=title, message=message)

    def _check_for_blanks(self) -> bool:
        if (self.web_var.get() == "" or
            self.user_var.get() == "" or
            self.pass_var.get() == ""
        ):
            messagebox.showerror(title="Missing values", message="Please do not leave any fields blank.")
            return False
        return True


        