
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
    vestuarios = {1: {1: "Lentes  ", 2: "Aretes  ", 3: "Piercing", 4: "Collar", 5: "Anillo", 6: "Reloj", 
                  7: "Brazalete", 8: "Diadema", 9: "Vincha", 10: "Monóculo"}, 
                  2: {1: "Camiseta", 2: "Camisa", 3: "Blusa", 4: "Pantalón", 5: "Falda", 6: "Abrigo", 7: "Vestido",
                  8: "Calcetines", 9: "Pantaloneta", 10: "Pantalones cortos", 11: "Saco", 12: "Corbata", 13: "Sombrero",
                  14: "Bufanda" }, 3: {1: "Oxford", 2: "Sandalias", 3: "Tenis", 4: "Mocasines", 5: "Botas",
                  6: "Botines de vestir", 7: "Brogue", 8: "Monk", 9: "Derby", 10: "Tacones"}}
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

        dic_persona = {1: cedulas[random.randint(1,len(cedulas))], 2: provincias[random.randint(1,len(provincias))], 3: Obj_Vestuario,
                       4: genero[random.randint(1,len(genero))], 5: colores_de_piel[random.randint(1,len(colores_de_piel))],
                       6: rostro[random.randint(1,len(rostro))], 7: emociones[random.randint(1,len(emociones))],
                       8: Obj_Cabello, 9: Obj_Ojos, 10: Edad_Años} #The attributes are randomly selected and saved in a dictionary
        Lista_Personas.append(dic_persona) #It is appended each dictionary to the person's list
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
        while nueva_cedula[1] == Personas[i-1][1]: #If the new ID card already exist, another one is created
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

    dic_persona = {1: nueva_cedula[1], 2: provincias[random.randint(1,len(provincias))], 3: Obj_Vestuario,
                   4: genero[random.randint(1,len(genero))], 5: colores_de_piel[random.randint(1,len(colores_de_piel))],
                   6: rostro[random.randint(1,len(rostro))], 7: emociones[random.randint(1,len(emociones))],
                   8: Obj_Cabello, 9: Obj_Ojos, 10: Edad_Años}  #The attributes are randomly selected and saved in a dictionary
    Personas.append(dic_persona)                                          #The dictionary is appended to the person's list
    print("\nPersona creada y agregada a la lista satisfactoriamente")
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
        print("* Digite:  2     para crear persona manualmente         *")
        print("* Digite: #>2    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:                                                       #Option number 1: Create a person automatically
            Personas = Crear_Persona_Auto(Personas,Crea_cedulas(1),Crea_provincias(),Crea_vestuario(),Crea_genero(),Crea_color_piel(),Crea_rostro(),Crea_emociones(),Crea_Atributos_Cabello(),Crea_Atributos_Ojos())
        elif comando == 2:                                                     #Option number 2: Create a person manually
            Personas = Crear_Persona_Manual(Personas,Crea_cedulas(1),Crea_provincias(),Crea_vestuario(),Crea_genero(),Crea_color_piel(),Crea_rostro(),Crea_emociones(),Crea_Atributos_Cabello(),Crea_Atributos_Ojos())
    return Personas

def Cuenta_Grupos_Etarios(Rango_edades,comando,Personas, provincia):
    """    Function that recieves: the list with persons, an specific province, a dictionary with an ages range and a "comando" (number).
    That number represents an specific age group, such as: babies, kids, teenagers, adults or older adults.
    Depending on the number and the province recieved, the function searchs on the person's list and find out:
    How many persons from that province and that age group there are on the list, then prints that quantity.

    Keyword arguments:
    Rango_edades -- Dictionary that contains the limits for belong to an specific age group.
    comando -- Number that represents an specific age group, such as: babies, kids, among others.
    Personas -- The list with persons.
    ID_provincia -- An specific province indicated.
    """
    Grupos_Etarios = {1: "Bebés          " , 2: "Niños          ", 3: "Adolescentes   ", 4: "Adultos        ", 5: "Adultos mayores"}
    Grupo_Etario = 0                     #Quantity of persons from the province and age group, previously stablished
    for i in range(0, (len(Personas))):  #The list of persons is toured, looking for those persons
        if Personas[i][2].get_Nombre() == provincia and Personas[i][10] <= Rango_edades[comando] and Personas[i][10] > Rango_edades[comando -1]:
            Grupo_Etario += 1            #If someone is found, the quantity increases
    if Grupo_Etario < 10 :
        print("\n _______________________")
        print("|",Grupos_Etarios[comando], "|", str(Grupo_Etario)+"  ","|") #The quantity of persons from that age group is printed
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    elif Grupo_Etario < 100 :
        print("\n _______________________")
        print("|",Grupos_Etarios[comando], "|", str(Grupo_Etario)+" ","|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")        
    else: 
        print("\n _______________________")
        print("|",Grupos_Etarios[comando], "|",Grupo_Etario,"|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")       
    return

def Informes_Provincias(Personas):
    """    Function that shows the statistics per province(population density) in Costa Rica.  
    For each person shows his personal information, such as: ID card, age, genre, among others. 

    Keyword arguments:
    Personas -- The list with persons.
    """
    Provincias = Crea_provincias()
    Rango_edades = {0: 0, 1: 4, 2: 11, 3: 17, 4: 64, 5: 100}        #Dictionary that contains the limits for belong to an specific age group.
    print("\n _________________________________________________")
    print("|     Estadística por provincia en Costa Rica     |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for e in range(1,(len(Provincias)+1)):     #For each province the list of persons will be toured.
        print("\n ___________")
        print("|",Provincias[e].get_Nombre())
        print(" ¯¯¯¯¯¯¯¯¯¯¯")
        PersonasProvi = 0                      #Quantity of persons per province.
        contador = 1                           #Number that represents an specific age group(since babies to older adults).
        while contador < len(Rango_edades):    #For each age group, the function "Cuenta_Grupos_Etarios" is called.
            Cuenta_Grupos_Etarios(Rango_edades, contador, Personas, Provincias[e].get_Nombre())
            for i in range(0, (len(Personas))):         #The list of persons is toured.
                if Personas[i][2].get_Nombre() == Provincias[e].get_Nombre():     #If someone from that province and that age group is found, his imformation is printed. 
                    if Personas[i][10] <= Rango_edades[contador] and Personas[i][10] > Rango_edades[contador -1]:       
                        print(" ___________________________________________________________________________ ")
                        print("| Cédula        | Edad     | Provincia      | Género        | Emoción       |")
                        if Personas[i][10] < 10:
                            print("|", Personas[i][1],"    |",str(Personas[i][10])+" ","      |",Personas[i][2].get_Nombre(),"    |", Personas[i][4].get_Nombre(),"    |",Personas[i][7].get_Nombre(),"    |")
                        else:
                            print("|", Personas[i][1],"    |",Personas[i][10],"      |",Personas[i][2].get_Nombre(),"    |", Personas[i][4].get_Nombre(),"    |",Personas[i][7].get_Nombre(),"    |")
                        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
                        print("|___________________________________________________________________________|")
                        print("| Color de piel   | Forma del rostro   | Forma de ojos   | Color de ojos    |")
                        print("|", Personas[i][5].get_Nombre(),"         |",Personas[i][6].get_Nombre(),"       |",Personas[i][9].get_Forma(),"    |",Personas[i][9].get_Color(),"        |")
                        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                        print("|___________________________________________________________________________|")
                        print("| Color cabello     | Densidad cabello    | Textura cabello    | Calzado    |")
                        print("|", Personas[i][8].get_Color(), "        |", Personas[i][8].get_Densidad(), "          |", Personas[i][8].get_Textura(), "          |", Personas[i][3].get_Calzado(),"  |")
                        print("\n| Accesorios        |")
                        for x in range(0,len(Personas[i][3].get_Accesorios())):
                            print(Personas[i][3].get_Accesorios()[x].get_Accesorio())
                        print("\n| Vestuario         |")    
                        for y in range(0,len(Personas[i][3].get_Ropa())):    
                            print(Personas[i][3].get_Ropa()[y].get_Ropa())
                        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                        print("---------------------------------------------------------------------------------")
                        PersonasProvi += 1                                     #The quantity of persons from that province increases.
            contador += 1                                                      #The "contador" increases, looking for the next age group.
        print("\nTotal de personas en ",Provincias[e].get_Nombre(),":",PersonasProvi,"\n")  #The quantity of persons for each province is printed.
        print("---------------------------------------------------------------------------------")
    return

def Informes_Grupos_Etarios(Personas):
    """    Function that shows the statistics per age group in Costa Rica.

    Keyword arguments:
    Personas -- The list with persons.
    """
    Grupos_Etarios = {1: "Bebés          " , 2: "Niños          ", 3: "Adolescentes   ", 4: "Adultos        ", 5: "Adultos mayores"}
    Rango_edades = {0: 0, 1: 4, 2: 12, 3: 18, 4: 60, 5: 100}       #Dictionary that contains the limits for belong to an specific age group.
    print("\n ____________________________________________________")
    print("|     Estadística por grupo etario en Costa Rica     |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for i in range(1, len(Rango_edades)):    #For each age group the list of persons will be toured.
        Total_etarios = 0                    #Quantity of persons per age group.
        for j in range(0, len(Personas)):    #The list of persons is toured.
            if Personas[j][10] <= Rango_edades[i] and Personas[j][10] > Rango_edades[i-1]: 
                Total_etarios += 1           #If someone from that age group is found his quantity of persons increases.
        print("\n ____________________________________________________________")    #For each age group: his quantity of persons and his percentage are printed.
        print("  Total de", Grupos_Etarios[i]," |  Porcentaje de", Grupos_Etarios[i], " ")  
        if Total_etarios < 10: 
            print(" ", str(Total_etarios)+"                         | ", round(Total_etarios*100/len(Personas), 1), "%")
        elif Total_etarios < 100 :
            print(" ", str(Total_etarios)+"                        | ", round(Total_etarios*100/len(Personas), 1), "%")
        else:
             print(" ", Total_etarios, "                      | ", round(Total_etarios*100/len(Personas), 1), "%")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print("-----------------------------------------------------------------------")
    return

def Informes_Emociones(Personas):
    """    Function that shows the statistics per emotion in Costa Rica.

    Keyword arguments:
    Personas -- The list with persons.
    """
    Cantidad_Emociones = {}    #Dictionary that will contain the quantity of persons for each emotion.
    Emociones = Crea_emociones()
    print("\n                        ________________________________________________________________")
    print("                       |     Estadística de emociones en las personas de Costa Rica     |")
    print("                        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for i in range(1,len(Emociones)+1):                     #For each emotion the list of persons will be toured.
        Personas_Emocion = 0                                #Quantity of persons with that emotion.
        for j in range(0,len(Personas)):                    #The list of persons is toured.
            if Personas[j][7].get_Nombre() == Emociones[i].get_Nombre():
                Personas_Emocion += 1                       #If someone with that emotion is found, the quantity of persons with that emotion increases.    
        Cantidad_Emociones[i] = Personas_Emocion            #The quantity of persons with that emotion is added to the dictionary.

    Lista_Clave_Valor = []                                  #List that will contain the key and value, for each element contained in the dictionary(Cantidad_Emociones).
    for x in range(1, len(Cantidad_Emociones)+1):           #The dictionary "Cantidad_Emociones" is toured.
        Lista_Clave_Valor.append(x)                         #The key is appended to the list.
        Lista_Clave_Valor.append(Cantidad_Emociones[x])     #The value is appended to the list.

    Cantidad_Emociones_Ordenadas = {}                       #Dictionary that will contain the same that "Cantidad_Emociones", but ordered from the highest value to the lowest.
    for y in range(1, len(Cantidad_Emociones)+1):           #The dictionary "Cantidad_Emociones" is toured.
        Mayor = max(Lista_Clave_Valor)                      #The max value is obtained.
        Cantidad_Emociones_Ordenadas[Lista_Clave_Valor[(Lista_Clave_Valor.index(Mayor))-1]] = Mayor  #The key that contained the max value is added to the dictionary with his value.
        Lista_Clave_Valor.remove(Mayor)                                                              #The max value is removed.
    Lista_Claves_Ordenadas = list(Cantidad_Emociones_Ordenadas.keys())   #List that contains the keys of "Cantidad_Emociones_Ordenadas". 
    print("              _______________________________________________________________________________________________")    #The statistics per emotion are printed.
    print("             |",Emociones[Lista_Claves_Ordenadas[0]].get_Nombre(),"|",Emociones[Lista_Claves_Ordenadas[1]].get_Nombre(),"|",Emociones[Lista_Claves_Ordenadas[2]].get_Nombre(),"|",
          Emociones[Lista_Claves_Ordenadas[3]].get_Nombre(),"|",Emociones[Lista_Claves_Ordenadas[4]].get_Nombre(),"|",Emociones[Lista_Claves_Ordenadas[5]].get_Nombre(),"|",
          Emociones[Lista_Claves_Ordenadas[6]].get_Nombre(),"|",Emociones[Lista_Claves_Ordenadas[7]].get_Nombre(),"|")
    print(" ____________|___________|___________|___________|___________|___________|___________|___________|___________|")
    print("| Total     ","|",Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[0]],"      |",Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[1]],"      |",
          Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[2]],"      |",Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[3]],"      |",
          Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[4]],"      |",Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[5]],"      |",
          Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[6]],"      |",Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[7]],"      |")
    print("|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|")    
    print("| Porcentaje","|",round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[0]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[1]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[2]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[3]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[4]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[5]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[6]]*100/len(Personas), 1),"%    |",
          round(Cantidad_Emociones_Ordenadas[Lista_Claves_Ordenadas[7]]*100/len(Personas), 1),"%    |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
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
        print("* Digite:  1     para ver estadísticas por provincia y por grupo etario            *")  
        print("* Digite:  2     para ver estadísticas de emoción en las personas de Costa Rica    *")
        print("* Digite: #>2    para regresar                                                     *") 
        print("*                                                                                  *")  
        print("************************************************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:                      #Option number 1: Show the statistics per province and age group in Costa Rica.
            Informes_Provincias(Personas)
            Informes_Grupos_Etarios(Personas)
        elif comando == 2:                    #Option number 2: Show the statistics per emotion in Costa Rica.
            Informes_Emociones(Personas)
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