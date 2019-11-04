# -*- coding: utf-8 -*-

from random import randint
from tkinter import *

def creation_grille() :
    x = 0
    y = 0
    while x != width :
        can.create_line(x, 0, x, height, width = 1, fill = 'black')
        can.create_line(0, y, width, y, width = 1, fill = 'black')
        x += c
        y += c

def init_cases() :
    i = 0
    while i != width/c :
        j = 0
        while j != height/c :
            x = i*c
            y = j*c
            cellules[x,y] = 0
            dureevie[x,y] = -1
            j += 1
        i += 1

# ========== Events ==========        
def clic_gauche(event) :
    global mini, maxi
    x = event.x - (event.x%c)
    y = event.y - (event.y%c)
    can.create_rectangle(x, y, x+c, y+c, fill = 'black')
    cellules[x,y] = 1
    dureevie[x,y] = randint(mini,maxi)

def clic_droit(event) :
    x = event.x - (event.x%c)
    y = event.y - (event.y%c)
    can.create_rectangle(x, y, x+c, y+c, fill = 'white')
    cellules[x,y] = 0
    dureevie[x,y] = -1
    
def go() :
    global flag
    if not flag :
        flag = True
        run()

def stop() :
    global flag
    flag = False

def reset() :
    global cellules, nbcellules
    cellules = dict.fromkeys(cellules, 0)
    nbcellules = dict.fromkeys(nbcellules, 0)
    evolution()
    label_steps.configure(text = "0")
    
# ========== Events ==========  
def run() :
    global flag, vitesse
    
    i = 0
    while i != width/c :
        j = 0
        while j != height/c :
            x = i*c
            y = j*c
            
            cpt = 0     #compte le nombre de cellules vivantes autour de la case
            #coin haut gauche
            if x == 0 and y == 0 :
                if cellules[x, y+c] == 1 :
                    cpt += 1
                if cellules[x+c, y] == 1 :
                    cpt += 1
                if cellules[x+c, y+c] == 1:
                    cpt += 1
            
            #coin haut droit
            elif x == int(width-c) and y == 0 :
                if cellules[x, y+c] == 1 :
                    cpt += 1
                if cellules[x-c, y] == 1 :
                    cpt += 1
                if cellules[x-c, y+c] == 1 :
                    cpt += 1
            
            #coin bas gauche
            elif x == 0 and y == int(height-c) :
                if cellules[x, y-c] == 1 :
                    cpt += 1
                if cellules[x+c, y] == 1 :
                    cpt += 1
                if cellules[x+c, y-c] == 1 :
                    cpt += 1
            
            #coin bas droit
            elif x == int(width-c) and y == int(height-c) :
                if cellules[x-c, y] == 1 :
                    cpt += 1
                if cellules[x, y-c] == 1 :
                    cpt += 1
                if cellules[x-c, y-c] == 1 :
                    cpt += 1
            
            #bord gauche de la grille
            elif x == 0 and 0 < y < int(height-c) :
                if cellules[x, y-c] == 1 :
                    cpt += 1
                if cellules[x, y+c] == 1 :
                    cpt += 1
                if cellules[x+c, y] == 1 :
                    cpt += 1
                if cellules[x+c, y-c] == 1 :
                    cpt += 1
                if cellules[x+c, y+c] == 1 :
                    cpt += 1
                
            #bord droit de la grille
            elif x == int(width-c) and 0 < y < int(height-c) :
                if cellules[x, y-c] == 1 :
                    cpt += 1
                if cellules[x, y+c] == 1 :
                    cpt += 1
                if cellules[x-c, y] == 1 :
                    cpt += 1
                if cellules[x-c, y-c] == 1 :
                    cpt += 1
                if cellules[x-c, y+c] == 1 :
                    cpt += 1
                    
            #bord haut de la grille
            elif 0 < x < int(width-c) and y == 0 :
                if cellules[x, y+c] == 1 :
                    cpt += 1
                if cellules[x-c, y] == 1 :
                    cpt += 1
                if cellules[x+c, y] == 1 :
                    cpt += 1
                if cellules[x-c, y+c] == 1 :
                    cpt += 1
                if cellules[x+c, y+c] == 1 :
                    cpt += 1
                    
            #bord bas de la grille
            elif 0 < x < int(width-c) and y == int(height-c) :
                if cellules[x, y-c] == 1 :
                    cpt += 1
                if cellules[x-c, y] == 1 :
                    cpt += 1
                if cellules[x+c, y] == 1 :
                    cpt += 1
                if cellules[x-c, y-c] == 1 :
                    cpt += 1
                if cellules[x+c, y-c] == 1 :
                    cpt += 1
                    
            #tous les autres cas
            else :
                if cellules[x, y+c] == 1 :
                    cpt += 1
                if cellules[x, y-c] == 1 :
                    cpt += 1
                if cellules[x+c, y] == 1 :
                    cpt += 1
                if cellules[x-c, y] == 1 :
                    cpt += 1
                if cellules[x-c, y-c] == 1 :
                    cpt += 1
                if cellules[x+c, y-c] == 1 :
                    cpt += 1
                if cellules[x-c, y+c] == 1 :
                    cpt += 1
                if cellules[x+c, y+c] == 1 :
                    cpt += 1
            
            nbcellules[x, y] = cpt
            
            j += 1
        i += 1
    
    evolution()
    
    if flag :
        fen.after(vitesse,run)
        

