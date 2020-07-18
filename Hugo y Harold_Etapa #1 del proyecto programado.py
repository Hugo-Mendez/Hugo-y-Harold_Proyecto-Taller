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
        self.Genero = Genero()
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
    def set_Genero(self, genero):
        self.Genero = genero
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
    def get_Genero(self):
        return self.Genero.get_Nombre()
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
        self.texto.configure(state= "disabled")
        self.texto.grid(row=fila, column=columna)
        return  
    def cerrar_texto(self):
        self.texto.destroy()
        return 
    def cerrar_botones(self, botones):  
        for boton in botones:
            boton.destroy()  
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
                  3: {1: "Jeans", 2: "Pantalon militar", 3: "Pantaloneta"},   4: {1: "Enagua", 2: "Short", 3: "Jeans"},
                  5: {1: "Tenis", 2: "Zapatillas", 3: "Sandalías"},           6: {1: "Tacones", 2: "Tenis", 3: "Botas"},
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
        linea = [str(i.get_Cedula()), str(i.get_Edad()), i.get_Genero(), i.get_Provincia(), i.get_Vestuario(2)] 
        for j in i.get_Vestuario(1):
            linea.append(j.get_Accesorio())
        for f in i.get_Vestuario(3):
            linea.append(f.get_Ropa())
        Linea = "/".join(linea)
        archi.write(Linea + "\n") 
    archi.close()
    return 

def Crea_Personas(Personas,cedulas,provincias,vestuarios,generos):
    """    Function that creates a list to store "Persona" objects. 
    Depending on the quantity of ID cards, the function creates "Persona" objects, through a "for" loop.
    All of the attributes are randomly selected for each person.
    Then, each "Persona" object is appended to the list. After that, returns the list.

    Keyword arguments:
    cedulas -- Dictionary that contains all the ID cards, previously created.
    provincias -- Dictionary that contains the "Provincia" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    genero -- Dictionary that contains the "Genero" objects.
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
        Obj_Persona.set_Genero(Genero) 
        Obj_Persona.set_Provincia(provincias[random.randint(1,len(provincias))])
        Personas.append(Obj_Persona) #It is appended each "Persona" object to the list
    return Personas 

def Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, comando, Identificador=0, Nuevo_Avatar = Persona()):
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto()
    Obj_menu.set_titulo("Crear Avatar")
    if comando == 10:
        Administrador(Personas, vestuarios, ventana, Obj_menu)

    elif comando == 1:
        generos = Crea_genero()
        Nuevo_Avatar.set_Genero(generos[Identificador])
        if Nuevo_Avatar.get_Genero() == "Femenino ":
            Calzados = [] 
        else:
            Calzados = ["C:/Avatar App/Imagenes/Hombres/C1.png", "C:/Avatar App/Imagenes/Hombres/C2.png", "C:/Avatar App/Imagenes/Hombres/C3.png"]

        Obj_menu.set_texto(" Selecccione el calzado ", 19, 2, "orange", "white", ["helvetica",15], 0, 0)
        ImagenC1 = ImageTk.PhotoImage(Image.open(Calzados[0],"r").resize((150, 50)))
        ImagenC2 = ImageTk.PhotoImage(Image.open(Calzados[1],"r").resize((150, 50)))
        ImagenC3 = ImageTk.PhotoImage(Image.open(Calzados[2],"r").resize((150, 50)))

        BotonC1 = tk.Button(ventana, image = ImagenC1, command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [BotonC1, BotonC2, BotonC3], 2, 1, Nuevo_Avatar))
        BotonC1.grid(row= 1, column= 0, padx = 3, pady = 4)
        BotonC2 = tk.Button(ventana, image = ImagenC2, command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [BotonC1, BotonC2, BotonC3], 2, 2, Nuevo_Avatar))
        BotonC2.grid(row= 2, column= 0, padx = 3, pady = 4)
        BotonC3 = tk.Button(ventana, image = ImagenC3, command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [BotonC1, BotonC2, BotonC3], 2, 3, Nuevo_Avatar))
        BotonC3.grid(row= 3, column= 0, padx = 3, pady = 4)
        ventana.mainloop()

    elif comando == 0:
        Obj_menu.set_texto(" Selecccione el género ", 19, 2, "orange", "white", ["helvetica",15], 0, 1)
        ImagenM = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Hombres/BaseH.png").resize((250, 510)))
        ImagenF = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Mujeres/BaseM.png").resize((250, 510)))

        BotonM = tk.Button(ventana, image = ImagenM, command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [BotonM, BotonF], 1, 2))
        BotonM.grid(row= 2, column= 0, padx = 3, pady = 4)
        BotonF = tk.Button(ventana, image = ImagenF, command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [BotonM, BotonF], 1, 1))
        BotonF.grid(row= 2, column= 2, padx = 3, pady = 4)
        ventana.mainloop()

def Administrador(Personas, vestuarios, ventana, Obj_menu):
    """    Is the "Administrador" user's function, it allows him to create new persons automatically. 
    Then, the new persons are added to the persons's list and returns the list.
    The "Administrador" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    Obj_menu.set_titulo("Administrador")
    Obj_menu.set_texto("       ¿Cuál opción desea realizar?", 30, 2, "orange", "white", ["helvetica",15], 0, 0) 
    boton_crear_avatar = tk.Button(ventana, text= "Crear avatar", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [boton_crear_avatar, boton_vestir_avatar, boton_regresar], 0))
    boton_crear_avatar.grid(row= 2, column= 0)
    boton_vestir_avatar = tk.Button(ventana, text= "Vestir avatar", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : cierra_ventana(ventana, 1)) 
    boton_vestir_avatar.grid(row= 5, column= 0)
    boton_regresar = tk.Button(ventana, text= "Regresar", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : cierra_ventana(ventana, 1))
    boton_regresar.grid(row = 8, column = 0) 
    ventana.mainloop()
    return

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

