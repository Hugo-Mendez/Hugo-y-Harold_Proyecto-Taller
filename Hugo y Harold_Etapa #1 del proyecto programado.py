
#Authors: Hugo Méndez and Harold Ramírez
#Date: June 14th 2020

import copy
import random
from datetime import date
import tkinter as tk
from PIL import ImageTk, Image 

class Provincia:
    """    Class for the "Provincia" objects.

    Attributes:
    Nombre -- The province's name (there are seven provinces).

    Methods:
    __init__ -- The constructor method.
    set_Nombre -- Sets the province's name.
    get_Nombre -- Returns the provincia's name.
    """
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre 

class Genero:
    """    Class for the "Genero" objects.

    Attributes:
    Nombre -- The kind of genre (male or female).

    Methods:
    __init__ -- The constructor method.
    set_Nombre -- Sets the genre.
    get_Nombre -- Returns the genre.
    """
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre

class Color_de_piel:
    """    Class for the "Color_de_piel" objects.

    Attributes:
    Nombre -- The skin color(There are five colors).

    Methods:
    __init__ -- The constructor method.
    set_Nombre -- Sets the skin color.
    get_Nombre -- Returns the skin color.
    """
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre

class Forma_rostro:
    """    Class for the "Forma_rostro" objects.

    Attributes:
    Nombre -- The face shape (there are six shapes).

    Methods:
    __init__ -- The constructor method.
    set_Nombre -- Sets the face shape.
    get_Nombre -- Returns the face shape.
    """
    def __init__(self):
        self.Nombre = ""
        return
    def set_Nombre(self, nombre):
        self.Nombre = nombre
        return
    def get_Nombre(self):
        return self.Nombre 

class Color_cabello:
    """    Class for the "Color_cabello" objects.

    Attributes:
    Color -- The hair's color (there are six colors).

    Methods:
    __init__ -- The constructor method.
    set_Color -- Sets the hair's color.
    get_Color -- Returns the hair's color.
    """
    def __Init__(self):
        self.Color = ""
        return
    def set_Color(self, color):
        self.Color = color
        return
    def get_Color(self):
        return self.Color 

class Densidad_cabello:
    """    Class for the "Densidad_cabello" objects.

    Attributes:
    Densidad -- The hair's density (there are three options).

    Methods:
    __init__ -- The constructor method.
    set_Densidad -- Sets the hair's density.
    get_Densidad -- Returns the hair's density.
    """
    def __Init__(self):
        self.Densidad = ""
        return
    def set_Densidad(self, densidad):
        self.Densidad = densidad
        return
    def get_Densidad(self):
        return self.Densidad 

class Textura_cabello:
    """    Class for the "Textura_cabello" objects.

    Attributes:
    Textura -- The hair's texture (there are three options).

    Methods:
    __init__ -- The constructor method.
    set_Textura -- Sets the hair's texture.
    get_Textura -- Returns the hair's texture.
    """
    def __Init__(self):
        self.Textura = ""
        return
    def set_Textura(self, textura):
        self.Textura = textura
        return
    def get_Textura(self):
        return self.Textura 

class Cabello:
    """    Class for the "Cabello" objects.

    Attributes:
    Atributos_cabello -- Dictionary that is empty (at the beginning) and then it'll contain a "Color_cabello", "Densidad_cabello" and "Textura_cabello" objects.
    Color -- a "Color_cabello" object.
    Densidad -- a "Densidad_cabello" object.
    Textura --- a "Textura_cabello" object.

    Methods:
    __init__ -- The constructor method.  
    set_Atributos_cabello -- Sets the dictionary with the objects.
    set_Color -- Takes the element in the dictionary that is a "Color_cabello" object and applies it the "get_Color" method to obtain the hair's color.
    set_Densidad -- Takes the element in the dictionary that is a "Densidad_cabello" object and applies it the "get_Densidad" method to obtain the hair's density.
    set_Textura -- Takes the element in the dictionary that is a "Textura_cabello" object and applies it the "get_Textura" method to obtain the hair's texture.
    get_Color -- Returns the hair's color.
    get_Densidad -- Returns the hair's density.
    get_Textura -- Returns the hair's texture.
    """
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
    def get_Color(self):
        return self.Color
    def get_Densidad(self):
        return self.Densidad
    def get_Textura(self):
        return self.Textura

class Color_ojos:
    """    Class for the "Color_ojos" objects.

    Attributes:
    Color -- The eyes's color (there are seven colors).

    Methods:
    __init__ -- The constructor method.
    set_Color -- Sets the eyes's color.
    get_Color -- Returns the eyes's color.
    """
    def ___init__(self):
        self.Color = ""
        return
    def set_Color(self, color):
        self.Color = color
        return
    def get_Color(self):
        return self.Color

class Forma_ojos:
    """    Class for the "Forma_ojos" objects.

    Attributes:
    Forma -- The eyes's shape (there are eight shapes).

    Methods:
    __init__ -- The constructor method.
    set_Forma -- Sets the eyes's shape.
    get_Forma -- Returns the eyes's shape.
    """
    def ___init__(self):
        self.Forma = ""
        return
    def set_Forma(self, forma):
        self.Forma = forma
        return
    def get_Forma(self):
        return self.Forma 

