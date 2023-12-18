import config
import clases
import main

# Renderiza el número de turno y devuelve ese número más uno
def num_turno():

	# Renderiza el número de turno
	print(f"Turno {config.num_turno}")

	# Devuelve el número de turno incrementado en uno
	config.num_turno += 1

# Renderiza el tablero
def tablero(tablero):

	pos = tablero.obtener_posicion()
	for posicion, pieza in pos.items():
		print(f"En la posición {posicion}")
		if pieza != None:
			print(f"hay una pieza {type(pieza).__name__} de color {pieza.color}")
		else:
			print("No hay nada")