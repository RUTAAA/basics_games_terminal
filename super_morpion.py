from pynput import keyboard



def on_press(key):
    global pressed
    try:
        if key.char==None:
            pressed = '5'
        else:
            pressed = key.char
    except AttributeError:
        pressed=0    
    return False


def afficher(g):
    for i in range(0, 8, 3):
        print('    ╷   ╷   ' + ' ┃ ' + '   ╷   ╷   ' + ' ┃ ' + '   ╷   ╷    ')
        print('  ' + g[i][0][0] + ' │ ' + g[i][0][1] + ' │ ' + g[i][0][2] + ' ' + ' ┃ ' + ' ' + g[i+1][0][0] + ' │ ' + g[i+1][0][1] + ' │ ' + g[i+1][0][2] + ' ' + ' ┃ ' + ' ' + g[i+2][0][0] + ' │ ' + g[i+2][0][1] + ' │ ' + g[i+2][0][2] + '  ')
        print(' ───┼───┼───' + ' ┃ ' + '───┼───┼───' + ' ┃ ' + '───┼───┼─── ')
        print('  ' + g[i][1][0] + ' │ ' + g[i][1][1] + ' │ ' + g[i][1][2] + ' ' + ' ┃ ' + ' ' + g[i+1][1][0] + ' │ ' + g[i+1][1][1] + ' │ ' + g[i+1][1][2] + ' ' + ' ┃ ' + ' ' + g[i+2][1][0] + ' │ ' + g[i+2][1][1] + ' │ ' + g[i+2][1][2] + '  ')
        print(' ───┼───┼───' + ' ┃ ' + '───┼───┼───' + ' ┃ ' + '───┼───┼─── ')
        print('  ' + g[i][2][0] + ' │ ' + g[i][2][1] + ' │ ' + g[i][2][2] + ' ' + ' ┃ ' + ' ' + g[i+1][2][0] + ' │ ' + g[i+1][2][1] + ' │ ' + g[i+1][2][2] + ' ' + ' ┃ ' + ' ' + g[i+2][2][0] + ' │ ' + g[i+2][2][1] + ' │ ' + g[i+2][2][2] + '  ')
        print('    ╵   ╵   ' + ' ┃ ' + '   ╵   ╵   ' + ' ┃ ' + '   ╵   ╵    ')
        if(i != 6):
            print('╺━━━━━━━━━━━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━╸')


def jouer(G, g, n, r):
    c=0
    for i in range(3):
        for j in range(3):
            if g[n][i][j] != ' ':
                c+=1
    if c==9:
        fin(G, g, r, True)
        return g, n
        

    if(r%2 == 0):
        player = 'x'
    else:
        player = 'o'
    
    global pressed
    a=True
    while a:
        b=True
        while b:
            pressed=0
            with keyboard.Listener(on_press=on_press) as listener:listener.join()
            if pressed=='7':
                x=0
                y=0
                b=False
            elif pressed=='8':
                x=1
                y=0
                b=False
            elif pressed=='9':
                x=2
                y=0
                b=False
            elif pressed=='4':
                x=0
                y=1
                b=False
            elif pressed=='5':
                x=1
                y=1
                b=False
            elif pressed=='6':
                x=2
                y=1
                b=False
            elif pressed=='1':
                x=0
                y=2
                b=False
            elif pressed=='2':
                x=1
                y=2
                b=False
            elif pressed=='3':
                x=2
                y=2
                b=False
        if g[n][y][x] == ' ':
            g[n][y][x] = player
            a=False
        else:
            print("Emplacement pris")    

    if x==0 and y==0:
        n=0
    elif x==1 and y==0:
        n=1
    elif x==2 and y==0:
        n=2
    elif x==0 and y==1:
        n=3
    elif x==1 and y==1:
        n=4
    elif x==2 and y==1:
        n=5
    elif x==0 and y==2:
        n=6
    elif x==1 and y==2:
        n=7
    elif x==2 and y==2:
        n=8

    return g, n



def verifier(G, g, r):
    if(r%2 == 0):
        player = 'x'
    else:
        player = 'o'
    
    for i in range(9):
        for j in range(3):
            if g[i][j][0] == g[i][j][1] == g[i][j][2] != ' ' :
                if G[i//3][i-(i//3*3)] == ' ':
                    G[i//3][i-(i//3*3)]=player
            if g[i][0][j] == g[i][1][j] == g[i][2][j] != ' ' :
                if G[i//3][i-(i//3*3)] == ' ':
                    G[i//3][i-(i//3*3)]=player
        if g[i][0][0] == g[i][1][1] == g[i][2][2] != ' ' :
            if G[i//3][i-(i//3*3)] == ' ':
                G[i//3][i-(i//3*3)]=player
        if g[i][2][0] == g[i][1][1] == g[i][0][2] != ' ' :
            if G[i//3][i-(i//3*3)] == ' ':
                G[i//3][i-(i//3*3)]=player
    
    for i in range(3):
        if G[i][0] == G[i][1] == G[i][2] != ' ' :
            return True, G
        if G[0][i] == G[1][i] == G[2][i] != ' ' :
            return True, G
    if G[0][0] == G[1][1] == G[2][2] != ' ' :
        return True, G
    if G[2][0] == G[1][1] == G[0][2] != ' ' :
        return True, G
    return False, G



def fin(G, g, r, tie):
    if tie:
        print()
        print('Egalite !')
    
    else:
        if(r%2 == 0):
            player = 'x'
        else:
            player = 'o'
        print()
        print('Les ' + player + ' ont gagnes !')
    
    print()
    afficher(g)
    print()
    print('   ╻   ╻   ')
    print(' ' + G[0][0] + ' ┃ ' + G[0][1] + ' ┃ ' + G[0][2] + ' ')
    print('━━━╋━━━╋━━━')
    print(' ' + G[1][0] + ' ┃ ' + G[1][1] + ' ┃ ' + G[1][2] + ' ')
    print('━━━╋━━━╋━━━')
    print(' ' + G[2][0] + ' ┃ ' + G[2][1] + ' ┃ ' + G[2][2] + ' ')
    print('   ╹   ╹   ')
    exit()





grids= [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]
grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
next = 4
round = 0
pressed = 0
verification = False
running = True

while running:
    round += 1
    afficher(grids)
    grids, next = jouer(grid, grids, next, round)
    print()
    print()
    print()
    verification, grid = verifier(grid, grids, round)
    if verification:
        running = fin(grid, grids, round, False)
