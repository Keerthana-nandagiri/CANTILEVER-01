import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone and email:
        contacts[name] = {"phone": phone, "email": email}
        update_listbox()
        clear_entries()
        messagebox.showinfo("Yay!", f"{name} added!")
    else:
        messagebox.showerror("Oops!", "All fields are required!")

def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        selected_text = contact_listbox.get(selected)
        name = selected_text.split(" - ")[0]
        if name in contacts:
            phone = phone_entry.get()
            email = email_entry.get()
            if phone and email:
                contacts[name] = {"phone": phone, "email": email}
                update_listbox()
                clear_entries()
                messagebox.showinfo("Updated", f"{name} updated!")
            else:
                messagebox.showerror("Oops!", "Phone and Email required!")
        else:
            messagebox.showerror("Oops!", "Contact not found.")
    else:
        messagebox.showerror("Oops!", "Choose something to update.")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        selected_text = contact_listbox.get(selected)
        name = selected_text.split(" - ")[0]
        if name in contacts:
            del contacts[name]
            update_listbox()
            clear_entries()
            messagebox.showinfo("Deleted", f"{name} removed!")
        else:
            messagebox.showerror("Oops!", "Contact not found.")
    else:
        messagebox.showerror("Oops!", "Choose something to delete.")

def update_listbox():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {info['phone']} - {info['email']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def load_selected_contact(event):
    selected = contact_listbox.curselection()
    if selected:
        selected_text = contact_listbox.get(selected)
        name, phone, email = selected_text.split(" - ")
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)
        email_entry.delete(0, tk.END)
        email_entry.insert(0, email)

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Student Contact Manager")
root.geometry("500x500")
root.config(bg="#ffe4b5")

tk.Label(root, text="Name:", font=("Comic Sans MS", 12, "bold"), bg="#ffe4b5").grid(row=0, column=0, pady=8)
name_entry = tk.Entry(root, font=("Comic Sans MS", 10), width=30)
name_entry.grid(row=0, column=1, pady=8)

tk.Label(root, text="Phone:", font=("Comic Sans MS", 12, "bold"), bg="#ffe4b5").grid(row=1, column=0, pady=8)
phone_entry = tk.Entry(root, font=("Comic Sans MS", 10), width=30)
phone_entry.grid(row=1, column=1, pady=8)

tk.Label(root, text="Email:", font=("Comic Sans MS", 12, "bold"), bg="#ffe4b5").grid(row=2, column=0, pady=8)
email_entry = tk.Entry(root, font=("Comic Sans MS", 10), width=30)
email_entry.grid(row=2, column=1, pady=8)

btn_frame = tk.Frame(root, bg="#ffe4b5")
btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

tk.Button(btn_frame, text="Add", command=add_contact, bg="#4caf50", fg="white", font=("Comic Sans MS", 10, "bold"), width=10).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Update", command=update_contact, bg="#2196f3", fg="white", font=("Comic Sans MS", 10, "bold"), width=10).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", command=delete_contact, bg="#f44336", fg="white", font=("Comic Sans MS", 10, "bold"), width=10).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Quit", command=quit_app, bg="#9c27b0", fg="white", font=("Comic Sans MS", 10, "bold"), width=10).grid(row=0, column=3, padx=5, pady=5)

contact_listbox = tk.Listbox(root, width=60, height=12, font=("Comic Sans MS", 10))
contact_listbox.grid(row=4, column=0, columnspan=2, pady=10)
contact_listbox.bind("<<ListboxSelect>>", load_selected_contact)

root.mainloop()
