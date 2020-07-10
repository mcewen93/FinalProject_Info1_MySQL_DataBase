
#Daniel Alexander Basto Moreno y David McEwen Arango


import mysql.connector #importar el modulo connector de mysql para conectar python y mysql

#datos de la base de datos:
usuario="informatica1"
servidor="localhost"
contrasena="bio123"
bd="informatica1"

cnx=mysql.connector.connect(user=usuario,host=servidor,password=contrasena,database=bd)#conexión con todos los parámetros tal cual están configurados en mysql (phpmyadmin)

conexion=cnx.cursor()#comando cursor para ejecutar la conexión


while True: #Estructura de control principal para que el programa tenga la opción de repetirse/salir cada vez que el usuario lo desee

    while True: #un while que va junto al Try/except para controlar que el usuario no ingrese in caracter ajeno al numérico. Hay muchos más Try/except en el código
        try:
            #Menú principal para escoger qué tabla de base de datos quiere intervenir
            menu_1=int(input("Señor usuario, escoja la información que desea gestionar:\n\n1. Equipos.\n2. Responsables.\n3. Ubicaciones.\n4. Salir.\n"))
            break
        except ValueError:#Excepcion de error por valor
            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")            

    
    if menu_1==1:#Menu para intervenir la tabla equipos

        while True: #Estructura de control while secundario dentro de un menú principal para que el programa se repita o salga cada vez que se desee
        
            print("Por favor seleccione la opción que desea:\n")
            #menú secundario
            while True:
                try:
                    menu_2=int(input("1. Ver la informacion de un equipo.\n2. Ingresar un nuevo equipo.\n3. Actualizar la información de un equipo.\n4. Ver la información de todos los equipos.\n5. Eliminar equipo.\n6. Volver al menú principal.\n"))
                    break
                except ValueError:
                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                        

            while True:#While para permitir que el usuario escoja si quiere o no realizar una nueva consulta, actualizacion, creacion, eliminacion de informacion
                
                if menu_2==1:#Opcion 1: Ver la informacion de un equipo
                    while True: #un while que va junto al Try/except para controlar que el usuario no ingrese in caracter ajeno al numérico. Hay muchos más Try/except en el código
                        try:
                            numactivo=int(input("Ingrese el número de activo del equipo: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    sql="select*from equipos where numactivo="+str(numactivo) #Con el comando select, se realiza la consulta en la tabla equipos de la base de datos cuando la columna numactivo tenga como valor el ingresado por el usuario
                    conexion.execute(sql) #Ejecuta la consulta, creacion, actualizacion y eliminacion de informacion en la base de datos (esta línea se va a repetir durante todo el código, por tanto, no hace falta explicarlo más)
                    eq=conexion.fetchall() #Guarda todos los registros en una variable. El fetchall retorna una lista de tuplas (esta línea se va a repetir durante todo el código, por tanto, no hace falta explicarlo más)
                    print("\n")
                    for equipos in eq: #Toma todos parámetros y los anexa
                        r=equipos[5]
                        sql2="select*from responsables where codigo="+str(r) #Selecciona en la tabla responsables, en la columna codigo, y lo concatena con r(equipos 5)
                        conexion.execute(sql2)
                        resp=conexion.fetchall()
                        for responsable in resp:
                            nomresp=responsable[1]+" "+responsable[2]
                        u=equipos[4]
                        sql3="select*from ubicacion where codigoubic="+str(u) 
                        conexion.execute(sql3)
                        ub=conexion.fetchall()
                        for ubicacion in ub: #Convierte toda la información tomada de Mysql de forma ordenada
                            ubic=ubicacion[1]
                        ser=equipos[1]
                        nomeq=equipos[2]
                        mar=equipos[3]
                        print("Número de activo: "+str(numactivo))
                        print("Serial: "+ser)
                        print("Nombre de equipo: "+nomeq)
                        print("Marca: "+mar)
                        print("Ubicación: "+ubic)
                        print("Responsable: "+nomresp)
                    print("\n")
                    #A continuacion una estructura try/except, como anteriormente se menciona, para garantizar que el usuario solo ingrese un tipo de dato determidnado,
                    #hay bastantes en el codigo, por eso se dejara de documentar a medida que vayan apareciendo en el codigo
                    while True:
                        try:
                            nuevaconsulta=int(input("Señor usuario, ¿desea realizar otra consulta?:\n1. Si\n2. No\n"))#Menu para que el usuario seleccione si quiere hacer otra consulta, creacion,actualizacion o eliminacion de informacion
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaconsulta==1:
                        continue
                    elif nuevaconsulta==2:
                        break
                    

                elif menu_2==2: #Opcion 2: Ingresar un nuevo equipo
                    print("Por favor ingrese los datos del nuevo equipo:\n") 
                    while True:#Estructura try/except
                        try:
                            numactivo=int(input("Ingrese el número de activo del equipo: ")) #Aquí se va agregar el nuevo equipo, con un Try/Except para que el usuario no se equivoque
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    ser=input("Serial: ")
                    nomeq=input("Nombre: ")
                    mar=input("Marca: ")
                    print("Las siguentes son las ubicaciones disponibles: ")
                    sql_ubic="select codigoubic,nomubic from ubicacion" #Sólo trae codigoubic y nomubic de la tabla ubicación
                    conexion.execute(sql_ubic)
                    u_all=conexion.fetchall()
                    for allubic in u_all:#for para que muestre la informacion de todas las ubicaciones, en caso de que se ingrese una nueva ubicacion, este for la mostrara aca
                        codubic=str(allubic[0])
                        nomubic=allubic[1]
                        print(codubic+". "+nomubic)
                    while True:#Estructura try/except
                        try:
                            ubic=int(input("Escoja una ubicación: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    print("Los siguientes son los responsables actuales: ")
                    sql_resp="select codigo,nombre,apellido from responsables" #Trae codigo,nombre,apellido de la tabla responsables
                    conexion.execute(sql_resp)
                    r_all=conexion.fetchall()
                    for respall in r_all:#for para que muestre la informacion de todos los responsable, en caso de que se ingrese un nuevo responsable, este for lo mostrara aca
                        codresp=str(respall[0])
                        nomresp=respall[1]+" "+respall[2]
                        print(codresp+". "+nomresp)  #Se muestra la información concatenada de las anteriores tablas
                    while True:#Estructura try/excep
                        try:
                            resp=int(input("Escoja un responsable: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    sql="insert into equipos (numactivo,serial,nomequipo,marca,codubicacion,codresp) values (%s,%s,%s,%s,%s,%s)" #Es la forma para añadir información a una base de datos
                    datos_nuevo=(numactivo,ser,nomeq,mar,ubic,resp)
                    #A continuacion: para crear informacion en una tabla de base de datos, hay que ejecutar la conexion con dos argumentos, el primero donde se encuentra la sentencia insert to, y el segundo donde se encuentran las variables a ingresar a la tabla
                    conexion.execute(sql,datos_nuevo)
                    cnx.commit()#El comando commit se usa a modo de confirmar que se realizara algun cambio en la informacion de la base de datos (creacion, actualizacion y eliminacion de informacion
                    print("\n")
                    print("Los datos del número de activo "+str(numactivo)+" han sido añadidos satisfactoriamente")
                    print("\n")
                    while True:#Estructura try/except
                        try:
                            nuevoingreso=int(input("Señor usuario, ¿desea ingresar otro equipo?:\n1. Si\n2. No\n"))#Menu para elegir si se quiere ingresar un nuevo equipo o no
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")                    
                    if nuevoingreso==1:
                        continue
                    elif nuevoingreso==2:
                        break
                    
                    

                elif menu_2==3:#Opcion 3: Actualizar un equipo
                    while True:#Estructura try/except
                        try:
                            numactivo=int(input("Ingrese el número de activo del equipo a actualizar: "))#Se busca en la tabla el numero de activo el cual es unico e irrepetible
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    while True:
                        try:
                            update=int(input("Seleccione el parámetro a actualizar:\n1. Serial\n2. Nombre\n3. Marca\n4. Ubicación\n5. Responsable\n"))#Menu para seleccionar el parametro de busqueda
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if update==1:
                        up="serial"
                        dato_act=input("Por favor ingrese el serial actualizado: ")
                    elif update==2:
                        up="nomequipo"
                        dato_act=input("Por favor ingrese el nombre del equipo actualizado: ")
                    elif update==3:
                        up="marca"
                        dato_act=input("Por favor ingrese la marca del equipo actualizado: ")
                    elif update==4:
                        up="codubicacion"
                        print("Las siguentes son las ubicaciones disponibles: ")
                        sql_ubic="select codigoubic,nomubic from ubicacion"
                        conexion.execute(sql_ubic)
                        u_all=conexion.fetchall()
                        for allubic in u_all:#For para mostrar todas las ubicaciones actualizadas al momento de la consulta
                            codubic=str(allubic[0])
                            nomubic=allubic[1]
                            print(codubic+". "+nomubic)
                        while True:
                            try:
                                dato_act=int(input("Por favor ingrese el código de la ubicación, actualizada: "))
                                break
                            except ValueError:
                                print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    elif update==5:
                        up="codresp"
                        print("Los siguientes son los responsables actuales: ")
                        sql_resp="select codigo,nombre,apellido from responsables"
                        conexion.execute(sql_resp)
                        r_all=conexion.fetchall()
                        for respall in r_all:#for para mostrar todos los responsables actualizados al momento de la consulta
                            codresp=str(respall[0])
                            nomresp=respall[1]+" "+respall[2]
                            print(codresp+". "+nomresp)
                        while True:
                            try:
                                dato_act=int(input("Por favor ingrese el código del responsable, actualizado: "))
                                break
                            except ValueError:
                                print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    #Estructura para actualizar un campo solicitado en el menu de la variable update con el dato de la variable dato_act para la columna numactivo de la tabla cuando tenga el valor de la variable numactivo
                    sql="update equipos set "+up+"= '"+str(dato_act)+"' where numactivo="+str(numactivo)
                    conexion.execute(sql)
                    cnx.commit()
                    print("\n")
                    print("La información del equipo con número de activo "+str(numactivo)+" ha sido actualizada")
                    print("\n")
                    while True:#Nuevamente una estructura try/except
                        try:
                            #Nuevamente un menu  para escoger si se quiere actualizar otro dato u otro numero de activo (equipo) o no
                            nuevaact=int(input("Señor usuario, ¿desea actualizar otro equipo?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaact==1:
                        continue
                    elif nuevaact==2:
                        break

                elif menu_2==4:#Opcion 4: Visualizar todos los equipos
                    sql="select*from equipos" #Selecciona todo lo que está en la base de datos de equipos y lo muestra
                    conexion.execute(sql)
                    todos=conexion.fetchall()
                    print("A continuacion se mostraran todos los equipos.\n")
                    for all_eq in todos:
                        r=all_eq[5]
                        sql2="select*from responsables where codigo="+str(r)
                        conexion.execute(sql2)
                        resp=conexion.fetchall()
                        for responsable in resp:
                            nomresp=responsable[1]+" "+responsable[2]
                        u=all_eq[4]
                        sql3="select*from ubicacion where codigoubic="+str(u)
                        conexion.execute(sql3)
                        ub=conexion.fetchall()
                        for ubicacion in ub:
                            ubic=ubicacion[1]
                        ser=all_eq[1]
                        nomeq=all_eq[2]
                        mar=all_eq[3]
                        codeq=str(all_eq[0])
                        #Mediante la siguiente serie de líneas, organizamos l información de tal forma que sea inteligible
                        print(" | "+codeq+" | "+ser+" | "+nomeq+" | "+mar+" | "+ubic+" | "+nomresp+" | ")
                    print("\n")
                    while True:#Nuevamente una estructura try/except
                        try:
                            #Nuevamente un menu  para escoger si se quiere volver a mostrar todos los equipos o no.
                            nuevaconsulta=int(input("Señor usuario, ¿desea volver a mostrar todos los equipos?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaconsulta==1:
                        continue
                    elif nuevaconsulta==2:
                        break
                                                
                    
                elif menu_2==5:#Opcion 5: Eliminar un equipo
                    while True:
                        try:
                            numactivo=int(input("Ingrese el número de activo del equipo que desea eliminar: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    sql="delete from equipos where numactivo="+str(numactivo) #Es el código para eliminar un campo de la base de datos de MySQL
                    conexion.execute(sql)
                    cnx.commit()
                    print("\n")
                    print("La información del equipo con número de activo "+str(numactivo)+" ha sido eliminada")
                    print("\n")
                    while True:
                        try:
                            nuevaelim=int(input("Señor usuario, ¿desea eliminar otro equipo?:\n1. Si\n2. No\n"))#Menu para elegir si se quiere eliminar otro equipo o no
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaelim==1:
                        continue
                    elif nuevaelim==2:
                        break

                elif menu_2==6:#Opcion 6: Salir
                    break

                else:#En caso de que el usuario ingrese un número que no este en el menu, el programa le va a indicar que es incorrecto y le volverá a mostrar las opciones
                    print("****HA INGRESADO UNA OPCIÓN INVÁLIDA, POR FAVOR SELECCIONE UNA OPCIÓN CORRECTA****")
                    print("\n")
                    break
                

            if menu_2==6:
                break


            else:#En caso de que el usuario ingrese un número que no este en el menu, el programa le va a indicar que es incorrecto y le volverá a mostrar las opciones
                continue

#####################################################################

                
#A partir de aquí, lo visto en el menú 1 (equipos), se repite pero con la tabla responsables, por tanto, consideramos que no hace falta redundar
    
    elif menu_1==2: #Menú para intervenir tabla responsables

        while True:
            
            print("Por favor seleccione la opcion que desea:\n")
            #menu secundario
            while True:
                try:
                    menu_2=int(input("1. Ver la información de un responsable.\n2. Ingresar un nuevo responsable.\n3. Actualizar la información de un responsable.\n4. Ver la información de todos los responsables.\n5. Eliminar responsable.\n6. Volver el menú principal.\n"))
                    break
                except ValueError:
                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")

                    
            while True:
                
                if menu_2==1:
                    
                    while True:
                        while True:
                                try:
                                    busqueda=int(input("Ingrese el parámetro a buscar:\n1. Código de responsable.\n2. Documento del responsable.\n"))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                        if busqueda==1:
                            parametro="codigo"
                            while True:
                                try:
                                    busq=int(input("Por favor ingrese el código del responsable: "))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                            break
                        elif busqueda==2:
                            parametro="id"
                            while True:                                
                                try:
                                    busq=int(input("Por favor ingrese el documento del responsable: "))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                            break
                        else:
                            print("Opción inválida, por favor ingrese la opción correcta")
                            continue
                    sql="select*from responsables where "+parametro+"="+str(busq)
                    conexion.execute(sql)
                    res=conexion.fetchall()
                    print("\n")
                    for responsables in res:
                        cod=str(responsables[0])
                        nom=responsables[1]+" "+responsables[2]
                        doc=str(responsables[3])
                        car=responsables[4]
                        print("La siguiente es la información del responsable:\n")
                        print("Código: "+cod)
                        print("Nombre: "+nom)
                        print("Documento: "+doc)
                        print("Cargo: "+car)
                        print("\n")
                    while True:
                        try:
                            nuevaconsulta=int(input("Señor usuario, ¿desea realizar otra consulta?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaconsulta==1:
                        continue
                    elif nuevaconsulta==2:
                        break


                elif menu_2==2:
                    print("Por favor ingrese los datos del nuevo responsable:\n")
                    while True:
                        try:
                            codigo=int(input("Código: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    nom=input("Nombre(s): ")
                    ape=input("Apellido(s): ")
                    while True:
                        try:
                            doc=int(input("Documento: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    car=input("Cargo: ")
                    sql="insert into responsables (codigo,nombre,apellido,id,cargo) values (%s,%s,%s,%s,%s)"
                    datos_nuevo=(codigo,nom,ape,doc,car)
                    conexion.execute(sql,datos_nuevo)
                    cnx.commit()
                    print("La información del nuevo responsable ha sido añadida con éxito\n")
                    while True:
                        try:
                            nuevoingreso=int(input("Señor usuario, ¿desea ingresar otro responsable?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")                    
                    if nuevoingreso==1:
                        continue
                    elif nuevoingreso==2:
                        break


                elif menu_2==3:
                        
                    while True:
                        act=int(input("Seleccione parámetro de busqueda para actualizar responsable:\n1. Código de responsable.\n2. Documento del responsable.\n"))
                        if act==1:
                            parametro="codigo"
                            par="codigo numero"
                            while True:
                                try:
                                    busq=int(input("Por favor ingrese el código del responsable a actualizar: "))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                            print("Se va a actualizar la informacion del responsable con código "+str(busq))
                            break
                        elif act==2:
                            parametro="id"
                            par="documento numero"
                            while True:
                                try:
                                    busq=int(input("Por favor ingrese el documento del responsable a actualizar: "))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                            print("Se va a actualizar la información del responsable con documento "+str(busq))
                            break
                        else:
                            print("Opción inválida, por favor ingrese la opción correcta")
                            continue
                    update=int(input("Seleccione el parámetro a actualizar:\n1. Nombre\n2. Apellido\n3. Cargo\n"))
                    if update==1:
                        up="nombre"
                        dato_act=input("Por favor ingrese el(los) nombre(s) actualizado(s): ")
                    elif update==2:
                        up="apellido"
                        dato_act=input("Por favor ingrese el(los) apellido(s) actualizado(s): ")
                    elif update==3:
                        up="cargo"
                        dato_act=input("Por favor ingrese el cargo actualizado: ")
                    sql="update responsables set "+up+"= '"+str(dato_act)+"' where "+parametro+"= "+str(busq)
                    conexion.execute(sql)
                    cnx.commit()
                    print("\n")
                    print("La información del responsable con "+par+" "+str(busq)+" ha sido actualizada satisfactoriamente")
                    print("\n")
                    while True:
                        try:
                            nuevaact=int(input("Señor usuario, ¿desea actualizar la informacion de otro responsable?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaact==1:
                        continue
                    elif nuevaact==2:
                        break


                elif menu_2==4:
                    sql="select*from responsables order by codigo asc"
                    conexion.execute(sql)
                    todos=conexion.fetchall()
                    for all_res in todos:
                        codigo=str(all_res[0])
                        nomres=all_res[1]+" "+all_res[2]
                        doc=str(all_res[3])
                        car=all_res[4]                    
                        print(" | "+codigo+" | "+nomres+" | "+doc+" | "+car+" | ")
                    print("\n")
                    while True:
                        try:
                            nuevaconsulta=int(input("Señor usuario, ¿desea volver a mostrar la informacion de todos los responsables?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaconsulta==1:
                        continue
                    elif nuevaconsulta==2:
                        break
                            
                        
                elif menu_2==5:
                    while True:
                        while True:
                            try:
                                elim=int(input("Seleccione parámetro para eliminar responsable:\n1. Código de responsable.\n2. Documento del responsable.\n"))
                                break
                            except ValueError:
                                print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                        if elim==1:
                            parametro="codigo"
                            par="codigo numero"
                            while True:
                                try:
                                    busq=int(input("Por favor ingrese el código del responsable a eliminar: "))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                            break
                        elif elim==2:
                            parametro="id"
                            par="documento numero"
                            while True:
                                try:
                                    busq=int(input("Por favor ingrese el documento del responsable a eliminar: "))
                                    break
                                except ValueError:
                                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                            break
                        else:
                            print("Opción inválida, por favor ingrese la opción correcta")
                            continue
                    sql="delete from responsables where "+parametro+"="+str(busq)
                    conexion.execute(sql)
                    cnx.commit()
                    print("\n")
                    print("La información del responsable con "+par+" "+str(busq)+" ha sido eliminada")
                    print("\n")
                    while True:
                        try:
                            nuevaelim=int(input("Señor usuario, ¿desea eliminar la innformacion de otro responsable?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaelim==1:
                        continue
                    elif nuevaelim==2:
                        break

                elif menu_2==6:
                    break

                else:
                    print("****HA INGRESADO UNA OPCIÓN INVÁLIDA, POR FAVOR SELECCIONE UNA OPCIÓN CORRECTA****")
                    print("\n")
                    break

            if menu_2==6:
                break


            else:#En caso de que el usuario ingrese un número que no este en el menu, el programa le va a indicar que es incorrecto y le volverá a mostrar las opciones
                continue

####################################################################
                
    elif menu_1==3:
        
        while True:
            
            print("Por favor seleccione la opción que desea:\n")
            while True:
                try:
                    menu_2=int(input("1. Ver la información de una ubicación.\n2. Ingresar una nueva ubicación.\n3. Actualizar la información de una ubicación.\n4. Ver la información de todas las ubicaciones.\n5. Eliminar ubicación.\n6. Volver el menú principal.\n"))
                    break
                except ValueError:
                    print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
            
            while True:
                
                if menu_2==1:
                    while True:
                        try:
                            ubic=int(input("Ingrese el código de la ubicación que desea validar: "))
                            break
                        except ValueError:
                            print("sólo se permiten números en este campo\n")                    
                    sql="select*from ubicacion where codigoubic="+str(ubic)
                    conexion.execute(sql)
                    ub=conexion.fetchall()
                    print("\n")
                    for ubicaciones in ub:
                        cod=str(ubicaciones[0])
                        nom=ubicaciones[1]
                        piso=str(ubicaciones[2])
                        tel=str(ubicaciones[3])
                        print("La siguiente es la información de la ubicación:\n")
                        print("Código: "+cod)
                        print("Nombre: "+nom)
                        print("Piso: "+piso)
                        print("Teléfono: "+tel)
                    print("\n")
                    while True:
                        try:
                            nuevaconsulta=int(input("Señor usuario, ¿desea realizar otra consulta?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaconsulta==1:
                        continue
                    elif nuevaconsulta==2:
                        break
                    

                elif menu_2==2:
                    print("Por favor ingrese los datos de la nueva ubicación:\n")
                    while True:
                        try:
                            codigo=int(input("Código: "))
                            break
                        except ValueError:
                            print("sólo se permiten números en este campo\n")
                    nom=input("Nombre ubicación: ")
                    while True:
                        try:
                            piso=int(input("Piso: "))
                            break
                        except ValueError:
                            print("sólo se permiten números en este campo\n")
                    while True:
                        try:
                            tel=int(input("Teléfono: "))
                            break
                        except ValueError:
                            print("sólo se permiten números en este campo\n")
                    sql="insert into ubicacion (codigoubic,nomubic,piso,telefono) values (%s,%s,%s,%s)"
                    datos_nuevo=(codigo,nom,piso,tel)
                    conexion.execute(sql,datos_nuevo)
                    cnx.commit()
                    print("Los datos han sido ingresados satisfactoriamente")
                    print("\n")
                    while True:
                        try:
                            nuevoingreso=int(input("Señor usuario, ¿desea ingresar informacion de otra ubicacion?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")                    
                    if nuevoingreso==1:
                        continue
                    elif nuevoingreso==2:
                        break

                    

                elif menu_2==3:
                    while True:
                        try:
                            ubic=int(input("Ingrese el código de la ubicación que desea actualizar: "))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    while True:
                        try:
                            update=int(input("Seleccione el parámetro a actualizar:\n1. Nombre\n2. Piso\n3. Teléfono\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if update==1:
                        up="nomubic"
                        dato_act=input("Por favor ingrese el nombre actualizado de la ubicación: ")
                    elif update==2:
                        up="piso"
                        while True:
                            try:
                                dato_act=int(input("Por favor ingrese el número de piso actualizado de la ubicación: "))
                                break
                            except ValueError:
                                print("sólo se permiten números en este campo\n")
                    elif update==3:
                        up="telefono"
                        while True:
                            try:
                                dato_act=int(input("Por favor ingrese el teléfono actualizado de la ubicación: "))
                                break
                            except ValueError:
                                print("sólo se permiten números en este campo\n")
                    sql="select nomubic from ubicacion where codigoubic="+str(ubic)
                    conexion.execute(sql)
                    ub=conexion.fetchall()
                    print("\n")
                    for ubicaciones in ub:
                        nombreubic=ubicaciones[0]
                    sql="update ubicacion set "+up+"= '"+str(dato_act)+"' where codigoubic="+str(ubic)
                    conexion.execute(sql)
                    cnx.commit()
                    print("La información de la ubicación con código "+str(ubic)+" ha sido actualizada")
                    print("\n")
                    while True:
                        try:
                            nuevaact=int(input("Señor usuario, ¿desea actualizar la informacion de otra ubicacion?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaact==1:
                        continue
                    elif nuevaact==2:
                        break


                elif menu_2==4:
                    sql="select*from ubicacion order by codigoubic asc"
                    conexion.execute(sql)
                    todos=conexion.fetchall()
                    for all_ubic in todos:
                        codigo=str(all_ubic[0])
                        nomubic=all_ubic[1]
                        piso=str(all_ubic[2])
                        tel=str(all_ubic[3])                    
                        print(" | "+codigo+" | "+nomubic+" | "+piso+" | "+tel+" | ")
                    print("\n")
                    while True:
                        try:
                            nuevaconsulta=int(input("Señor usuario, ¿desea volver a mostrar todas las ubicaciones?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaconsulta==1:
                        continue
                    elif nuevaconsulta==2:
                        break
                        
                    
                elif menu_2==5:
                    while True:
                        try:
                            ubic=int(input("Ingrese el código de la ubicación que desea eliminar: "))
                            break
                        except ValueError:
                            print("sólo se permiten números en este campo\n")
                    sql="select nomubic from ubicacion where codigoubic="+str(ubic)
                    conexion.execute(sql)
                    ub=conexion.fetchall()
                    print("\n")
                    for ubicaciones in ub:
                        nombreubic=ubicaciones[0]
                    sql="delete from ubicacion where codigoubic="+str(ubic)
                    conexion.execute(sql)
                    cnx.commit()
                    print("La información de la ubicación con código "+str(ubic)+"("+nombreubic+") ha sido eliminada")
                    print("\n")
                    while True:
                        try:
                            nuevaelim=int(input("Señor usuario, ¿desea eliminar otra ubicacion?:\n1. Si\n2. No\n"))
                            break
                        except ValueError:
                            print("Sólo se permiten números en este campo, por favor vuelva a intentarlo\n")
                    if nuevaelim==1:
                        continue
                    elif nuevaelim==2:
                        break

                elif menu_2==6:
                    break

                else:
                    print("****HA INGRESADO UNA OPCIÓN INVÁLIDA, POR FAVOR SELECCIONE UNA OPCIÓN CORRECTA****")
                    print("\n")
                    break

            if menu_2==6:
                break


            else:#En caso de que el usuario ingrese un número que no este en el menu, el programa le va a indicar que es incorrecto y le volverá a mostrar las opciones
                continue

            

    elif menu_1==4:
        print("****FIN DEL PROGRAMA*****")
        break

    else:
        print("****HA INGRESADO UNA OPCIÓN INVÁLIDA, POR FAVOR SELECCIONE UNA OPCIÓN CORRECTA****")
        print("\n")
        continue
