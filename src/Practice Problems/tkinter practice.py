# ------------------ First section: import statements -----------------
import tkinter as tk


# ------------------ Second section: class and methods ----------------

class BasicGui:

    def __init__(self):
        self.rootWin = tk.Tk() #creates the window
        self.rootWin.title("My first tkinter")
        self.rootWin.config(bg="pink")

        testLabel = tk.Label(self.rootWin,text="hello",font="Arial 18 bold", bg="#DD10C1")
        testLabel.grid(row=0, column=0)

        label2 = tk.Label(self.rootWin)
        label2.config(text="This is the second label", justify = tk.CENTER)
        label2.grid(row=1,column=1)

        label3 = tk.Label(self.rootWin)
        label3["text"]="Label 3"
        label3["bg"]="#dd10c1"
        label3.grid(row=2,column=1)

        self.counter_label=tk.Label(self.rootWin,text="")
        self.counter_label.grid(row=6,column=5)

        testButton=tk.Button(self.rootWin,text="Copy",font="Arial 12",bg="#997711",fg="blue")
        testButton.grid(row=1,column=0)
        testButton["command"]=self.testButtonResponse

        quitButton=tk.Button(self.rootWin,text="Quit",bg='white',fg='red')
        quitButton.grid(row=5,column=5)
        quitButton["command"] = self.quitButtonResponse

        self.testEntry = tk.Entry(self.rootWin,bg='purple',bd=5,font="Times 12",justify=tk.CENTER,width=40)
        self.testEntry.grid(row=5,column=1)
        self.testEntry.bind("<Return>",self.entryResponse)
        self.testEntry.bind("<Tab>",self.entryResponse)

    def run(self):
        self.rootWin.mainloop() #mainloop method runs the GUI

    def testButtonResponse(self):
        txt=self.testEntry.get()
        self.counter_label["text"]=txt
    def quitButtonResponse(self):
        self.rootWin.destroy()
    def entryResponse(self,event):
        if event.keysym == "Return":
            print("Return pressed")
        elif event.keysym == "Tab":
            print("Tab pressed")
        txt = self.testEntry.get()
        revTxt = txt[::1] #makes a copy of the text in reverse order?
        self.testEntry.delete(0,tk.END)
        self.testEntry.insert(0,revTxt)


# ------------------ Third section: main program ----------------------

myGui = BasicGui()
myGui.run()
