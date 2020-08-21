import frontend as front
from tkinter import messagebox
import json
action = ""
with open("data/cfg.json") as file:
    cfg = json.load(file)
def newmark():
    front.entry.grid(row=1, column=1)
    front.marklab.grid(row=1, column=0)
    front.submit.grid(row=2, column=1)
    action = "mark"
def newsubject():
    front.entry.grid(row=1, column=1)
    front.submit.grid(row=2, column=1)
    front.marklab.grid_forget()
    front.subjectlab.grid(row=1, column=0)
    action = "subject"
def data():
    if action == "mark":
        info = front.entry.get()
        if not ", " in info:
            messagebox.showwarning("Warning", "gib bitte ein Fach an.")
        else:
            subject = info.split(", ")[0]
            mark = info.split(", ")[1]
            try:
                mark = int(mark)
                if subject not in cfg:
                    messagebox.showwarning("Warning", "Subject doesn't exist")
                else:
                    cfg[subject].append(mark)
                    messagebox.showinfo("Success", "Mark added")
                    with open("data/cfg", "w") as file:
                        file.write(json.dumps(cfg, indent=4))
            except:
                messagebox.showwarning("Warning", "Mark is not supported")
    elif action == "subject":
        pass