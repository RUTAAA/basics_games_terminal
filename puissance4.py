def afficher(g):
    print('╷   ╷   ╷   ╷   ╷   ╷   ╷   ╷')
    for i in range(len(g)-1):
        for j in range(len(g[i])-1):
            print('│ ' + g[i][j], end=' ')
        print('│ ' + g[i][len(g[i])-1] + ' │')
        print('├───┼───┼───┼───┼───┼───┼───┤')
    
    for j in range(len(g[len(g)-1])-1):
        print('│ ' + g[len(g)-1][j], end=' ')
    print('│ ' + g[len(g)-1][len(g[len(g)-1])-1] + ' │')
    print('└───┴───┴───┴───┴───┴───┴───┘')



def jouer(g, r):
    if(r%2 == 0):
        player = 'x'
    else:
        player = 'o'
    
    a=True
    while a:
        x=0
        while x<1 or x>7:
            x = int(input("Colonne numero : "))
        y=''
        while not(y == '+' or y == '-'):
            y = input("Mettre (+) ou enlever (-) : ")

        if y == '+':
            for i in range(len(g)-1, -1, -1):
                if g[i][x-1] == ' ':
                    g[i][x-1] = player
                    a=False
                    return g
            print("Pas de place")
        
        elif y == '-':
            b=[]
            for i in range(len(g)-1):
                b.append(g[i][x-1])
            g[0][x-1]=' '
            for i in range(len(g)-1):
                g[i+1][x-1]=b[i]
            a=False
            return g
    



def verifier(g):
    L = len(g)

    for i in range(L):
        for j in range(len(g[i])-3):
            if g[i][j] == g[i][j+1] == g[i][j+2] == g[i][j+3] != ' ' :
                return True
    
    for i in range(len(g[0])):
        for j in range(L-3):
            if g[j][i] == g[j+1][i] == g[j+2][i] == g[j+3][i] != ' ' :
                return True
    
    for i in range(L-3):
        for j in range(len(g[0])-3):
            if g[i][j] == g[i+1][j+1] == g[i+2][j+2] == g[i+3][j+3] != ' ' :
                return True
            if g[L-i-1][j] == g[L-i-2][j+1] == g[L-i-3][j+2] == g[L-i-4][j+3] != ' ' :
                return True
    
    return False



def fin(g, r):
    if(r%2 == 0):
        player = 'x'
    else:
        player = 'o'
    print('Les ' + player + ' ont gagnes !')
    afficher(g)





grid = [[' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ']]

round = 0
running = True

while running:
    round += 1
    afficher(grid)
    grid = jouer(grid, round)
    if verifier(grid):
        running = False
        fin(grid, round)
