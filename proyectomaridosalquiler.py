clientes = []       #CREACION DE 3 LISTAS QUE SE UTILIZARAN EN EL PROGRAMA
empleados = []
serviciosBrindados = []


def agregar_Empleado ():     # Se crea una funcion para agregar empleados que basicamente crea un diccionario , con la informacionque ingresa el ususario.
 empleado = {}               # Posteriormente se verifica que el usuario no haya sido previamente ingresado y se almacena en la lista.
 empleado['nombre'] = input("Nombre del Empleado a Insertar: ")
 empleado['especialidad'] = input("Especialidad del Empleado: ")                                                                                                          
 empleado['sexo']= int (input ("selccione  1. Masculino /  2. Femenino   "))
 empleado['cedula']= input ("ingrese la cedula del empleado:  ")
 if empleado['sexo']==1:
        empleado['sexo']=("Masculino")
 else:
        empleado['sexo']=("Femenino")
 find = False
 for a in empleados:
    if a['nombre'] == empleado['nombre']:
     find = True
    break
                    
 if find:
                    print("Empleado ya se registro anteriormente")

 else:
                    
                    indice = 0
                    for a in empleados:
                        if a['nombre'] > empleado['nombre']:
                            break
                        indice += 1
                        
                    
                    empleados.insert(indice, empleado)
                    print("Empleado Añadido de forma exitosa")


def eliminar_Empleado():# se crea una funcion par eliminar el empleado mediante su cedula.
 ver_Empleado()
 cedulaempleado = input("Ingrese la cedula del empleado a eliminar: ")
 buscador = False
 for a in empleados:
                    if a['cedula'] == cedulaempleado:
                        buscador = True
                        empleados.remove(a)
                        print("Empleado Eliminado Satisfactoriamente.")
                        break
 if not buscador:
                    print("Empleado no se encuentra en la base de datos.")



def ver_Empleado():#funcion para ver los empleados que se han ingresado con la funcion len sobre la lista empleados se corrobora que haya registros porteriormente se manda a imprimir 
     if len(empleados) == 0:#con un ciclo for los campos guardados en la lista.
                    print("No se encuentran registrado ningun empleado")
     else:
                    for a in empleados:
                        print(f"Nombre: {a['nombre']}")
                        print(f"Especialidad: {a['especialidad']}")
                        print(f"Sexo: {a['sexo']}")
                        print(f"cedula: {a['cedula']}")
                        print()
def ingresar_Cliente():# funcion para ingresar clientes , se crea un diccionario que captura lo que ingresa el cliente y posterior se guarda en una lista.
     cliente = {}
     cliente['nombre'] = input("Nombre del cliente: ")
     cliente['cedula'] = input("Cedula del cliente: ")
     cliente['telefono'] = input("Telefono del cliente: ")
     cliente['direccion'] = input ("Digite la direccion del cliente:  ")
     print("Cliente agregado correctamente.")       
                
     index = 0
     for a in clientes:
                    if a['cedula'] > cliente['cedula']:
                        break
                    index += 1
     clientes.insert(index, cliente)


def modificar_Cliente(): # SE CREA UNA FUNCION PARA MODIFICAR LOS VALORES DEL CLIENTE TOMANDO COMO REFERENCIA LA CEDULA , NO SE PERMITE MODIFICAR LA CEDULA SOLO LOS OTROS DATOS.
     ver_Cliente ()
     cedula = input("Digite la cedula del Cliente a Modificar : ")
     search = False
     for a in clientes:
                    if a['cedula'] == cedula:
                        search = True
                        a['telefono'] = input("Digite el nuevo telefono : ")
                        a['nombre'] = input("Ingrese el nuevo Nombre ")
                        a['direccion'] = input("Ingrese la nueva direccion  ")
                        print("Datos del cliente modificados satisfactoriamente.")
                        break
     if not search:
                    print("Cliente no REGISTRADO.")


def ver_Cliente ():      # SE CREA UNA FUNCION PARA VER LOS CLIENTES QUE ESTAN ALMACENADOS EN LA LISTA RESPECTIVA.
      
      if len(clientes) == 0:
                    print("No hay clientes Registrados")
      else:
                    for a in clientes:
                        print(f"Nombre Cliente: {a['nombre']}")
                        print(f"Cedula Cliente: {a['cedula']}")
                        print(f"Telefono Cliente: {a['telefono']}")
                        print(f"Direccion Cliente: {a['direccion']}")
                        print()
