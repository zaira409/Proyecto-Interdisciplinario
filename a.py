import random
import mysql.connector

from mysql.connector import errorcode
cursor = None
cnx = None


def ConectarBase():
    global cnx, cursor

    try:
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="Casino")
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)
ConectarBase()



def juego1():
   
    def dar_carta():
        numeros_posibles=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        palos_posibles=["Corazones", "Diamantes", "Tréboles", "Picas"]
        num=random.choice(numeros_posibles)
        palos=random.choice(palos_posibles)
        cartas=[num, palos]
        return(cartas)


    def generar_mano_y_valor():
        carta1=dar_carta()
        carta2=dar_carta()
        carta3=dar_carta()
        manno=[carta1, carta2, carta3]
        mano=[carta1[0], carta2[0], carta3[0]]
        print(manno)
        if carta1[0]>10:
            carta1[0]=10

        if carta2[0]>10:
            carta2[0]=10

        if carta3[0]>10:
            carta3[0]=10
        mano=[carta1[0], carta2[0], carta3[0]]
        if carta1[1]==carta2[1]  or carta1[1]==carta3[1] or carta2[1]==carta3[1]:
            valor_mano=sum(mano)+15
        elif carta1[1]==carta2[1]==carta3[1]:
            valor_mano=sum(mano)+30
        else:
            valor_mano=sum(mano)
        return(valor_mano)




    def menu_juego():
        puntaje_total=0
        for i in range(0, 3):
            print("1. Dar mano")
            print("2. Salir")
            opcion=int(input("Ingrese una opción: "))
            if opcion==1:
                print("Su mano es: ",generar_mano_y_valor())
                puntaje_ronda=generar_mano_y_valor()
                print("Su puntaje de ronda es: ", puntaje_ronda)
                puntaje_total=puntaje_total+puntaje_ronda
                print("Su puntaje total hasta ahora es: ", puntaje_total)
            elif opcion==2:
                if puntaje_total<100:
                    print("Cerrando programa")
                elif puntaje_total>=100:
                    print("Ganaste tu puntaje total es: ", puntaje_total)
                break


        if puntaje_total<100:
            print("perdiste tu puntaje total es: ", puntaje_total)
        elif puntaje_total>=100:
            print("Ganaste tu puntaje total es: ", puntaje_total)
        return puntaje_total
   
    puntaje_total=menu_juego()
    return puntaje_total





def juego2():
   
    def fila_al():
        num=[0,1,2,3,4]
        fila=random.choice(num)
        return(fila)


    def columna_al():
        num=[0,1,2,3,4]
        columna=random.choice(num)
        return(columna)
    def crear_tablero():
        matriz=[["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"]]
        fila=fila_al()
        columna=columna_al()
        if matriz[fila][columna]!="B":
            matriz[fila][columna]="B"


        fila=fila_al()
        columna=columna_al()
        if matriz[fila][columna]!="B":
            matriz[fila][columna]="B"


        fila=fila_al()
        columna=columna_al()
        if matriz[fila][columna]!="B":
            matriz[fila][columna]="B"


        fila=fila_al()
        columna=columna_al()
        if matriz[fila][columna]!="B":
            matriz[fila][columna]="B"
   
        return(matriz)


    def disparar():
        intentos=7
        matriz1=crear_tablero()
        matriz=[["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"],
                ["-","-","-","-","-"]]
        i=0
        for fila in matriz1:
            for elemento in fila:
                if elemento=="B":
                    i=i+1
        while i>0 and intentos!=0:
            intentos=intentos-1
            print("Te quedan ", intentos, "intentos")
            for fila in matriz:
                print(fila)
            fila=int(input("Ingrese la fila: "))
            columna=int(input("Ingrese la columna: "))
            if matriz1[fila][columna]=="B":
                matriz[fila][columna]="X"
                print("Le pegaste a un barco!!")
                intentos=intentos+3
                i=i-1
            else:
                print("Agua!!!")
                matriz[fila][columna]="~"

        if intentos>0:
            print("Ganaste!!!")
        else:
            print("Perdiste...")
        return i


    i=disparar()
    return i
import random


def juego3(saldo):
    print("~~~~~ RULETA ~~~~~~")
   
    apuesta=0
    o=1
    while saldo>0 and o==1:
        print("Tenes $ ", saldo)
        apuesta=int(input("¿Cuanto queres apostar? Si queres salir pone 0 "))
        if apuesta>saldo:
            print("No tenes tanto saldo")
            break
        elif apuesta==0:
            print("Saliendo")
            o==0
            break


        eleccion=str(input("Elegí 'rojo' o 'negro'")).lower()

        colores = ["rojo", "negro"]

        color_elegido = random.choice(colores)


        print("El color elegido al azar es: ", color_elegido)


        resultado=color_elegido
        if resultado==eleccion:
            saldo=saldo+apuesta
            print("Ganaste!! se te va a sumar", apuesta)
        elif resultado!=eleccion:
            saldo=saldo-apuesta
            print("Perdiste se te va a descontar", apuesta)
    return saldo




