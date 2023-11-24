import config

# Renderiza el número de turno y devuelve ese número más uno
def num_turno():

	# Renderiza el número de turno
	print(f"Turno {config.num_turno}")

	# Devuelve el número de turno incrementado en uno
	config.num_turno += 1

# Renderiza el tablero vacio
def casillas():
	for i in range(1, 9):
		print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
		for i in range(1, 8):
			print("  |   ", end='')
		print("  |     ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")