def f_Servicio (): # FUNCION PARA ASIGNAR UN TRABAJO
        print("Empleados disponibles:")
        for i, e in enumerate(empleados):
                    print(f"{i+1}. {e['nombre']} - {e['especialidad']}")
                
                
        empleado = None
        while not empleado:
                    opcion_empleado = input("DIGITE EL NUMERO ASOCIADO AL EMPLEADO")
                    if opcion_empleado.isdigit() and int(opcion_empleado) in range(1, len(empleados)+1):
                        empleado = empleados[int(opcion_empleado)-1]
                    else:
                        print("Opción INCORRECTA.")

        ver_Cliente()       
        servicio = {}
        servicio['cliente'] = input("Ingrese el nombre del cliente: ")
        servicio['servicio'] = input("Ingrese el servicio: ")
        servicio['empleado'] = empleado['nombre']
        serviciosBrindados.append(servicio)
        print("Servicio agregado correctamente.")


def f_serviciosbrindados(): #FUNCION PARA VER TRABAJOS ASIGNADOS
      if len(serviciosBrindados) == 0:
                    print("No hay servicios brindados.")
      else:
                    for a in serviciosBrindados:
                        print(f"Cliente: {a['cliente']}")
                        print(f"Servicio: {a['servicio']}")
                        print(f"Empleado: {a['empleado']}")
                        


def f_empleadosdisponibles(): #FUNCION PARA VER LOS EMPLEADOS QUE ESTAN DISPONIBLES.
       if len(empleados) == 0:
                    print("No hay empleados.")
       else:
                    disponibles = []
                    for a in empleados:
                        encontrado = False
                        for b in serviciosBrindados:
                            if b['empleado'] == a['nombre']:
                                encontrado = True
                                break
                        if not encontrado:
                            disponibles.append(a)
                    
                    if len(disponibles) == 0:
                        print("No hay empleados disponibles.")
                    else:
                        print("Empleados disponibles:")
                        for j, a in enumerate(disponibles):
                            print(f"{j+1}. {a['nombre']} - {a['especialidad']}")                        
while True:
    print("**** MARIDOS DE ALQUILER SA*****")
    print("--------Gestion de Ingresos--------")
    print("              1. EMPLEADOS")
    print("              2. CLIENTES")
    print("              3. TRABAJOS")
    print("              4. EXIT")
    
    opcion = input("     Ingrese UNA OPCION VALIDA: ")


    
    if opcion == "1":
        while True:
            print("******GESTION DE EMPLEADOS******  ")
            print("1. INGRESAR EMPLEADO  ")
            print("2. BORRAR EMPLEADO")
            print("3. VER EMPLEADOS")
            print("4. SALIR")

            opcion_sub = input("Ingrese UNA OPCION VALIDA: ")

            if opcion_sub == "1":
                
                agregar_Empleado()
            
            elif opcion_sub == "2":
                eliminar_Empleado()
            
            elif opcion_sub == "3":
                ver_Empleado()
            elif opcion_sub == "4":
                break 
            else:
                print("OPCION INCORRECTA")
    
    elif opcion == "2":
        while True:
            print("******GESTION DE CLIENTES*****")
            print("1. INGRESAR CLIENTES")
            print("2. MODIFICAR CLIENTES")
            print("3. VER CLIENTES")
            print("4. SALIR")

            opcion_sub = input("Ingrese UNA OPCION VALIDA: ")
            
            if opcion_sub == "1":
                ingresar_Cliente ()
            
            elif opcion_sub == "2":
                modificar_Cliente()
            
            elif opcion_sub == "3":
                ver_Cliente()

            elif opcion_sub == "4":
                break 
            else:
                print("Opción incorrecta favor ingrese una opcion valida")
    
    elif opcion == "3":
        while True:
            print("1. OFERTA DE SERVICIOS")
            print("2. SERVICIOS CONTRATADOS")
            print("3. EMPLEADOS EN LISTA DE ESPERA")
            print("4. Atras")

            opcion_sub = input("Ingrese UNA OPCION VALIDA: ")

            if opcion_sub == "1":
              f_Servicio()    # SE LLAMA A LA FUNCION DE SERVICIOS.
            
            elif opcion_sub == "2":
                f_serviciosbrindados() #SE LLAMA A LA FUNCION PARA VER LOS SERVICIOS QUE SE ASIGNAN.
            
            elif opcion_sub == "3":
                f_empleadosdisponibles() #SE LLAMA A LA FUNCION PARA VER LOS EMPLEADOS DISPONIBLES .
            elif opcion_sub == "4":
                break 
            else:
                print("OPCION INCORRECTA")

    elif opcion == "4":
        break  

    else:
        print("OPCION INCORRECTA")