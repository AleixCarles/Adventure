import psycopg2
import self as self

from config import config
from colorama import Back, Fore, Style

def menuPrincipal():
    print("1.Localitzacions")
    print("2.Camins")
    print("3.Objectes")
    print("4.Personalitzar protagonista.")
    print("5.Veure protagonista.")
    print("6.Sortir.")
    opcio = int(input("Opció:"))
    if opcio == 1:
        menuLocalitzacion()
    elif opcio == 2:
        menuCamins()
    elif opcio == 3:
        menuObjectes()
    elif opcio == 4:
        personalizarProta()
    elif opcio == 5:
        mostrarProta()
    elif opcio == 6:
        False


def menuLocalitzacion():
    while True:
        print("CRUD LOCALITZACIONS")
        print("1.Mostrar una localització\n"
              "2.Crear una localització.\n"
              "3.Modificar una localització.\n"
              "4.Eliminar una localització.\n"
              "5.Llistar totes les localitzacions.\n"
              "6.Tornar al menu principal.\n"
              "7.Sortir.\n")
        resultatmenu = int(input("Opció:"))
        if int(resultatmenu) == 1:
            mostrarLocalitzacio()
        elif int(resultatmenu) == 2:
            crearLocalitzacio()
        elif int(resultatmenu) == 3:
            modificarLocalitzacio()
        elif int(resultatmenu) == 4:
            eliminarLocalitzacio()
        elif int(resultatmenu) == 5:
            llistarLocalitzacio()
        elif int(resultatmenu) == 6:
            menuPrincipal()
        elif int(resultatmenu) == 7:

            break

def menuCamins():
    while True:
        print("CRUD LOCALITZACIONS")
        print("1.Mostrar un camí.\n"
              "2.Crear un camí.\n"
              "3.Modificar un camí.\n"
              "4.Eliminar un camí.\n"
              "5.Llistar totes els camins.\n"
              "6.Tornar al menu principal.\n"
              "7.Sortir.\n")
        resultatmenu = int(input("Opció:"))
        if int(resultatmenu) == 1:
            mostrarCamins()
        elif int(resultatmenu) == 2:
            crearCamins()
        elif int(resultatmenu) == 3:
            modificarCamins()
        elif int(resultatmenu) == 4:
            eliminarCamins()
        elif int(resultatmenu) == 5:
            llistarCamins()
        elif int(resultatmenu) == 6:
            menuPrincipal()
        elif int(resultatmenu) == 7:

            break

def menuObjectes():
    while True:
        print("CRUD OBJECTES")
        print("1.Mostrar objectes\n"
              "2.Crear objectes.\n"
              "3.Modificar objectes.\n"
              "4.Eliminar objectes.\n"
              "5.Llistar tots els objectes.\n"
              "6.Tornar al menu principal.\n"
              "7.Sortir.\n")
        resultatmenu = int(input("Opció:"))
        if int(resultatmenu) == 1:
            mostrarObjectes()
        elif int(resultatmenu) == 2:
            crearObjectes()
        elif int(resultatmenu) == 3:
            modificarObjectes()
        elif int(resultatmenu) == 4:
            eliminarObjecte()
        elif int(resultatmenu) == 5:
            llistarObjecte()
        elif int(resultatmenu) == 6:
            menuPrincipal()
        elif int(resultatmenu) == 7:

            break



