#!/usr/bin/env python

#import pygame
from logic import *

#world = tk.Canvas()
noneimg=tk.PhotoImage(                 width=50, height=50)
coinimg=tk.PhotoImage(file='Coin.gif', width=50, height=50)
dotimg =tk.PhotoImage(file='Dot.gif' , width=50, height=50)
def btnapply(obj, x, y, **increment):
    # print(x,y)
    obj = tk.Button(win, image=noneimg, relief='flat', command=(lambda:changebtncolor(obj)))
    obj.grid(column=x, row=y)
    # print(obj.place_info())
    return obj
win.config(width=888, height=565)
win.resizable(False, False)
matrix = create_matrix(22, 14, command=btnapply)
# for (obj, x, y) in getmatrixobjs(matrix):
#     print('coord:({0},{1})'.format(x,y), 'vis_coord:({x},{y})'.format(**obj.place_info()))
#world.mainloop()

# exec('import %s.simpledialog as simpledialog'%tk.__name__)
import shelve
lvls = shelve.open('levels')
import pickle
def new():
    for column in matrix:
        for btn in column:
            btn.config(bg='white')
def save():
    lvls[simpledialog.askstring('File', 'File to save to')] = getlvlinfo(matrix)
    lvls.sync()
def load():
    lvl = simpledialog.askstring('File', 'File to load from')
    if lvl.startswith('\\\\'): cmdswitch(lvl)
    else: setlvlinfo(lvls[lvl], matrix)
def cmdswitch(cmd):
    pass
def exportlvl():
    pickle.dump(getlvlinfo(matrix), filedialog.asksaveasfile('wb', defaultextension='.whg'))
def importlvl():
    setlvlinfo(pickle.load(filedialog.askopenfile('rb', defaultextension='.whg')), matrix)
import os
import webbrowser
def play():
    if not os.path.isdir('level'):
        os.mkdir('level')
    spawn(config(matrix))
    webbrowser.open_new_tab('file://%s' % os.path.abspath('level/level.html'))
menu_bar = tk.Menu(win)
menu_file = tk.Menu(menu_bar, tearoff=5)
menu_file.add_command(label='New', command=new)
menu_file.add_command(label='Save', command=save)
menu_file.add_command(label='Load', command=load)
menu_file.add_command(label='Import', command=importlvl)
menu_file.add_command(label='Export', command=exportlvl)
menu_file.add_separator()
menu_demo = tk.Menu(menu_file, tearoff=0)
menu_demo.add_command(label='Level 1', command=lambda:webbrowser.open_new_tab('file://%s' % os.path.abspath('Level1/level1.html')))
menu_demo.add_command(label='Level 2', command=lambda:webbrowser.open_new_tab('file://%s' % os.path.abspath('Level2/level2.html')))
menu_demo.add_command(label='Level 3', command=lambda:webbrowser.open_new_tab('file://%s' % os.path.abspath('Level3/level3.html')))
menu_demo.add_command(label='Level 4', command=lambda:webbrowser.open_new_tab('file://%s' % os.path.abspath('Level4/level4.html')))
menu_demo.add_command(label='Level 5', command=lambda:webbrowser.open_new_tab('file://%s' % os.path.abspath('Level5/level5.html')))
menu_demo.add_command(label='Level 6', command=lambda:webbrowser.open_new_tab('file://%s' % os.path.abspath('Level6/level6.html')))
menu_file.add_command(label='Play', command=play)
menu_file.add_cascade(label='Play Demo', menu=menu_demo)
menu_file.add_separator()
menu_file.add_command(label='Quit', command=win.quit)
menu_bar.add_cascade(label='File', menu=menu_file)
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label='Help', command=lambda:showinfo('Help', 'White = Nothing\nGray = Ground\nRed = Start\nYellow = Green\nGreen = Goal'))
menu_help.add_command(label='About', command=lambda:showinfo('About', 'Credits:\n\tOriginal Game: Snubby Land\n\tAI and Remake: Code Bullet\n\tLevel Editor: Gaming32\n\tInstaller: InstallForge'))
menu_bar.add_cascade(label='Help', menu=menu_help)
win.config(menu=menu_bar)

win.title("World's Hardest Game Remake")
win.iconbitmap('Player.ico')

if __name__ == "__main__":
    new()
    win.mainloop()