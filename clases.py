class Pieza:

	def __init__(self, color):
		self.color = color


class Peon(Pieza):

	def __init__(self, color):
		super().__init__(color)

class Torre(Pieza):

	def __init__(self, color):
		super().__init__(color)

class Caballo(Pieza):

	def __init__(self, color):
		super().__init__(color)

class Alfil(Pieza):

	def __init__(self, color):
		super().__init__(color)

class Dama(Pieza):

	def __init__(self, color):
		super().__init__(color)

class Rey(Pieza):

	def __init__(self, color):
		super().__init__(color)
		self.esta_en_jaque = False

# Define la clase tablero
class Tablero():

	def __init__(self):

		#Indica que hay en cada casillad el tablero al principio de la partida, cada casilla llama a una pieza
		self.casillas_tablero = {
			(8, 1): Torre("negro"),
			(8, 2): Caballo("negro"),
			(8, 3): Alfil("negro"),
			(8, 5): Rey("negro"),
			(8, 4): Dama("negro"),
			(8, 6): Alfil("negro"),
			(8, 7): Caballo("negro"),
			(8, 8): Torre("negro"),

			(7, 1): Peon("negro"),
			(7, 2): Peon("negro"),
			(7, 3): Peon("negro"),
			(7, 4): Peon("negro"),
			(7, 5): Peon("negro"),
			(7, 6): Peon("negro"),
			(7, 7): Peon("negro"),
			(7, 8): Peon("negro"),

			(2, 1): Peon("blanco"),
			(2, 2): Peon("blanco"),
			(2, 3): Peon("blanco"),
			(2, 4): Peon("blanco"),
			(2, 5): Peon("blanco"),
			(2, 6): Peon("blanco"),
			(2, 7): Peon("blanco"),
			(2, 8): Peon("blanco"),

			(1, 1): Torre("blanco"),
			(1, 2): Caballo("blanco"),
			(1, 3): Alfil("blanco"),
			(1, 4): Dama("blanco"),
			(1, 5): Rey("blanco"),
			(1, 6): Alfil("blanco"),
			(1, 7): Caballo("blanco"),
			(1, 8): Torre("blanco"),
		}

	# Permite almacenar piezas en el lugar deseado
	def colocar_pieza(self, posicion, pieza):
		self.casillas_tablero[posicion] = pieza

	# Devulve lo que contiene una posicion del tablero
	def obtener_pieza(self, posicion):
		return self.casillas_tablero.get(posicion, None)

	# Permite eliminar piezas de las casillas
	def eliminar_pieza(self, posicion):
		if posicion in self.casillas_tablero:
			del self.casillas_tablero[posicion]
		else:
			print("No hay una pieza en esa posición.")

	# Mueve una pieza de una posicion a otra
	def mover_pieza(self, posicion_inicial, posicion_final):
		pieza = self.obtener_pieza(posicion_inicial)

		if pieza:
			# Verificar si la posición final está vacía o si hay una pieza rival
			if (
				self.obtener_pieza(posicion_final) is None
				or self.obtener_pieza(posicion_final).color != pieza.color
			):
				# Mueve la pieza
				self.colocar_pieza(posicion_final, pieza)
				self.eliminar_pieza(posicion_inicial)
			else:
				print("Movimiento no válido. Hay una pieza propia en la posición final.")
		else:
			print("No hay una pieza en la posición inicial.")