def evolution() :
    can.delete(ALL)
    creation_grille()
    
    i = 0
    while i != width/c :
        j = 0
        while j != width/c :
            x = i*c
            y = j*c
            
            #décrémentation de la durée de vie
            if dureevie[x,y] > 0 :
                dureevie[x,y] -= 1
            
            #règles
            if cellules[x,y] == 0 and nbcellules[x,y] >= 3 :
                cellules[x,y] = 1
                dureevie[x,y] = randint(mini,maxi)
                can.create_rectangle(x, y, x+c, y+c, fill='black')
            elif nbcellules[x,y] == 2 :
                if cellules[x,y] == 1 :
                    can.create_rectangle(x, y, x+c, y+c, fill='black')
                else :
                    can.create_rectangle(x, y, x+c, y+c, fill='white')
            elif nbcellules[x,y] < 2 or dureevie[x,y] == 0 :
                cellules[x,y] = 0
                dureevie[x,y] = -1
                can.create_rectangle(x, y, x+c, y+c, fill='white')
            #cas où rien ne se passe. Il faut redessiner la cellule
            else:
                if cellules[x,y] == 1 :
                    can.create_rectangle(x, y, x+c, y+c, fill='black')
                else :
                    can.create_rectangle(x, y, x+c, y+c, fill='white')
            
            j += 1
        i += 1
        
    step = int(label_steps.cget("text"))
    newstep = step + 1
    label_steps.configure(text = newstep)


# ========== Variables ==========

#taille des cellules
c = 15

#taille de la grille
height = 600
width = 600

#booléen indiquant l'état de la simulation (true pour lancée, false pour stoppée)
flag = False

#vitesse de l'animation
vitesse = 200

#bornes pour la durée de vie aléatoire
mini = 4
maxi = 10

#dictionnaires
cellules = {}       # contient les valeurs de chaque cellule (1 pour vivant, 0 pour mort)
nbcellules = {}     #contient le nombre de cellules vivanttes autour de chaque cellule
dureevie = {}

# Fenetre
    
fen = Tk()
fen.title("Life game waste version")
can = Canvas(fen, width = width, height = height, bg = 'white')

# Events binding
can.bind("<Button-1>", clic_gauche)
can.bind("<Button-3>", clic_droit)
can.pack(side = TOP, padx = 5, pady = 5)

creation_grille()
init_cases();

button_go = Button(fen, text = 'Démarrer', command = go)
button_stop = Button(fen, text = 'Arrêter', command = stop)
button_reset = Button(fen, text = 'Réinitialiser', command = reset)
label_steps = Label(fen, text="0")

button_go.pack(side = LEFT, padx = 3, pady = 3)
button_stop.pack(side = LEFT, padx = 3, pady = 3)
button_reset.pack(side = LEFT, padx = 3, pady = 3)
label_steps.pack(side = RIGHT, padx = 3, pady = 3)

fen.mainloop()