#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
parser = argparse.ArgumentParser(description="Conversor de llaves a tabulaciones")
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument("-i", "--input", help="Nombre de archivo a procesar. Si contiene espacios, encerrar entre comillas dobles", required=True)
parser.add_argument("-o", "--output", help="Nombre de archivo destino. Si contiene espacios, encerrar entre comillas dobles. Default: \"output.py\"", default="output.py")
parser.add_argument("-t", "--tab", help="Caracter de tabulación. Valores aceptados: \"tabs\" para \\t, o \"spaces\" para cuatro espacios. Default: \"tabs\"", choices=["tabs","spaces"], default="tabs")
parser.add_argument("-x", "--execute", help="Ejecutar el script al terminar. Default: false", choices=["true","false"], default="false")
args = parser.parse_args()

numTabs=0
nextTabs=0
tabSimbol="\t" if(args.tab=="tabs") else "    "
returnSimbol="\n"
blockSimbol=""

f = open(args.input)
g = open(args.output,"w")
for linea in f:
    if len(linea)>2 and linea[-2:]=="\r\n":
        returnSimbol="\r\n"
    elif linea[-1]=="\r":
        returnSimbol="\r"
    else:
        returnSimbol="\n"
    while len(linea)>=len(returnSimbol) and linea[-len(returnSimbol)]==returnSimbol:
        linea=linea[:-len(returnSimbol)]
    linea=linea.strip()
    if len(linea)>0:
        inicio=linea[0]
    else:
        g.write(returnSimbol)
        inicio=""
    if inicio=="{" or inicio=="}":
        while inicio=="{" or inicio=="}":
            if inicio == "{":
                numTabs=numTabs+1
                linea=linea[1:].strip()
            elif inicio=="}":
                numTabs=numTabs-1
                linea=linea[1:].strip()
            if len(linea)>0:
                inicio=linea[0]
            else:
                inicio=""
    if len(linea)>0:
        fin=linea[-1]
    else:
        fin=""
    if fin=="{" or fin=="}":
        while fin=="{" or fin=="}":
            if fin=="{":
                linea=linea[:-1].strip()
                nextTabs=nextTabs+1
                blockSimbol=":"
            elif fin=="}":
                linea=linea[:-1].strip()
                nextTab=nextTab-1
            if len(linea)>0:
                fin=linea[-1]
            else:
                fin=""
    if len(linea)>0:
        g.write(tabSimbol*numTabs+linea+blockSimbol+returnSimbol)
    numTabs=numTabs+nextTabs
    nextTabs=0
    blockSimbol=""
g.close()
f.close()
if args.execute=="true":
    os.system (args.output)