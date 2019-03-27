#!/usr/bin/env python
# -*- coding: utf-8 -*-
def saludo(nombre="mundo", numero=1){
if nombre!="mundo"{
if numero!=1{
for num in range(numero){
print("Hola "+nombre)
}
}else{
print("Hola "+nombre)
}
}else{
print("Hola mundo")
}
}
# Creando un diccionario con caracteres de escape en las llaves
personas=\{"Ernesto":5,"Juan":2,"Pedro":3}\
for persona in personas{
    saludo(persona, personas[persona])
}