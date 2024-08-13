played = []
response = []
allowed = ['r', 'p', 's']
win = []
bot_plays, user_plays = 'r', 'r'
r, p, s = 0, 0, 0
# dummy = 1
def user_play():
    global user_plays
    while True:
      # user_plays = input('Select what will you play \nR for rock, P for paper, S for scissors \n --> ').lower()
      user_plays = input('You played --> ').lower()

      if user_plays in allowed:
        played.append(user_plays)
        break
      elif user_plays == 'i':
        print(win)
        print(played)
      else:
        print('wrong')

def bot_play(dummy=0, vals=1):
    global bot_plays, r, p, s
    if dummy: pass
    else:
      for i in range(len(played)-1):
        value = i/len(played)
        if win[i] == 1:
          if played[i] == 'r': r += 1 * value
          if played[i] == 'p': p += 1 * value
          if played[i] == 's': s += 1 * value
        elif win[i] == 0:
          if played[i] == 'r': r -= 1 * value
          if played[i] == 'p': p -= 1 * value
          if played[i] == 's': s -= 1 * value
        elif win[i] == 2:
          if played[i] == 'r': r -= 0.1 * value
          if played[i] == 'p': p -= 0.1 * value
          if played[i] == 's': s -= 0.1 * value
        if vals:
          print('Value - ', round(value, 3), '| Values for r/p/s -', round(r, 3), round(p, 3), round(s, 3))
    if max(r,p,s) == r: bot_plays = 'r'
    if max(r,p,s) == p: bot_plays = 'p'
    if max(r,p,s) == s: bot_plays = 's'
    print('Bot played -->', bot_plays)
        


    return bot_plays

def check_win():
    if bot_plays == 'r' and user_plays == 'p' or bot_plays == 'p' and user_plays == 's' or bot_plays == 's' and user_plays == 'r':
      print('won')
      win.append(1)
    elif bot_plays == user_plays:
      print('draw')
      win.append(2)
    else:
      print('lost')
      win.append(0)
        
for i in range(2):
    user_play()
    bot_play(1)
    check_win()
while True:
    user_play()
    bot_plays = bot_play(0)
    check_win()
