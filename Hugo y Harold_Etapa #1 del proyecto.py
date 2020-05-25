import random

def Creacedulas():
    cedulas = random.sample(list(range(200000000,209999999)), 800)
    return cedulas
 
def Creaprovincias():
    provincias = ["San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
    return Creaprovincias

def Crea_accesorios():
    accesorios = ["Lentes", "Aretes", "Piercing", "Ninguno"]
    return Crea_accesorios

def Crea_genero():
    genero = ["Masculino", "Femenino"]
    return  Crea_genero

def Crea_color_piel():
    colorpiel = ["Negra", "Marrón", "Morena", "Clara", "Blanca"]
    return Crea_color_piel

def Crea_rostro():
    rostro = ["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]
    return Crea_rostro

def Crea_emociones():
    emociones = ["Enfado", "Desprecio", "Disgusto", "Miedo", "Sorpresa", "Alegría", "Neutral", "Tristeza"]
    return Crea_emociones

def Crea_Atributos_Cabello():
    color = ["Negro", "Rubio", "Café", "Castaño", "Gris", "Invisible"]
    densidad = ["Escaso", "Moderado", "Abundante"]
    textura = ["Lacio", "Ondulado", "Rizado"]
    A_cabello = {"c": color, "d": densidad, "t": textura}
    return A_cabello

def Crea_atributos_ojos():
    color = ["Negro", "Castaño", "Ámbar", "Abellana", "Verde", "Azul", "Gris"]
    forma = ["Almendrados", "Separados", "Redondos", "Caídos", "Saltones", "Juntos", "Profundos", "Asiáticos"]
    A_ojos = {"c": color, "f": forma}
    return A_ojos


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
            Creacedulas()
            if comando == 1 :
                print("\nEsta en usuario Administrador")
            elif comando == 2 :
                print("\nEsta en usuario Analista")
            elif comando == 3 :
                print("\nEsta en usuario Usuario")
        else :
            print("\n*****************")
            print("                *")
            print(" Hasta luego!   *")
            print("                *")
            print("*****************")
login()



