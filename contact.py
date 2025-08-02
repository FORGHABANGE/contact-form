import tkinter as tk
from tkinter import messagebox
import csv
import re  # For email validation

# Create the main application window
window = tk.Tk()
window.title("Contact Form")
window.geometry("400x500")
window.resizable(False, False)

# Title Label
tk.Label(window, text="Contact Us", font=("Arial", 16, "bold")).pack(pady=10)

# --- Input Fields ---
tk.Label(window, text="Full Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(window, width=30, font=("Arial", 12))
name_entry.pack()

tk.Label(window, text="Email:", font=("Arial", 12)).pack(pady=5)
email_entry = tk.Entry(window, width=30, font=("Arial", 12))
email_entry.pack()

tk.Label(window, text="Phone:", font=("Arial", 12)).pack(pady=5)
phone_entry = tk.Entry(window, width=30, font=("Arial", 12))
phone_entry.pack()

tk.Label(window, text="Message:", font=("Arial", 12)).pack(pady=5)
message_entry = tk.Text(window, width=30, height=5, font=("Arial", 12))
message_entry.pack()

# --- Submit Function with Email Validation ---
def submit():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    message = message_entry.get("1.0", "end").strip()

    # Validate email using regex
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    # Ensure all fields are filled
    if not (name and email and phone and message):
        messagebox.showwarning("Missing Info", "Please fill in all the fields.")
        return

    # Save data to CSV
    with open("contacts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, message])

    messagebox.showinfo("Success", "Your message has been sent!")

    # Clear the fields
    name_entry.delete(0, "end")
    email_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    message_entry.delete("1.0", "end")

# --- Submit Button ---
tk.Button(window, text="Submit", command=submit, font=("Arial", 12)).pack(pady=20)

# Start the GUI event loop
window.mainloop()
