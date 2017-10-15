import Tkinter as tk

class App(tk.Frame):
    def __init__(self,master):
        self.master = master
        main_window = tk.Frame.__init__(self, master)
        self.configure_gui()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        return()

#Configures the master GUI window with a title and
#fixed dimensions. Plan to make a resizeable window
#at a later date

    def configure_gui(self):
        self.master.title("budgetme")
        self.master.geometry("1000x1000")
        self.master.resizable(False,False)

def main():
    root = tk.Tk()
    app=App(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
