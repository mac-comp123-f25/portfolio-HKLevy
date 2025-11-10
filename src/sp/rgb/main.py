from hw5.rgb.helpers import *
import tkinter as tk


class RGBGUI:
    def __init__(self):
        self.mainWin=tk.Tk()
        self.mainWin.title("RGB Illustrator")
        title_label=tk.Label(self.mainWin,text="RGB Illustrator", font="Impact 16",bd=5,relief=tk.RAISED)
        title_label.grid(row=0, column=1, padx=5, pady=5)

        red_label=tk.Label(self.mainWin,text="Red value (0–255):",font="Impact 16",bd=5,relief=tk.RAISED,width=20)
        red_label.grid(row=1, column=0, padx=5, pady=10)
        self.red_entry=tk.Entry(self.mainWin,font="Impact 16",bd=5,relief=tk.RAISED,justify=tk.CENTER)
        self.red_entry.grid(row=1, column=1, padx=5, pady=10)
        self.red_entry.insert(0,"255")
        self.red_entry.bind("<Return>",self.update_color)

        green_label=tk.Label(self.mainWin,text="Green value (0–255):",font="Impact 16",bd=5,relief=tk.RAISED,width=20)
        green_label.grid(row=2, column=0, padx=5, pady=10)
        self.green_entry=tk.Entry(self.mainWin,font="Impact 16",bd=5,relief=tk.RAISED,justify=tk.CENTER)
        self.green_entry.grid(row=2, column=1, padx=5, pady=10)
        self.green_entry.insert(0,"255")
        self.green_entry.bind("<Return>",self.update_color)

        blue_label=tk.Label(self.mainWin,text="Blue value (0–255):",font="Impact 16",bd=5,relief=tk.RAISED,width=20)
        blue_label.grid(row=3, column=0, padx=5, pady=10)
        self.blue_entry=tk.Entry(self.mainWin,font="Impact 16",bd=5,relief=tk.RAISED,justify=tk.CENTER)
        self.blue_entry.grid(row=3, column=1, padx=5, pady=10)
        self.blue_entry.insert(0,"255")
        self.blue_entry.bind("<Return>",self.update_color)

        self.color_label=tk.Label(self.mainWin,bd=5,relief=tk.RAISED,width=20,height=10)
        self.color_label.grid(row=1,column=2, padx=5, pady=5,rowspan=3)

    def go(self):
        self.mainWin.mainloop()

    def update_color(self,event):
        new_red=get_num_from_entry(self.red_entry)
        new_green=get_num_from_entry(self.green_entry)
        new_blue=get_num_from_entry(self.blue_entry)
        new_string=make_tk_color(new_red,new_green,new_blue)
        self.color_label.config(bg=new_string)


if __name__ == "__main__":
    rgb = RGBGUI()
    rgb.go()