class Ojos:
    """    Class for the "Ojos" objects.

    Attributes:
    Atributos_ojos -- Dictionary that is empty (at the beginning) and then it'll contain a "Color_ojos" and "Forma_ojos" objects.
    Forma -- a "Forma_ojos" object.
    Color -- a "Color_ojos" object.

    Methods:
    __init__ -- The constructor method.  
    set_Atributos_ojos -- Sets the dictionary with the objects.
    set_Forma -- Takes the element in the dictionary that is a "Forma_ojos" object and applies it the "get_Forma" method to obtain the eyes's shape.
    set_Color -- Takes the element in the dictionary that is a "Color_ojos" object and applies it the "get_Color" method to obtain the eyes's color.
    get_Forma -- Returns the eyes's shape.
    get_Color -- Returns the eyes's color.
    """
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
    """    Class for the "Accesorios" objects.

    Attributes:
    Nombre -- The accessorie's name (there are ten accessories).

    Methods:
    __init__ -- The constructor method.
    set_Accesorio -- Sets the accessorie's name.
    get_Accesorio -- Returns the accessorie's name.
    """
    def ___init__(self):
        self.Nombre = ""
        self.ID = 0
        return
    def set_Accesorio(self, nombre):
        self.Nombre = nombre
        return
    def set_ID(self, id):
        self.ID = id
        return
    def get_Accesorio(self):
        return self.Nombre
    def get_ID(self):
        return self.ID 

class Ropa:
    """    Class for the "Ropa" objects.

    Attributes:
    Nombre -- The clothing's name (there are fourteen kind of clothing).

    Methods:
    __init__ -- The constructor method.
    set_Ropa -- Sets the clothing's name.
    get_Ropa -- Returns the clothing's name.
    """
    def ___init__(self):
        self.Nombre = ""
        self.Tipo = ""
        self.ID = 0
        return
    def set_Ropa(self, nombre):
        self.Nombre = nombre
        return
    def set_Tipo(self, tipo):
        self.Tipo = tipo
        return 
    def set_ID(self, id):
        self.ID = id
        return
    def get_Ropa(self):
        return self.Nombre
    def get_Tipo(self):
        return self.Tipo
    def get_ID(self):
        return self.ID 

class Calzado:
    """    Class for the "Calzado" objects.

    Attributes:
    Nombre -- The shoes's name (there are ten kind of shoes).

    Methods:
    __init__ -- The constructor method.
    set_Calzado -- Sets the shoes's name.
    get_Calzado -- Returns the shoes's name.
    """
    def ___init__(self):
        self.Nombre = ""
        self.ID = 0
        return
    def set_Calzado(self, nombre):
        self.Nombre = nombre
        return
    def set_ID(self, id):
        self.ID = id
        return
    def get_Calzado(self):
        return self.Nombre
    def get_ID(self):
        return self.ID

class Vestuario:
    """    Class for the "Vestuario" objects.

    Attributes:
    Ropa -- a list with "Ropa" objects.
    Calzado -- a "Calzado" object.
    Accesorios --- a list with "Accesorios" objects.

    Methods:
    __init__ -- The constructor method.  
    set_Ropa -- Sets the list with clothing.
    set_Calzado -- Receives the "Calzado" object and applies it the "get_Calzado" method to obtain the kind of shoes.
    set_Accesorios -- Sets the list with accessories.
    get_Ropa -- Returns the list with clothing.
    get_Calzado -- Returns the kind of shoes.
    get_Accesorios -- Returns the list with accessories.
    """
    def __init__(self):
        self.Ropa = []
        self.Calzado = Calzado()
        self.Accesorios = [] 
        return
    def set_Ropa(self, lista_Rop):
        self.Ropa = lista_Rop
        return
    def set_Calzado(self, calzado):
        self.Calzado = calzado
        return
    def set_Accesorios(self, lista_Acc):
        self.Accesorios = lista_Acc
        return
    def get_Ropa(self):
        return self.Ropa
    def get_ID_Calzado(self):
        return self.Calzado.get_ID()
    def get_Calzado(self):
        return self.Calzado.get_Calzado()
    def get_Accesorios(self):
        return self.Accesorios

class Persona:
    """    Class for the "Persona" objects.

    Attributes:
    Clave -- A person's key.
    Cedula -- An unique ID card.
    Edad -- An integer number that represent the age of a person.
    Vestuario -- A "Vestuario" object.
    Ojos -- A "Ojos" object.
    Cabello -- A "Cabello" object. 
    Color_piel -- A "Color_de_piel" object.
    Genero -- A "Genero" object.
    Forma_rostro -- A "Forma_rostro" object.
    Provincia -- A "Provincia" object.

    Methods:
    __init__ -- The constructor method.  
    set_Cedula -- Sets an ID card.
    set_Edad -- Sets the age.
    set_Vestuario -- Sets a "Vestuario" object.
    set_Ojos -- Sets a "Ojos" object.
    set_Cabello -- Sets a "Cabello" object.
    set_Color_piel -- Sets a "Color_de_piel" object.
    set_Genero -- Sets a "Genero" object.
    set_Forma_rostro -- Sets a "Forma_Rostro" object.
    set_Provincia -- Sets a "Provincia" object.
    get_Cedula -- Returns the ID card.
    get_Edad --  Returns the age.
    get_Vestuario -- Receives a numeric identifier and depending on it, returns : the list with clothing, the list with accessories or the kind of shoes.
    get_Ojos -- Receives a numeric identifier and depending on it, returns : the eyes's shape or the eyes's color.
    get_Cabello -- Receives a numeric identifier and depending on it, returns : the hair's color, the hair's density or the hair's texture.
    get_Color_piel -- Takes the "Color_de_piel" object and applies it the "get_Nombre" method to obtain the skin color.
    get_Genero -- Takes the "Genero" object and applies it the "get_Nombre" method to obtain the genre.
    get_Forma_rostro -- Takes the "Forma_rostro" object and applies it the "get_Nombre" method to obtain the face shape.
    get_Provincia -- Takes the "Provincia" object and applies it the "get_Nombre" method to obtain the province.
    """
    def __Init__(self):
        self.Clave = ""
        self.Cedula = 0
        self.Edad = 0
        self.Vestuario = Vestuario()
        self.Ojos = Ojos()
        self.Cabello = Cabello()
        self.Color_piel = Color_de_piel()
        self.Genero = Genero()
        self.Forma_rostro = Forma_rostro()
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
    def set_Provincia(self, provincia):
        self.Provincia = provincia 
        return
    def set_Clave(self, clave):
        self.Clave = clave
        return
    def get_Cedula(self):
        return self.Cedula
    def get_Edad(self):
        return self.Edad 
    def get_Vestuario(self, identificador):
        if identificador == 1:
            for accesorio in self.Vestuario.get_Accesorios():
                self.Clave += str(accesorio.get_ID())
            return self.Vestuario.get_Accesorios()
        elif identificador == 2:
            self.Clave += str(self.Vestuario.get_ID_Calzado())
            return self.Vestuario.get_Calzado() 
        else:
            for prenda in self.Vestuario.get_Ropa():
                self.Clave += str(prenda.get_ID())
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
    def get_Provincia(self):
        return self.Provincia.get_Nombre()
    def get_Clave(self):
        return self.Clave

