from tkinter import *
import sys

played = []
response = []
temp1 = []
temp2 = []
allowed = ['r', 'p', 's']
win = []
bot_plays, user_plays = 'r', 'r'
status = 'Waiting'
ver = 'v0.04 14082024'
value = 0
r, p, s = 0, 0, 0


def playing(select='r'):
    global user_plays
    user_plays = select
    played.append(select)
    print('You played -->', select)
    bot_plays = bot_play(0)
    check_win()
def bot_play(dummy=0, vals=0):
    global bot_plays, r, p, s, info, value
    if dummy: pass
    else:
      for i in range(len(played)-1):
        value = i/len(played)
        
        if win[i] == 1:
          if played[i] == 'r': r += 1 * value
          if played[i] == 'p': p += 1 * value
          if played[i] == 's': s += 1 * value
        if len(played) > 4:
          temp1.clear()
          temp2.clear()
          temp1.insert(0, response[-1])
          temp1.insert(0, response[-2])
          temp2.insert(0, response[-3])
          temp2.insert(0, response[-4])
          
          if temp1 == temp2:
            print('trend recognized')
            #print(temp1,'\n',temp2)
            if response[i] == 'r': r -= 2 * value
            if response[i] == 'p': p -= 2 * value
            if response[i] == 's': s -= 2 * value
          if len(played) > 6:
            temp1.clear()
            temp2.clear()
                
            temp1.insert(0, response[-1])
            temp1.insert(0, response[-2])
            temp1.insert(0, response[-3])
          
            temp2.insert(0, response[-4])
            temp2.insert(0, response[-5])
            temp2.insert(0, response[-6])
          
            if temp1 == temp2:
              print('big trend recognized')
              #print(temp1,'\n',temp2)
              if response[i] == 'r': r -= 3.2 * value
              if response[i] == 'p': p -= 3.2 * value
              if response[i] == 's': s -= 3.2 * value
          
        if win[i] == 0:
          if response[i] == 'r': r -= 1
          if response[i] == 'p': p -= 1
          if response[i] == 's': s -= 1
          
        elif win[i] == 2:
          if response[i] == 'r': r -= 0.01 * value
          if response[i] == 'p': p -= 0.01 * value
          if response[i] == 's': s -= 0.01 * value
          
        if vals:
          print('Value - ', round(value, 3), '| Values for r/p/s -', round(r, 3), round(p, 3), round(s, 3))
    if r + p + s != 0:
      if max(r,p,s) == r: bot_plays = 'r'
      if max(r,p,s) == p: bot_plays = 'p'
      if max(r,p,s) == s: bot_plays = 's'
    else:
      bot_plays = 'p'
    response.append(bot_plays)
    print('Bot played -->', bot_plays)


    return bot_plays

def check_win():
    global status
    if bot_plays == 'r' and user_plays == 'p' or bot_plays == 'p' and user_plays == 's' or bot_plays == 's' and user_plays == 'r':
      status = 'won'
      win.append(0)
    elif bot_plays == user_plays:
      status = 'draw'
      win.append(2)
    else:
      status = 'lost'
      win.append(1)
    create_info()

def update_text(value=0):
    text = StringVar()
    text.set(str(value))
    root.update_idletasks()
    root.after(1000, update_text)
    return text

def create_info():
    global info, info2
    text = StringVar()
    wins = 0
    pl = len(played)
    for i in range(len(played)):
      if win[i] == 1:
        wins += 1
      elif win[i] == 2:
        pl -= 1
    if pl < 0:
      pl = 0
    try:
      wr = str(round((wins * 100/ pl ),3)) + '%'
    except ZeroDivisionError:
      wr = 0
    print(wr)
    if len(played) >= 1:
      text.set(status+'\nBot played '+bot_plays+'\nTotal games: '+str(len(played))+' | AI winrate: '
               +wr+'\n                                    Value: '
               +str(round(value,3))+' | Values for r/p/s: '
               +str(round(r,3))+' '+str(round(p,3))+' '+str(round(s,3))+'                                    ')
    if status == 'lost':
      info.config(bg='red')
    if status == 'won':
      info.config(bg='green')
    if status == 'draw':
      info.config(bg='gray')
    
    info.config(textvar = text)
def about():
    about = Tk()
    w, h = 200, 100
    about.title('About')
    about.minsize(w, h)  # width, height
    about.maxsize(w, h)
    label = Label(about, text="smart-RPS "+ver+"\nCreated using Python 3.7.9\n\n\nMade by Matroftt", font=("Times New Roman", 12))
    label.pack()
    about.mainloop()
def tk_init():
    global root, w, h, welcome, info
    root = Tk()
    root.configure(background="palegreen")
    w, h = 700, 500
    root.title('RPS with smart AI')
    root.minsize(w, h)  # width, height
    root.maxsize(w, h)
    welcome = Label(root, text="   Welcome to the RPS "+ver+"   ", font=("Helvetica", 22), bg='palegreen', anchor = CENTER)
    info = Label(root, text='Waiting...', font=("Helvetica", 20))
    
tk_init()

welcome.pack()
    
info.place(rely=0.85, relx=0.5, anchor=CENTER)
    
rbtn=Button(root, text="         Rock          ", command=lambda: playing('r'), font=("Helvetica", 30))
pbtn=Button(root, text="         Paper         ", command=lambda: playing('p'), font=("Helvetica", 30))
sbtn=Button(root, text="       Scissors        ", command=lambda: playing('s'), font=("Helvetica", 30))
clearbtn=Button(root, text=" About app ", command=about, font=("Helvetica", 12), bg='palegreen')
quitbtn=Button(root, text=" Quit game ", command=sys.exit, font=("Helvetica", 12), bg='palegreen')


clearbtn.place(relx=0, y=16, anchor=W)
quitbtn.place(relx=1, y=16, anchor=E)

rbtn.place(relx=0.5, y=100, anchor=CENTER)
pbtn.place(relx=0.5, y=200, anchor=CENTER)
sbtn.place(relx=0.5, y=300, anchor=CENTER)

root.mainloop()
