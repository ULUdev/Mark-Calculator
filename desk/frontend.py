import tkinter as tk
import backend as bck
root = tk.Tk()
#init
title = tk.Label(root, text="Noten Rechner")
fach = tk.Label(root, text="Fach")
mark = tk.Radiobutton(root, text="Neue Note", command=bck.newmark)
newsubject = tk.Radiobutton(root, text="Neues Fach", command=bck.newsubject)
marklab = tk.Label(root, text="Note")
subjectlab = tk.Label(root, text="Fach")
submit = tk.Button(root, text="Submit", bg="green")
entry = tk.Entry(root, width=20)

#grid
title.grid(row=0, column=0)
fach.grid(row=0, column=2)
mark.grid(row=1, column=2)
newsubject.grid(row=2, column=2)
root.mainloop()