class menu:
    def __init__(self, ventana):
        self.ventana = ventana
        self.texto = tk.Text()
        return
    def set_fondo(self, color_fondo):
        self.ventana.configure(bg=color_fondo)
        return    
    def set_titulo(self, titulo):
        self.ventana.title(titulo)
        return
    def set_texto(self, texto, ancho, alto, fondo, color_letras, fuente, fila, columna):
        self.texto = tk.Text(self.ventana, width=ancho, height=alto, bg=fondo, foreground=color_letras, font=fuente)
        self.texto.insert(tk.END,texto)
        self.texto.configure(state="disabled")
        self.texto.grid(row=fila, column=columna)
        return        

def Crea_cedulas(cantidad):
    """    Function that creates a dictionary, then, through a "for" loop: creates a list of ID cards and adds them to the dictionary.
    After, returns the dictionary.
    
    Keyword arguments:
    cantidad -- Number that indicates the quantity of ID cards, that will be generated.
    """
    Cedulas = {}
    cedula = random.sample(range(200000000,299999999), cantidad)#Depending on "cantidad" (the given number), the ID cards are randomly created
    for i in range(0, len(cedula)):    #The list of ID cards is toured
        Cedulas[i+1] = cedula[i]       #It is added each ID card to the dictionary
    return Cedulas

def Crea_provincias():
    """    Function that creates a dictionary which stores the provinces of Costa Rica.
    Later, creates a copy of that dictionary and turns his elements to "Provincia" objects and applies them the "set_Nombre" method.
    Finally, returns the dictionary with the objects.
    """
    provincias = {1: "San José  ", 2: "Alajuela  ", 3: "Cartago   ", 4: "Heredia   ", 5: "Puntarenas", 6: "Guanacaste", 7: "Limón     "}
    Obj_provincia = provincias.copy()
    for j in range(1, len(provincias)+1):       
        Obj_provincia[j] = Provincia()      #The elements are transformed to objects, through a "for" loop
        Obj_provincia[j].set_Nombre(provincias[j])  
    return Obj_provincia

def Crea_vestuario():
    """    Function that creates a dictionary with three dictionaries inside.
    Those dictionaries stores the accessories, clothes and shoes, respectively.
    Then, creates a copy of that dictionary and turns his elements to objects of his respective classess and applies them the "set" method.
    Lastly returns the dictionary with the objects.
    """
    vestuarios = {1: {1: "Camiseta", 2: "Camiseta de tirantes", 3: "Suéter"}, 2: {1: "Blusa", 2: "Suéter", 3: "Chaqueta"},
                  3: {1: "Jeans", 2: "Shorts", 3: "Pantaloneta"},             4: {1: "Enagua", 2: "Short", 3: "Jeans"},
                  5: {1: "Tenis", 2: "Zapato casual", 3: "Sandalías"},        6: {1: "Tacones", 2: "Tenis", 3: "Botas"},
                  7: {1: "Lentes", 2: "Sombrero", 3: "Piercing"}} 
    Obj_vestuarios = copy.deepcopy(vestuarios)
    for i in range(1, len(vestuarios)+1):              #The elements are transformed to objects, through a "for" loop
        for e in range(1, len(vestuarios[i])+1):
            if i in range(1, 5):                       #Depending on the kind of element, the element is transformed to an object of his respective class
                Obj_vestuarios[i][e] = Ropa()
                Obj_vestuarios[i][e].set_Ropa(vestuarios[i][e])
                if i < 3:
                    Obj_vestuarios[i][e].set_Tipo("Superior")
                else:
                    Obj_vestuarios[i][e].set_Tipo("Inferior")
            elif i in range(5, 7): 
                Obj_vestuarios[i][e] = Calzado()  
                Obj_vestuarios[i][e].set_Calzado(vestuarios[i][e])
            else:
                Obj_vestuarios[i][e] = Accesorios()
                Obj_vestuarios[i][e].set_Accesorio(vestuarios[i][e])
            Obj_vestuarios[i][e].set_ID(e)
    return Obj_vestuarios 

def Crea_genero():
    """    Function that creates a dictionary which stores the two possible genres (female or male).
    After, creates a copy of that dictionary and turns his elements to "Genero" objects and applies them the "set_Nombre" method.
    Finally, returns the dictionary with the objects. 
    """
    genero = {1: "Femenino ", 2: "Masculino"}
    Obj_genero = genero.copy()
    for j in range(1, len(genero)+1):          
        Obj_genero[j] = Genero()           #The elements are transformed to objects, through a "for" loop
        Obj_genero[j].set_Nombre(genero[j])
    return Obj_genero

def Crea_color_piel():
    """    Function that creates a dictionary which stores diferent skin colors (just five, in this case).
    After, creates a copy of that dictionary and turns his elements to "Color_de_piel" objects and applies them the "set_Nombre" method.
    Finally, returns the dictionary with the objects.
    """
    colorpiel = {1: "Negra       ", 2: "Marrón      ", 3: "Morena      ", 4: "Clara       ", 5: "Blanca      "}
    Obj_color_de_piel = colorpiel.copy()
    for j in range(1, len(colorpiel)+1):
        Obj_color_de_piel[j] = Color_de_piel()     #The elements are transformed to objects, through a "for" loop
        Obj_color_de_piel[j].set_Nombre(colorpiel[j])
    return Obj_color_de_piel

