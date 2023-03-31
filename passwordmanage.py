import tkinter as tk

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    with open("passwords.txt", "a") as f:
        f.write(f"{website} | {username} | {password}\n")

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Manager")

website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0, padx=10, pady=10)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)

website_entry = tk.Entry(root, width=30)
website_entry.grid(row=0, column=1)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1)

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
