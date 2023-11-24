import entradas
import render
import config

def main():

	# Bucle principal del programa, se ejecutará continuamente
	while (True):

		# Actualiza el valor del número de turno
		render.num_turno()

		# Pregunta en cada turno qué movimiento quiere hacer el usuario (actualmente inútil)
		entradas.movimiento()

		render.casilla()
		# Comprueba si el programa debe salir o continuar
		entradas.salir()


# Inicializa a main
if __name__ == "__main__":
	main()