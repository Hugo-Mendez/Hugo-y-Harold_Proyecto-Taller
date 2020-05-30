import random
from datetime import date


def Crea_cedulas(cantidad):
    Cedulas = {}
    for i in range(1,cantidad+1):
        cedula = random.sample(range(200000000,209999999), cantidad)
        Cedulas[i] = cedula[i-1]
    return Cedulas
 
def Crea_provincias():
    provincias = {1: "San José  ", 2: "Alajuela  ", 3: "Cartago   ", 4: "Heredia   ", 5: "Puntarenas", 6: "Guanacaste", 7: "Limón     "}
    return provincias

def Crea_accesorios():
    accesorios = {1: "Lentes  ", 2: "Aretes  ", 3: "Piercing", 4: "Ninguno "}
    return accesorios

def Crea_genero():
    genero = {1: "Femenino ", 2: "Masculino"}
    return  genero

def Crea_color_piel():
    colorpiel = {1: "Negra ", 2: "Marrón", 3: "Morena", 4: "Clara ", 5: "Blanca"}
    return colorpiel

def Crea_rostro():
    rostro = {1: "Redondo    ", 2: "Alargado   ", 3: "Corazón    ", 4: "Cuadrado   ", 5: "Ovalado    ", 6: "Rectangular"}
    return rostro

def Crea_emociones():
    emociones = {1: "Enfado   ", 2: "Desprecio", 3: "Disgusto ", 4: "Miedo    ", 5: "Sorpresa ", 6: "Alegría  ", 7: "Neutral  ", 8: "Tristeza "}
    return emociones

def Crea_Atributos_Cabello():
    Atr_cabello = {1: {1:"Negro    ", 2:"Rubio    ", 3:"Café     ", 4:"Castaño  ", 5:"Gris     ", 6:"Invisible"},
                   2: {1:"Escaso   ", 2:"Moderado ", 3:"Abundante"}, 3: {1:"Lacio   ", 2:"Ondulado", 3:"Rizado  "}}
    return Atr_cabello

def Crea_Atributos_Ojos():
    Atr_ojos = {1: {1: "Almendrados", 2: "Separados  ", 3: "Redondos   ", 4: "Caídos     ", 5: "Saltones   ", 6: "Juntos     ", 7: "Profundos  ", 8: "Asiáticos  "},
                2: {1: "Negro   ", 2: "Castaño ", 3: "Ámbar   ", 4: "Avellana", 5: "Verde   ", 6: "Azul    ", 7: "Gris    "}}       
    return Atr_ojos

def Crea_Fecha_Nac():
    Fecha_Nacimiento = {1: random.randint(1,30), 2: random.randint(1,12), 3: random.randint(1920,2018)}
    return Fecha_Nacimiento

def Calcula_Edad(Fecha_na):
    fecha_a = date.today()
    Fecha_Actual = {1: fecha_a.day, 2: fecha_a.month, 3: fecha_a.year}
    Años = Fecha_Actual[3] - Fecha_na[3]
    if Fecha_na[2] > Fecha_Actual[2] :
        Años = Años - 1 
        Meses = 12 - (Fecha_na[2] - Fecha_Actual[2])
    else :    
        Meses = Fecha_Actual[2] - Fecha_na[2]
    if Fecha_na[1] > Fecha_Actual[1] :
        Meses = Meses - 1
        Dias = 30 - (Fecha_na[1]-Fecha_Actual[1])
    else :
        Dias = Fecha_Actual[1] - Fecha_na[1]    
    return Años

