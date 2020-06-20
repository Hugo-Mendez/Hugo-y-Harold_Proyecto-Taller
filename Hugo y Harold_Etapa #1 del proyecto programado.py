
#Authors: Hugo Méndez and Harold Ramírez
#Date: June 14th 2020
import copy
import random
from datetime import date

class Provincia:
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre 

class Genero:
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre

class Color_de_piel:
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre

class Forma_rostro:
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre 

class Emocion:
    def __Init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre

class Color_cabello:
    def __Init__(self):
        self.Color = ""
        return
    def set_Color(self, color):
        self.Color = color
        return
    def get_Color(self):
        return self.Color 

class Densidad_cabello:
    def __Init__(self):
        self.Densidad = ""
        return
    def set_Densidad(self, densidad):
        self.Densidad = densidad
        return
    def get_Densidad(self):
        return self.Densidad 

class Textura_cabello:
    def __Init__(self):
        self.Textura = ""
        return
    def set_Textura(self, textura):
        self.Textura = textura
        return
    def get_Textura(self):
        return self.Textura 

class Cabello:
    def __Init__(self):
        self.Atributos_cabello = {}
        self.Color = Color_cabello()
        self.Densidad = Densidad_cabello()
        self.Textura = Textura_cabello()
        return
    def set_Atributos_cabello(self, objetos):
        self.Atributos_cabello = objetos 
        return
    def set_Color(self):
        self.Color = self.Atributos_cabello[1].get_Color()
        return
    def set_Densidad(self):
        self.Densidad = self.Atributos_cabello[2].get_Densidad()
        return
    def set_Textura(self):
        self.Textura = self.Atributos_cabello[3].get_Textura()
        return
    def get_Atributos_cabello(self):
        return self.Atributos_cabello
    def get_Color(self):
        return self.Color
    def get_Densidad(self):
        return self.Densidad
    def get_Textura(self):
        return self.Textura

class Color_ojos:
    def ___init__(self):
        self.Color = ""
        return
    def set_Color(self, color):
        self.Color = color
        return
    def get_Color(self):
        return self.Color

class Forma_ojos:
    def ___init__(self):
        self.Forma = ""
        return
    def set_Forma(self, forma):
        self.Forma = forma
        return
    def get_Forma(self):
        return self.Forma 

class Ojos:
    def __init__(self):
        self.Atributos_ojos = {}
        self.Forma = Forma_ojos()
        self.Color = Color_ojos()
        return
    def set_Atributos_ojos(self, objetos):
        self.Atributos_ojos = objetos
        return
    def set_Forma(self):
        self.Forma = self.Atributos_ojos[1].get_Forma()
        return
    def set_Color(self):
        self.Color = self.Atributos_ojos[2].get_Color()
        return
    def get_Forma(self):
        return self.Forma 
    def get_Color(self):
        return self.Color

class Accesorios:
    def ___init__(self):
        self.Nombre = ""
        return
    def set_Accesorio(self, nombre):
        self.Nombre = nombre
        return
    def get_Accesorio(self):
        return self.Nombre

class Ropa:
    def ___init__(self):
        self.Nombre = ""
        return
    def set_Ropa(self, nombre):
        self.Nombre = nombre
        return
    def get_Ropa(self):
        return self.Nombre

class Calzado:
    def ___init__(self):
        self.Nombre = ""
        return
    def set_Calzado(self, nombre):
        self.Nombre = nombre
        return
    def get_Calzado(self):
        return self.Nombre

class Vestuario:
    def __init__(self):
        self.Ropa = []
        self.Calzado = Calzado()
        self.Accesorios = [] 
        return
    def set_Ropa(self, lista_Rop):
        self.Ropa = lista_Rop
        return
    def set_Calzado(self, calzado):
        self.Calzado = calzado.get_Calzado()
        return
    def set_Accesorios(self, lista_Acc):
        self.Accesorios = lista_Acc
        return
    def get_Ropa(self):
        return self.Ropa
    def get_Calzado(self):
        return self.Calzado
    def get_Accesorios(self):
        return self.Accesorios

