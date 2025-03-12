import tkinter as tk
from tkinter import messagebox

def love_response():
    messagebox.showinfo("Response", "I love you too! ❤️")

def move_no_button(event):
    """Move the 'No' button to a random location when hovered over."""
    import random
    new_x = random.randint(50, 300)
    new_y = random.randint(50, 300)
    no_button.place(x=new_x, y=new_y)

# Create the main window
root = tk.Tk()
root.title("Do You Love Me?")
root.geometry("400x300")

# Create the question label
question_label = tk.Label(root, text="Do you love me?", font=("Arial", 14))
question_label.pack(pady=20)

# Create the "Yes" button
yes_button = tk.Button(root, text="Yes", font=("Arial", 12), command=love_response)
yes_button.pack(pady=10)

# Create the "No" button with a trick
no_button = tk.Button(root, text="No", font=("Arial", 12))
no_button.place(x=150, y=150)

# Bind hover event to move the "No" button
no_button.bind("<Enter>", move_no_button)

# Run the Tkinter event loop
root.mainloop()