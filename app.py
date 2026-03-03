import tkinter as tk
import crud

def add_item():
    item = entry.get().strip()
    if item:
        crud.create(item)
        refresh_list()
        entry.delete(0, tk.END)

def refresh_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(crud.read()):
        listbox.insert(tk.END, f"{i}: {item}")

root = tk.Tk()
root.title("CRUD Básico en Python")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

add_button = tk.Button(root, text="Agregar", command=add_item)
add_button.pack(padx=10, pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(padx=10, pady=10)

refresh_list()
root.mainloop()