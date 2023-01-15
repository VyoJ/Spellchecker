import tkinter as tk
import tkinter.font as tkFont

import re
from collections import Counter
from string import ascii_lowercase as letters



# def words(text): 
#     return re.findall(r'\w+', text.lower())

# def known(words):
#     "The subset of `words` that appear in the dictionary of word_ct."
#     #print(words(open(r'C:\Users\shamb\The codes\college\big.txt').read()))
#     Counter(words(open(r'C:\Users\shamb\The codes\college\big.txt').read())))

#     return set(w for w in words if w in word_ct)
def words(text): 
    return re.findall(r'\w+', text.lower())

def known(words):
    "The subset of `words` that appear in the dictionary of word_ct."
    return set(w for w in words if w in word_ct)


def edits1(word):
    "All edits that are one edit away from the word."
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from word."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def P(word): 
    "Probability of the word appearing in big.txt"
    # word_ct = Counter(words(open(r'C:\Users\shamb\The codes\college\big.txt').read()))
    global word_ct
    N = sum(word_ct.values())
    return word_ct[word] / N

def correction(word, type): 
    "Most probable spelling correction for word."
    if type == 'mp':
        return max(candidates(word), key = P)
    elif type == 'all':
        return sorted(candidates(word), key=P)


word_ct = Counter(words(open(r'C:\Users\shamb\The codes\college\big.txt').read()))

def main(txt):
    global word_ct
    print(word_ct)
#txt = input("Enter text: ").split()

    print("Most probable corrections:")
    for i in txt:
        print(correction(i, 'mp'), end = " ")
    print()

    print("All possibilites of corrections:")
    correct_list = []
    for i in txt:
        if correction(i, 'mp') == i:
            print(i, end = " ")
        else:
            correct_list.append(correction(i, 'all'))
    return correct_list

def file_spellcheck():
    name = box.get()
    f = open(name + '.txt','r')
    content = f.read()
    if content != '':
        #label = tk.Label(win,text = name)
        label.config(text = "Contents of file : \n " + content)
        print(content)
        suggestion = main(content.split())
        print('LENGTH:',len(content.split()))
        label_sugg.config(text = suggestion)
        #out = tk.Text(win,height = 30, width = 40)
        #label.grid(row = 41,column= 1)
    else:
        pass


#def file_spellcheck():
#    name = box.get()
#    f = open(name+'.txt','r')
#    content = f.read()
#    #call spellcheck on content
#    label = tk.Label(win,text=coxntent)
#   label.pack()

'''win = tk.Tk()
win.geometry('1000x1000')
box = tk.Entry(win,width=25,text = 'Enter File Name here')
box.pack()

button = tk.Button(win,bg = '#ADD8E6',command=file_spellcheck,text = 'Submit')
button.pack()
win.mainloop()'''



win = tk.Tk()
win.title("Spell Checker")

win.geometry("600x500")
win.resizable(width=False, height=False)


button=tk.Button(win,command=file_spellcheck)
button["bg"] = "#1b1b1a"
ft = tkFont.Font(family='Times',size=10)
button["font"] = ft
button["fg"] = "#fede54"
button["justify"] = "center"
button["text"] = "Spell Check"
button.place(x=240,y=160,width=114,height=37)

box=tk.Entry(win)
box["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
box["font"] = ft
#box["fg"] = "#dbcfbb"
box["justify"] = "center"
box["text"] = "file_name.txt"
box.place(x=290,y=90,width=247,height=35)

GLabel_124=tk.Label(win)
ft = tkFont.Font(family='Times',size=10)
GLabel_124["font"] = ft
#GLabel_124["fg"] = "#dbcfbb"
GLabel_124["justify"] = "left"
GLabel_124["text"] = ".  Enter a filename to spell check"
GLabel_124.place(x=50,y=80,width=208,height=55)

label=tk.Label(win)
ft = tkFont.Font(family='Times',size=10)
label["font"] = ft
#label["fg"] = "#dbcfbb"
label["justify"] = "center"
label["text"] = ""
label.place(x=60,y=220,width=477,height=69)

label_sugg=tk.Label(win)
ft = tkFont.Font(family='Times',size=10)
label_sugg["font"] = ft
#label_sugg["fg"] = "#dbcfbb"
label_sugg["justify"] = "center"
label_sugg["text"] = "Suggestions"
label_sugg.place(x=60,y=330,width=479,height=56)

GLabel_42=tk.Label(win)
GLabel_42["activebackground"] = "#ffd700"
GLabel_42["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=18)
GLabel_42["font"] = ft
GLabel_42["fg"] = "#ffe24b"
GLabel_42["justify"] = "center"
GLabel_42["text"] = "Welcome to Spell Checker"
GLabel_42.place(x=50,y=30,width=500,height=38)


win.mainloop()

