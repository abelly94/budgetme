import tkinter as tk

class App(tk.Frame):
    def __init__(self,master =None):
        super().__init__(master)
        self.grid()
        self.create_widgets()


#Configures the master GUI window with a title and
#fixed dimensions. Plan to make a resizeable window
#at a later date

    def configure_gui(self):
        self.master.title("budgetme")
        self.master.geometry("1000x1000")
        self.master.resizeable(False,False)


root = tk.Tk()
app=App(master=root)
app.mainloop()
