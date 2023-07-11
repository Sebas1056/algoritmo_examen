import os
import numpy as np
def llenarMatriz(dept,deptusados):

    p=1
    for i in range (10):
        for j in range(4):
            dept[i,j]=p
            deptusados[i,j]=p
            p+=1
def ValidaOp():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp 
def validaDept():
    depto=0
    while(True):
        try:
            depto=input(" Ingrese lacolumna: A, B, C, D")
            if(depto=="A" or depto=="B" or depto=="C" or depto=="D"):
                break
            else:
                print("Error debe ingresar una columna que corresponda")
        except ValueError:
            print("Debe ser un caracter entre A y D")
    return depto 
def ed(dept,deptusados):
    for i in range(10):
        for j in range(4):
            if(dept==deptusados[i,j]):
                return True
    return False
def comprarDepto(dept,depto,ed,depusados,ruts):
    if(ed=="Tipo A = 3.800"):
        pago=3800
    if(ed=="Tipo B = 3.000"):
        pago=3000
    if(ed=="Tipo C = 2.800"):
        pago=2800
    if(ed=="Tipo D = 3.500"):
        pago=3500
    for i in range(10):
        for j in range(4):
            if(depto==dept[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Rut debe tener 8 digitos minimo "))
                            if(rut<9999999):
                                print("Error, debe tener 8 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(ruts)>0): 
                        rt=0
                        for r in range(len(ruts)):
                            if(rut==ruts[r]):
                                rt=1
                        if(rt==1):
                            print("El rut ya existe y no se puede agregar el pasajero")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break






