import config


# Renderiza el número de turno y devuelve ese número más uno
def num_turno():

	# Renderiza el número de turno
	print(f"Turno {config.num_turno}")

	# Devuelve el número de turno incrementado en uno
	config.num_turno += 1


# Renderiza un tablero de prueba (actualmente es inútil)
def tablero():
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("8 |  t  |  c  |  a  |  r  |  d  |  a  |  c  |  t  | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("7 |  p  |  p  |  p  |  p  |  p  |  p  |  p  |  p  | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("6 |     |     |     |     |     |     |     |     | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("5 |     |     |     |     |     |     |     |     | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("4 |     |     |     |     |     |     |     |     | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("3 |     |     |     |     |     |     |     |     | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("2 |  P  |  P  |  P  |  P  |  P  |  P  |  P  |  P  | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("1 |  T  |  C  |  A  |  D  |  R  |  A  |  C  |  T  | ")
	print("  +-----+-----+-----+-----+-----+-----+-----+-----+ ")
	print("     a     b     c     d     e     f     g     h    ")