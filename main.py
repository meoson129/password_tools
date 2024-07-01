import re
import tkinter as tk

def check_password_strength(password):
    # Define regex patterns for each criteria
    length_pattern = re.compile(r".{8,}")
    uppercase_pattern = re.compile(r"[A-Z]")
    lowercase_pattern = re.compile(r"[a-z]")
    digit_pattern = re.compile(r"\d")
    special_char_pattern = re.compile(r"[!@#$%^&*]")

    # Check each criteria
    strength = 0
    if length_pattern.search(password):
        strength += 1
    if uppercase_pattern.search(password):
        strength += 1
    if lowercase_pattern.search(password):
        strength += 1
    if digit_pattern.search(password):
        strength += 1
    if special_char_pattern.search(password):
        strength += 1

    # Categorize password strength
    return strength

def on_enter(event):
    check_password()


def check_password():
    user_password = password_entry.get()
    score = check_password_strength(user_password)
    result = ""
    canvas.delete("all")
    if score == 0:
        result = "Very Weak"
    elif score == 1: 
        result = "Weak"
        canvas.create_rectangle(50, 10, 30, 30, fill="red", outline="")
    elif score == 2:
        result = "Weak"
        canvas.create_rectangle(50, 10, 60, 30, fill="red", outline="")
    elif score == 3:
        result = "Medium"
        canvas.create_rectangle(50, 10, 90, 30, fill="yellow", outline="")
    elif score == 4:
        result = "Medium"
        canvas.create_rectangle(50, 10, 120, 30, fill="yellow", outline="")
    else:
        result = "Strong"
        canvas.create_rectangle(50, 10, 150, 30, fill="green", outline="")
    result_label.config(text=f"Password strength: {result}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")  # Set window size

# Create input field
password_label = tk.Label(root, text="Enter a password:", font=("Arial", 16))
password_label.pack(pady=20)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Pressing Enter yields the result 
password_entry.bind("<Return>", on_enter)

# Create button to check password
check_button = tk.Button(root, text="Check Strength", command=check_password)
check_button.pack()

# Create label for displaying result
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()


canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()



root.mainloop()