class Persona:
    def __Init__(self):
        self.Cedula = 0
        self.Edad = 0
        self.Vestuario = Vestuario()
        self.Ojos = Ojos()
        self.Cabello = Cabello()
        self.Color_piel = Color_de_piel()
        self.Genero = Genero()
        self.Forma_rostro = Forma_rostro()
        self.Emocion = Emocion()
        self.Provincia = Provincia()
        return
    def set_Cedula(self, cedula):
        self.Cedula = cedula
        return
    def set_Edad(self, edad):
        self.Edad = edad
        return
    def set_Vestuario(self, vestuario):
        self.Vestuario = vestuario
        return
    def set_Ojos(self, ojos):
        self.Ojos = ojos
        return
    def set_Cabello(self, cabello):
        self.Cabello = cabello
        return
    def set_Color_piel(self, color_piel):
        self.Color_piel = color_piel
        return
    def set_Genero(self, genero):
        self.Genero = genero
        return
    def set_Forma_rostro(self, forma_rostro):
        self.Forma_rostro = forma_rostro
        return
    def set_Emocion(self, emocion):
        self.Emocion = emocion
        return
    def set_Provincia(self, provincia):
        self.Provincia = provincia 
        return
    def get_Cedula(self):
        return self.Cedula
    def get_Edad(self):
        return self.Edad 
    def get_Vestuario(self, identificador):
        if identificador == 1:
            return self.Vestuario.get_Accesorios()
        elif identificador == 2:
            return self.Vestuario.get_Calzado()
        else:
            return self.Vestuario.get_Ropa()
    def get_Ojos(self, identificador):
        if identificador == 1:
            return self.Ojos.get_Forma()
        else:
            return self.Ojos.get_Color()
    def get_Cabello(self, identificador):
        if identificador == 1:
            return self.Cabello.get_Color()
        elif identificador == 2:
            return self.Cabello.get_Densidad()
        else:
            return self.Cabello.get_Textura()
    def get_Color_piel(self):
        return self.Color_piel.get_Nombre()
    def get_Genero(self):
        return self.Genero.get_Nombre()
    def get_Forma_rostro(self):
        return self.Forma_rostro.get_Nombre()
    def get_Emocion(self):
        return self.Emocion.get_Nombre()
    def get_Provincia(self):
        return self.Provincia.get_Nombre()

def Crea_cedulas(cantidad):
    """    Function that creates a dictionary, then, through a "for" loop: creates a list of ID cards and adds them to the dictionary.
    After, returns the dictionary.
    
    Keyword arguments:
    cantidad -- Number that indicates the quantity of ID cards, that will be generated.
    """
    Cedulas = {}
    cedula = random.sample(range(200000000,209999999), cantidad)#Depending on "cantidad" (the given number), the ID cards are randomly created
    for i in range(0, len(cedula)):    #The list of ID cards is toured
        Cedulas[i+1] = cedula[i]       #It is added each ID card to the dictionary
    return Cedulas

def Crea_provincias():
    """Function that creates a dictionary which stores the provinces of Costa Rica, then returns the dictionary."""
    provincias = {1: "San José  ", 2: "Alajuela  ", 3: "Cartago   ", 4: "Heredia   ", 5: "Puntarenas", 6: "Guanacaste", 7: "Limón     "}
    Obj_provincia = provincias.copy()
    for j in range(1, len(provincias)+1):
        Obj_provincia[j] = Provincia()
        Obj_provincia[j].set_Nombre(provincias[j])  
    return Obj_provincia