def Crea_rostro():
    """    Function that creates a dictionary which stores diferent face shapes (just six, in this case).
    After, creates a copy of that dictionary and turns his elements to "Forma_rostro" objects and applies them the "set_Nombre" method.
    Finally, returns the dictionary with the objects.
    """
    rostro = {1: "Redondo    ", 2: "Alargado   ", 3: "Corazón    ", 4: "Cuadrado   ", 5: "Ovalado    ", 6: "Rectangular"}
    Obj_rostro = rostro.copy()
    for e in range(1,len(Obj_rostro)+1):
        Obj_rostro[e] = Forma_rostro()     #The elements are transformed to objects, through a "for" loop
        Obj_rostro[e].set_Nombre(rostro[e])
    return Obj_rostro

def Crea_Atributos_Cabello():
    """    Function that creates a dictionary (with three dictionaries inside).
    These dictionaries stores diferent hair attributes (such as: color, density or texture).
    After that, creates a copy of that dictionary and turns his elements to objects of his respective classess and applies them the "set" method.
    Finally, returns the dictionary with the objects.
    """
    Atr_cabello = {1: {1:"Negro    ", 2:"Rubio    ", 3:"Café     ", 4:"Castaño  ", 5:"Gris     ", 6:"Invisible"},
                   2: {1:"Escaso   ", 2:"Moderado ", 3:"Abundante"}, 3: {1:"Lacio   ", 2:"Ondulado", 3:"Rizado  "}}    

    Obj_cabello = copy.deepcopy(Atr_cabello)
    for i in range(1, len(Atr_cabello)+1):         #The elements are transformed to objects, through a "for" loop
        for j in range(1, len(Atr_cabello[i])+1):
            if i == 1:             #Depending on the kind of element, the element is transformed to an object of his respective class
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
    After that, creates a copy of that dictionary and turns his elements to objects of his respective classess and applies them the "set" method.
    Finally, returns the dictionary with the objects.
    """
    Atr_ojos = {1: {1: "Almendrados", 2: "Separados  ", 3: "Redondos   ", 4: "Caídos     ", 5: "Saltones   ", 6: "Juntos     ", 7: "Profundos  ", 8: "Asiáticos  "},
                2: {1: "Negro   ", 2: "Castaño ", 3: "Ámbar   ", 4: "Avellana", 5: "Verde   ", 6: "Azul    ", 7: "Gris    "}}
    Obj_ojos = copy.deepcopy(Atr_ojos) 
    for i in range(1, len(Obj_ojos)+1):           #The elements are transformed to objects, through a "for" loop
        for j in range(1, len(Obj_ojos[i])+1):
            if i == 1:               #Depending on the kind of element, the element is transformed to an object of his respective class
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

def Grabar_informacion_avatars(Personas):
    archi = open("Info_avatars.txt", "a")
    for i in Personas:
        linea = [str(i.get_Cedula()), str(i.get_Edad()), i.get_Genero(), i.get_Provincia(), i.get_Color_piel(), i.get_Forma_rostro(),
                 i.get_Cabello(1), i.get_Cabello(2), i.get_Cabello(3), i.get_Ojos(1), i.get_Ojos(2), i.get_Vestuario(2)] 
        for j in i.get_Vestuario(1):
            linea.append(j.get_Accesorio())
        for f in i.get_Vestuario(3):
            linea.append(f.get_Ropa())
        Linea = "/".join(linea)
        archi.write(Linea + "\n") 
    archi.close()
    return 

def Crea_Personas(Personas,cedulas,provincias,vestuarios,generos,colores_de_piel,rostro,atri_cabello,atri_ojos):
    """    Function that creates a list to store "Persona" objects. 
    Depending on the quantity of ID cards, the function creates "Persona" objects, through a "for" loop.
    All of the attributes are randomly selected for each person.
    Then, each "Persona" object is appended to the list. After that, returns the list.

    Keyword arguments:
    cedulas -- Dictionary that contains all the ID cards, previously created.
    provincias -- Dictionary that contains the "Provincia" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    genero -- Dictionary that contains the "Genero" objects.
    colores_de_piel -- Dictionary that contains the "Color_de_piel" objects.
    rostro -- Dictionary that contains the "Forma_rostro" objects.
    emociones -- Dictionary that contains the "Emocion" objects.
    atri_cabello -- Dictionary that contains tree dictionaries inside, which ones, contain the: "Color_cabello", "Densidad_cabello" and "Textura_cabello" objects.
    atri_ojos -- Dictionary that contains two dictionaries inside, which ones, contain the: "Color_ojos" and "Forma_ojos" objects.
    """
    if Personas != []:
        for y in range(1,len(cedulas)+1):
            for i in range(1, (len(Personas)+1)):  
                while cedulas[y] == Personas[i-1].get_Cedula(): 
                    cedulas[y] = Crea_cedulas(1)[1]

    for i in range(1,len(cedulas)+1):       #The dictionary that contains ID cards, is toured
        Fecha_na = Crea_Fecha_Nac()         #The function "Crea_Fecha_Nac" is called to generate a random date of birth
        Edad_Años = Calcula_Edad(Fecha_na)  #The function "Calcula_Edad" is called to calculate the person's age
        Genero = generos[random.randint(1,len(generos))] 

        cabello = {1: atri_cabello[1][random.randint(1,6)], 2: atri_cabello[2][random.randint(1,3)], 3: atri_cabello[3][random.randint(1,3)]}
        Obj_Cabello = Cabello()    #The "Cabello" object is instantiated, for each person 
        Obj_Cabello.set_Atributos_cabello({1: cabello[1], 2: cabello[2], 3: cabello[3]}) 
        Obj_Cabello.set_Color()
        Obj_Cabello.set_Densidad() #The "set" methods are applied to the "Cabello" object
        Obj_Cabello.set_Textura()

        ojos = {1: atri_ojos[1][random.randint(1,8)], 2: atri_ojos[2][random.randint(1,7)]}
        Obj_Ojos = Ojos()         #The "Ojos" object is instantiated, for each person
        Obj_Ojos.set_Atributos_ojos({1: ojos[1], 2: ojos[2]})
        Obj_Ojos.set_Color()      #The "set" methods are applied to the "Ojos" object
        Obj_Ojos.set_Forma()

        cant_accesorios = random.randint(0,3) #A person, could only have between zero or five accesoriess, this quantity is randomly selected
        accesorios = []              #There is a list to store the person's accesoriess, with the purpose of don't repeat them
        for j in range(0, cant_accesorios): 
            accesorio = vestuarios[7][random.randint(1,len(vestuarios[7]))]
            while accesorio in accesorios:          #Is checked that the accesoriess aren't repeat
                accesorio = vestuarios[7][random.randint(1,len(vestuarios[7]))]
            accesorios.append(accesorio) 

        Obj_Vestuario = Vestuario()            #The "Vestuario" object is instantiated, for each person
        if Genero.get_Nombre() == "Femenino ":
            claves = [2, 4, 6] 
        else:
            claves = [1, 3, 5]
        Obj_Vestuario.set_Calzado(vestuarios[claves[2]][random.randint(1, len(vestuarios[claves[2]]))])     #The "set" methods are applied to the "Vestuario" object
        Obj_Vestuario.set_Accesorios(accesorios)
        Obj_Vestuario.set_Ropa([vestuarios[claves[0]][random.randint(1, len(vestuarios[claves[0]]))], vestuarios[claves[1]][random.randint(1, len(vestuarios[claves[1]]))]])

        Obj_Persona = Persona()                #The "Persona" object is instantiated, for each person
        Obj_Persona.set_Clave("")
        Obj_Persona.set_Cedula(cedulas[i])
        Obj_Persona.set_Edad(Edad_Años)
        Obj_Persona.set_Vestuario(Obj_Vestuario)    #All the respective "set" methods are applied to the "Persona" object
        Obj_Persona.set_Ojos(Obj_Ojos)
        Obj_Persona.set_Cabello(Obj_Cabello)
        Obj_Persona.set_Color_piel(colores_de_piel[random.randint(1,len(colores_de_piel))])
        Obj_Persona.set_Genero(Genero) 
        Obj_Persona.set_Forma_rostro(rostro[random.randint(1,len(rostro))])
        Obj_Persona.set_Provincia(provincias[random.randint(1,len(provincias))])
        Personas.append(Obj_Persona) #It is appended each "Persona" object to the list
    return Personas 
    
def Muestra_InfoP(Persona_seleccionada,mensaje):
    """    Function that shows the clothing of the person selected.

    Keyword arguments:
    Persona_seleccionada -- The "Persona" object selected
    mensaje -- A simple message to distinguish between the current clothing of the person and the previous clothing
    """
    print(" ___________________________________ ")
    print("|",mensaje,"|")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    print("\t _______________ ")
    print("\t| Calzado       |")
    print("\t|---------------|")
    print("\t|",Persona_seleccionada.get_Vestuario(2),"\t|")     #The person's kind of shoes is printed
    print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")                                 #For do that, the "get_Vestuario(2)" method is applied
    print("\t _______________ ")
    print("\t| Accesorios    |")
    print("\t|---------------|")
    for x in range(0,len(Persona_seleccionada.get_Vestuario(1))):                   #The person's accessories are printed
        print("\t|",Persona_seleccionada.get_Vestuario(1)[x].get_Accesorio(),"\t|") #For do that, the "get_Vestuario(1)" method is applied
    print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    print("\t _______________ ")        
    print("\t| Vestuario     |")  
    print("\t|---------------|")  
    for y in range(0,len(Persona_seleccionada.get_Vestuario(3))):               #The person's clothing is printed  
        print("\t|",Persona_seleccionada.get_Vestuario(3)[y].get_Ropa(),"\t|")  #For do that, the "get_Vestuario(2)" method is applied
    print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    return

def Modificar_Persona(Persona_seleccionada,vestuarios):
    """    Function that allows the Administrator user to modify the clothing of the selected person.
    Finally, returns the person.

    Keyword arguments:
    Persona_seleccionada -- The "Persona" object selected by the administrator.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    Muestra_InfoP(Persona_seleccionada,"  Esta es su vestimenta actual   ") #The "Muestra_InfoP" function is called
    comando = 0
    while comando < 4:
        print("\n*********************************************************")
        print("*                                                       *")   
        print("* Digite:  1     para agregar una prenda                *")  
        print("* Digite:  2     para agregar un accesorio              *") #There is a menu to select the option to perform
        print("* Digite:  3     para cambiar su calzado                *")
        print("* Digite: #>3    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando <4:

            if comando == 1:
                print("Prendas disponibles")
                print(" _______________________________ ")                         #All the clothes are printed, to select one to add 
                for j in range(1,len(vestuarios[2])+1):    
                    print("|","Prenda #",j,"\t",vestuarios[2][j].get_Ropa(),"\t|") #For do that, the "get_Ropa" method is applied
                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")     
                prenda_agregar = int(input("Digite un número correspondiente con la prenda que desea agregar: "))
                while prenda_agregar not in range(1,15):
                    print("Digito incorrecto")
                    prenda_agregar = int(input("Por favor digite un número correspondiente con la prenda que desea agregar: "))
                Persona_seleccionada.get_Vestuario(3).append(vestuarios[2][prenda_agregar]) #The kind of clothing selected
                                                                                            #Is appended to the person's clothing list
            elif comando == 2:
                print("Accesorios disponibles")
                print(" _______________________________________ ")                   #All the accessories are printed, to select one to add 
                for j in range(1,len(vestuarios[1])+1):
                    print("|","Accesorio #",j,"\t",vestuarios[1][j].get_Accesorio(),"\t|") #For do that, the "get_Accesorio" method is applied
                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")    
                accesorio_agregar = int(input("Digite un número correspondiente con el accesorio que desea agregar: "))
                while accesorio_agregar not in range(1,11):
                    print("Digito incorrecto")                                      
                    accesorio_agregar = int(input("Por favor digite un número correspondiente con el accesorio que desea agregar: "))
                Persona_seleccionada.get_Vestuario(1).append(vestuarios[1][accesorio_agregar]) #The accessorie selected
                                                                                               #Is appended to the person's accessories list
            else:
                print("Calzados disponibles")
                print(" _______________________________ ")   #All the kind of shoes are printed, to select the wanted kind of shoe
                for j in range(1,len(vestuarios[3])+1):
                    print("|","Calzado #",j,"\t",vestuarios[3][j].get_Calzado(),"\t|") #For do that, the "get_Calzado" method is applied
                print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")     
                calzado_cambiar = int(input("Digite un número correspondiente con el calzado que desea: "))
                while calzado_cambiar not in range(1,11):
                    print("Digito incorrecto")
                    calzado_cambiar = int(input("Por favor digite un número correspondiente con el calzado que desea : "))
                Nuevo_vestuario = Vestuario()          #A new "Vestuario" object is created to set the new information             
                Nuevo_vestuario.set_Accesorios(Persona_seleccionada.get_Vestuario(1)) 
                Nuevo_vestuario.set_Ropa(Persona_seleccionada.get_Vestuario(3))
                Nuevo_vestuario.set_Calzado(vestuarios[3][calzado_cambiar]) 
                Persona_seleccionada.set_Vestuario(Nuevo_vestuario) #The "set_Vestuario" method is applied to the person, with the new "Vestuario" object 
            Muestra_InfoP(Persona_seleccionada,"Ahora esta es su nueva vestimenta") #The "Muestra_InfoP" function is called to see the new information
        else:
            return
    return Persona_seleccionada

def Seleccionar_PersonaM(Personas):
    """    Function that shows five ID cards to the administrator user, with the purpose of he selects one of them to modify that person.
    After he modified the person, the list with is returned.

    Keyword arguments:
    Personas -- List with the "Persona" objects
    """
    Muestra_de_personas = []
    for i in range(1,6):                      #A list is created to store the five "Persona" objects, which are randomly selected
        persona_muestra = random.choice(Personas)
        while persona_muestra in Muestra_de_personas:
            persona_muestra = random.choice(Personas)
        Muestra_de_personas.append(persona_muestra)
    print("Seleccione la cedula de la persona que desea modificar")
    print("\n***************************************")
    print("*                                     *")
    for e in range(0,len(Muestra_de_personas)):     #The ID cards of that persons are showed, to select one
        print("*   Digite:  ",e+1,"    para:",Muestra_de_personas[e].get_Cedula(),"  *")
    print("*   Digite:  #>5    para: regresar    *")
    print("*                                     *")
    print("***************************************\n")
    comando = int(input("Digite un número correspondiente con el menú: "))
    if comando < 6 :
        Persona_seleccionada = Muestra_de_personas[comando-1]  #It's stored the "Persona" object selected
        Persona_seleccionada = Modificar_Persona(Persona_seleccionada, Crea_vestuario()) #The "Modificar_Persona" function is called
    else:
        return Personas 
    return Personas

def Administrador(Personas,vestuarios):
    """    Is the "Administrador" user's function, it allows him to create new persons automatically.
    Then, the new persons are added to the persons's list and returns the list.
    The "Administrador" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    comando = 0
    while comando < 3:   #There is a menu, where the "Administrador" can select the option that he wants.
        print("\n*********************************************************")
        print("*                                                       *")   
        print("* Digite:  1     para crear personas automáticamente    *")   
        print("* Digite:  2     para modificar una persona             *")
        print("* Digite: #>2    para regresar                          *") 
        print("*                                                       *")  
        print("*********************************************************\n")
        comando = int(input("Digite un número correspondiente con el menú: "))
        if comando == 1:                              #Option number 1: Create persons automatically
            cantidad = int(input("\nIngrese la cantidad de personas que desea crear: ")) #This user, selects the quantity that he wants
            Personas = Crea_Personas(Personas,Crea_cedulas(cantidad),Crea_provincias(),vestuarios,Crea_genero(),Crea_color_piel(),Crea_rostro(),Crea_Atributos_Cabello(),Crea_Atributos_Ojos())
        elif comando == 2:
            Personas = Seleccionar_PersonaM(Personas) #Option number 2: Modify the clothing of a person    
    return Personas

def Cuenta_P_Accesorios(Personas, genero, provincia, accesorio):
    """   Function that founds out the quantity of persons who use a specific accessorie, depending on the province and genre given.
    Then, returns that quantity.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    genero -- A "Genero" object.    
    provincia -- A "Provincia" object or a number.
    accesorio -- A "Accesorio" object.
    """
    Personas_accesorio = 0
    if provincia == 0:       #If "provincia" is '0' the function will find the persons of the genre given
        for i in Personas:
            if i.get_Genero() == genero.get_Nombre() and accesorio in i.get_Vestuario(1):
                Personas_accesorio += 1
    else:                    #If "provincia" is an object the function will find the persons of the genre and province given
        for i in Personas:
            if i.get_Genero() == genero.get_Nombre() and i.get_Provincia() == provincia.get_Nombre() and accesorio in i.get_Vestuario(1):
                Personas_accesorio += 1
    return Personas_accesorio

def Consultar_accesorio(Personas, vestuario, provincias, genero):
    """    Function that shows the quantity and percentage of persons who use a specific accessorie in all provinces, for each genre.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuario -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    provincias -- Dictionary that contains the "Provincia" objects.
    genero -- Dictionary that contains the "Genero" objects.
    """
    print("Accesorios disponibles")
    print(" _______________________________________ ")
    for j in range(1,len(vestuario[1])+1):                                      #All the accessories are printed, to select one 
        print("|","Accesorio #",j,"\t",vestuario[1][j].get_Accesorio(),"\t|")   #For do that, the "get_Accesorio" method is applied
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    accesorio_buscar = int(input("Digite un número correspondiente con el accesorio que desea consultar: "))  #The user selects the accessorie that he wants
    while accesorio_buscar not in range(1,11):
        print("Digito incorrecto")
        accesorio_buscar = int(input("Por favor digite un número correspondiente con el accesorio que desea consultar: "))
    TOTAL = 0
    for i in range(1, len(genero)+1):       #For each genre the function "Cuenta_P_Accesorios" is called to get the quantity of persons who use the selected accessorie 
        Total_accesorios = Cuenta_P_Accesorios(Personas, genero[i], 0, vestuario[1][accesorio_buscar])
        print("\n\t\t       ___________ ")
        print("\t\t     ","|",genero[i].get_Nombre(),"|")
        print("\t\t       ¯¯¯¯¯¯¯¯¯¯¯ ")
        print(" ____________________________________________________ ")
        print("| Provincia","\t|","Personas que lo usan","\t|","Porcentaje |") #The statistics per province are printed
        print("|---------------|-----------------------|------------|")
        for e in range(1, len(provincias)+1):       #For each province the function "Cuenta_P_Accesorios" is called to get the quantity of persons who use the selected accessorie
            cantidad_personas = Cuenta_P_Accesorios(Personas, genero[i], provincias[e], vestuario[1][accesorio_buscar])
            print("|",provincias[e].get_Nombre(), "\t|\t", cantidad_personas, "\t\t|",round((cantidad_personas * 100) / Total_accesorios, 1),"%","    |")
            print("|---------------|-----------------------|------------|")
        print("|Total", genero[i].get_Nombre()+"|\t",Total_accesorios,"\t\t|","100 %","     |")    
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
        TOTAL = TOTAL + Total_accesorios            #The total of persons in Costa Rica that use the accessorie is got it
    print(" ______________________________________________________________ ")
    print("| Total de personas que usan el accesorio en Costa Rica :",TOTAL,"|")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
    return 

def Impresion_personas_consultadas(Personas, vestuario, ojos, cabello, lista_caracteristicas, lista_indices):
    """    Function that shows the information of the persons that have the characteristics selected by the user.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuario -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    ojos -- Dictionary that contains the "Ojos" objects.
    cabello -- Dictionary that contains the "Cabello" objects.
    lista_caracteristicas -- List that contains the characteristics to select, each characteristic is a dictionary which contain objects.
    lista_indices -- List that contain the options that the user selects.
    """
    Rango_edades = {0: 0, 1: 4, 2: 11, 3: 17, 4: 64, 5: 100}   #Dictionary that contains the limits for belong to an specific age group
    bandera = False      #There is a "flag variable" for comproving if there are or there aren't persons with that characteristics
    for i in Personas:   #Searches the persons that complies with that characteristics and prints his information
        if i.get_Edad() <= Rango_edades[lista_indices[4]] and i.get_Edad() > Rango_edades[(lista_indices[4])-1] and i.get_Color_piel() == lista_caracteristicas[0][lista_indices[0]].get_Nombre() and i.get_Genero() == lista_caracteristicas[1][lista_indices[1]].get_Nombre() and i.get_Forma_rostro() == lista_caracteristicas[2][lista_indices[2]].get_Nombre() and i.get_Provincia() == lista_caracteristicas[3][lista_indices[3]].get_Nombre():
            print("\n ___________________________________ ")
            print("| Cédula:", i.get_Cedula(),"                |")
            print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            Muestra_InfoP(i, "            Vestuario            ")
            print(" ___________________________________ ")
            print("|               Ojos                |")
            print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print("\t _______________ ")
            print("\t| Forma         |")
            print("\t|---------------|")
            print("\t|",i.get_Ojos(1),"\t|")
            print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print("\t _______________ ")
            print("\t| Color         |")
            print("\t|---------------|")
            print("\t|",i.get_Ojos(2),"\t|")
            print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print(" ___________________________________ ")
            print("|             Cabello               |")
            print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print("\t _______________ ")
            print("\t| Color         |")
            print("\t|---------------|")
            print("\t|",i.get_Cabello(1),"\t|")
            print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print("\t _______________ ")
            print("\t| Densidad      |")
            print("\t|---------------|")
            print("\t|",i.get_Cabello(2),"\t|")
            print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print("\t _______________ ")
            print("\t| Textura       |")
            print("\t|---------------|")
            print("\t|",i.get_Cabello(3),"\t|")
            print("\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
            print("---------------------------------------------------------")
            bandera = True
    if bandera == False:
        print("\n __________________________________________ ")
        print("| No hay personas con esas caracteristicas |")    
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")    
    return

def Consultar_personas(Personas, vestuario, ojos, cabello, lista_caracteristicas, indicador, lista_indices):
    """    Recursive function that allows the "Analista" user to ask for persons with some characteristics that he selects.
    
    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuario -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    ojos -- Dictionary that contains the "Ojos" objects.
    cabello -- Dictionary that contains the "Cabello" objects.
    lista_caracteristicas -- List that contains the characteristics to select, each characteristic is a dictionary which contain objects.
    indicador -- A number that represent the base case for the recursion.
    lista_indices -- List (empty at the beginning) that will contain the options that the user selects.
    """
    atributos_consultar = ["Colores de piel  ", "Género           ", "Formas del rostro", "Provincias       "]
    if indicador > 3:                       #When the base case is reached, the last menu is printed to select the only characteristic that isn't an object
        print("\n ___________________ ") 
        print("| Grupos Etarios    |")      #Which is the age group
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
        print(" ________________________________ ")
        print("| Digite: 1 para bebés           |")
        print("| Digite: 2 para niños           |")
        print("| Digite: 3 para adolescentes    |")
        print("| Digite: 4 para adultos         |")
        print("| Digite: 5 para adultos mayores |")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
        comando = int(input("Digite un número correspondiente con el grupo etario: "))
        while comando not in range(1, 6):
            print("Digito incorrecto")
            comando = int(input("Por favor digite un número correspondiente con el menú: "))
        lista_indices.append(comando)  #After the user selects the option, an identifier that represents the characteristic is appended to "lista_indices"
        Impresion_personas_consultadas(Personas, vestuario, ojos, cabello, lista_caracteristicas, lista_indices) #The function "Impresion_personas_consultadas" is called
        return
    else:                              #While the base case isn't reached, print a menu for each characteristic where the user selects the option that he wants
        print("\n ___________________ ")
        print("|",atributos_consultar[indicador],"|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")
        print(" _______________________________ ")
        for i in range(1, len(lista_caracteristicas[indicador])+1):
            print("| Digite:", i, "para", lista_caracteristicas[indicador][i].get_Nombre(),"\t|")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ")    
        caracteristica_deseada = int(input("Digite un número correspondiente con la caracteristica que desea consultar: "))
        while caracteristica_deseada not in range(1, len(lista_caracteristicas[indicador])+1):
            print("Digito incorrecto")
            caracteristica_deseada = int(input("Por favor digite un número correspondiente con la caracteristica que desea consultar: "))
        lista_indices.append(caracteristica_deseada)     #After the user selects the option, an identifier that represents the characteristic is appended to "lista_indices"
        Consultar_personas(Personas, vestuario, ojos, cabello, lista_caracteristicas, indicador+1, lista_indices) #Recursion is applied in order to continue with the next characteristic 

def Analista(Personas, vestuarios):
    """    Is the "Analista" user's function, it allows him to apply for statatistics and information of the country.
    The "Analista" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
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
        if comando == 1:  #Option number 1: Show the statistics of persons who use an specific accessorie, per genre and province
            Consultar_accesorio(Personas, vestuarios, Crea_provincias(), Crea_genero())
        elif comando == 2: #Option number 2: Show the information of persons with characteristics selected by this user
            Consultar_personas(Personas, vestuarios, Crea_Atributos_Ojos(), Crea_Atributos_Cabello(), [Crea_color_piel(), Crea_genero(),
            Crea_rostro(), Crea_provincias()], 0, [])
    return

def validar_contraseña(contraseña,comando,Personas, vestuarios): 
    """    Function that verify the user password, independently of which user was chosen ("Analista", or "Administrador").

    Keyword arguments:
    contraseña -- The typed password.
    comando -- Number that indicates which user was chosen ("Usuario", "Analista", or "Administrador").
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    if comando == 1 :        
        while contraseña != "admi123" : #If the typed password was incorrect, the user has to type it again or return to the menu
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Administrador")
        Administrador(Personas,vestuarios)         #If the typed password was correct, the "Administrador" function is called
        
    elif comando == 2 :
        while contraseña != "ana456" :  #If the typed password was incorrect, the user has to type it again or return to the menu
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Analista")
        Analista(Personas, vestuarios)              #If the typed password was correct, the "Analista" function is called

    return 
"""
def cierra_ventana(ventana, comando):
    ventana.quit()
    if comando == 1:       # prueba
        login() 
    return
"""
def Crea_personas_pordefecto(comando, ventana): 
    vestuarios = Crea_vestuario() #The "Crea_Vestuario" function is called to store the dictionary that it returns, in a variable.
    #The "Crea_Personas" function is called and the list that it returns is saved in a variable (Personas).
    Personas = Crea_Personas([], Crea_cedulas(5), Crea_provincias(), vestuarios ,Crea_genero(), Crea_color_piel(), Crea_rostro(),Crea_Atributos_Cabello(), Crea_Atributos_Ojos())
    Grabar_informacion_avatars(Personas)

    ventana.withdraw()
    ventana_contraseña = tk.Toplevel()
    menu_contraseña = menu(ventana_contraseña)
    menu_contraseña.set_fondo("dark gray")
    menu_contraseña.set_titulo("Validar contraseña")
    menu_contraseña.set_texto("Ingrese su contraseña:", 30, 2, "orange", "white", ["helvetica",15], 0, 0)
    contraseña = tk.Entry(ventana_contraseña)
    contraseña.grid(row= 2, column= 0, padx= 5, pady= 5, ipadx= 5, ipady= 5)

    boton_continuar = tk.Button(ventana_contraseña, text= "Continuar", width= 12, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : validar_contraseña(contraseña.get(), comando, Personas, vestuarios))
    boton_continuar.grid(row = 5, column = 0)

    boton_regresar = tk.Button(ventana_contraseña, text= "Regresar", width= 12, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : login())
    boton_regresar.grid(row = 8, column = 0)
    return
    
def login():
    """Is the main function, allows select as which user login."""
    ventana = tk.Tk()
    menu_login = menu(ventana)
    menu_login.set_fondo("dark gray")
    menu_login.set_titulo("LOGIN")
    menu_login.set_texto("Seleccione el tipo de usuario", 30, 2, "light blue", "black", ["helvetica",15], 0, 0)

    boton_admi = tk.Button(ventana, text= "Administrador", width= 12, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : Crea_personas_pordefecto(1, ventana))
    boton_admi.grid(row = 2, column = 0)

    boton_ana = tk.Button(ventana, text= "Analista", width= 12, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : Crea_personas_pordefecto(2, ventana))
    boton_ana.grid(row = 5, column = 0)

    boton_salir = tk.Button(ventana, text= "Salir", width= 12, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = ventana.destroy)
    boton_salir.grid(row = 8, column = 0)
    
    ventana.mainloop()
login()