def Analista(Personas, vestuarios, ventana, Obj_menu):
    """    Is the "Analista" user's function, it allows him to apply for statatistics and information of the country.
    The "Analista" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    Obj_menu.set_titulo("Analista")
    Obj_menu.set_texto("       ¿Cuál opción desea realizar?", 30, 2, "orange", "white", ["helvetica",15], 0, 0) 
    boton1 = tk.Button(ventana, text= "Opcion 1", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda :cierra_ventana(ventana, 1))
    boton1.grid(row= 2, column= 0)
    boton2 = tk.Button(ventana, text= "Opcion 2", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda :cierra_ventana(ventana, 1))
    boton2.grid(row= 5, column= 0) 
    boton_regresar = tk.Button(ventana, text= "Regresar", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : cierra_ventana(ventana, 1)) 
    boton_regresar.grid(row = 8, column = 0)
    ventana.mainloop()
    return

def Crea_personas_pordefecto(comando, ventana, Obj_menu, botones_anteriores):
    vestuarios = Crea_vestuario() #The "Crea_Vestuario" function is called to store the dictionary that it returns, in a variable.
    #The "Crea_Personas" function is called and the list that it returns is saved in a variable (Personas).
    Personas = Crea_Personas([], Crea_cedulas(5), Crea_provincias(), vestuarios ,Crea_genero() )
    Grabar_informacion_avatars(Personas) 

    Obj_menu.cerrar_botones(botones_anteriores) 
    Obj_menu.cerrar_texto()
    if comando == 1: 
        Administrador(Personas, vestuarios, ventana, Obj_menu)   #If the typed password was correct, the "Administrador" function is called
    elif comando == 2:
        Analista(Personas, vestuarios, ventana, Obj_menu)        #If the typed password was correct, the "Analista" function is called
    return

def validar_contrasena(ventana, Obj_menu, botones_anteriores, contrasena, comando): 
    """    Function that verify the user password, independently of which user was chosen ("Analista", or "Administrador").

    Keyword arguments:
    contraseña -- The typed password.
    comando -- Number that indicates which user was chosen ("Usuario", "Analista", or "Administrador").
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    if comando == 1 and contrasena.get()  == "admi123": 
        contrasena.destroy()
        Crea_personas_pordefecto(comando, ventana, Obj_menu, botones_anteriores)               
    elif comando == 2 and contrasena.get() == "ana456" :
        contrasena.destroy()
        Crea_personas_pordefecto(comando, ventana, Obj_menu, botones_anteriores) 
    else:
        contrasena.destroy()
        Ingresar_contrasena(False, comando, ventana, Obj_menu, botones_anteriores)  
    return 

def Ingresar_contrasena(estado, comando, ventana, Obj_menu, botones_anteriores): 
    Obj_menu.cerrar_botones(botones_anteriores)
    Obj_menu.cerrar_texto() 
    if estado == True:
        Obj_menu.set_texto("           Ingrese su contraseña:", 30, 2, "orange", "white", ["helvetica",15], 0, 0) 
    else:
        Obj_menu.set_texto("          Contraseña incorrecta,                 Vuelva a digitar su contraseña:", 30, 2, "orange", "white", ["helvetica",15], 0, 0)

    Obj_menu.set_titulo("Validar contraseña")
    contraseña = tk.Entry(ventana)
    contraseña.grid(row= 2, column= 0, pady= 2, ipadx= 103, ipady= 5)
    
    boton_continuar = tk.Button(ventana, text= "Continuar", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : validar_contrasena(ventana, Obj_menu, [boton_continuar, boton_regresar], contraseña, comando))
    boton_continuar.grid(row = 5, column = 0)
    boton_regresar = tk.Button(ventana, text= "Regresar", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : cierra_ventana(ventana, 1)) 
    boton_regresar.grid(row = 8, column = 0) 

    ventana.mainloop()
    return  

def cierra_ventana(ventana, comando):
    ventana.destroy()
    if comando == 1:       
        login() 
    return

def login():
    """Is the main function, allows select as which user login."""
    ventana = tk.Tk()
    menu_login = menu(ventana)
    menu_login.set_fondo("dark gray")
    menu_login.set_titulo("LOGIN")
    menu_login.set_texto("       Seleccione el tipo de usuario", 30, 2, "light blue", "black", ["helvetica",15], 0, 0)

    boton_admi = tk.Button(ventana, text= "Administrador", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : Ingresar_contrasena(True, 1, ventana, menu_login, [boton_admi, boton_ana, boton_salir]))
    boton_admi.grid(row = 2, column = 0)

    boton_ana = tk.Button(ventana, text= "Analista", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = lambda : Ingresar_contrasena(True, 2, ventana, menu_login, [boton_admi, boton_ana, boton_salir]))
    boton_ana.grid(row = 5, column = 0)

    boton_salir = tk.Button(ventana, text= "Salir", width= 30, height= 1, bg= "black", fg = "cyan", font= ["helvetica", 15], command = ventana.destroy)
    boton_salir.grid(row = 8, column = 0)
    
    ventana.mainloop()
login()