def mostrarLocalitzacio():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        print("Indica la id de la localitzacio:")
        ficarid = input()
        cursor.execute("SELECT * FROM localitzacions WHERE id = " + ficarid)
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def mostrarCamins():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        print("Indica la id del camí:")
        ficarid = input()
        cursor.execute("SELECT * FROM camins WHERE idorigen = " + ficarid)
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def mostrarObjectes():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        print("Indica la id de l'objecte:")
        ficarid = input()
        cursor.execute("SELECT * FROM objectes WHERE id = " + ficarid)
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def crearLocalitzacio():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        idlocalitzacio = input("ID de la localització que vols crear:")
        nomlocalitzacio = input("Nom de la localització que vols crear:")
        descripciolocalitzacio = input("Descripció de la localització que vols crear:")
        cursor.execute(
            "INSERT INTO localitzacions(id,nom,descripcio) VALUES (" + idlocalitzacio + ",'" + nomlocalitzacio + "','" + descripciolocalitzacio + "');")
        conn.commit()
        print(Fore.GREEN+"\nLocalitacio creada.\n"+Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def crearCamins():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        idOrigen = input("ID del origien del cami que vols crear:")
        idDesti = input("ID del desti del cami que vols crear:")
        nomOrigen = input("Nom de l'origen del camí:")
        nomDesti = input("Nom del desti del camí:")
        cursor.execute(
            "INSERT INTO camins(idorigen,iddesti,nomorigen,nomdesti) VALUES (" + idOrigen + ",'" + idDesti + "','" + nomOrigen + "','" + nomDesti + "');")
        conn.commit()
        print(Fore.GREEN+"\nCamí creat.\n"+Style.RESET_ALL)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def crearObjectes():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        idobjecte = input(" ID del nou objecte: ")
        pesobjecte = input("Pes de l'objecte que vols crear:")
        nomobjecte = input("Nom de l'objecte que vols crear:")
        descripciobjecte = input("Descripció de l'objecte que vols crear:")
        idlocalitzacio = input("ID de la localització d'on es trova:")
        consulta = ("insert into objectes(id, objecte, idLocalitzacio) VALUES  ('" + idobjecte + "',('" + pesobjecte  + "','" + nomobjecte + "','" + descripciobjecte + "'),'" + idlocalitzacio + "');")


        cursor.execute(consulta)
        conn.commit()
        print(Fore.GREEN+"\nObjecte creat.\n"+Style.RESET_ALL)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def  modificarCamins():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        idOrigen = input("ID de l'origen del camí que vols modificar:")
        idDesti = input("ID destí per a modificar-ho:")
        nomOrigen = input("Nom de l'origen del camí:")
        nomDesti = input("Nom del desti del camí:")
        cursor.execute("UPDATE camins SET iddesti='"+idDesti+"', nomorigen='"+nomOrigen +"', nomdesti='"+nomDesti +"' WHERE idorigen=" + idOrigen + ";")

        conn.commit()
        print(Fore.GREEN+"\nCamí modificat.\n"+Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def modificarLocalitzacio():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        ficarIdMod = input("Indica la id de la localitzacio que vols modificar:")
        nomLocalitzacioMod = input("Nom de la localització que vols modificar:")
        descripcioLocalitzacioMod = input("Descripció de la localització que vols modificar:")
        cursor.execute(
            "UPDATE localitzacions SET nom='" + nomLocalitzacioMod + "', descripcio='" + descripcioLocalitzacioMod + "' WHERE id=" + ficarIdMod + ";")

        conn.commit()
        print(Fore.GREEN + "\nLocalitacio modificada.\n" + Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def modificarObjectes():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        idobjecte = input(" ID de l'objecte que vols modificar: ")
        pesobjecte = input("Pes de l'objecte que vols modificar:")
        nomobjecte = input("Nom de l'objecte que vols modificar:")
        descripciobjecte = input("Descripció de l'objecte que vols modificar:")
        idlocalitzacio = input("ID de la localització d'on es trova:")

        cursor.execute("UPDATE objectes SET objecte= ('" + pesobjecte + "','" + nomobjecte + "','" + descripciobjecte + "'), idLocalitzacio='" + idlocalitzacio + "' WHERE id=" + idobjecte + ";")

        conn.commit()
        print(Fore.GREEN + "\nObjecte modificat.\n" + Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def eliminarLocalitzacio():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        print("Indica la id de la localitzacio que vols esborrar:")
        esborrarid = input()
        cursor.execute("DELETE FROM localitzacions WHERE id=" + esborrarid + ";")
        conn.commit()
        print(Fore.GREEN+"\nLocalitacio esborrada.\n"+Style.RESET_ALL)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def eliminarCamins():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        print("Indica la id del cami que vols esborrar:")
        esborrarid = input()
        cursor.execute("DELETE FROM camins WHERE id=" + esborrarid + ";")
        conn.commit()
        print(Fore.GREEN+"\nCamí esborrat.\n"+Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def eliminarObjecte():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        print("Indica la id de l'objecte que vols esborrar:")
        esborrarid = input()
        cursor.execute("DELETE FROM objectes WHERE id=" + esborrarid + ";")
        conn.commit()
        print(Fore.GREEN+"\nObjecte esborrat.\n"+Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def llistarLocalitzacio():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM localitzacions;")
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def llistarCamins():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM camins;")
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def llistarObjecte():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM objectes;")
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def personalizarProta():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        nomProta = input("Nom del protagonista:")
        descripcioProta = input("Descripció del protagonista:")
        sexeProta = input("Sexe podem escollir entre: masculi, femeni, altres:")
        edatProta = input("Edat de el/la protagonista es de 18 a 99:")
        alturaProta = input("Altura del protagonista en cm:")
        pesProta = input("Pes del protagonista:")
        forcaProta = input("Força del personatge: (de 1 a 20) ")
        destresaProta = input("Destresa del personatge: (de 1 a 20) ")
        resistenciaProta = input("Resistència del personatge: (de 1 a 20) ")
        int_res = int(resistenciaProta)
        salutprota = (int_res*2)
        salutprota2 = str(salutprota)
        cursor.execute(
            "UPDATE protagonista SET nom='" + nomProta + "', descripcio='" + descripcioProta + "', sexe='"+sexeProta+"', edat='"+edatProta+"', altura='"+alturaProta+"', pes='"+pesProta+"', forca='"+forcaProta+"', destresa='"+destresaProta+"', resistencia='"+resistenciaProta+"', salut='"+salutprota2+"';")


        conn.commit()
        print(Fore.GREEN + "\nProtagonista personalitzat.\n" + Style.RESET_ALL)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def mostrarProta():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM protagonista;")
        row = cursor.fetchone()
        while row is not None:
            print(Fore.BLUE + str(row) + Style.RESET_ALL + "\n")
            row = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

menuPrincipal()

class objecte:
    def __int__(self,pes,nom,descripcio,idLocalitzacio):
        self.pes = pes
        self.nom = nom
        self.descripcio = descripcio
        self.idLocalitzacio = idLocalitzacio