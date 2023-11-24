import keyboard
import sys

# Examina si se ha presionado la tecla esc y si eso ocurre sale del programa o, si por el contrario, se ha presionado espacio, en cuyo caso el programa continuará normalmente
def salir():
	while(True):
		if keyboard.is_pressed('esc'):
			sys.exit()
		if keyboard.is_pressed('space'):
			break

"""
 Esto es una tremenda chapuza porque evalúa una única vez al final de cada turno, sirve para un apaño, pero esta por revisar 
 PD: No sé usar la librería Keyboard ayuda por favor :(
"""


# Espera a que el usuario introduzca el movimiento por pantalla y guarda ese valor en la variable mov
def movimiento():
	mov = input("Introduce un movimiento: ")

"""
 En un futuro, esto interactuará con logica.py o clases.py para hacer cosos, de momento es para probar a parar el programa
"""