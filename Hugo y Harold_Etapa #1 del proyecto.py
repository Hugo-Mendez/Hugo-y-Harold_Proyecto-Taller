import random
from datetime import date


def Crea_cedulas(cantidad):
    cedulas = random.sample(list(range(200000000,209999999)), cantidad)
    return cedulas
 
def Crea_provincias():
    provincias = ["San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
    return provincias

def Crea_accesorios():
    accesorios = ["Lentes", "Aretes", "Piercing", "Ninguno"]
    return accesorios

def Crea_genero():
    genero = ["Masculino", "Femenino"]
    return  genero

def Crea_color_piel():
    colorpiel = ["Negra", "Marrón", "Morena", "Clara", "Blanca"]
    return colorpiel

def Crea_rostro():
    rostro = ["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]
    return rostro

def Crea_emociones():
    emociones = ["Enfado", "Desprecio", "Disgusto", "Miedo", "Sorpresa", "Alegría", "Neutral", "Tristeza"]
    return emociones

def Crea_Atributos_Cabello():
    Atr_cabello = [{1:"Negro", 2:"Rubio", 3:"Café", 4:"Castaño", 5:"Gris", 6:"Invisible"},{1:"Escaso", 2:"Moderado", 3:"Abundante"}, {1:"Lacio", 2:"Ondulado", 3:"Rizado"}]
    return Atr_cabello

def Crea_Atributos_Ojos():
    Atr_ojos = [{1: "Negro", 2: "Castaño", 3: "Ámbar", 4: "Abellana", 5: "Verde", 6: "Azul", 7: "Gris"},
                {1: "Almendrados", 2: "Separados", 3: "Redondos", 4: "Caídos", 5: "Saltones", 6: "Juntos", 7: "Profundos", 8: "Asiáticos"}]         
    return Atr_ojos

def Crea_Fecha_Nac():
    Fecha_Nacimiento = {1: random.randint(1,30), 2: random.randint(1,12), 3: random.randint(1920,2019)}
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
    for i in cedulas:
        Fecha_na = Crea_Fecha_Nac()
        Edad_Años = Calcula_Edad(Fecha_na)
        dic_persona = {1: i, 2: random.choice(provincias), 3: random.choice(accesorios),
                       4: random.choice(genero), 5: random.choice(colores_de_piel),
                       6: random.choice(rostro), 7: random.choice(emociones),
                       8: atri_cabello[0][random.randint(1,6)], 9: atri_cabello[1][random.randint(1,3)],
                       10: atri_cabello[2][random.randint(1,3)], 11: atri_ojos[0][random.randint(1,7)], 
                       12: atri_ojos[1][random.randint(1,8)], 13: Edad_Años}
        Lista_Personas.append(dic_persona)
    return Lista_Personas


def Crear_Persona_Auto(Personas,nueva_cedula,cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    while nueva_cedula[0] in cedulas:
        nueva_cedula = Crea_cedulas(1)
    Fecha_na = Crea_Fecha_Nac()
    Edad_Años = Calcula_Edad(Fecha_na)
    dic_persona = {1: nueva_cedula, 2: random.choice(provincias), 3: random.choice(accesorios),
                    4: random.choice(genero), 5: random.choice(colores_de_piel),
                    6: random.choice(rostro), 7: random.choice(emociones),
                    8: atri_cabello[0][random.randint(1,6)], 9: atri_cabello[1][random.randint(1,3)],
                    10: atri_cabello[2][random.randint(1,3)], 11: atri_ojos[0][random.randint(1,7)], 
                    12: atri_ojos[1][random.randint(1,8)], 13: Edad_Años}
    Personas.append(dic_persona)
    return

def Crear_Persona_Manual(Personas,nueva_cedula,cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    while nueva_cedula[0] in cedulas:
        nueva_cedula = Crea_cedulas(1)
    print("\nPara crear una persona manualmente por favor indica cada uno de los siguientes atributos:")

    print("\nIngrese su fecha de nacimiento, en formato dd(1-30)/mm(1-12)/aaaa(1920-2019)")
    dia = 0
    mes = 0
    año = 0
    while dia not in range(1, 31) and mes not in range(1,13) and año not in range(1920, 2020):
        dia = int(input("\Ingrese el día de nacimiento: "))
        mes = int(input("\Ingrese el mes de nacimiento: "))
        año = int(input("\Ingrese el año de nacimiento: "))
        if dia not in range(1, 31) and mes not in range(1,13) and año not in range(1920, 2020):
            print("\nDía, mes o año fuera del rango establecido")
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

    genero = 0
    while genero not in range(1,3):
        print("\n****************************************")
        print("*                                      *") 
        print("*           Género                     *")   
        print("* Digite:  1     para femenino         *")
        print("* Digite:  2     para masculino        *")
        print("*                                      *")  
        print("****************************************\n")
        genero = int(input("Digite un número correspondiente con el menú: "))
        if genero not in range(1,3):
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
    dic_persona = {1: nueva_cedula, 2: provincia, 3: accesorio,
                    4: genero, 5: Color_piel, 6: F_rostro, 7: emocion,
                    8: color_cabello, 9: densidad_cabello, 10: textura_cabello, 
                    11: Forma_ojos, 12: Color_ojos, 13: Edad_Años}
    Personas.append(dic_persona)
    return


def Administrador(Personas,cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    comando = 0
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
            Crear_Persona_Auto(Personas,Crea_cedulas(1),cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos)
        elif comando == 2:
            Crear_Persona_Manual(Personas,Crea_cedulas(1),cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos)
    return

def validar_contraseña(contraseña,comando,Personas) :
    contraseña_Admin = "admi123"
    contraseña_Analista = "ana456"
    contraseña_Usuario = "usu789"
    if comando == 1 :        
        while contraseña != contraseña_Admin :
            contraseña = input("Contraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Administrador")
        Administrador(Personas, Crea_cedulas(2), Crea_provincias(), Crea_accesorios(),
                      Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),
                      Crea_Atributos_Cabello(), Crea_Atributos_Ojos())

    elif comando == 2 :
        while contraseña != contraseña_Analista :
            contraseña = input("Contraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Analista")

    else :
        while contraseña != contraseña_Usuario :
            contraseña = input("Contraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Usuario")
    return

def login():
    comando = 0
    while comando < 4 :
        print("\n*******************************************************")
        print("*                                                     *")
        print("* Digite:  1     para ingresar como Administrador     *")
        print("* Digite:  2     para ingresar como Analista          *")
        print("* Digite:  3     para ingresar como Usuario           *")
        print("* Digite: #>3:   para salir                           *")
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