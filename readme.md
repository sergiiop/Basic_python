- Ventajas de aprender python
  - Es Fácil de aprender, es un lenguaje que esta en contacto con el idioma ingles
  - Elegante, python necesita de una estructura definida para funcionar correctamente
  - Python ayuda a tener buenas practicas, para que a la hora de pasar a otro lenguaje se nos haga mucho más sencillo
- ¿Que es un Algoritmo?
  - Un algoritmo es una serie de pasos ordenados para resolver un problema
  - Tiene que tener un Inicio y Fin claro, es decir un Algoritmo es Finito
  - No es Ambiguo
- La mejor herramienta: La consola
  - La consola nos permite interactuar con nuestra computadora mediante el codigo
  - Comandos basicos en la consola.
    - Ctrl + L o clear = Limpia La consola
    - cd = change directory cambia de directorio
    - cd .. = cambia de directorio a la carpeta padre de esta
    - ls = list nos lista todos los archivos del directorio
    - mkdir = Make Directory, Crear directorio
    - touch = nos crea un archivo
  - Python cuenta con una consola interactiva que se inicia con el comando py en windows, python3 para usuarios Unix
- Cuales son los operadores aritméticos en Python?

  - En python los operadores aritméticos son los que nos ayudan a hacer las distintas operaciones matematicas

    - Suma (+)

      5+5 ⇒ 5

    - Resta (-)

      5-5 ⇒ 0

    - Multiplicación (\*)

      5\*5 ⇒ 25

    - División (/)
    - 21/5 ⇒ 4.2
    - División entera (//), Esta nos trae el numero entero de la division

      21 // 5 ⇒ 4

    - Modulo (%), Este nos trae el recidio de la division

      21 % 5 ⇒ 1

    - Potencia (\*\*)

      2 \*\* 2 ⇒ 4

    - Python respeta las reglas matematicas que dice

      5 + 5 \* 2 ⇒ 15

    - Raiz

      math.sqrt(9)

- ¿Que es una variable?

  - El termino variable se utiliza fuera del ambito matematico para designar una cantidad susceptible de tomar distintos valores numéricos dentro de un cojunto de números especificado. En otras palabras podemos asociar una variable en la vida real con una caja, esta caja tendra un identificador unico y en esta podemos guardar objetos: números, texto, etc.
  - Para declarar una variable en python lo hacemos de la siguiente manera:

    ```python
    // primero colocamos el nombre de la variable "identificador" seguido de un
    igual (=) que significa asignación

    numero = 3
    print(numero)
    => 3
    ```

  - Las variables las podemos operar, lo que entendera el lenguaje es que tiene que operar el contenido de la variable, tambien podemos guardar una variable dentro de otra por ejemplo, si guardamos dos numeros en dos distintas variables y luego hacemos alguna operacion matematica, podemos guardar el resultado de esa operacion en una variable

    ```python
    	numero1 = 2
    	numero2 = 3
    	numero_resultado = numero1 + numero2
    	print(numero_resultado) => 5
    ```

  - Las variables se pueden reescribir
  - Las variables tienen reglas que son:
    - El identificador o nombre de variable no puede comenzar con un número y debe estar en minúsculas. Las palabras dentro del mismo se separan con un guión bajo
