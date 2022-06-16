import curses
import random

# Configuracion del tamaño de la ventada
ALTO  = 20
ANCHO = 60
curses.initscr()

window = curses.newwin(ALTO, ANCHO, 0, 0)

# Leer teclas especiales (arriba, abajo, ...)
window.keypad(True)

# Esconder las teclas que se presionen
curses.noecho()

# Esconder el cursor
curses.curs_set(False)

window.border()
window.nodelay(1)

# Culebra: [[y1, x1], [y2, x2], ...]
snake = [[4,4],[4,3],[4,2]]

# Comida: [y, x]
food  = [10,20]

# Dibujando la comida
window.addch(food[0],food[1],'O')

key   = curses.KEY_RIGHT 
moves = [curses.KEY_DOWN, 
         curses.KEY_UP, 
         curses.KEY_RIGHT, 
         curses.KEY_LEFT,
         27]

while key != 27:
    window.border()

    # Tiempo de espera
    window.timeout(100)

    default_key = key
    event = window.getch()
    
    # Si no presiona una tecla
    if event != -1: 
        key = event
    
    # Se conserva el movimiento
    if key not in moves:
        key = default_key
    else:
        if key == curses.KEY_DOWN:
            snake.insert(0, [snake[0][0]+1, snake[0][1]])
        elif key == curses.KEY_UP:
            snake.insert(0, [snake[0][0]-1, snake[0][1]])
        elif key == curses.KEY_LEFT:
            snake.insert(0, [snake[0][0], snake[0][1]-1])
        elif key == curses.KEY_RIGHT:
            snake.insert(0, [snake[0][0], snake[0][1]+1])
    
    # Dibujando una nueva comida
    if snake[0] == food:
        while food in snake:
            food = [random.randint(1,18), random.randint(1,58)]
        window.addch(food[0], food[1], 'O')
    
    # Se elimina la cola y crea una nueva cabeza
    else: 
        last = snake.pop()
        window.addch(last[0],last[1]," ")

    for i in range(len(snake)):
        window.addch(snake[i][0],snake[i][1],"X")
    
    window.refresh()
    
    # Si se sale de la ventana
    if snake[0][0] < 1 or snake[0][0] > ALTO - 2:
        break
    if snake[0][1] < 1 or snake[0][1] > ANCHO - 2:
        break

curses.endwin()
