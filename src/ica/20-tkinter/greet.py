import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        button1=tk.Button(self.mainWin, text="Quit")
        button1.grid(row=1, column=1)
        button1["command"]=self.quit_callback
        button2=tk.Button(self.mainWin, text="Hello")
        button2.grid(row=2, column=1)
        button2["command"]=self.change_text
        button3=tk.Button(self.mainWin, text="Goodbye")
        button3.grid(row=3, column=1)
        button3["command"]=self.change_goodbye
        self.label1=tk.Label(self.mainWin, text="Welcome")
        self.label1.grid(row=2,column=2)


    def run(self):
        self.mainWin.mainloop()
    def quit_callback(self):
        self.mainWin.destroy()
    def change_text(self):
        self.label1.config(text="Hello")
    def change_goodbye(self):
        self.label1.config(text="Goodbye")



# ----- Main program -----
myGui = BasicGui()
myGui.run()