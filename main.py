import re
import tkinter as tk
from tkinter import messagebox

# password strength check conditions
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your password is secure!"


# GUI function
def check_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return
    
    result = check_password_strength(password)
    result_label.config(text=result)


# GUI Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Title
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check Password", command=check_strength)
check_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

# Run GUI
root.mainloop()