# OPCION NUMERO 1 (CLIENTE HABITUAL O EXISTENTE) ------------------------------------

def menujuegos(Id_Jugador, Saldo):
    menu=1
    while menu==1:
        print("Tu saldo es de: ", Saldo)
        if Saldo>=1000:
            print("  MENU ")  
            print("1. Balatro ")
            print("2. Batalla naval ")
            print("3. Ruleta")
           
               
            op=int(input("Ingrese una opcion: "))
            if op==1:
                puntaje_total=juego1()
                if puntaje_total<100:
                    print("Perdiste, se te van a descontar 500 de tu saldo actual")
                    Saldo=Saldo-500
                elif puntaje_total>=100:
                    print("Ganaste se te van a sumar 700 a tu saldo actual")
                    Saldo=Saldo+700
            elif op==2:
                i=juego2()
                if i!=0:
                    print("Perdiste, se te van a descontar 250 de tu saldo actual")
                    Saldo=Saldo-250
                elif i==0:
                    print("Ganaste, se te van a sumar 1000 a tu saldo actual")
                    Saldo=Saldo+1000
            elif op==3:
                Saldo=juego3(Saldo)
           
            else:
                print("Saliste del menu.")
            print("Queres continuar jugando?")
            menu=int(input("1.SI, 2.NO" ))
        else:
            print("Te quedaste sin saldo, no podes jugar mas")
            menu=0
    sql = "UPDATE jugadores SET saldo = %s   WHERE id_jugador = %s;"
    cursor.execute(sql,(Saldo, Id_Jugador))
    cnx.commit()



def Consulta_Saldo(Id_Jugador):
    consulta="select Saldo from jugadores where id_jugador= %s"
    cursor.execute(consulta, (Id_Jugador,))
    resultado = cursor.fetchone()
    if resultado:
            # Si el resultado es {'Saldo': 1500}, esto devuelve 1500
            return resultado['Saldo']
    else:
            # Jugador no encontrado
        return None



# ----------------------------- MENU PRINCIPAL ----------------------------------
def menu1():
 
    print("")
    print("                         MENU PRINCIPAL ")
    print("")
    print("1. Cliente, 2. Empleado del casino, 3. Cliente nuevo ")
    opc=int(input("Elija con que tipo de usuario desea ingresar: "))
    if opc==1:
        Id_Jugador=int(input("Ingrese su ID"))
        Saldo=Consulta_Saldo(Id_Jugador)
        menujuegos(Id_Jugador, Saldo)
    elif opc==2:
        menu_EmpleadoCasino()
    elif opc==3:
        menu_ClienteNuevo()



#  OPCION NUMERO 2 (EMPLEADO DEL CASINO) ----------------------------------

