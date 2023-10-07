import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    guess = int(guess_entry.get())
    if guess == num:
        messagebox.showinfo("Result", "Congratulations! You've won!")
        reset_game()
    elif guess > num:
        messagebox.showinfo("Result", " Try a lower number.")
    else:
        messagebox.showinfo("Result", " Try a higher number.")
    guess_entry.delete(0, tk.END)
    check_chances()

def reset_game():
    global num
    num = random.randint(1, 100)
    chances_label.config(text=f"Chances left: 10")
    guess_entry.delete(0, tk.END)

    global chances
    chances = 0

def check_chances():
    global chances
    chances += 1
    if chances >= 10:
        messagebox.showinfo("Result", f"Sorry, you've run out of chances. The correct number was {num}")
        reset_game()
    else:
        chances_label.config(text=f"Chances left: {10 - chances}")

root = tk.Tk()
root.title("Number Guessing Game")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

num = random.randint(1, 100)
chances = 0

chances_label = tk.Label(root, text=f"Chances left: {10 - chances}" , fg = "darkgreen",font=("Helvetica",20,"bold"))
chances_label.pack()

intro_label = tk.Label(root, text="Guess a number between 1 and 100",fg = "darkblue",font=("Helvetica",20,"bold"))
intro_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Submit Guess", command=check_guess,fg = "purple",font=("Helvetica",20,"bold"))
guess_button.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game,fg = "blue",font=("Helvetica",20,"bold"))
reset_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit,fg = "darkgreen",font=("Helvetica",20,"bold"))
exit_button.pack()

root.mainloop()