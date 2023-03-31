import random
import tkinter as tk

root = tk.Tk()
root.title("Dice Simulator")

dice_label = tk.Label(root, text="Roll the dice!")
dice_label.pack(pady=20)

def roll_dice():
    
    number = random.randint(1, 6)
    dice_label.config(text=f"You rolled a {number}!")

roll_button = tk.Button(root, text="Roll the dice!", command=roll_dice)
roll_button.pack(pady=10)

root.mainloop()
