import curses
import random

from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

ANCHO = 35
ALTO  = 20

MAX_X = ANCHO - 2
MAX_Y = ALTO - 2

TIMEOUT = 500

class Cuerpo:
    def __init__(self, x, y, char="X"):
        self.x = x
        self.y = y
        self.char = char

    def coor(self):
        return self.x, self.y

class Comida:
    def __init__(self, window, char="@"):
        self.x = random.randint(1, MAX_X)
        self.y = random.randint(1, MAX_Y)
        self.char = char
        self.window = window

    def dibujar(self):
        self.window.addstr(self.y, self.x, self.char)

    def resetear(self):
        self.x = random.randint(1, MAX_X)
        self.y = random.randint(1, MAX_Y)

class Snake:
    def __init__(self, window):
        self.cuerpo_lista = []  
        self.x = 1
        self.y = 3
        self.lenght = 3

        for i in range(self.x, self.x + self.lenght):
            self.cuerpo_lista.append(Cuerpo(i, self.y))

        self.window = window
        self.direccion = curses.KEY_RIGHT
        self.movimientos = {
            curses.KEY_UP: self.mov_arriba,
            curses.KEY_DOWN: self.mov_abajo,
            curses.KEY_RIGHT: self.mov_derecha,
            curses.KEY_LEFT: self.mov_izquierda}

        self.direccion_rev = {
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_RIGHT: curses.KEY_LEFT}

    @property
    def cabeza(self):
        return self.cuerpo_lista[-1]

    def cambiar_direccion(self, direccion):
        if direccion != self.direccion_rev[self.direccion]:
            self.direccion = direccion

    def actualizar(self):
        nueva_cabeza = Cuerpo(self.cabeza.x, self.cabeza.y)
        self.cuerpo_lista.insert(-1, nueva_cabeza)
        self.movimientos[self.direccion]()

        if snake.cabeza.x == comida.x and snake.cabeza.y == comida.y:
            self.comer(comida)
        else:
            self.cuerpo_lista.pop(0)

    def mov_arriba(self):
        self.cabeza.y -= 1
        if self.cabeza.y < 1:
            self.cabeza.y = MAX_Y
    
    def mov_abajo(self):
        self.cabeza.y += 1
        if self.cabeza.y > MAX_Y:
            self.cabeza.y = 1
    
    def mov_derecha(self):
        self.cabeza.x += 1
        if self.cabeza.x > MAX_X:
            self.cabeza.x = 1

    def mov_izquierda(self):
        self.cabeza.x -= 1
        if self.cabeza.x < 1:
            self.cabeza.x = MAX_X

    def dibujar(self):
        for cuerpo in self.cuerpo_lista:
            self.window.addstr(cuerpo.y, cuerpo.x, "X")

    def comer(self, comida):
        comida.resetear()

if __name__ == "__main__":
    curses.initscr()
    curses.beep()
    window = curses.newwin(ALTO, ANCHO, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)    
    curses.noecho()
    curses.curs_set(0)

    snake = Snake(window)
    comida = Comida(window)

    while True:
        window.clear()
        window.border(0)

        snake.dibujar()
        comida.dibujar()

        event = window.getch()
        if event == 27:
            break
        if event in [KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP]:
            snake.cambiar_direccion(event)
        snake.actualizar()
        
    curses.echo()
    curses.endwin()
