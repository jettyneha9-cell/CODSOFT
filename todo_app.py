import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# ---------------- DATABASE ---------------- #
def connect_db():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            due_date TEXT,
            priority TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_task(title, due, priority):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks VALUES (NULL,?,?,?,?)",
                (title, due, priority, "Pending"))
    conn.commit()
    conn.close()

def fetch_tasks():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def mark_done(task_id):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

# ---------------- GUI ---------------- #
def add_task():
    if title_entry.get() == "":
        messagebox.showerror("Error", "Task title is required")
        return
    insert_task(title_entry.get(), date_entry.get(), priority_combo.get())
    load_tasks()
    clear_fields()

def load_tasks():
    for row in task_list.get_children():
        task_list.delete(row)

    for task in fetch_tasks():
        task_list.insert("", END, values=task)

def clear_fields():
    title_entry.delete(0, END)
    date_entry.delete(0, END)
    priority_combo.set("Medium")

def remove_task():
    selected = task_list.focus()
    if not selected:
        messagebox.showerror("Error", "Select a task")
        return
    values = task_list.item(selected, 'values')
    delete_task(values[0])
    load_tasks()

def complete_task():
    selected = task_list.focus()
    if not selected:
        messagebox.showerror("Error", "Select a task")
        return
    values = task_list.item(selected, 'values')
    mark_done(values[0])
    load_tasks()

# ---------------- UI ---------------- #
connect_db()

app = Tk()
app.title("Real World To-Do List")
app.geometry("750x500")
app.config(bg="#f2f2f2")

Label(app, text="To-Do List Application", font=("Arial", 20, "bold"), bg="#f2f2f2").pack(pady=10)

frame = Frame(app, bg="#f2f2f2")
frame.pack(pady=10)

Label(frame, text="Task", bg="#f2f2f2").grid(row=0, column=0)
title_entry = Entry(frame, width=25)
title_entry.grid(row=0, column=1)

Label(frame, text="Due Date", bg="#f2f2f2").grid(row=0, column=2)
date_entry = Entry(frame, width=15)
date_entry.grid(row=0, column=3)

Label(frame, text="Priority", bg="#f2f2f2").grid(row=0, column=4)
priority_combo = ttk.Combobox(frame, values=["High", "Medium", "Low"], width=10)
priority_combo.set("Medium")
priority_combo.grid(row=0, column=5)

Button(frame, text="Add Task", command=add_task, bg="green", fg="white").grid(row=0, column=6, padx=10)

# Table
columns = ("ID", "Title", "Due Date", "Priority", "Status")
task_list = ttk.Treeview(app, columns=columns, show="headings")

for col in columns:
    task_list.heading(col, text=col)

task_list.pack(fill=BOTH, expand=True, pady=20)

# Buttons
btn_frame = Frame(app, bg="#f2f2f2")
btn_frame.pack()

Button(btn_frame, text="Mark Completed", command=complete_task, bg="blue", fg="white").grid(row=0, column=0, padx=10)
Button(btn_frame, text="Delete Task", command=remove_task, bg="red", fg="white").grid(row=0, column=1, padx=10)

load_tasks()
app.mainloop()
