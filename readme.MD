# Py-chess

Proyecto de ajedrez basico en python

## Índice

- Módulos
- Depencias

### Módulos (sujeto a cambios):

- main.py     -->   Bucle principal              (Izan)
- config.py   -->   Constantes y opciones        (????)
- clases.py   -->   Definiciones de las clases   (Javi)
- lógica.py   -->   Lógica del ajedrez           (????)
- render.py   -->   Render de elementos          (Izan)
- entradas.py -->   Gestión de entradas          (????)

#### main.py

Este módulo contiene el bucle principal del programa, la idea es que aquí haya el mínimo código y que main vaya llamando a cada módulo para las diferentes tareas

#### config.py

Este módulo tiene todas las constantes que solo se pueden definir al principio del programa, si hay algo que cambie el comportamiento general del programa hay que ponerlo aquí
(Módulo dudoso: ¿Quizá es posible tener muchas de las variables haciendo clases con ciertas funciones y metiéndolas como atributos?)

#### clases.py

Este módulo contiene todas las clases necesarias para el programa, esto incluye sus métodos y atributos, este módulo almacenará toda la información de todos los elementos de la partida

#### lógica.py

La idea es tener toda la lógica del ajedrez aquí, este módulo se comunica con clases.py para modificar sus propiedades y efectuar los movimientos en la partida
(Módulo dudoso: ¿Quizá es posible tener toda la lógica en clases.py?)

#### render.py 

Este módulo se encarga de procesar la situación de la partida consultando a clases.py y sacando por pantalla el resultado

#### entradas.py

Este módulo gestiona todo lo que el usuario introduzca por pantalla, incluido comprobar y parsear los movimientos, posteriormente comunica al módulo lógica.py. las acciones

## Dependencias

- Librería keyboard para entradas por teclado (pip install keyboard)