import curses

# curses.initscr() retorna un objeto que
# representa a la ventana en la cual
# queremos dibujar 
screen = curses.initscr()

# Crear una nueva ventana
window = curses.newwin(20, 60, 0, 0)

# Esconder las teclas que se presionen
curses.noecho()

# Reaccionar a una tecla intantaneamente
curses.cbreak()

i = 0
while True:
#   Leer la tecla presionada. El resultado
#   es un numero de 0-255 que representa un
#   codigo ASCII (a es 097)
    char = screen.getch()

#   Si se presiona la tecla "q" entonces...
    if char == ord('q') or char == ord('Q'):
#       Salimos del bucle WHILE
        break

#   Si se presiona la tecla "h" entonces...
    if char == ord('p'):
#       Añadir un string en una posición
        window.addstr(2+i,2,"X")
        i = i + 1
#       Actualizacion de los caracteres
#       de la ventana
        window.refresh()

# Cerrar la ventana
curses.endwin()