def Crea_vestuario():
    """Function that creates a dictionary which stores the accessories, then returns the dictionary."""
    vestuarios = {1: {1: "Lentes  ", 2: "Aretes  ", 3: "Piercing", 4: "Collar", 5: "Anillo", 6: "Reloj ", 
                  7: "Brazalete", 8: "Diadema", 9: "Vincha", 10: "Monóculo"}, 
                  2: {1: "Camiseta", 2: "Camisa", 3: "Blusa ", 4: "Pantalón", 5: "Falda ", 6: "Abrigo", 7: "Vestido",
                  8: "Calcetines", 9: "Pantaloneta", 10: "Shorts", 11: "Saco  ", 12: "Corbata", 13: "Sombrero",
                  14: "Bufanda" }, 3: {1: "Oxford", 2: "Sandalias", 3: "Tenis ", 4: "Mocasines", 5: "Botas ",
                  6: "Botines", 7: "Brogue", 8: "Monk  ", 9: "Derby ", 10: "Tacones"}}
    Obj_vestuarios = copy.deepcopy(vestuarios)
    for i in range(1, len(vestuarios)+1):
        for e in range(1, len(vestuarios[i])+1):
            if i == 1:
                Obj_vestuarios[i][e] = Accesorios()
                Obj_vestuarios[i][e].set_Accesorio(vestuarios[i][e])
            elif i == 2:
                Obj_vestuarios[i][e] = Ropa()
                Obj_vestuarios[i][e].set_Ropa(vestuarios[i][e])
            else:
                Obj_vestuarios[i][e] = Calzado()
                Obj_vestuarios[i][e].set_Calzado(vestuarios[i][e])
    return Obj_vestuarios

def Crea_genero():
    """Function that creates a dictionary which stores the two possible genres (female or male), then returns the dictionary."""
    genero = {1: "Femenino ", 2: "Masculino"}
    Obj_genero = genero.copy()
    for j in range(1, len(genero)+1):
        Obj_genero[j] = Genero()
        Obj_genero[j].set_Nombre(genero[j])
    return Obj_genero

def Crea_color_piel():
    """Function that creates a dictionary which stores diferent skin colors (just five, in this case), then returns the dictionary."""
    colorpiel = {1: "Negra ", 2: "Marrón", 3: "Morena", 4: "Clara ", 5: "Blanca"}
    Obj_color_de_piel = colorpiel.copy()
    for j in range(1, len(colorpiel)+1):
        Obj_color_de_piel[j] = Color_de_piel()
        Obj_color_de_piel[j].set_Nombre(colorpiel[j])
    return Obj_color_de_piel

def Crea_rostro():
    """Function that creates a dictionary which stores diferent face shapes (just six, in this case), then returns the dictionary."""
    rostro = {1: "Redondo    ", 2: "Alargado   ", 3: "Corazón    ", 4: "Cuadrado   ", 5: "Ovalado    ", 6: "Rectangular"}
    Obj_rostro = rostro.copy()
    for e in range(1,len(Obj_rostro)+1):
        Obj_rostro[e] = Forma_rostro()
        Obj_rostro[e].set_Nombre(rostro[e])
    return Obj_rostro

def Crea_emociones():
    """Function that creates a dictionary which stores diferent expressions (just eight, in this case), then returns the dictionary."""
    emociones = {1: "Enfado   ", 2: "Desprecio", 3: "Disgusto ", 4: "Miedo    ", 5: "Sorpresa ", 6: "Alegría  ", 7: "Neutral  ", 8: "Tristeza "}
    Obj_emocion = emociones.copy()
    for e in range(1, len(emociones)+1):
        Obj_emocion[e] = Emocion()
        Obj_emocion[e].set_Nombre(emociones[e])
    return Obj_emocion

def Crea_Atributos_Cabello():
    """    Function that creates a dictionary (with three dictionaries inside).
    These dictionaries stores diferent hair attributes (such as: color, density or texture), then returns the dictionary.
    """
    Atr_cabello = {1: {1:"Negro    ", 2:"Rubio    ", 3:"Café     ", 4:"Castaño  ", 5:"Gris     ", 6:"Invisible"},
                   2: {1:"Escaso   ", 2:"Moderado ", 3:"Abundante"}, 3: {1:"Lacio   ", 2:"Ondulado", 3:"Rizado  "}}    

    Obj_cabello = copy.deepcopy(Atr_cabello)
    for i in range(1, len(Atr_cabello)+1):
        for j in range(1, len(Atr_cabello[i])+1):
            if i == 1:
                Obj_cabello[i][j] = Color_cabello()
                Obj_cabello[i][j].set_Color(Atr_cabello[i][j])
            elif i == 2:
                Obj_cabello[i][j] = Densidad_cabello()
                Obj_cabello[i][j].set_Densidad(Atr_cabello[i][j])
            else:
                Obj_cabello[i][j] = Textura_cabello()
                Obj_cabello[i][j].set_Textura(Atr_cabello[i][j])          
    return Obj_cabello 

