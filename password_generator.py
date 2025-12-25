from tkinter import *
from tkinter import messagebox
import random
import string

# Main window
app = Tk()
app.title("Password Generator")
app.geometry("400x250")
app.resizable(False, False)

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(length))

        result_entry.delete(0, END)
        result_entry.insert(0, password)

    except:
        messagebox.showerror("Error", "Please enter a valid number")

# UI Design
Label(app, text="Password Generator", font=("Arial", 18, "bold")).pack(pady=10)

frame = Frame(app)
frame.pack(pady=10)

Label(frame, text="Password Length:").grid(row=0, column=0, padx=5)
length_entry = Entry(frame, width=10)
length_entry.grid(row=0, column=1)

Button(frame, text="Generate", command=generate_password, bg="green", fg="white").grid(row=0, column=2, padx=10)

Label(app, text="Generated Password:").pack(pady=5)

result_entry = Entry(app, width=30, font=("Arial", 12))
result_entry.pack(pady=5)

app.mainloop()
