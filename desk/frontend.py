import tkinter as tk
root = tk.Tk()
#init
title = tk.Label(root, text="Noten Rechner")
fach = tk.Label(root, text="Fach")
#grid
title.grid(row=0, column=0)
fach.grid(row=0, column=1)
root.mainloop()