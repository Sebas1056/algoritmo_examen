import os 
import numpy as np
import SebaFunciones as sf
dept=np.empty([10,4],type(object)) 
deptusados=np.empty([10,4],type(object)) # arreglo para guardar los departamentos que ya se compraron
ruts=[] # arreglo para guardar los ruts de las personas
sf.llenarMatriz(dept,deptusados)
op=0
depto=0

while(op!=5):
    os.system("cls")
    print('**************"Casa Feliz"****************')
    print("1. --->  Comprar Departamento             ")
    print("2. --->  Mostrar departamentos disponibles")
    print("3. --->  Ver listado de compradores       ")
    print("4. --->  Mostrar ganancias totales        ")
    print("5. --->  Salir                            ")
    op=sf.ValidaOp()

    if (op==1):
        depto=sf.validarDept()
        sf.mostrarDisponibles(dept)
        ed_opcupado=sf.validaEdOpcupado()
        ed=sf.disponible(dept,ed_opcupado)
        if (ed): #si cc es verdadero o si el asiento está disponioble
            print("Pisos disponibles")
            pagar=(sf.comprarDepto(dept),ed_opcupado, deptusados,ruts)
            print("\t Usted deberá cancelar un total de: $", pagar)
            os.system("pause")

    if (op==2):
        sf.MostrarDisponibles(dept)
        os.system("pause")

    if (op==5):
        print("Fin del programa (Sebastian Delgado, 11/07/2023)")
        break



