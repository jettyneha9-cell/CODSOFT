from tkinter import *
from tkinter import messagebox

# Main Window
app = Tk()
app.title("Contact Manager")
app.geometry("700x500")
app.resizable(False, False)

contacts = []

# --------- FUNCTIONS ---------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required")
        return

    contacts.append([name, phone, email, address])
    show_contacts()
    clear_fields()

def show_contacts():
    listbox.delete(0, END)
    for c in contacts:
        listbox.insert(END, c[0] + " - " + c[1])

def search_contact():
    keyword = search_entry.get()
    listbox.delete(0, END)

    for c in contacts:
        if keyword.lower() in c[0].lower() or keyword in c[1]:
            listbox.insert(END, c[0] + " - " + c[1])

def select_contact(event):
    try:
        index = listbox.curselection()[0]
        selected = contacts[index]

        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)

        name_entry.insert(0, selected[0])
        phone_entry.insert(0, selected[1])
        email_entry.insert(0, selected[2])
        address_entry.insert(0, selected[3])
    except:
        pass

def update_contact():
    try:
        index = listbox.curselection()[0]
        contacts[index] = [
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get()
        ]
        show_contacts()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a contact to update")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        contacts.pop(index)
        show_contacts()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a contact to delete")

def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# --------- UI DESIGN ---------
Label(app, text="Contact Management System", font=("Arial", 18, "bold")).pack(pady=10)

frame = Frame(app)
frame.pack()

Label(frame, text="Name").grid(row=0, column=0)
Label(frame, text="Phone").grid(row=1, column=0)
Label(frame, text="Email").grid(row=2, column=0)
Label(frame, text="Address").grid(row=3, column=0)

name_entry = Entry(frame, width=30)
phone_entry = Entry(frame, width=30)
email_entry = Entry(frame, width=30)
address_entry = Entry(frame, width=30)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

Button(frame, text="Add", width=12, command=add_contact, bg="green", fg="white").grid(row=4, column=0, pady=10)
Button(frame, text="Update", width=12, command=update_contact, bg="blue", fg="white").grid(row=4, column=1)
Button(frame, text="Delete", width=12, command=delete_contact, bg="red", fg="white").grid(row=4, column=2)

search_entry = Entry(app, width=40)
search_entry.pack(pady=10)

Button(app, text="Search", command=search_contact).pack()

listbox = Listbox(app, width=50, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_contact)

app.mainloop()