def Crea_Atributos_Ojos():
    """    Function that creates a dictionary (with two dictionaries inside).
    Both dictionaries stores diferent eye characteristics (the first one stores shapes and the second one stores colors).
    After, returns the dictionary.
    """
    Atr_ojos = {1: {1: "Almendrados", 2: "Separados  ", 3: "Redondos   ", 4: "Caídos     ", 5: "Saltones   ", 6: "Juntos     ", 7: "Profundos  ", 8: "Asiáticos  "},
                2: {1: "Negro   ", 2: "Castaño ", 3: "Ámbar   ", 4: "Avellana", 5: "Verde   ", 6: "Azul    ", 7: "Gris    "}}
    Obj_ojos = copy.deepcopy(Atr_ojos) 
    for i in range(1, len(Obj_ojos)+1):
        for j in range(1, len(Obj_ojos[i])+1):
            if i == 1:
                Obj_ojos[i][j] = Forma_ojos()
                Obj_ojos[i][j].set_Forma(Atr_ojos[i][j])
            else:
                Obj_ojos[i][j] = Color_ojos()
                Obj_ojos[i][j].set_Color(Atr_ojos[i][j])
    return Obj_ojos 

def Crea_Fecha_Nac(): 
    """    Function that generates a random date of birth: a random day since 1 to 30, month since 1 to 12 and year since 1920 to 2018).
    Also stores these values in a dictionary and returns it.
    """
    Fecha_Nacimiento = {1: random.randint(1,30), 2: random.randint(1,12), 3: random.randint(1920,2018)}
    return Fecha_Nacimiento

def Calcula_Edad(Fecha_na):
    """    Function that calculates the age of a person, depending on his date of birth and the current date.
    Then, returns the person's age.

    Keyword arguments:
    Fecha_na -- Contains the person's date of birth.
    """
    fecha_a = date.today()             
    Fecha_Actual = {1: fecha_a.day, 2: fecha_a.month, 3: fecha_a.year}  #It is obtained the current date through the system. 
    Años = Fecha_Actual[3] - Fecha_na[3]                                #It is compared boht dates to calculate the person's age.
    if Fecha_na[2] > Fecha_Actual[2] or Fecha_na[2] >= Fecha_Actual[2] and Fecha_na[1] > Fecha_Actual[1] :
        Años = Años - 1 
    return Años

