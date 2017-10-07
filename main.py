import tkinter as tk

class App(tk.Frame):
    def __init__(self,master =None):
        super().__init__(master)
        self.grid()
        self.create_widgets()


root = tk.Tk()
app=App(master=root)
app.mainloop()
