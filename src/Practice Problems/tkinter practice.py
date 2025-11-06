# ------------------ First section: import statements -----------------
import tkinter as tk


# ------------------ Second section: class and methods ----------------

class BasicGui:

    def __init__(self):
        self.rootWin = tk.Tk() #creates the window
        """self.rootWin.title("My first tkinter")
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
        self.testEntry.bind("<Tab>",self.entryResponse)"""
        self.title_label=tk.Label(self.rootWin,text="Experiments with Canvas")
        self.title_label.grid(row=0,column=0)

        myCanvas=tk.Canvas(self.rootWin,width=400,height=300,bg="pink",bd=5)
        myCanvas.grid(row=10,column=0)
        l1=myCanvas.create_line(50,50,50,100)
        l2=myCanvas.create_line(10,150,50,250,arrow=tk.FIRST,activewidth=3,activefill='red')
        l3=myCanvas.create_line(100,10,100,30,250,50,100,250,fill='green',smooth=True)
        l4=myCanvas.create_line(130,10,130,30,280,50,130,250,fill='darkgreen')
        r1=myCanvas.create_rectangle(250,50,260,60,fill='blue')
        r2=myCanvas.create_rectangle(160,150,210,250)
        r3=myCanvas.create_rectangle(350,10,400,50,outline='green',fill='darkgreen')
        oList=[None,None,None]
        oList[0]=myCanvas.create_oval(350,250,370,270,fill='lightblue')
        oList[1]=myCanvas.create_oval(50,250,70,295,outline='red',fill='pink')
        oList[2]=myCanvas.create_oval(350,110,390,290)
        p1=myCanvas.create_polygon(280,120,320,250,295,0,outline='yellow',fill="")
        p2=myCanvas.create_polygon(100,100,120,120,140,80,120,60,fill='green')
        t1=myCanvas.create_text(0,0,text="hi there",fill='dark blue',anchor=tk.NW)
        t2=myCanvas.create_text(150,150,text="WOW!",fill='dark red',activefill='white')
        t3=myCanvas.create_text(80,280,text='another',font="Arial 10")
        a1=myCanvas.create_arc(30,280,60,300,fill='dark blue',start=45,extent=135)
        a2=myCanvas.create_arc(170,150,200,180,activeoutline='white',start=280,extent=300,style=tk.ARC)
        a3=myCanvas.create_arc(290,190,390,290,fill='gray',start=180,extent=45,style=tk.PIESLICE)
        a4=myCanvas.create_arc(290,90,390,190,fill='gray',start=180,extent=45,style=tk.CHORD)
    def run(self):
        self.rootWin.mainloop() #mainloop method runs the GUI

    """def testButtonResponse(self):
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
        self.testEntry.insert(0,revTxt)"""


# ------------------ Third section: main program ----------------------

myGui = BasicGui()
myGui.run()