def Crea_Personas(cedulas,provincias,vestuarios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    """    Function that creates a list to store persons. 
    Depending on the quantity of ID cards, the function creates persons, through a "for" loop.
    All of the attributes are randomly selected and saved in a dictionary, for each person.
    Then, each dictionary is appended to the list. After that, returns the list.

    Keyword arguments:
    cedulas -- Dictionary that contains all the ID cards, previously created.
    provincias -- Dictionary that contains all the provinces of Costa Rica.
    accesorios -- Dictionary that contains all the possible attributes.
    genero -- Dictionary that contains the two possible genres.
    colores_de_piel -- Dictionary that contains all the possible skin colors.
    rostro -- Dictionary that contains all the possible face shapes.
    emociones -- Dictionary that contains all the possible expressions.
    atri_cabello -- Dictionary that contains tree dictionaries inside, which ones, contain all the possible hair attributes.
    atri_ojos -- Dictionary that contains two dictionaries inside, which ones, contain all the possible eye attributes.
    """
    Lista_Personas = []                     #It is created the list
    for i in range(1,len(cedulas)+1):       #The dictionary that contains ID cards, is toured
        Fecha_na = Crea_Fecha_Nac()         #The function "Crea_Fecha_Nac" is called to generate a random date of birth
        Edad_Años = Calcula_Edad(Fecha_na)  #The function "Calcula_Edad" is called to calculate the person's age

        cabello = {1: atri_cabello[1][random.randint(1,6)], 2: atri_cabello[2][random.randint(1,3)], 3: atri_cabello[3][random.randint(1,3)]}
        Obj_Cabello = Cabello()
        Obj_Cabello.set_Atributos_cabello({1: cabello[1], 2: cabello[2], 3: cabello[3]})
        Obj_Cabello.set_Color()
        Obj_Cabello.set_Densidad()
        Obj_Cabello.set_Textura()

        ojos = {1: atri_ojos[1][random.randint(1,8)], 2: atri_ojos[2][random.randint(1,7)]}
        Obj_Ojos = Ojos()
        Obj_Ojos.set_Atributos_ojos({1: ojos[1], 2: ojos[2]})
        Obj_Ojos.set_Color()
        Obj_Ojos.set_Forma()

        cant_accesorios = random.randint(0,5)
        cant_ropa = random.randint(4,7)
        accesorios = []
        prendas = []
        calzado = vestuarios[3][random.randint(1,len(vestuarios[3]))]

        for j in range(0,cant_accesorios):
            accesorio = vestuarios[1][random.randint(1,len(vestuarios[1]))]
            while accesorio in accesorios:
                accesorio = vestuarios[1][random.randint(1,len(vestuarios[1]))]
            accesorios.append(accesorio)

        for e in range(0,cant_ropa):
            ropa = vestuarios[2][random.randint(1,len(vestuarios[2]))]
            while ropa in prendas:
                ropa = vestuarios[2][random.randint(1,len(vestuarios[2]))]
            prendas.append(ropa)

        Obj_Vestuario = Vestuario()
        Obj_Vestuario.set_Accesorios(accesorios)
        Obj_Vestuario.set_Calzado(calzado)
        Obj_Vestuario.set_Ropa(prendas)

        Obj_Persona = Persona()
        Obj_Persona.set_Cedula(cedulas[random.randint(1,len(cedulas))])
        Obj_Persona.set_Edad(Edad_Años)
        Obj_Persona.set_Vestuario(Obj_Vestuario)
        Obj_Persona.set_Ojos(Obj_Ojos)
        Obj_Persona.set_Cabello(Obj_Cabello)
        Obj_Persona.set_Color_piel(colores_de_piel[random.randint(1,len(colores_de_piel))])
        Obj_Persona.set_Genero(genero[random.randint(1,len(genero))])
        Obj_Persona.set_Forma_rostro(rostro[random.randint(1,len(rostro))])
        Obj_Persona.set_Emocion(emociones[random.randint(1,len(emociones))])
        Obj_Persona.set_Provincia(provincias[random.randint(1,len(provincias))])
        Lista_Personas.append(Obj_Persona) #It is appended each dictionary to the person's list
    return Lista_Personas

def Crear_Persona_Auto(Personas,nueva_cedula,provincias,vestuarios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    """    Function that creates a person and add him to the list of persons, after that, returns the list. 
    The attributes of this person are randomly selected.

    Keyword arguments:
    Personas -- The list with persons.
    nueva_cedula -- An ID card is generated trough the "Crea_cedulas" function.
    provincias -- Dictionary that contains all the provinces of Costa Rica.
    accesorios -- Dictionary that contains all the possible attributes.
    genero -- Dictionary that contains the two possible genres.
    colores_de_piel -- Dictionary that contains all the possible skin colors.
    rostro -- Dictionary that contains all the possible face shapes.
    emociones -- Dictionary that contains all the possible expressions.
    atri_cabello -- Dictionary that contains tree dictionaries inside, which ones, contain all the possible hair attributes.
    atri_ojos -- Dictionary that contains two dictionaries inside, which ones, contain all the possible eye attributes.
    """
    for i in range(1, (len(Personas)+1)):  #The list of persons is toured to comprove that the new ID card isn't repeat
        while nueva_cedula[1] == Personas[i-1].get_Cedula(): #If the new ID card already exist, another one is created
            nueva_cedula = Crea_cedulas(1)
    Fecha_na = Crea_Fecha_Nac()                   #The function "Crea_Fecha_Nac" is called to generate a random date of birth
    Edad_Años = Calcula_Edad(Fecha_na)            #The function "Calcula_Edad" is called to calculate the person's age

    cabello = {1: atri_cabello[1][random.randint(1,6)], 2: atri_cabello[2][random.randint(1,3)], 3: atri_cabello[3][random.randint(1,3)]}
    Obj_Cabello = Cabello()
    Obj_Cabello.set_Atributos_cabello({1: cabello[1], 2: cabello[2], 3: cabello[3]})
    Obj_Cabello.set_Color()
    Obj_Cabello.set_Densidad()
    Obj_Cabello.set_Textura()

    ojos = {1: atri_ojos[1][random.randint(1,8)], 2: atri_ojos[2][random.randint(1,7)]}
    Obj_Ojos = Ojos()
    Obj_Ojos.set_Atributos_ojos({1: ojos[1], 2: ojos[2]})
    Obj_Ojos.set_Color()
    Obj_Ojos.set_Forma()

    cant_accesorios = random.randint(0,5)
    cant_ropa = random.randint(4,7)
    accesorios = []
    prendas = []
    calzado = vestuarios[3][random.randint(1,len(vestuarios[3]))]

    for j in range(0,cant_accesorios):
        accesorio = vestuarios[1][random.randint(1,len(vestuarios[1]))]
        while accesorio in accesorios:
            accesorio = vestuarios[1][random.randint(1,len(vestuarios[1]))]
        accesorios.append(accesorio)

    for e in range(0,cant_ropa):
        ropa = vestuarios[2][random.randint(1,len(vestuarios[2]))]
        while ropa in prendas:
            ropa = vestuarios[2][random.randint(1,len(vestuarios[2]))]
        prendas.append(ropa)

    Obj_Vestuario = Vestuario()
    Obj_Vestuario.set_Accesorios(accesorios)
    Obj_Vestuario.set_Calzado(calzado)
    Obj_Vestuario.set_Ropa(prendas)

    Obj_Persona = Persona()
    Obj_Persona.set_Cedula(nueva_cedula[1])
    Obj_Persona.set_Edad(Edad_Años)
    Obj_Persona.set_Vestuario(Obj_Vestuario)
    Obj_Persona.set_Ojos(Obj_Ojos)
    Obj_Persona.set_Cabello(Obj_Cabello)
    Obj_Persona.set_Color_piel(colores_de_piel[random.randint(1,len(colores_de_piel))])
    Obj_Persona.set_Genero(genero[random.randint(1,len(genero))])
    Obj_Persona.set_Forma_rostro(rostro[random.randint(1,len(rostro))])
    Obj_Persona.set_Emocion(emociones[random.randint(1,len(emociones))])
    Obj_Persona.set_Provincia(provincias[random.randint(1,len(provincias))])
    Personas.append(Obj_Persona)                                          #The dictionary is appended to the person's list
    print("\nPersona creada y agregada a la lista satisfactoriamente")
    return Personas

def Muestra_InfoP(Persona_seleccionada,mensaje):
    print(" ___________________________________ ")
    print("|",mensaje,"|")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    print("\t _______________ ")
    print("\t| Calzado       |")
    print("\t|---------------|")
    print("\t|",Persona_seleccionada.get_Vestuario(2),"\t|")
    print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    print("\t _______________ ")
    print("\t| Accesorios    |")
    print("\t|---------------|")
    for x in range(0,len(Persona_seleccionada.get_Vestuario(1))):
        print("\t|",Persona_seleccionada.get_Vestuario(1)[x].get_Accesorio(),"\t|")
    print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    print("\t _______________ ")        
    print("\t| Vestuario     |")  
    print("\t|---------------|")  
    for y in range(0,len(Persona_seleccionada.get_Vestuario(3))):    
        print("\t|",Persona_seleccionada.get_Vestuario(3)[y].get_Ropa(),"\t|")
    print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    return

def Modificar_Persona(Persona_seleccionada,vestuarios):
    Muestra_InfoP(Persona_seleccionada,"  Esta es su vestimenta actual   ")
    comando = 0
    while comando < 4:
        print("\n*********************************************************")
        print("*                                                       *")   
        print("* Digite:  1     para agregar una prenda                *")  
        print("* Digite:  2     para agregar un accesorio              *") 
        print("* Digite:  3     para cambiar su calzado                *")
        print("* Digite: #>3    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando <4:

            if comando == 1:
                print("Prendas disponibles")
                print(" _______________________________ ")
                for j in range(1,len(vestuarios[2])+1):
                    print("|","Prenda #",j,"\t",vestuarios[2][j].get_Ropa(),"\t|")
                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")     
                prenda_agregar = int(input("Digite un número correspondiente con la prenda que desea agregar: "))
                while prenda_agregar not in range(1,15):
                    print("Digito incorrecto")
                    prenda_agregar = int(input("Por favor digite un número correspondiente con la prenda que desea agregar: "))
                Persona_seleccionada.get_Vestuario(3).append(vestuarios[2][prenda_agregar])

            elif comando == 2:
                print("Accesorios disponibles")
                print(" _______________________________________ ")
                for j in range(1,len(vestuarios[1])+1):
                    print("|","Accesorio #",j,"\t",vestuarios[1][j].get_Accesorio(),"\t|")
                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")    
                accesorio_agregar = int(input("Digite un número correspondiente con el accesorio que desea agregar: "))
                while accesorio_agregar not in range(1,11):
                    print("Digito incorrecto")
                    accesorio_agregar = int(input("Por favor digite un número correspondiente con el accesorio que desea agregar: "))
                Persona_seleccionada.get_Vestuario(1).append(vestuarios[1][accesorio_agregar])
                
            else:
                print("Calzados disponibles")
                print(" _______________________________ ")
                for j in range(1,len(vestuarios[3])+1):
                    print("|","Calzado #",j,"\t",vestuarios[3][j].get_Calzado(),"\t|")
                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")     
                calzado_cambiar = int(input("Digite un número correspondiente con el calzado que desea: "))
                while calzado_cambiar not in range(1,11):
                    print("Digito incorrecto")
                    calzado_cambiar = int(input("Por favor digite un número correspondiente con el calzado que desea : "))
                Nuevo_vestuario = Vestuario()
                Nuevo_vestuario.set_Accesorios(Persona_seleccionada.get_Vestuario(1))
                Nuevo_vestuario.set_Ropa(Persona_seleccionada.get_Vestuario(3))
                Nuevo_vestuario.set_Calzado(vestuarios[3][calzado_cambiar])
                Persona_seleccionada.set_Vestuario(Nuevo_vestuario)
            Muestra_InfoP(Persona_seleccionada,"Ahora esta es su nueva vestimenta")
        else:
            return
    return Persona_seleccionada

def Seleccionar_PersonaM(Personas):
    Muestra_de_personas = []
    for i in range(1,6):
        Muestra_de_personas.append(random.choice(Personas))
    print("Seleccione la cedula de la persona que desea modificar")
    print("\n***************************************")
    print("*                                     *")
    for e in range(0,len(Muestra_de_personas)):
        print("*   Digite:  ",e+1,"    para:",Muestra_de_personas[e].get_Cedula(),"  *")
    print("*   Digite:  #>5    para: regresar    *")
    print("*                                     *")
    print("***************************************\n")
    comando = int(input("Digite un número correspondiente con el menú: "))
    if comando < 6 :
        Persona_seleccionada = Muestra_de_personas[comando-1]
        Persona_seleccionada = Modificar_Persona(Persona_seleccionada, Crea_vestuario())
    else:
        return Personas
    return Personas

def Administrador(Personas):
    """    Is the "Administrador" user's function, it allows him to create a new person either manually or automatically.
    Then, the new person is added to the persons's list and returns the list.
    The "Administrador" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with persons.
    """
    comando = 0
    while comando < 3:   #There is a menu, where the "Administrador" can select the option that he wants.
        print("\n*********************************************************")
        print("*                                                       *")   
        print("* Digite:  1     para crear persona automáticamente     *")   
        print("* Digite:  2     para modificar una persona             *")
        print("* Digite: #>2    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:                                                       #Option number 1: Create a person automatically
            Personas = Crear_Persona_Auto(Personas,Crea_cedulas(1),Crea_provincias(),Crea_vestuario(),Crea_genero(),Crea_color_piel(),Crea_rostro(),Crea_emociones(),Crea_Atributos_Cabello(),Crea_Atributos_Ojos())
        elif comando == 2:
            Personas = Seleccionar_PersonaM(Personas)
    return Personas

def Cuenta_P_Accesorios(Personas, genero, provincia, accesorio):
    Personas_provincia = 0
    Personas_accesorio = 0
    for i in Personas:
        if i.get_Genero() == genero.get_Nombre() and i.get_Provincia() == provincia.get_Nombre():
            Personas_provincia += 1
            if accesorio in i.get_Vestuario(1):
                Personas_accesorio += 1
    return [Personas_accesorio, Personas_provincia]

def Consultar_accesorio(Personas, vestuario, provincias, genero):
    print("Accesorios disponibles")
    print(" _______________________________________ ")
    for j in range(1,len(vestuario[1])+1):
        print("|","Accesorio #",j,"\t",vestuario[1][j].get_Accesorio(),"\t|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")    
    accesorio_buscar = int(input("Digite un número correspondiente con el accesorio que desea consultar: "))
    while accesorio_buscar not in range(1,11):
        print("Digito incorrecto")
        accesorio_buscar = int(input("Por favor digite un número correspondiente con el accesorio que desea consultar: "))
    
    for i in range(1, len(genero)+1):
        print(genero[i].get_Nombre())
        for e in range(1, len(provincias)+1):
            cantidad_personas = Cuenta_P_Accesorios(Personas, genero[i], provincias[e], vestuario[1][accesorio_buscar])
            print(provincias[e].get_Nombre(), "\t", cantidad_personas[0], "\t" , round((cantidad_personas[0] * 100) / cantidad_personas[1], 2))   
    return 

def Consultar_personas(Personas, vestuario, ojos, cabello, color_piel, genero, forma_rostro, emocion, provincia):
    return

def Analista(Personas):
    """    Is the "Analista" user's function, it allows him to apply for statatistics of the country.
    The "Analista" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with persons.
    """
    comando = 0
    while comando < 3:    #There is a menu, where the "Analista" can select the option that he wants.
        print("\n************************************************************************************")
        print("*                                                                                  *") 
        print("* Digite:  1     para ver estadísticas por accesorio en Costa Rica                 *")  
        print("* Digite:  2     para ver información de personas con caracteristicas deseadas     *")
        print("* Digite: #>2    para regresar                                                     *") 
        print("*                                                                                  *")  
        print("************************************************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:                      #Option number 1: Show the statistics per province and age group in Costa Rica.
            Consultar_accesorio(Personas, Crea_vestuario(), Crea_provincias(), Crea_genero())
        elif comando == 2:
            Consultar_personas(Personas, Crea_vestuario(), Crea_Atributos_Ojos(), Crea_Atributos_Cabello(), Crea_color_piel(), Crea_genero(),
            Crea_rostro(), Crea_emociones(), Crea_provincias())
    return

def validar_contraseña(contraseña,comando,Personas):
    """    Function that verify the user password, independently of which user was chosen ("Usuario", "Analista", or "Administrador").

    Keyword arguments:
    contraseña -- The typed password.
    comando -- Number that indicates which user was chosen ("Usuario", "Analista", or "Administrador").
    Personas -- The list with persons.
    """
    if comando == 1 :        
        while contraseña != "admi123" : #If the typed password was incorrect, the user has to type it again or return to the menu
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Administrador")
        Administrador(Personas)         #If the typed password was correct, the "Administrador" function is called
        
    elif comando == 2 :
        while contraseña != "ana456" :  #If the typed password was incorrect, the user has to type it again or return to the menu
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Analista")
        Analista(Personas)              #If the typed password was correct, the "Analista" function is called
    return 

def login():
    """Is the main function, allows select as which user login."""
    comando = 0
    #The "Crea_Personas" function is called and the list that it returns is saved in a variable (Personas).
    Personas = Crea_Personas(Crea_cedulas(1111), Crea_provincias(), Crea_vestuario(),Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),Crea_Atributos_Cabello(), Crea_Atributos_Ojos())
    while comando < 3:
        print("\n*******************************************************")
        print("*                                                     *")  #There is a menu for select as which user login
        print("* Digite:  1     para ingresar como Administrador     *")
        print("* Digite:  2     para ingresar como Analista          *")
        print("* Digite: #>2    para salir                           *")
        print("*                                                     *")
        print("*******************************************************\n")
        comando=int(input("Digite un número correspondiente con el menú: "))
        if comando < 3 :
            contraseña = input("\nDigite su contraseña: ")    #The password is typed, even if it's incorrect
            validar_contraseña(contraseña,comando,Personas)   #The "validar_contraseña" function is called
        else :
            print("\n********************\n*   Hasta luego!   *\n********************")
            return
login()