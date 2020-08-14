from separasilabas import *
import sys

print ('Argument List:', str(sys.argv))
palabra = str(sys.argv[1])
silabas = silabizer()
print(silabas(palabra))