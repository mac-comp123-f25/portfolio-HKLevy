import tkinter as tk

def find_words_with(string,big_file):
    """Takes in a string, may include some blank spots represented by *.
    Returns all acceptable answers that have that string in any place inside them."""
    word_file = open(big_file)
    word_list=[]
    for line in word_file:
        if string in line:
            word_list.append(line)
    return word_list

def find_words_in_file(big_file,key):
    words=open(big_file)
    word_list=[]
    length=len(key)
    for line in words:
        #This will work by toggling the condition to false if something is wrong.
        #That way, if any part is false, condition=False. condition can never be switched back to True
        condition = True
        if len(line) == length+1:
            for letter in range(length):
                if key[letter]=='V' and line[letter] not in ['a','e','i','o','u','y']:
                    #If a vowel is requested and it's not a vowel (or y)...
                    condition = False
                elif key[letter]=='C' and line[letter] in ['a','e','i','o','u']:
                    #If a consonant is requested and it is a vowel (not y)...
                    condition = False
                elif key[letter]!='*' and key[letter]!='V' and key[letter]!='C' and key[letter]!=line[letter]:
                    #If it's a specific letter but it doesn't match...
                    condition = False

            if condition:
                #If every letter matched what we gave it...
                word_list.append(line)

    return word_list

def find_words(string):
    """Accepts *, C,V, or specific lowercase letters.
    Should consider acronyms and normal words. Add names later?"""
    word_list = find_words_in_file('better_crosswords.txt',string)
    word_list = word_list + find_words_in_file('crossword_acronyms_and_other.txt',string)
    word_list = word_list + find_words_in_file('crossword_names',string)

    word_list.sort()
    return word_list

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.on_screen_words = []

        # Instructions
        self.instruction1 = tk.Label(self.mainWin,text="Enter the pattern that you're looking for.")
        self.instruction2 = tk.Label(self.mainWin,text="Use * for any letter. Use V or C for vowels or consonants.")
        self.instruction3 = tk.Label(self.mainWin,text="Use lowercase letters for the actual letter.")
        self.instruction1.grid(row=0,column=0,columnspan=4,padx=10,pady=5)
        self.instruction2.grid(row=1,column=0,columnspan=4,padx=10)
        self.instruction3.grid(row=2,column=0,columnspan=4,padx=10)

        # Entry for the key
        self.text_box = tk.Entry(self.mainWin,bg='#eeeeee',fg='#000000',bd=5,font='Times 12',justify='center')
        self.text_box.grid(row=3,column=0,columnspan=2,pady=10)
        self.text_box.bind("<Return>",self.get_words)
        self.text_box.bind("<Tab>",self.get_words)

        # Clear button
        self.clear_button = tk.Button(self.mainWin,bg='#eeeeee',fg='#000000',bd=5,text="Clear Words",command=self.clear_words)
        self.clear_button.grid(row=3,column=2,columnspan=2,padx=10,pady=10)

    def get_words(self,event):
        if event.keysym == 'Return':
            current_row = 4
            txt=self.text_box.get()
            word_list=find_words(txt)
            for x in range(len(word_list)):
                self.txt = tk.Label(self.mainWin,text=word_list[x])
                self.txt.grid(row=current_row,column=x%4)
                self.on_screen_words.append(self.txt)
                if x%4==3:
                    current_row = current_row + 1

    def clear_words(self):
        for thing in self.on_screen_words:
            thing.destroy()
        self.on_screen_words=[]

    def run(self):
        self.mainWin.mainloop()

myGui = BasicGui()
myGui.run()