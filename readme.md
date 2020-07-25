<div align="center"> <h1> Curso Básico de Python </h1> </div>

## Ventajas de aprender python

- Es Fácil de aprender, es un lenguaje que esta en contacto con el idioma ingles
- Elegante, python necesita de una estructura definida para funcionar correctamente
- Python ayuda a tener buenas practicas, para que a la hora de pasar a otro lenguaje se nos haga mucho más sencillo

## ¿Que es un Algoritmo?

- Un algoritmo es una serie de pasos ordenados para resolver un problema
- Tiene que tener un Inicio y Fin claro, es decir un Algoritmo es Finito
- No es Ambiguo

## La mejor herramienta: La consola

- La consola nos permite interactuar con nuestra computadora mediante el codigo
- Comandos basicos en la consola.
  - Ctrl + L o clear = Limpia La consola
  - cd = change directory cambia de directorio
  - cd .. = cambia de directorio a la carpeta padre de esta
  - ls = list nos lista todos los archivos del directorio
  - mkdir = Make Directory, Crear directorio
  - touch = nos crea un archivo
- Python cuenta con una consola interactiva que se inicia con el comando py en windows, python3 para usuarios Unix

## Cuales son los operadores aritméticos en Python?

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

## ¿Que es una variable?

- El termino variable se utiliza fuera del ambito matematico para designar una cantidad susceptible de tomar distintos valores numéricos dentro de un cojunto de números especificado. En otras palabras podemos asociar una variable en la vida real con una caja, esta caja tendra un identificador unico y en esta podemos guardar objetos: números, texto, etc.
- Para declarar una variable en python lo hacemos de la siguiente manera:

  ```python
  ## primero colocamos el nombre de la variable "identificador" seguido de un
  ##igual (=) que significa asignación

  numero = 3
  print(numero) # => 3
  ```

- Las variables las podemos operar, lo que entendera el lenguaje es que tiene que operar el contenido de la variable, tambien podemos guardar una variable dentro de otra por ejemplo, si guardamos dos numeros en dos distintas variables y luego hacemos alguna operacion matematica, podemos guardar el resultado de esa operacion en una variable

  ```python
  	numero1 = 2
  	numero2 = 3
  	numero_resultado = numero1 + numero2
  	print(numero_resultado) # => 5
  ```

- Las variables se pueden reescribir
- Las variables tienen reglas que son:
  - El identificador o nombre de variable no puede comenzar con un número y debe estar en minúsculas. Las palabras dentro del mismo se separan con un guión bajo

## Tipos de datos

- En python todo es un objeto
- Los más sencillos son, los enteros (int), Números punto flotante(float), texto o cadenas de caracteres (string), Booleanos (true o false)
- Trabajando con las variables

  ```python
  nombre = "Sergio"
  nombre2 = 'Luis'

  nombre + nombre2 # => "SergioLuis" # Concatenacion la union de dos o más strings
  nombre + " " + nombre2 # => "Sergio Luis"
  nombre * 4 # => "SergioSergioSergioSergio" # Podemos multiplicar el string

  numero_decimal = 3.4 # Para los numeros decimales siempre se utiliza el punt (.)

  es_estudiante = True

  ```

## Operadores lógicos y de comparacion

- Operadores logicos
  - and - para que se pueda cumplir la condicion todas las variables comparadas tienen que ser verdaderas
  - or - para que se pueda cumplir la condicion almenos una de las variables comparadas tiene que ser verdaderas, para que la condicion de falso todas las variables comparadas tienen que ser false
  - not - invierte el valor de una variable, es decir si una variable es true y colocamos not la variable cambiara a false
- Operadores de comparacion

  - (==) igualdad, nos valida que el contenido de las variables sean iguales

    ```python
    numero1 = 5
    numero2 = 5

    numero1 == numero2 #=> True
    ```

  - (≠) distinto, nos valida que el contenido de las variables no sean iguales
  - (>) mayor, compara si una variale es mayor que el otro
  - (<) menor,compara si una variale es menor que el otro
  - (⇒) mayor o igual
  - (≤) menor o igual

## Condicionales

- La regla de identacion seguido de if es de 4 espacios
- If es una condicion que nos dice en pocas palabras, Sí la condicion se cumple haz algo y Si no haz otra cosa

  ```python
  if edad >= 18:
  		print('Eres mayor de edad')
  else:
  		print('Eres menor de edad')
  ```

  Esto se leé de la siguiente forma: Si tu edad es mayor o igual a 18 eres mayor de edad, si no eres menor de edad.

- elif significa si no y va entre el if y el else
- else si no, que significa, si ninguno de los casos anteriores se cumplieron ejecuta lo que esta dentro

## Funciones

- Para declarar una funcion se utiliza la palabra reservada "def" seguido del nombre de la funcion con dos parentesis y en caso de que la funcion reciba parametros se los ponemos dentro
- Las funciones pueden devolver datos en caso de que los necesitemos y para esto se utiliza la palabra reservada "return" seguido del nombre de la variable que queremos retornar

## Metodos

