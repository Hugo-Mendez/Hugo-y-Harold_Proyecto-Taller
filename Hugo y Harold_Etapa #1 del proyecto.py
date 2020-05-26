import random
import time


def Crea_cedulas():
    cedulas = random.sample(list(range(200000000,209999999)), 800)
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

def Crea_Personas(cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    Lista_Personas = []
    for i in cedulas:
        Fecha_na = Crea_Fecha_Nac()
        dic_persona = {1: i, 2: random.choice(provincias), 3: random.choice(accesorios),
                       4: random.choice(genero), 5: random.choice(colores_de_piel),
                       6: random.choice(rostro), 7: random.choice(emociones),
                       8: atri_cabello[0][random.randint(1,6)], 9: atri_cabello[1][random.randint(1,3)],
                       10: atri_cabello[2][random.randint(1,3)], 11: atri_ojos[0][random.randint(1,7)], 
                       12: atri_ojos[1][random.randint(1,8)]}
        Lista_Personas.append(dic_persona)
    print(Lista_Personas)
    return Lista_Personas

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

            Personas = Crea_Personas(Crea_cedulas(), Crea_provincias(), Crea_accesorios(),
                                      Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),
                                      Crea_Atributos_Cabello(), Crea_Atributos_Ojos())

            if comando == 1 :
                print("\nEsta como Administrador")
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