def Crea_Personas(cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    Lista_Personas = []
    for i in range(1,len(cedulas)+1):
        Fecha_na = Crea_Fecha_Nac()
        Edad_Años = Calcula_Edad(Fecha_na)
        dic_persona = {1: cedulas[random.randint(1,len(cedulas))], 2: provincias[random.randint(1,len(provincias))], 3: accesorios[random.randint(1,len(accesorios))],
                       4: genero[random.randint(1,len(genero))], 5: colores_de_piel[random.randint(1,len(colores_de_piel))],
                       6: rostro[random.randint(1,len(rostro))], 7: emociones[random.randint(1,len(emociones))],
                       8: atri_cabello[1][random.randint(1,6)], 9: atri_cabello[2][random.randint(1,3)],
                       10: atri_cabello[3][random.randint(1,3)], 11: atri_ojos[1][random.randint(1,8)], 
                       12: atri_ojos[2][random.randint(1,7)], 13: Edad_Años}
        Lista_Personas.append(dic_persona)
    return Lista_Personas

def Crear_Persona_Auto(Personas,nueva_cedula,cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    while nueva_cedula[1] in cedulas:
        nueva_cedula = Crea_cedulas(1)
    Fecha_na = Crea_Fecha_Nac()
    Edad_Años = Calcula_Edad(Fecha_na)
    dic_persona = {1: nueva_cedula[1], 2: provincias[random.randint(1,len(provincias))], 3: accesorios[random.randint(1,len(accesorios))],
                   4: genero[random.randint(1,len(genero))], 5: colores_de_piel[random.randint(1,len(colores_de_piel))],
                   6: rostro[random.randint(1,len(rostro))], 7: emociones[random.randint(1,len(emociones))],
                   8: atri_cabello[1][random.randint(1,6)], 9: atri_cabello[2][random.randint(1,3)],
                   10: atri_cabello[3][random.randint(1,3)], 11: atri_ojos[1][random.randint(1,8)], 
                   12: atri_ojos[2][random.randint(1,7)], 13: Edad_Años}
    Personas.append(dic_persona)
    print("\nPersona creada y agregada a la lista satisfactoriamente")
    return Personas

def Crear_Persona_Manual(Personas,nueva_cedula,cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    while nueva_cedula[1] in cedulas:
        nueva_cedula = Crea_cedulas(1)
    print("\nPara crear una persona manualmente por favor indica cada uno de los siguientes atributos:")

    print("\nIngrese su fecha de nacimiento, en formato dd(1-30)/mm(1-12)/aaaa(1920-2019)")
    dia = 0
    mes = 0
    año = 0
    while dia not in range(1, 31) or mes not in range(1,13) or año not in range(1920, 2020):
        dia = int(input("\nIngrese el día de nacimiento: "))
        mes = int(input("\nIngrese el mes de nacimiento: "))
        año = int(input("\nIngrese el año de nacimiento: "))
        if dia not in range(1, 31) or mes not in range(1,13) or año not in range(1920, 2020):
            print("\nError: día, mes o año fuera del rango establecido")
    fecha_naci = {1: dia, 2: mes, 3: año}

    F_rostro = 0
    while F_rostro not in range(1,7):
        print("\n****************************************")
        print("*                                      *") 
        print("*       Forma del rostro               *")   
        print("* Digite:  1     para redondo          *")
        print("* Digite:  2     para alargado         *")
        print("* Digite:  3     para corazón          *")
        print("* Digite:  4     para cuadrado         *")
        print("* Digite:  5     para ovalado          *")
        print("* Digite:  6     para rectangular      *") 
        print("*                                      *")  
        print("****************************************\n")
        F_rostro = int(input("Digite un número correspondiente con el menú: "))
        if F_rostro not in range(1,7):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.") 
    
    Color_piel = 0
    while Color_piel not in range(1,6):
        print("\n****************************************")
        print("*                                      *") 
        print("*        Color de piel                 *")   
        print("* Digite:  1     para negra            *")
        print("* Digite:  2     para marrón           *")
        print("* Digite:  3     para morena           *")
        print("* Digite:  4     para clara            *")
        print("* Digite:  5     para blanca           *")
        print("*                                      *")  
        print("****************************************\n")
        Color_piel = int(input("Digite un número correspondiente con el menú: "))
        if Color_piel not in range(1,6):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    emocion = 0
    while emocion not in range(1,9):
        print("\n****************************************")
        print("*                                      *") 
        print("*           Emoción                    *")   
        print("* Digite:  1     para enfado           *")
        print("* Digite:  2     para desprecio        *")
        print("* Digite:  3     para disgusto         *")
        print("* Digite:  4     para miedo            *")
        print("* Digite:  5     para sorpresa         *")
        print("* Digite:  6     para alegría          *")
        print("* Digite:  7     para neutral          *") 
        print("* Digite:  8     para tristeza         *")
        print("*                                      *")  
        print("****************************************\n")
        emocion = int(input("Digite un número correspondiente con el menú: "))
        if emocion not in range(1,9):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    Genero = 0
    while Genero not in range(1,3):
        print("\n****************************************")
        print("*                                      *") 
        print("*           Género                     *")   
        print("* Digite:  1     para femenino         *")
        print("* Digite:  2     para masculino        *")
        print("*                                      *")  
        print("****************************************\n")
        Genero = int(input("Digite un número correspondiente con el menú: "))
        if Genero not in range(1,3):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    accesorio = 0
    while accesorio not in range(1,5):
        print("\n****************************************")
        print("*                                      *") 
        print("*          Accesorio                   *")   
        print("* Digite:  1     para lentes           *")
        print("* Digite:  2     para aretes           *")
        print("* Digite:  3     para piercing         *")
        print("* Digite:  4     para ninguno          *")
        print("*                                      *")  
        print("****************************************\n")
        accesorio = int(input("Digite un número correspondiente con el menú: "))
        if accesorio not in range(1,5):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    color_cabello = 0
    while color_cabello not in range(1,7):
        print("\n****************************************")
        print("*                                      *") 
        print("*      Color del cabello               *")   
        print("* Digite:  1     para negro            *")
        print("* Digite:  2     para rubio            *")
        print("* Digite:  3     para café             *")
        print("* Digite:  4     para castaño          *")
        print("* Digite:  5     para gris             *")
        print("* Digite:  6     para invisible        *")
        print("*                                      *")  
        print("****************************************\n")
        color_cabello = int(input("Digite un número correspondiente con el menú: "))
        if color_cabello not in range(1,7):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    densidad_cabello = 0
    while densidad_cabello not in range(1,4):
        print("\n****************************************")
        print("*                                      *") 
        print("*      Densidad del cabello            *")   
        print("* Digite:  1     para escaso           *")
        print("* Digite:  2     para moderado         *")
        print("* Digite:  3     para abundante        *")
        print("*                                      *")  
        print("****************************************\n")
        densidad_cabello = int(input("Digite un número correspondiente con el menú: "))
        if densidad_cabello not in range(1,4):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    textura_cabello = 0
    while textura_cabello not in range(1,4):
        print("\n****************************************")
        print("*                                      *") 
        print("*      Textura del cabello             *")   
        print("* Digite:  1     para lacio            *")
        print("* Digite:  2     para ondulado         *")
        print("* Digite:  3     para rizado           *")
        print("*                                      *")  
        print("****************************************\n")
        textura_cabello = int(input("Digite un número correspondiente con el menú: "))
        if textura_cabello not in range(1,4):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    Forma_ojos = 0
    while Forma_ojos not in range(1,9):
        print("\n****************************************")
        print("*                                      *") 
        print("*      Forma de los ojos               *")   
        print("* Digite:  1     para almendrados      *")
        print("* Digite:  2     para separados        *")
        print("* Digite:  3     para redondos         *")
        print("* Digite:  4     para caídos           *")
        print("* Digite:  5     para saltones         *")
        print("* Digite:  6     para juntos           *")
        print("* Digite:  7     para profundos        *")
        print("* Digite:  8     para asiáticos        *") 
        print("*                                      *")  
        print("****************************************\n")
        Forma_ojos = int(input("Digite un número correspondiente con el menú: "))
        if Forma_ojos not in range(1,9):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.") 

    Color_ojos = 0
    while Color_ojos not in range(1,8):
        print("\n****************************************")
        print("*                                      *") 
        print("*       Color de los ojos              *")   
        print("* Digite:  1     para negro            *")
        print("* Digite:  2     para castaño          *")
        print("* Digite:  3     para ámbar            *")
        print("* Digite:  4     para abellana         *")
        print("* Digite:  5     para verde            *")
        print("* Digite:  6     para azul             *")
        print("* Digite:  7     para gris             *") 
        print("*                                      *")  
        print("****************************************\n")
        Color_ojos = int(input("Digite un número correspondiente con el menú: "))
        if Color_ojos not in range(1,8):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")

    provincia = 0
    while provincia not in range(1,8):
        print("\n****************************************")
        print("*                                      *") 
        print("*          Provincias                  *")   
        print("* Digite:  1     para San José         *")
        print("* Digite:  2     para Alajuela         *")
        print("* Digite:  3     para Cartago          *")
        print("* Digite:  4     para Heredia          *")
        print("* Digite:  5     para Puntarenas       *")
        print("* Digite:  6     para Guanacaste       *")
        print("* Digite:  7     para Limón            *") 
        print("*                                      *")  
        print("****************************************\n")
        provincia = int(input("Digite un número correspondiente con el menú: "))
        if provincia not in range(1,8):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.") 
    
    Edad_Años = Calcula_Edad(fecha_naci)
    dic_persona = {1: nueva_cedula[1], 2: provincias[provincia], 3: accesorios[accesorio],
                   4: genero[Genero], 5: colores_de_piel[Color_piel],
                   6: rostro[F_rostro], 7: emociones[emocion],
                   8: atri_cabello[1][color_cabello], 9: atri_cabello[2][densidad_cabello],
                   10: atri_cabello[3][textura_cabello], 11: atri_ojos[1][Forma_ojos], 
                   12: atri_ojos[2][Color_ojos], 13: Edad_Años}
    Personas.append(dic_persona)
    return Personas

def Administrador(comando,Personas,cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    while comando < 3:
        print("\n*********************************************************")
        print("*                                                       *") 
        print("* Digite:  1     para crear persona automáticamente     *")   
        print("* Digite:  2     para crear persona manualmente         *")
        print("* Digite: #>2    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:
            Personas = Crear_Persona_Auto(Personas,Crea_cedulas(1),cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos)
        elif comando == 2:
            Personas = Crear_Persona_Manual(Personas,Crea_cedulas(1),cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos)
    return Personas

def Informes(Personas):
    print(Personas)
    return

def Analista(Personas):
    comando = 0
    while comando < 2:
        print("\n*********************************************************")
        print("*                                                       *") 
        print("* Digite:  1     para ver informes                      *")   
        print("* Digite: #>1    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:
            Informes(Personas)
    return

def Impresion_Datos_Usuario(usuario,mensaje):
    print("\n ________________________________________________________________________________ ")
    print("|                                                                                |")
    print("|                         ",mensaje,"                   |")
    print("|________________________________________________________________________________|")
    print("| Cédula        | Edad   | Provincia      | Género         | Grupo Etario        |")
    if usuario[13] < 4:
        print("|", usuario[1],"    |",str(usuario[13])+" ","    |",usuario[2],"    |", usuario[4],"     | Bebe                |")
    elif usuario[13] < 12:
        if usuario[13] < 10:
            print("|", usuario[1],"    |",str(usuario[13])+" ","    |",usuario[2],"    |", usuario[4],"     | Bebe                |")
        else:
            print("|", usuario[1],"    |",usuario[13],"    |",usuario[2],"    |", usuario[4],"     | Niño                |")
    elif usuario[13] < 18:
        print("|", usuario[1],"    |",usuario[13],"    |",usuario[2],"    |", usuario[4],"     | Adolescente         |")
    elif usuario[13] < 60:
        print("|", usuario[1],"    |",usuario[13],"    |",usuario[2],"    |", usuario[4],"     | Adulto              |")
    else:
        print("|", usuario[1],"    |",usuario[13],"    |",usuario[2],"    |", usuario[4],"     | Adulto mayor        |")
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
    print("|________________________________________________________________________________|")
    print("| Color de piel   | Forma del rostro   | Forma ojos  | Color ojos   | Emoción    |")
    print("|", usuario[5],"         |",usuario[6],"       |",usuario[11],"|",usuario[12],"    |", usuario[7]," |")
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|________________________________________________________________________________|")
    print("| Color cabello     | Densidad cabello    | Textura cabello    | Accesorio       |")
    print("|", usuario[8], "        |", usuario[9], "          |", usuario[10], "          |", usuario[3],"       |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    return

def Modificar_emocion(usuario,emociones):
    emocion = 0
    while emocion not in range(1,9):
        print("\n****************************************")
        print("*                                      *") 
        print("*           Emoción                    *")   
        print("* Digite:  1     para enfado           *")
        print("* Digite:  2     para desprecio        *")
        print("* Digite:  3     para disgusto         *")
        print("* Digite:  4     para miedo            *")
        print("* Digite:  5     para sorpresa         *")
        print("* Digite:  6     para alegría          *")
        print("* Digite:  7     para neutral          *") 
        print("* Digite:  8     para tristeza         *")
        print("*                                      *")  
        print("****************************************\n")
        emocion = int(input("Digite un número correspondiente con el menú: "))
        if emocion not in range(1,9):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")
    usuario[7] = emociones[emocion]
    Impresion_Datos_Usuario(usuario,"Ahora esta es su nueva información")
    return 

def Modificar_provincia(usuario, provincias):
    provincia = 0
    while provincia not in range(1,8):
        print("\n****************************************")
        print("*                                      *")
        print("*          Provincias                  *")   
        print("* Digite:  1     para San José         *")
        print("* Digite:  2     para Alajuela         *")
        print("* Digite:  3     para Cartago          *")
        print("* Digite:  4     para Heredia          *")
        print("* Digite:  5     para Puntarenas       *")
        print("* Digite:  6     para Guanacaste       *")
        print("* Digite:  7     para Limón            *") 
        print("*                                      *")
        print("****************************************\n")
        provincia = int(input("Digite un número correspondiente con el menú: "))
        if provincia not in range(1,8):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.")
    usuario[2] = provincias[provincia]
    Impresion_Datos_Usuario(usuario,"Ahora esta es su nueva información")
    return

def Usuario(Personas,emociones,provincias):
    usuario = random.choice(Personas)
    comando = 0
    Impresion_Datos_Usuario(usuario,"Esta es su información actual     ")
    while comando < 3:
        print("\n**************************************************************************")
        print("*                                                                        *") 
        print("*        Los atributos que se pueden modificar son los siguientes        *")
        print("*                                                                        *")
        print("* Digite:  1     para modificar emoción                                  *")   
        print("* Digite:  2     para modificar provincia                                *")
        print("* Digite: #>2    para regresar                                           *")  
        print("*                                                                        *")
        print("**************************************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:
            Modificar_emocion(usuario,emociones)
        elif comando == 2:
            Modificar_provincia(usuario,provincias)
    return Personas

def validar_contraseña(contraseña,comando,Personas) :
    if comando == 1 :        
        while contraseña != "admi123" :
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Administrador")
        Administrador(0,Personas, Crea_cedulas(2), Crea_provincias(), Crea_accesorios(),
                      Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),
                      Crea_Atributos_Cabello(), Crea_Atributos_Ojos())
                      
    elif comando == 2 :
        while contraseña != "ana456" :
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Analista")
        Analista(Personas)

    else :
        while contraseña != "usu789" :
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Usuario")
        Usuario(Personas,  Crea_emociones(), Crea_provincias())
    return

def login():
    comando = 0
    while comando < 4 :
        print("\n*******************************************************")
        print("*                                                     *")
        print("* Digite:  1     para ingresar como Administrador     *")
        print("* Digite:  2     para ingresar como Analista          *")
        print("* Digite:  3     para ingresar como Usuario           *")
        print("* Digite: #>3    para salir                           *")
        print("*                                                     *")
        print("*******************************************************\n")
        comando=int(input("Digite un número correspondiente con el menú: "))
        if comando < 4 :
            Personas = Crea_Personas(Crea_cedulas(2), Crea_provincias(), Crea_accesorios(),
                                      Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),
                                      Crea_Atributos_Cabello(), Crea_Atributos_Ojos())
            contraseña = input("\nDigite su contraseña: ")
            validar_contraseña(contraseña,comando,Personas)
        else :
            print("\n******************")
            print("*                *")
            print("* Hasta luego!   *")
            print("*                *")
            print("******************")
            return
login()