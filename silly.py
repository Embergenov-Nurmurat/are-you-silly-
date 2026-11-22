import tkinter as tk
import random

WIDTH, HEIGHT = 400, 250
BTN_W, BTN_H = 80, 36

root = tk.Tk()
root.title("Question")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

label = tk.Label(root, text="Are you silly?", font=("Arial", 20, "bold"))
label.place(relx=0.5, y=40, anchor="center")

def on_yes():
    label.config(text="I knew it")
    yes_btn.place_forget()
    no_btn.place_forget()

yes_btn = tk.Button(root, text="Yes", font=("Arial", 12), command=on_yes)
yes_btn.place(x=100, y=170, width=BTN_W, height=BTN_H)

no_btn = tk.Button(root, text="No", font=("Arial", 12))
no_btn.place(x=220, y=170, width=BTN_W, height=BTN_H)

def move_no():
    # Pick a new random spot far enough from the mouse and away from the Yes button
    for _ in range(50):
        x = random.randint(10, WIDTH - BTN_W - 10)
        y = random.randint(80, HEIGHT - BTN_H - 10)
        mx = root.winfo_pointerx() - root.winfo_rootx()
        my = root.winfo_pointery() - root.winfo_rooty()
        far_from_mouse = abs(mx - (x + BTN_W / 2)) > 100 or abs(my - (y + BTN_H / 2)) > 80
        yes_x, yes_y = yes_btn.winfo_x(), yes_btn.winfo_y()
        overlaps_yes = abs(x - yes_x) < BTN_W + 10 and abs(y - yes_y) < BTN_H + 10
        if far_from_mouse and not overlaps_yes:
            no_btn.place(x=x, y=y)
            return

def on_motion(event):
    # Run away when the mouse gets close to the button
    bx = no_btn.winfo_x() + BTN_W / 2
    by = no_btn.winfo_y() + BTN_H / 2
    mx = root.winfo_pointerx() - root.winfo_rootx()
    my = root.winfo_pointery() - root.winfo_rooty()
    if abs(mx - bx) < 70 and abs(my - by) < 50:
        move_no()

root.bind("<Motion>", on_motion)
no_btn.bind("<Enter>", lambda e: move_no())

root.mainloop()
