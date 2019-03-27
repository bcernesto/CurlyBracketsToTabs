# Script Python para convertir llaves en tabulaciones

## Descripción

Este script está pensado para personas que tienen algún problema escribiendo código indentado, y prefieren el uso de llaves típico en otros lenguajes de programación como Java o C#.

El script convierte las llaves tanto al principio como al final de cada línea, en tabulaciones o espacios, según se especifique en los parámetros

Los retornos de carro utilizados en el archivo origen son respetados en el archivo destino, tanto para Windows, Mac o Linux.

Para usar llaves en diccionarios, será necesario usar el caracter de escape, ejemplo "\\{" para iniciarlo y "}\\" para cerrarlo.

personas=\\{"Ernesto":5,"Juan":2,"Pedro":3}\\

Para mejor comprensión, ver archivo ejemplo.py

## Funcionamiento

$ py cb2t.py --help

usage: cb2t.py [-h] -i INPUT [-o OUTPUT] [-t {tabs,spaces}] [-x {true,false}]

Conversor de llaves a tabulaciones

required arguments:

-i INPUT, --input INPUT:
Nombre de archivo a procesar. Si contiene espacios, encerrar entre comillas dobles

optional arguments:

-h, --help            show this help message and exit

-o OUTPUT, --output OUTPUT:
Nombre de archivo destino. Si contiene espacios, encerrar entre comillas dobles. Default: "output.py"

-t {tabs,spaces}, --tab {tabs,spaces}:
Caracter de tabulación. Valores aceptados: "tabs" para \t, o "spaces" para cuatro espacios. Default: "tabs"

-x {true,false}, --execute {true,false}:
Ejecutar el script al terminar. Default: false

## Ejemplo

$ py cb2t.py -i ejemplo.py -o ejemplo2.py -t tabs -x true

Se incluye el script de ejemplo con llaves.

## Anotaciones y Errores detectados

* Solo son interpretadas las llaves que están o al principio o al final de cada línea, no se procesan llaves intermedias.
* Si una línea comienza con "{", el signo de ":" no se aplica a la línea anterior, por lo que se recomienda poner las llaves de abrir al final de la línea donde comenzará el bloque, ejemplo: "def funcion(parametro){"
* En los diccionarios hay que usar los signos de escape en las llaves, a fin de que se copien al script de destino, mirar en el apartado descripción la manera.