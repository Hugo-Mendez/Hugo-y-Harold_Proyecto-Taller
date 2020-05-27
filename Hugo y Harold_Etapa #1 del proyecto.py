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
    print("\n Para crear una persona manualmente por favor indica cada uno de los siguientes atributos:")
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

            if comando == 1 :
                print("\nEsta como Administrador")
                Administrador(Personas, Crea_cedulas(2), Crea_provincias(), Crea_accesorios(),
                              Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),
                              Crea_Atributos_Cabello(), Crea_Atributos_Ojos())
            elif comando == 2 :
                print("\nEsta como Analista")
            elif comando == 3 :
                print("\nEsta como Usuario")
        else :
            print("\n*****************")
            print("                *")
            print(" Hasta luego!   *")
            print("                *")
            print("*****************")
            return
login()