def crear_consulta(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()


consulta1 = crear_consulta ("select j.nombre, g.nombre_juego from apuestas a inner join jugadores j on j.id_jugador = a.id_jugador inner join juegos g on g.id_juego = a.id_juego;")
consulta2 = crear_consulta ("select j.nombre, j.apellido, m.nivel from jugadores j inner join membresias m on m.id_jugador = j.id_jugador;")
consulta3 = crear_consulta ("select j.nombre, j.apellido, a.monto from apuestas a inner join jugadores j on j.id_jugador = a.id_jugador where a.monto > 100;")
consulta4 = crear_consulta ("select m.id_mesa, g.nombre_juego, c.nombre as crupier from mesas m inner join juegos g on g.id_juego = m.id_juego inner join crupieres c on c.id_crupier = g.id_crupier;")
consulta5 = crear_consulta ("select  j.id_jugador, j.nombre, j.apellido, t.id_transaccion, t.monto, t.fecha_hora from transacciones t inner join jugadores j on j.id_jugador = t.id_jugador where t.tipo = 'retiro';")
consulta6 = crear_consulta ("select  c.nombre, c.apellido, p.puesto from crupieres c inner join puestos p on p.id_puesto = c.id_puesto;")
consulta7 = crear_consulta ("select j.id_jugador, j.nombre, j.apellido, sum(p.monto_ganado) as total_ganado from jugadores j inner join apuestas a on a.id_jugador = j.id_jugador inner join premios p on p.id_apuesta = a.id_apuesta inner join juegos g on g.id_juego = a.id_juego where g.nombre_juego = 'Ruleta' group by j.id_jugador, j.nombre, j.apellido order by total_ganado desc limit 1;")
consulta8 = crear_consulta ("select g.id_juego, g.nombre_juego, count(a.id_apuesta) as cantidad_apuestas, avg(a.monto) as promedio_monto from juegos g inner join apuestas a on a.id_juego = g.id_juego group by g.id_juego, g.nombre_juego order by promedio_monto desc;")
tablaprevisional = crear_consulta("select * from jugadores;")


def menu_EmpleadoCasino():
    menu3=0
    while menu3==0:
        print("              MENU    ")  
        print("")
        print("1.Nombre del jugador y el nombre del juego en cada apuesta ")
        print("2. Jugador y su nivel de membresía ")
        print("3.Jugadores con apuestas superiores a 100 ")
        print("4. Listado de mesas con su juego y crupier ")
        print("5. Jugadores que retiraron plata ")
        print("6. Crupieres y los puestos en los que trabajan")
        print("7. Jugador que mas plata gano en el juego ")
        print("8. Total de apuestas y promedio de plata por juego  ")
        print("9. Salir")
       
        o=int(input("Ingrese una opcion: "))
        if o==1:
            print(consulta1)
        elif o==2:
            print(consulta2)
        elif o==3:
            print(consulta3)
        elif o==4:
            print(consulta4)
        elif o==5:
            print(consulta5)
        elif o==6:
            print(consulta6)
        elif o==7:
            print(consulta7)
        elif o==8:
            print(consulta8)
        elif o==9:
            return
            menu3 = 0


def Consulta(nombre,apellido,dni,fecha_nacimiento,saldo):
    sql = "INSERT INTO Jugadores (nombre, apellido, dni, fecha_nacimiento, saldo)VALUES( %s, %s, %s, %s,%s)"
    cursor.execute(sql,(nombre,apellido,dni,fecha_nacimiento,saldo))
    cnx.commit()
    return cursor.lastrowid


def Consulta2(id_jugador,nivel,fecha_inicio,fecha_vencimiento):
    sql = "INSERT INTO Membresias (id_jugador,nivel,fecha_inicio,fecha_vencimiento)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql,(id_jugador,nivel, fecha_inicio, fecha_vencimiento))
    cnx.commit()
    return cursor.lastrowid


def Consulta3(id_jugador, tipo, monto, fecha_hora):
    sql = "INSERT INTO Transacciones (id_jugador, tipo, monto, fecha_hora)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql,(id_jugador, tipo, monto, fecha_hora))
    cnx.commit()
    return cursor.lastrowid


#  OPCION NUMERO 3 (MENU CLIENTE NUEVO) ------------------
def menu_ClienteNuevo():
    print("Nuevo jugador")
    #nombre, apellido, dni, fecha_nacimiento, saldo
    nombre=str(input("Ingrese su nombre: "))
    apellido= str(input("Ingrese su apellido: "))
    dni=int(input("Ingrese su DNI sin espacios ni puntos: "))
    fecha_nacimiento=str(input("Ingrese su fecha de nacimiento: "))
    saldo=input("Su saldo actual es 0 (cero) ")
    Id=Consulta(nombre,apellido, dni, fecha_nacimiento, saldo)
    #id_jugador,nivel,fecha_inicio,fecha_vencimiento
    print("Tu id es: ", Id)
    nivel=str(input("Ingrese su nivel 'bronce' 'oro' 'plata': "))
    fecha_inicio=str(input("Ingrese la fecha en la que inicio: "))
    fecha_vencimiento=str(input("Ingrese la fecha de vencimiento: "))
    #id_jugador, tipo, monto, fecha_hora
    id_jugador=Id
    Consulta2(id_jugador,nivel,fecha_inicio,fecha_vencimiento)
    tipo=str(input("Ingrese si su carga es de recarga o retiro: "))
    monto=int(input("Ingrese el monto que quiera recargar/retirar: "))
   
    def retiro_o_recarga(saldo, id_jugador):
        if tipo=="retiro":
            saldo=saldo - monto
            sql = "UPDATE jugadores SET saldo = %s   WHERE id_jugador = %s;"
            cursor.execute(sql,(saldo, id_jugador))
            cnx.commit()
        elif tipo=="recarga":
            saldo=saldo + monto
            sql = "UPDATE jugadores SET saldo = %s   WHERE id_jugador = %s;"
            cursor.execute(sql,(saldo, id_jugador))
            cnx.commit()
        else:
            print("Ingreso una opcion no valida")
    retiro_o_recarga(saldo, id_jugador)
    fecha_hora=str(input("Ingrese la hora y fecha: "))

menu1()


       
