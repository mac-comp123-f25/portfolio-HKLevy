import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        label1=tk.Label(self.mainWin, text="Instructions")
        label1.grid(row=0, column=0)
        self.label2=tk.Label(self.mainWin)
        self.label2.grid(row=2, column=0)
        self.entry1=tk.Entry(self.mainWin)
        self.entry1.grid(row=1, column=0)
        self.entry1.bind("<Return>", self.entry_response)
        self.entry1.bind("<Tab>", self.entry_response)

    def run(self):
        self.mainWin.mainloop()
    def entry_response(self, event):
        string=self.entry1.get()
        string2=string[::-1]
        self.label2.config(text=string2)



# ----- Main program -----
myGui = BasicGui()
myGui.run()