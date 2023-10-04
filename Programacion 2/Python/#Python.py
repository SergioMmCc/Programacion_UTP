#Python
#Taller ciclos - While

''' 1)  Implementar un algoritmo que muestre todos
los múltiplos de 7 comprendidos entre 1 y 1000. '''

def multiplos ():
    i=1
    while (i<=1000):
        if (i%7==0):
            print(i)
        i+=1

#----------------------------------------------------

multiplos ()