- Un metodo es una funcion especial para un tipo de dato en particular
- Convertir Datos a un tipo diferente

  - input() para pedirle al usuario que introduzca datos.

    ```python
    numero1 = input("Escribe un numero") # 2
    print(numero1)
    #=> '2'
    ```

  - int() convierte datos o variables dentro de los parentecis en tipo entero

    ```python
    numero1 = int(numero1) # pasamos la variable que tiene nuestro string
    print(numero1)
    # => 2
    ```

  - str() nos convierte datos o variables dentro de los parentecis en tipo string

    ```python
    numero_decimal = 4.5
    str(numero_decimal)
    # => '4.5'
    ```

  - float() nos convierte datos o variables en tipo float

- Transformar Cadenas de caracteres
  - upper() Transforma todos los caracteres en mayusculas
  - capitalize() Transforma el primer caracter en mayusculas
  - strip() Elimina los espacios que estan al principio o al final de la cadena
  - lower() transforma la cadena de caracteres a minisculas
  - replace('in','out') este metodo recibe dos parametros el primero es el dato que sera reemplazado por el segundo
  - para poder acceder a los indices de una cadena se hace con [ ]
  - len() nos trae cuantos caracteres tiene la cadena
- round(dato, numero de decimales) recibe dos parametros el dato o variable y el numero de decimales que queremos EJ: round(5.76543, 2) ⇒ 5.76
- range(valor inicial, valor final, incremento) la funcion range devuelve una secuencia de numeros, comenzando desde el valor inicial y se encrementa en 1(por defecto), sin embargo, es posible especificar el valor de incremento agregando un tercer parámetro y termina en el valor final que le establezcamos.

**EJ:** range(1,5) ⇒ [1, 2, 3, 4]. Como se ve en el ejemplo el valor final no es incluyente

## Slices

- Podemos dividir cadenas de texto utilizando slices de la siguiente forma

  Se accede a los indices, en los corchetes colocamos el indice desde donde queremos dividir la cadena colocamos dos puntos y el indice hasta donde queremos dividir

  ```python
  nombre[1:3]
  # Cuando no colocamos el primer indice
  nombre[:3]
  # Quiere decir que empieza a dividir desde el principio de la cadena
  nombre[3:]
  # y es igual para el caso contrario
  ```

  A esto tambien le podemos agregar un tercer valor que es el numero de saltos que va a dar para dividir la cadena es decir si colocamos dos va a ir de dos en dos

## Punto de entrada y funcion principal

- En python es una buena practica tener una funcion principal que es la que nos va a correr el programa al principio, un estandar para definir esta funcion es:

  ```python
  def run():
  ```

- Punto de entrada en python se hace de la siguiente forma

  ```python
  if __name__ == '__main__':
  		pass
  ```

  Esto quiere decir que python va a correr todo lo que este dentro de este bloque de codigo

- Una buena practica en python es siempre dejar dos espacios entre funciones

## Bucles en Python

Un bucle es algo que podemos hacer iterar una cantidad determinada de veces

- while

  While significa Mientras qué y lo que hace es que mientras que la condicion en la exprecion se cumpla ejecutara el bloque de codigo

  ```python
  while expresión:
      pass
  ```

- for

  Un bucle for se usa para iterar sobre una secuencia(que es una lista, una tupla, un diccionario, un cojunto o una cadena), podemos ejecutar un cojunto de declaraciones, una vez para cada elemento de una lista, tupla, etc.

  ```python
  for target_list in expression_list:
      pass
  ```

  Tambien podemos recorrer una cadena(string) con un for, esto quiere decir que vamos a tomar una cadena de caracteres y vamos a ir por cada parte unica o indice a la vez dentro de un ciclo

  - **Interrumpiendo ciclos con break y continue**

    - **break** simplemente termina el bucle actual y continua con la ejecucíon de la siguiente instrucción, por ejemplo:

      ```python
      def run():
          for i in range(10000):
              print(i)
              if i == 5678:
                  break
      ```

      En el anterior ejemplo declaramos un bucle **for** y lo hacemos iterar desde el 0 hasta 9999, imprimiendo cada paso que de **i**, cuando **i** llegue a 5678 el bucle se terminara

    - **break** con while

      ```python
      def run():
      		LIMITE = 10
          contador = 0
          while contador < LIMITE:
              print(contador)
              contador += 1
              if contador == 5:
                  break
      ```

      En este ejemplo definimos un **Limite**, un **contador** y decimos, mientras que el **contador** sea menor que el **limite** imprime el contador y despues sumale 1, si contador es igual a 5 termina de ejecutarte.

    - **continue** Cuando aparece un continue en python este regresa al comienzo del bucle, ignorando todos los estamentos que quedan en la iteración del bucle e inicia la siguiente iteración, **continue** se puede utilizar tanto en bucles **for** como en bucles **while.** Ejemplo de **continue** en bucle **for**

      ```python
      def run():
          for contador in range(1000):
              if contador % 2 != 0:
                  continue
              print(contador)
      ```

      En este ejemplo declaramos un ciclo for con un contador y que este itere en un rango de 0 a 9999, si contador % 2 ≠ 0, es decir si el contador es impar ejecuta continue y al final imprime contador. Lo que nos retornara el programa son todos los numeros pares de 0 a 9999 por que **continue** nunca dejara que se impriman los impares

## Constantes en Python

- Las constates son lo opuesto a las variables es decir, que no va a variar y que siempre estara en un numero fijo, en python estas variables se declaran colocando su nombre todo en mayuscula

  ```python
  LIMITE = 1000;
  ```
