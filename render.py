import config
import clases
import main

# Renderiza el número de turno y devuelve ese número más uno
def num_turno():

	# Renderiza el número de turno
	print(f"Turno {config.num_turno}")

	# Devuelve el número de turno incrementado en uno
	config.num_turno += 1

# Renderiza el tablero en modo dev
def dev_tablero(tablero):

	pos = tablero.obtener_posicion()
	for posicion, pieza in pos.items():
		print(f"En la posición {posicion}")
		if pieza != None:
			print(f"hay una pieza {type(pieza).__name__} de color {pieza.color}")
		else:
			print("No hay nada")

# Renderiza el tablero graficamente
def tablero(tablero):

	pos = tablero.obtener_posicion()

	pos0= pos[0]


	for posicion, pieza in pos.items():
		if pieza == None:
			print("________")
			print("|       ")
			print("|       ")
			print("|       ", end="")
		if pieza != None:
			print("________")
			print("|       ")
			print("|   a   ")
			print("|       ", end="")