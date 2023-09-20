from pynput import keyboard



def afficher(g):
    print('   ╷   ╷   ')
    print(' ' + g[0][0] + ' │ ' + g[0][1] + ' │ ' + g[0][2] + ' ')
    print('───┼───┼───')
    print(' ' + g[1][0] + ' │ ' + g[1][1] + ' │ ' + g[1][2] + ' ')
    print('───┼───┼───')
    print(' ' + g[2][0] + ' │ ' + g[2][1] + ' │ ' + g[2][2] + ' ')
    print('   ╵   ╵   ')



def jouer(g, r):
    if(r%2 == 0):
        player = 'x'
    else:
        player = 'o'
    
    x=3
    while x<0 or x>2:
        x = int(input("Placement en x : "))
    y=3
    while y<0 or y>2:
        y = int(input("Placement en y : "))
    
    g[y][x] = player
    return g



def verifier(g):
    for i in range(3):
        if g[i][0] == g[i][1] == g[i][2] != ' ' :
            return True
        if g[0][i] == g[1][i] == g[2][i] != ' ' :
            return True
    if g[0][0] == g[1][1] == g[2][2] != ' ' :
        return True
    if g[2][0] == g[1][1] == g[0][2] != ' ' :
        return True
    return False


def fin(r):
    if(r%2 == 0):
        player = 'x'
    else:
        player = 'o'
    print('Les ' + player + ' ont gagnes !')





grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

round = 0
running = True

while running:
    round += 1
    afficher(grid)
    grid = jouer(grid, round)
    if verifier(grid):
        running = False
        fin(round)
