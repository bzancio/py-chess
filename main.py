import entradas
import render
import config
import logica
import clases

def main():

	# Inicializa el tablero, donde se definen las posiciones iniciales de cada pieza
	tablero = clases.Tablero()

	# Bucle principal del programa, se ejecutará continuamente
	while (True):

		# Actualiza el valor del número de turno
		render.num_turno()

		# Renderiza el tablero en modo dev (mostrando posición directamente)
		render.dev_tablero(tablero)

		# Renderiza el tablero de forma grafica (en desarrollo)
		render.tablero(tablero)

		# Pregunta en cada turno qué movimiento quiere hacer el usuario (actualmente inútil)
		entradas.movimiento(tablero)

		# Comprueba si el programa debe salir o continuar
		entradas.salir()


# Inicializa a main
if __name__ == "__main__":
	main()