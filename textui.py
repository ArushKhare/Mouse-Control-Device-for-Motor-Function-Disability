from tkinter import *
import word_generator as word
import time
#from letterfunctions import *
#import keyboard

#_________________________________________________________________________________________________
def user_interface():
    root = Tk()
    root.title("Letters")
    root.geometry("1440x360")

    height = 3
    width = 2
    font_color = 'black'
    global phraseText
    phraseText= ''
    phraseLabel = Label(root, text=phraseText, bg='white', fg='black', font=('Arial', 20))

    global suggestions 
    suggestions = ['n/a','n/a','n/a','n/a','n/a']
    sugButtons = [
        Button(text=suggestions[0], fg=font_color, height=height, width=width),
        Button(text=suggestions[1], fg=font_color, height=height, width=width),
        Button(text=suggestions[2], fg=font_color, height=height, width=width),
        Button(text=suggestions[3], fg=font_color, height=height, width=width),
        Button(text=suggestions[4], fg=font_color, height=height, width=width)
    ]
    def generate_words():
        global phraseText, suggestions
        if phraseText:
            suggestions = list(word.word_generate(phraseText, 5))
        for i in range(len(sugButtons)):
            sugButtons[i].config(text=suggestions[i])

    def sg1():
        global phraseText
        if suggestions[0] != 'n/a':
            phraseText+= " " + suggestions[0]
            phraseLabel.config(text=phraseText)
        generate_words()
    def sg2():
        global phraseText
        if suggestions[1] != 'n/a':
            phraseText+= " " + suggestions[1]
            phraseLabel.config(text=phraseText)
        generate_words()
    def sg3():
        global phraseText
        if suggestions[2] != 'n/a':
            phraseText+= " " + suggestions[2]
            phraseLabel.config(text=phraseText)
        generate_words()
    def sg4():
        global phraseText
        if suggestions[3] != 'n/a':
            phraseText+= " " + suggestions[3]
            phraseLabel.config(text=phraseText)
        generate_words()
    def sg5():
        global phraseText
        if suggestions[4] != 'n/a':
            phraseText+= " " + suggestions[4]
            phraseLabel.config(text=phraseText)
        generate_words()
    def a():
        global phraseText
        phraseText+='a'
        phraseLabel.config(text=phraseText)
        generate_words()
    def b():
        global phraseText
        phraseText+='b'
        phraseLabel.config(text=phraseText)
        generate_words()
    def c():
        global phraseText
        phraseText+='c'
        phraseLabel.config(text=phraseText)
        generate_words()
    def d():
        global phraseText
        phraseText+='d'
        phraseLabel.config(text=phraseText)
        generate_words()
    def e():
        global phraseText
        phraseText+='e'
        phraseLabel.config(text=phraseText)
        generate_words()
    def f():
        global phraseText
        phraseText+='f'
        phraseLabel.config(text=phraseText)
        generate_words()
    def g():
        global phraseText
        phraseText+='g'
        phraseLabel.config(text=phraseText)
        generate_words()
    def h():
        global phraseText
        phraseText+='h'
        phraseLabel.config(text=phraseText)
        generate_words()
    def i():
        global phraseText
        phraseText+='i'
        phraseLabel.config(text=phraseText)
        generate_words()
    def j():
        global phraseText
        phraseText+='j'
        phraseLabel.config(text=phraseText)
        generate_words()
    def k():
        global phraseText
        phraseText+='k'
        phraseLabel.config(text=phraseText)
        generate_words()
    def l():
        global phraseText
        phraseText+='l'
        phraseLabel.config(text=phraseText)
        generate_words()
    def m():
        global phraseText
        phraseText+='m'
        phraseLabel.config(text=phraseText)
        generate_words()
    def n():
        global phraseText
        phraseText+='n'
        phraseLabel.config(text=phraseText)
        generate_words()
    def o():
        global phraseText
        phraseText+='o'
        phraseLabel.config(text=phraseText)
        generate_words()
    def p():
        global phraseText
        phraseText+='p'
        phraseLabel.config(text=phraseText)
        generate_words()
    def q():
        global phraseText
        phraseText+='q'
        phraseLabel.config(text=phraseText)
        generate_words()
    def r():
        global phraseText
        phraseText+='r'
        phraseLabel.config(text=phraseText)
        generate_words()
    def s():
        global phraseText
        phraseText+='s'
        phraseLabel.config(text=phraseText)
        generate_words()
    def t():
        global phraseText
        phraseText+='t'
        phraseLabel.config(text=phraseText)
        generate_words()
    def u():
        global phraseText
        phraseText+='u'
        phraseLabel.config(text=phraseText)
        generate_words()
    def v():
        global phraseText
        phraseText+='v'
        phraseLabel.config(text=phraseText)
        generate_words()
    def w():
        global phraseText
        phraseText+='w'
        phraseLabel.config(text=phraseText)
        generate_words()
    def x():
        global phraseText
        phraseText+='x'
        phraseLabel.config(text=phraseText)
        generate_words()
    def y():
        global phraseText
        phraseText+='y'
        phraseLabel.config(text=phraseText)
        generate_words()
    def z():
        global phraseText
        phraseText+='z'
        phraseLabel.config(text=phraseText)
        generate_words()
    def space():
        global phraseText
        phraseText+=' '
        phraseLabel.config(text=phraseText)
        generate_words()
    def new_line():
        global phraseText
        phraseText+='\n'
        phraseLabel.config(text=phraseText)
        generate_words()
    def backspace():
        global phraseText
        phraseText = phraseText[0:len(phraseText)-1]
        phraseLabel.config(text=phraseText)
        generate_words()


    buttons = [
    Button(text='a', fg=font_color, command=a, height=height, width=width),
    Button(text='b', fg=font_color, command=b, height=height, width=width),
    Button(text='c', fg=font_color, command=c, height=height, width=width),
    Button(text='d', fg=font_color, command=d, height=height, width=width),
    Button(text='e', fg=font_color, command=e, height=height, width=width),
    Button(text='f', fg=font_color, command=f, height=height, width=width),
    Button(text='g', fg=font_color, command=g, height=height, width=width),
    Button(text='h', fg=font_color, command=h, height=height, width=width),
    Button(text='i', fg=font_color, command=i, height=height, width=width),
    Button(text='j', fg=font_color, command=j, height=height, width=width),
    Button(text='k', fg=font_color, command=k, height=height, width=width),
    Button(text='l', fg=font_color, command=l, height=height, width=width),
    Button(text='m', fg=font_color, command=m, height=height, width=width),
    Button(text='n', fg=font_color, command=n, height=height, width=width),
    Button(text='o', fg=font_color, command=o, height=height, width=width),
    Button(text='p', fg=font_color, command=p, height=height, width=width),
    Button(text='q', fg=font_color, command=q, height=height, width=width),
    Button(text='r', fg=font_color, command=r, height=height, width=width),
    Button(text='s', fg=font_color, command=s, height=height, width=width),
    Button(text='t', fg=font_color, command=t, height=height, width=width),
    Button(text='u', fg=font_color, command=u, height=height, width=width),
    Button(text='v', fg=font_color, command=v, height=height, width=width),
    Button(text='w', fg=font_color, command=w, height=height, width=width),
    Button(text='x', fg=font_color, command=x, height=height, width=width),
    Button(text='y', fg=font_color, command=y, height=height, width=width),
    Button(text='z', fg=font_color, command=z, height=height, width=width),
    Button(text="SPACE", fg=font_color, command=space, height=height, width=width),
    Button(text="ENTER", fg=font_color, command=new_line, height=height, width=width),
    Button(text="DEL", fg=font_color, command=backspace, height=height, width=width)]


    for i in range(13):
        buttons[i].grid(row=0, column=i)
    for i in range(13, 26):
        buttons[i].grid(row=1, column=i-13)

    buttons[26].grid(row=3, column=5)
    buttons[27].grid(row=3, column=6)
    buttons[28].grid(row=3, column=7)

    sugButtons[0].config(command=sg1)
    sugButtons[1].config(command=sg2)
    sugButtons[2].config(command=sg3)
    sugButtons[3].config(command=sg4)
    sugButtons[4].config(command=sg5)

    for i in range(5):
        sugButtons[i].grid(row=2, column=i+4)

    phraseLabel.grid(row=4, columnspan=26)
    time.sleep(0.0005)
    root.mainloop()

