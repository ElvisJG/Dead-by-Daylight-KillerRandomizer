import tkinter as Tk
from random import randint

frame = Tk.Tk()

lbl = Tk.Label(
    frame,
    text=""
)
lbl.pack()


def roll6():

    # Dictionary of killers, to add a future killer simply iterate up by one and associate that number to the new killers name

    killers = {
        1: "Trapper",
        2: "Wraith",
        3: "Hillbilly",
        4: "Nurse",
        5: "Huntress",
        6: "Legion",
        7: "Michael",
        8: "Hag",
        9: "Cannibal",
        10: "Doctor",
        11: "Freddy",
        12: "Pig",
        13: "Clown",
        14: "Spirit",
        15: "Plague"
    }

    # Make sure to change the max randint (currently set to 15) to the highest number in the dictionary!
    # Currently set to give you 6 random names, you can change the value located inside of -> Range() if you want more or less

    x = randint(1, 15)
    y = []
    for i in range(6):
        y.append(killers.get(x))
        x = randint(1, 15)
    lbl.config(text=y)


btn = Tk.Button(
    frame,
    text="Roll 6 killers",
    command=roll6,
    height=80,
    width=80
).pack()

frame.geometry("350x100")
frame.mainloop()