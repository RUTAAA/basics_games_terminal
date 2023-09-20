from pynput import keyboard
import random
import os



def moveUp(g):
    l = len(g)
    for i in range(l):
        z = 0
        for j in range(l-1):
            if g[j][i] == 0:
                z+=1
        if z == 1:
            for j in range(l-1):
                if g[j][i] == 0:
                    g[j][i] = g[j+1][i]
                    g[j+1][i] = 0
        elif z == 2:
            a = 0
            for j in range(1, l):
                if g[j][i] != 0:
                    if j == l-1:
                        a = 1
                    g[a][i] = g[j][i]
                    g[j][i] = 0
                    a = 1
        elif z == 3:
            for j in range(l):
                if g[j][i] != 0:
                    g[0][i] = g[j][i]
                    g[j][i] = 0

def addUp(g):
    l = len(g)
    for i in range(l):
        for j in range(l-1):
            if g[j][i] == g[j+1][i]:
                g[j][i] += g[j+1][i]
                g[j+1][i] = 0



def moveDown(g):
    l = len(g)
    for i in range(l):
        z = 0
        for j in range(l-1, 0, -1):
            if g[j][i] == 0:
                z+=1
        if z == 1:
            for j in range(l-1, 0, -1):
                if g[j][i] == 0:
                    g[j][i] = g[j-1][i]
                    g[j-1][i] = 0
        elif z == 2:
            a = l-1
            for j in range(l-2, -1, -1):
                if g[j][i] != 0:
                    if j == 0:
                        a = l-2
                    g[a][i] = g[j][i]
                    g[j][i] = 0
                    a = l-2
        elif z == 3:
            for j in range(l-1, -1, -1):
                if g[j][i] != 0:
                    g[l-1][i] = g[j][i]
                    g[j][i] = 0

def addDown(g):
    l = len(g)
    for i in range(l):
        for j in range(l-1, 0, -1):
            if g[j][i] == g[j-1][i]:
                g[j][i] += g[j-1][i]
                g[j-1][i] = 0



def moveLeft(g):
    l = len(g)
    for i in range(l):
        z = 0
        for j in range(l-1):
            if g[i][j] == 0:
                z+=1
        if z == 1:
            for j in range(l-1):
                if g[i][j] == 0:
                    g[i][j] = g[i][j+1]
                    g[i][j+1] = 0
        elif z == 2:
            a = 0
            for j in range(1, l):
                if g[i][j] != 0:
                    if j == l-1:
                        a = 1
                    g[i][a] = g[i][j]
                    g[i][j] = 0
                    a = 1
        elif z == 3:
            for j in range(l):
                if g[i][j] != 0:
                    g[i][0] = g[i][j]
                    g[i][j] = 0

def addLeft(g):
    l = len(g)
    for i in range(l):
        for j in range(l-1):
            if g[i][j] == g[i][j+1]:
                g[i][j] += g[i][j+1]
                g[i][j+1] = 0



def moveRight(g):
    l = len(g)
    for i in range(l):
        z = 0
        for j in range(l-1, 0, -1):
            if g[i][j] == 0:
                z+=1
        if z == 1:
            for j in range(l-1, 0, -1):
                if g[i][j] == 0:
                    g[i][j] = g[i][j-1]
                    g[i][j-1] = 0
        elif z == 2:
            a = l-1
            for j in range(l-2, -1, -1):
                if g[i][j] != 0:
                    if j == 0:
                        a = l-2
                    g[i][a] = g[i][j]
                    g[i][j] = 0
                    a = l-2
        elif z == 3:
            for j in range(l-1, -1, -1):
                if g[i][j] != 0:
                    g[i][l-1] = g[i][j]
                    g[i][j] = 0

def addRight(g):
    l = len(g)
    for i in range(l):
        for j in range(l-1, 0, -1):
            if g[i][j] == g[i][j-1]:
                g[i][j] += g[i][j-1]
                g[i][j-1] = 0






def apparaitre(g):
    z = 0
    iz = []
    jz = []
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 0:
                z += 1
                iz.append(i)
                jz.append(j)
    if z != 0:
        x = random.randint(0, z-1)
        if random.randint(1, 10) == 10:
            g[iz[x]][jz[x]] = 4
        else:
            g[iz[x]][jz[x]] = 2
        
                    


def afficher(g):
    os.system('clear')
    print()
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 0:
                print("    ", end=" ")
            else:
                
                print(str(g[i][j]).center(4), end=" ")
        print()
        print()
    print()



def jouer(g, x):
    G = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(g)):
        for j in range(len(g[i])):
            G[i][j] = g[i][j]
    if x == 'up':
        moveUp(g)
        addUp(g)
        moveUp(g)
    elif x == 'down':
        moveDown(g)
        addDown(g)
        moveDown(g)
    elif x == 'left':
        moveLeft(g)
        addLeft(g)
        moveLeft(g)
    elif x == 'right':
        moveRight(g)
        addRight(g)
        moveRight(g)
    a = False
    for i in range(len(g)):
        for j in range(len(g[i])):
            print(a)
            if G[i][j] != g[i][j]:
                a = True
    if a:
        apparaitre(grid)





grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

def on_press(key):
    if str(key) == 'Key.esc':
        exit()
    elif str(key) == 'Key.up':
        jouer(grid, 'up')
    elif str(key) == 'Key.down':
        jouer(grid, 'down')
    elif str(key) == 'Key.left':
        jouer(grid, 'left')
    elif str(key) == 'Key.right':
        jouer(grid, 'right')
    afficher(grid)

apparaitre(grid)
afficher(grid)
print("ESC to quit")
with keyboard.Listener(on_press=on_press) as listener:listener.join()