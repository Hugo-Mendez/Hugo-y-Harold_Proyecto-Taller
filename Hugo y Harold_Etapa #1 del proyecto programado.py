#Authors: Hugo Méndez and Harold Ramírez
#Date: July 10th 2020 

import copy 
import time
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
    Nombre -- The accessorie's name (there are three accessories).
    ID -- An identifier that represents each accessorie.

    Methods:
    __init__ -- The constructor method.
    set_Accesorio -- Sets the accessorie's name.
    set_ID -- Sets the accessorie's ID
    get_Accesorio -- Returns the accessorie's name.
    get_ID -- Returns the accessorie's ID
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
    Nombre -- The clothing's name (there are six kind of clothing per genre).
    ID -- An identifier that represents each garment.

    Methods:
    __init__ -- The constructor method.
    set_Ropa -- Sets the clothing's name.
    set_ID -- Sets the clothing's ID.
    get_Ropa -- Returns the clothing's name.
    get_ID -- Returns the clothing's ID.
    """
    def ___init__(self):
        self.Nombre = ""
        self.ID = 0
        return
    def set_Ropa(self, nombre):
        self.Nombre = nombre
        return
    def set_ID(self, id):
        self.ID = id
        return
    def get_Ropa(self):
        return self.Nombre
    def get_ID(self):
        return self.ID 

class Calzado:
    """    Class for the "Calzado" objects.

    Attributes:
    Nombre -- The shoes's kind (there are three kind of shoes per genre).
    ID -- An identifier that represents each kind of shoe.

    Methods:
    __init__ -- The constructor method.
    set_Calzado -- Sets the shoes's kind.
    set_ID -- Sets the shoes's ID.
    get_Calzado -- Returns the shoes's kind.
    get_ID -- Returns the shoes's ID.
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
    Accesorios --- a list with an "Accesorio" object.

    Methods:
    __init__ -- The constructor method.  
    set_Ropa -- Sets the list with clothing.
    set_Calzado -- Receives the "Calzado" object.
    set_Accesorios -- Sets the list with the "Accesorio" object.
    get_Ropa -- Returns the list with clothing.
    get_ID_Calzado -- Applies the get_ID method to the "Calzado" object in order to return the shoes's ID.
    get_Calzado -- Applies the get_Calzado method to the "Calzado" object in order to return the kind of shoes.
    get_Accesorios -- Returns the list with the "Accesorio" object.
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
    Clave -- A person's key that represents the person's clothing.
    Cedula -- An unique ID card.
    Edad -- An integer number that represent the age of a person.
    Vestuario -- A "Vestuario" object.
    Genero -- A "Genero" object.
    Provincia -- A "Provincia" object.

    Methods:
    __init__ -- The constructor method.  
    set_Cedula -- Sets an ID card.
    set_Edad -- Sets the age.
    set_Vestuario -- Sets a "Vestuario" object.
    set_Genero -- Sets a "Genero" object.
    set_Provincia -- Sets a "Provincia" object.
    set_Clave -- Resets the person's key as a "".
    get_Cedula -- Returns the ID card.
    get_Edad --  Returns the age.
    get_Vestuario -- Receives a numeric identifier and depending on it, returns : the list with clothing, the list with accessories or the kind of shoes. At the same time, modifies the person's key.
    get_Genero -- Takes the "Genero" object and applies it the "get_Nombre" method to obtain the genre.
    get_Provincia -- Takes the "Provincia" object and applies it the "get_Nombre" method to obtain the province.
    get_Clave -- Returns the person's key.
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
            self.Clave += str(self.Vestuario.get_ID_Calzado())  #The person's key is generated according to the differents IDs of the person's clothing.
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
    """    Class for the "menu" objects.

    Attributes:
    ventana -- A tk.Tk object (graphical interface window)
    texto -- A tk.Text object (A text square of the window)

    Methods:
    __init__ -- The constructor method.
    set_fondo -- Sets the background color of the window.
    set_titulo -- Sets the title of the window.
    set_texto -- Sets the indicated characteristics to the "texto" attribute.
    cerrar_texto -- quits the "texto" attribute.
    cerrar_botones -- Receives a list with "tk.Button" objects and quit all of them.
    cerrar_label -- Receives a "tk.Label" object and quits it.
    """
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
        self.texto.grid(row=fila, column=columna, padx= 2, pady= 2)
        return  
    def cerrar_texto(self):
        self.texto.destroy()
        return 
    def cerrar_botones(self, botones):  
        for boton in botones:
            boton.destroy()  
        return         
    def cerrar_label(self, label):
        label.destroy()    
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
    provincias = {1: "San José  ", 2: "Alajuela  ", 3: "Cartago   ", 4: "Heredia   ", 5: "Guanacaste", 6: "Puntarenas", 7: "Limón     "}
    Obj_provincia = provincias.copy()
    for j in range(1, len(provincias)+1):       
        Obj_provincia[j] = Provincia()      #The elements are transformed to objects, through a "for" loop
        Obj_provincia[j].set_Nombre(provincias[j])  
    return Obj_provincia

def Crea_vestuario():
    """    Function that creates a dictionary with seven dictionaries inside.
    Those dictionaries stores the accessories, clothes and shoes.
    Then, creates a copy of that dictionary and turns his elements to objects of his respective classess and applies them the "set" and "set_ID" methods.
    Lastly returns the dictionary with the objects.
    """
    vestuarios = {1: {1: "Camiseta", 2: "Suéter", 3: "Camiseta de tirantes"}, 2: {1: "Blusa", 2: "Chaqueta", 3: "Abrigo"},
                  3: {1: "Jeans", 2: "Pantaloneta", 3: "Pantalon militar"},   4: {1: "Jeans", 2: "Shorts", 3: "Enagua"},
                  5: {1: "Tenis", 2: "Zapatillas", 3: "Sandalías"},           6: {1: "Tenis", 2: "Botas", 3: "Tacones"},
                  7: {1: "Lentes", 2: "Piercing", 3: "Reloj", 4: "Ninguno"}} 
    Obj_vestuarios = copy.deepcopy(vestuarios)
    for i in range(1, len(vestuarios)+1):              #The elements are transformed to objects, through a "for" loop
        for e in range(1, len(vestuarios[i])+1):
            if i in range(1, 5):                       #Depending on the kind of element, the element is transformed to an object of his respective class
                Obj_vestuarios[i][e] = Ropa()
                Obj_vestuarios[i][e].set_Ropa(vestuarios[i][e])
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

def Grabar_informacion_avatars(Personas, bandera):
    """Function that writes or rewrites the persons's information in a ".txt" file, if the file doesn't exist, it is created. 

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    bandera -- A boolean value, that indicates: write or rewrite.
    """
    if bandera == False:
        archi = open("C:/Avatar App/Info_avatars.txt", "a")
    else:
        for i in Personas:    #For each person, his key is reseted.
            i.set_Clave("")
        archi = open("C:/Avatar App/Info_avatars.txt", "w")
    for i in Personas:        #The information is obtained throught the differents "get" methods of the "Persona" objects in order to write it in the file.   
        linea = [str(i.get_Cedula()), str(i.get_Edad()), i.get_Genero(), i.get_Provincia(), i.get_Vestuario(1)[0].get_Accesorio(), i.get_Vestuario(2)] 
        for f in i.get_Vestuario(3):
            linea.append(f.get_Ropa())
        Linea = "/".join(linea)
        archi.write(Linea + "\n")
    archi.close()
    return

def Crea_Personas(cedulas, provincias, vestuarios, generos):
    """    Function that creates a list to store "Persona" objects. 
    Depending on the quantity of ID cards, the function creates "Persona" objects, through a "for" loop.
    All of the attributes are randomly selected for each person.
    Then, each "Persona" object is appended to the list. After that, returns the list.

    Keyword arguments:
    cedulas -- Dictionary that contains all the ID cards, previously created.
    provincias -- Dictionary that contains the "Provincia" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    generos -- Dictionary that contains the "Genero" objects.
    """
    Personas = []
    for i in range(1,len(cedulas)+1):       #The dictionary that contains ID cards, is toured
        Fecha_na = Crea_Fecha_Nac()         #The function "Crea_Fecha_Nac" is called to generate a random date of birth
        Edad_Años = Calcula_Edad(Fecha_na)  #The function "Calcula_Edad" is called to calculate the person's age
        Genero = generos[random.randint(1,len(generos))]  #A random genre is selected for each person

        accesorios = [vestuarios[7][random.randint(1,len(vestuarios[7]))]]  #There is a list to store the person's accesorie.

        Obj_Vestuario = Vestuario()  #The "Vestuario" object is instantiated, for each person
        if Genero.get_Nombre() == "Femenino ":  #Depending on the genre there are diffenrent keys to access in the "vestuarios" dictionary for getting the right clothing.
            claves = [2, 4, 6]
        else:
            claves = [1, 3, 5]
        Obj_Vestuario.set_Accesorios(accesorios)
        Obj_Vestuario.set_Calzado(vestuarios[claves[2]][random.randint(1, len(vestuarios[claves[2]]))])     #The "set" methods are applied to the "Vestuario" object
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

def Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, comando, Id, direccion, avatar): 
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto()
    indices = [1, 2, 3]
    if comando == 4:
        Obj_menu.set_texto("      Ahora este es su avatar ", 26, 2, "springgreen2", "black", ["helvetica",15], 0, 0)      

        if avatar.get_Genero() == "Femenino ":
            claves = [2, 4, 6]
        else:
            claves = [1, 3, 5]
        nuevo_vestuario = Vestuario()
        nuevo_vestuario.set_Accesorios([vestuarios[7][Id[3]]])
        nuevo_vestuario.set_Calzado(vestuarios[claves[2]][Id[0]])
        nuevo_vestuario.set_Ropa([vestuarios[claves[0]][Id[2]], vestuarios[claves[1]][Id[1]]])
        avatar.set_Vestuario(nuevo_vestuario)
        Grabar_informacion_avatars(Personas, True)

        Imagen_Av = ImageTk.PhotoImage(Image.open(direccion+avatar.get_Clave()+".png","r").resize((250, 510))) 
        Label = tk.Label(image= Imagen_Av)
        Label.grid(row=3, column=0, padx = 3, pady= 3)

        boton_continuar = tk.Button(ventana, text= "Regresar a menú de opciones", cursor= "hand2", width= 26, height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [boton_continuar], Label, 1)) 
        boton_continuar.grid(row = 4, column = 0)
        ventana.mainloop()

    elif comando == 3:
        Obj_menu.set_texto(" Seleccione el nuevo accesorio ", 27, 2, "springgreen2", "black", ["helvetica",15], 0, 0)      
        indiceAC = int(avatar.get_Clave()) // 1000
        if indiceAC != 4:    
            indices.remove(indiceAC)
            ImagenAC1 = ImageTk.PhotoImage(Image.open("C:/Avatar App/Imagenes/Accesorios/A" + str(indices[0]) + ".png","r").resize((110, 150)))  
            ImagenAC2 = ImageTk.PhotoImage(Image.open("C:/Avatar App/Imagenes/Accesorios/A" + str(indices[1]) + ".png","r").resize((110, 150))) 
            BotonAC1 = tk.Button(ventana, image = ImagenAC1, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Id[0], Id[1], Id[2],indices[0]], direccion, avatar))
            BotonAC2 = tk.Button(ventana, image = ImagenAC2, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Id[0], Id[1], Id[2],indices[1]], direccion, avatar)) 
            Botones_anteriores = [BotonAC1, BotonAC2]  
            for i in range(0, len(Botones_anteriores)):
                Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4)
            ventana.mainloop()
        else:
            ImagenAC1 = ImageTk.PhotoImage(Image.open("C:/Avatar App/Imagenes/Accesorios/A1.png","r").resize((110, 150)))  
            ImagenAC2 = ImageTk.PhotoImage(Image.open("C:/Avatar App/Imagenes/Accesorios/A2.png","r").resize((110, 150))) 
            ImagenAC3 = ImageTk.PhotoImage(Image.open("C:/Avatar App/Imagenes/Accesorios/A3.png","r").resize((110, 150))) 
            BotonAC1 = tk.Button(ventana, image = ImagenAC1, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Id[0], Id[1], Id[2],1], direccion, avatar))
            BotonAC2 = tk.Button(ventana, image = ImagenAC2, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Id[0], Id[1], Id[2],2], direccion, avatar)) 
            BotonAC3 = tk.Button(ventana, image = ImagenAC3, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Id[0], Id[1], Id[2],3], direccion, avatar)) 
            Botones_anteriores = [BotonAC1, BotonAC2, BotonAC3]
            for i in range(0, len(Botones_anteriores)):
                Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4)
            ventana.mainloop()

    elif comando == 2:
        Obj_menu.set_texto(" Seleccione la nueva prenda superior ", 31, 2, "springgreen2", "black", ["helvetica",15], 0, 0)  
        indiceA = (int(avatar.get_Clave()) // 10 )% 10 
        indices.remove(indiceA)

        ImagenA1 = ImageTk.PhotoImage(Image.open(direccion + "A" + str(indices[0]) + ".png","r").resize((110, 150)))  
        ImagenA2 = ImageTk.PhotoImage(Image.open(direccion + "A" + str(indices[1]) + ".png","r").resize((110, 150))) 
        BotonA1 = tk.Button(ventana, image = ImagenA1, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 3, [Id[0], Id[1], indices[0]], direccion, avatar))
        BotonA2 = tk.Button(ventana, image = ImagenA2, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 3, [Id[0], Id[1], indices[1]], direccion, avatar)) 
        Botones_anteriores = [BotonA1, BotonA2]  
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop()   

    elif comando == 1:
        Obj_menu.set_texto(" Seleccione la nueva prenda inferior ", 30, 2, "springgreen2", "black", ["helvetica",15], 0, 0) 
        indiceB = int(avatar.get_Clave()) % 10  
        indices.remove(indiceB)
    
        ImagenB1 = ImageTk.PhotoImage(Image.open(direccion + "B" + str(indices[0]) + ".png","r").resize((100, 140))) 
        ImagenB2 = ImageTk.PhotoImage(Image.open(direccion + "B" + str(indices[1]) + ".png","r").resize((100, 140))) 
        BotonB1 = tk.Button(ventana, image = ImagenB1, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 2, [Id[0], indices[0]], direccion, avatar))
        BotonB2 = tk.Button(ventana, image = ImagenB2, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 2, [Id[0], indices[1]], direccion, avatar))
        Botones_anteriores = [BotonB1, BotonB2]
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop()  

    elif comando == 0:
        Obj_menu.set_titulo("Vestir avatar")
        Obj_menu.set_texto(" Seleccione el nuevo calzado ", 25, 2, "springgreen2", "black", ["helvetica",15], 0, 0)

        indiceC = (int(avatar.get_Clave()) // 100) % 10

        indices.remove(indiceC) 
        if avatar.get_Genero() == "Masculino": 
            direccion = "C:/Avatar App/Imagenes/Hombres/" 
        else:
            direccion = "C:/Avatar App/Imagenes/Mujeres/"
        ImagenC1 = ImageTk.PhotoImage(Image.open(direccion + "C" + str(indices[0]) + ".png","r").resize((100, 100))) 
        ImagenC2 = ImageTk.PhotoImage(Image.open(direccion + "C" + str(indices[1]) + ".png","r").resize((100, 100))) 
        BotonC1 = tk.Button(ventana, image = ImagenC1, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 1, [indices[0]], direccion, avatar))
        BotonC2 = tk.Button(ventana, image = ImagenC2, cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 1, [indices[1]], direccion, avatar))
        Botones_anteriores = [BotonC1, BotonC2]
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop()  

def Seleccionar_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores):
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto() 
    Obj_menu.set_titulo("Seleccionar avatar a modificar")
    Obj_menu.set_texto("Seleccione el avatar que desea modificar", 33, 2, "springgreen2", "black", ["helvetica",15], 0, 2)
    Avatars_seleccionados = random.sample(range(0, len(Personas)-1), 5)
    imagenes = []
    for i in range(0, 5):
        if Personas[Avatars_seleccionados[i]].get_Genero() == "Masculino": 
            direccion = "C:/Avatar App/Imagenes/Hombres/" 
        else:
            direccion = "C:/Avatar App/Imagenes/Mujeres/" 
        Imagen_Av = ImageTk.PhotoImage(Image.open(direccion+Personas[Avatars_seleccionados[i]].get_Clave()+".png","r").resize((200, 450))) 
        imagenes.append(Imagen_Av)  

    Av_1 = tk.Button(ventana, image = imagenes[0], cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 0, 0, "", Personas[Avatars_seleccionados[0]]))
    Av_2 = tk.Button(ventana, image = imagenes[1], cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 0, 0, "", Personas[Avatars_seleccionados[1]]))
    Av_3 = tk.Button(ventana, image = imagenes[2], cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 0, 0, "", Personas[Avatars_seleccionados[2]]))
    Av_4 = tk.Button(ventana, image = imagenes[3], cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 0, 0, "", Personas[Avatars_seleccionados[3]]))
    Av_5 = tk.Button(ventana, image = imagenes[4], cursor= "hand2", command = lambda: Vestir_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 0, 0, "", Personas[Avatars_seleccionados[4]]))
    Botones_anteriores = [Av_1, Av_2, Av_3, Av_4, Av_5]  
    for i in range(0, len(Botones_anteriores)):
        Botones_anteriores[i].grid(row=3, column=i, padx = 2, pady= 2)
    ventana.mainloop()
    return

def Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, comando, Identificador, Nuevo_Avatar):
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto()
    if comando == 6:
        provincias = Crea_provincias()
        edad = Crea_Fecha_Nac() 
        edad = Calcula_Edad(edad)
        cedula = Crea_cedulas(1)

        for i in range(1, (len(Personas)+1)):
            while cedula[1] == Personas[i-1].get_Cedula():
                cedula = Crea_cedulas(1)          

        Nuevo_Avatar.set_Provincia(provincias[Identificador[5]])
        Nuevo_Avatar.set_Cedula(cedula[1])
        Nuevo_Avatar.set_Edad(edad)
        Nuevo_Avatar.set_Clave("")

        Personas.append(Nuevo_Avatar)
        Grabar_informacion_avatars([Nuevo_Avatar],False)
        Obj_menu.set_texto("     Este es su avatar", 19, 2, "springgreen2", "black", ["helvetica",15], 0, 0)
                
        if Nuevo_Avatar.get_Genero() == "Femenino ":
            direccion = "C:/Avatar App/Imagenes/Mujeres/"
        else:
            direccion = "C:/Avatar App/Imagenes/Hombres/"

        Imagen_Av = ImageTk.PhotoImage(Image.open(direccion+Nuevo_Avatar.get_Clave()+".png","r").resize((250, 510))) 
        Label = tk.Label(image= Imagen_Av)
        Label.grid(row=3, column=0, padx = 3, pady= 3)

        boton_continuar = tk.Button(ventana, text= "Regresar a menú de opciones", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [boton_continuar], Label, 1)) 
        boton_continuar.grid(row = 4, column = 0)
        ventana.mainloop()

    elif comando == 5:
        if Nuevo_Avatar.get_Genero() == "Femenino ":
            claves = [2, 4, 6]
        else:
            claves = [1, 3, 5]
        Obj_Vestuario = Vestuario()
        Obj_Vestuario.set_Accesorios([vestuarios[7][Identificador[4]]])
        Obj_Vestuario.set_Calzado(vestuarios[claves[2]][Identificador[1]])
        Obj_Vestuario.set_Ropa([vestuarios[claves[0]][Identificador[3]], vestuarios[claves[1]][Identificador[2]]])
        Nuevo_Avatar.set_Vestuario(Obj_Vestuario)

        Obj_menu.set_texto(" Seleccione la provincia ", 21, 2, "springgreen2", "black", ["helvetica",15], 0, 0)
        Provi_1 = tk.Button(ventana, text= "San José", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 1], Nuevo_Avatar))
        Provi_2 = tk.Button(ventana, text= "Alajuela", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 2], Nuevo_Avatar))
        Provi_3 = tk.Button(ventana, text= "Cartago", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu,  Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 3], Nuevo_Avatar))
        Provi_4 = tk.Button(ventana, text= "Heredia", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu,  Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 4], Nuevo_Avatar))
        Provi_5 = tk.Button(ventana, text= "Guanacaste", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 5], Nuevo_Avatar))
        Provi_6 = tk.Button(ventana, text= "Puntarenas", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 6], Nuevo_Avatar))
        Provi_7 = tk.Button(ventana, text= "Limón", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 6, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], Identificador[4], 7], Nuevo_Avatar))

        Botones_anteriores = [Provi_1, Provi_2, Provi_3, Provi_4, Provi_5, Provi_6, Provi_7]
        for x in range(0, len(Botones_anteriores)): 
            Botones_anteriores[x].grid(row = x+2, column = 0, padx = 3, pady= 3)
        ventana.mainloop() 
    
    elif comando == 4:
        Obj_menu.set_texto("  Seleccione el accesorio ", 27, 2, "springgreen2", "black", ["helvetica",15], 0, 0)
        ImagenAC1 = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Accesorios/A1.png").resize((110, 150)))
        ImagenAC2 = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Accesorios/A2.png").resize((110, 150)))
        ImagenAC3 = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Accesorios/A3.png").resize((110, 150))) 

        BotonAC1 = tk.Button(ventana, image = ImagenAC1, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 5, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], 1], Nuevo_Avatar))
        BotonAC2 = tk.Button(ventana, image = ImagenAC2, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 5, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], 2], Nuevo_Avatar))
        BotonAC3 = tk.Button(ventana, image = ImagenAC3, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 5, [Identificador[0], Identificador[1], Identificador[2], Identificador[3], 3], Nuevo_Avatar))
        Botones_anteriores = [BotonAC1, BotonAC2, BotonAC3] 
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop()         

    elif comando == 3:
        if Nuevo_Avatar.get_Genero() == "Femenino ":
            Prendas = ["C:/Avatar App/Imagenes/Mujeres/A1.png", "C:/Avatar App/Imagenes/Mujeres/A2.png", "C:/Avatar App/Imagenes/Mujeres/A3.png"]
        else:
            Prendas = ["C:/Avatar App/Imagenes/Hombres/A1.png", "C:/Avatar App/Imagenes/Hombres/A2.png", "C:/Avatar App/Imagenes/Hombres/A3.png"]

        Obj_menu.set_texto("  Seleccione la prenda superior ", 27, 2, "springgreen2", "black", ["helvetica",15], 0, 0)
        ImagenA1 = ImageTk.PhotoImage(Image.open(Prendas[0],"r").resize((110, 150)))
        ImagenA2 = ImageTk.PhotoImage(Image.open(Prendas[1],"r").resize((110, 150)))
        ImagenA3 = ImageTk.PhotoImage(Image.open(Prendas[2],"r").resize((110, 150))) 

        BotonA1 = tk.Button(ventana, image = ImagenA1, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Identificador[0], Identificador[1], Identificador[2], 1], Nuevo_Avatar))
        BotonA2 = tk.Button(ventana, image = ImagenA2, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Identificador[0], Identificador[1], Identificador[2], 2], Nuevo_Avatar))
        BotonA3 = tk.Button(ventana, image = ImagenA3, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 4, [Identificador[0], Identificador[1], Identificador[2], 3], Nuevo_Avatar))
        Botones_anteriores = [BotonA1, BotonA2, BotonA3]
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop() 

    elif comando == 2:
        if Nuevo_Avatar.get_Genero() == "Femenino ":
            Prendas = ["C:/Avatar App/Imagenes/Mujeres/B1.png", "C:/Avatar App/Imagenes/Mujeres/B2.png", "C:/Avatar App/Imagenes/Mujeres/B3.png"]
        else:
            Prendas = ["C:/Avatar App/Imagenes/Hombres/B1.png", "C:/Avatar App/Imagenes/Hombres/B2.png", "C:/Avatar App/Imagenes/Hombres/B3.png"]

        Obj_menu.set_texto("  Seleccione la prenda inferior ", 27, 2, "springgreen2", "black", ["helvetica",15], 0, 0)
        ImagenB1 = ImageTk.PhotoImage(Image.open(Prendas[0],"r").resize((100, 180)))
        ImagenB2 = ImageTk.PhotoImage(Image.open(Prendas[1],"r").resize((100, 100)))
        ImagenB3 = ImageTk.PhotoImage(Image.open(Prendas[2],"r").resize((100, 180)))

        BotonB1 = tk.Button(ventana, image = ImagenB1, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 3, [Identificador[0], Identificador[1], 1], Nuevo_Avatar))
        BotonB2 = tk.Button(ventana, image = ImagenB2, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 3, [Identificador[0], Identificador[1], 2], Nuevo_Avatar))
        BotonB3 = tk.Button(ventana, image = ImagenB3, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 3, [Identificador[0], Identificador[1], 3], Nuevo_Avatar))
        Botones_anteriores = [BotonB1, BotonB2, BotonB3]
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop()

    elif comando == 1:
        generos = Crea_genero()
        Nuevo_Avatar.set_Genero(generos[Identificador[0]])
        if Nuevo_Avatar.get_Genero() == "Femenino ":
            Calzados = ["C:/Avatar App/Imagenes/Mujeres/C1.png", "C:/Avatar App/Imagenes/Mujeres/C2.png", "C:/Avatar App/Imagenes/Mujeres/C3.png"] 
        else:
            Calzados = ["C:/Avatar App/Imagenes/Hombres/C1.png", "C:/Avatar App/Imagenes/Hombres/C2.png", "C:/Avatar App/Imagenes/Hombres/C3.png"]

        Obj_menu.set_texto(" Seleccione el calzado ", 19, 2, "springgreen2", "black", ["helvetica",15], 0, 0)
        ImagenC1 = ImageTk.PhotoImage(Image.open(Calzados[0],"r").resize((100, 100)))
        ImagenC2 = ImageTk.PhotoImage(Image.open(Calzados[1],"r").resize((100, 100)))
        ImagenC3 = ImageTk.PhotoImage(Image.open(Calzados[2],"r").resize((100, 100)))

        BotonC1 = tk.Button(ventana, image = ImagenC1, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 2, [Identificador[0], 1], Nuevo_Avatar))
        BotonC2 = tk.Button(ventana, image = ImagenC2, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 2, [Identificador[0], 2], Nuevo_Avatar))
        BotonC3 = tk.Button(ventana, image = ImagenC3, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 2, [Identificador[0], 3], Nuevo_Avatar))
        Botones_anteriores = [BotonC1, BotonC2, BotonC3]  
        for i in range(0, len(Botones_anteriores)):
            Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
        ventana.mainloop()

    elif comando == 0:
        Obj_menu.set_titulo("Crear Avatar")
        Obj_menu.set_texto(" Seleccione el género ", 19, 2, "springgreen2", "black", ["helvetica",15], 0, 1)
        ImagenM = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Hombres/BaseH.png").resize((250, 510)))
        ImagenF = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Mujeres/BaseM.png").resize((250, 510)))

        BotonM = tk.Button(ventana, image = ImagenM, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 1, [2], Nuevo_Avatar))
        BotonF = tk.Button(ventana, image = ImagenF, cursor= "hand2", command = lambda: Crear_avatar(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, 1, [1], Nuevo_Avatar)) 
        Botones_anteriores = [BotonM, BotonF] 
        BotonM.grid(row= 2, column= 0, padx = 3, pady = 4)
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
    Nueva_persona = Persona()
    ventana.iconbitmap("C:/Avatar App/Imagenes/IconoAD.ico")
    Obj_menu.set_titulo("Administrador")
    Obj_menu.set_texto("       ¿Cuál opción desea realizar?", 30, 2, "springgreen2", "black", ["helvetica",15], 0, 0) 
    boton_crear_avatar = tk.Button(ventana, text= "Crear avatar", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Crear_avatar(Personas, vestuarios, ventana, Obj_menu, [boton_crear_avatar, boton_vestir_avatar, boton_regresar], 0, 0, Nueva_persona))
    boton_crear_avatar.grid(row= 2, column= 0)
    boton_vestir_avatar = tk.Button(ventana, text= "Vestir avatar", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "springgreen2", font= ["helvetica", 15], command = lambda : Seleccionar_avatar(Personas, vestuarios, ventana, Obj_menu, [boton_crear_avatar, boton_vestir_avatar, boton_regresar]))
    boton_vestir_avatar.grid(row= 5, column= 0)
    boton_regresar = tk.Button(ventana, text= "Regresar", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [boton_crear_avatar, boton_vestir_avatar, boton_regresar], 0 ,3))
    boton_regresar.grid(row = 8, column = 0) 
    ventana.mainloop()
    return 

def vestuarios_mas_utilizados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, Id):
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto()

    lista_vestuarios = []
    personas_genero = []
    archi = open("C:/Avatar App/Info_avatars.txt", "r")
    informacion = archi.readlines()
    for i in range(0, len(informacion)):
        info = informacion[i].split("/")
        if info[2] == Id:
            personas_genero.append(Personas[i])
            lista_vestuarios.append(info[4:])

    veces = []
    for lista in lista_vestuarios:
        cantidad = lista_vestuarios.count(lista)
        veces.append(cantidad)

    mayor = max(veces)
    indice_mayor = veces.index(mayor)
    porcentaje = round((mayor*100)/len(veces),2) 

    if Id == "Masculino": 
        direccion = "C:/Avatar App/Imagenes/Hombres/" 
    else:
        direccion = "C:/Avatar App/Imagenes/Mujeres/"

    Obj_menu.set_texto(" Este es el vestuario más utilizado por dicho genero.                       Con un porcentaje de: "+str(porcentaje)+"%", 44, 4, "deep sky blue", "black", ["helvetica",15], 0, 0)

    Imagen_Av = ImageTk.PhotoImage(Image.open(direccion + personas_genero[indice_mayor].get_Clave()+".png","r").resize((250, 510))) 
    Label = tk.Label(image= Imagen_Av)
    Label.grid(row=4, column=0, padx = 3, pady= 3)

    boton_regresar = tk.Button(ventana, text= "Regresar a menú de opciones", cursor= "hand2", width= 44 , height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [boton_regresar], Label, 2))
    boton_regresar.grid(row= 5, column= 0, padx=2, pady=2)
    ventana.mainloop()
    return 

def Consultar_vestuario(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores):
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto()

    Obj_menu.set_titulo("Consultar vestuarios más utilizados")

    Obj_menu.set_texto(" Seleccione el género ", 19, 2, "deep sky blue", "black", ["helvetica",15], 0, 1)
    ImagenM = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Hombres/BaseH.png").resize((250, 510)))
    ImagenF = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Mujeres/BaseM.png").resize((250, 510)))

    BotonM = tk.Button(ventana, image = ImagenM, cursor= "hand2", command = lambda: vestuarios_mas_utilizados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, "Masculino",))
    BotonF = tk.Button(ventana, image = ImagenF, cursor= "hand2", command = lambda: vestuarios_mas_utilizados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, "Femenino ",)) 
    Botones_anteriores = [BotonM, BotonF]
    BotonM.grid(row= 2, column= 0, padx = 3, pady = 4)
    BotonF.grid(row= 2, column= 2, padx = 3, pady = 4)
    ventana.mainloop()
    return

def muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, id, linea):
    if linea == len(Personas): 
        Obj_menu.cerrar_texto() 
        Obj_menu.set_texto(" No existen más avatars que utilizan dicho accesorio", 42, 2, "deep sky blue", "black", ["helvetica",15], 0, 0) 
        boton_regresar = tk.Button(ventana, text= "Regresar a menú de opciones", cursor= "hand2", width= 41 , height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [boton_regresar], 0, 2)) 
        boton_regresar.grid(row= 3, column= 0, padx=2, pady=2) 
        ventana.mainloop()

    elif Botones_anteriores == []: 
        archi = open("C:/Avatar App/Info_avatars.txt", "r")
        informacion = archi.readlines()
        info = informacion[linea].split("/")
        archi.close() 
        if info[4] == id:
            if info[2] == "Masculino": 
                direccion = "C:/Avatar App/Imagenes/Hombres/" 
            else:
                direccion = "C:/Avatar App/Imagenes/Mujeres/" 
            Imagen_Av = ImageTk.PhotoImage(Image.open(direccion + Personas[linea].get_Clave()+ ".png","r").resize((250, 510))) 
            Label = tk.Label(image= Imagen_Av)
            Label.grid(row=3, column=0, padx = 3, pady= 3)

            boton_continuar = tk.Button(ventana, text= "Continuar con el siguiente avatar", cursor= "hand2", width= 26, height= 1, bg= "black", fg = "deep sky blue", font= ["helvetica", 15], command = lambda : (regresar_usuario(0, 0, 0, Obj_menu, [boton_continuar], Label, 4) , muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, [], id, linea+1))) 
            boton_continuar.grid(row = 4, column = 0)
            ventana.mainloop() 
        else:
            muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, [], id, linea+1) 
    else:
        Obj_menu.cerrar_botones(Botones_anteriores) 
        Obj_menu.cerrar_texto()
        Obj_menu.set_texto("Se muestran los avatars que utilizan dicho accesorio", 42, 2, "deep sky blue", "black", ["helvetica",15], 0, 0) 
        muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, [], id, linea)  

def Consultar_accesorio(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores):
    Obj_menu.cerrar_botones(Botones_anteriores)
    Obj_menu.cerrar_texto()
    Obj_menu.set_titulo("Consultar accesorio")
    Obj_menu.set_texto(" ¿Cuál accesorio desea consultar? ", 29, 2, "deep sky blue", "black", ["helvetica",15], 0, 0) 

    ImagenAC1 = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Accesorios/A1.png").resize((110, 150)))
    ImagenAC2 = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Accesorios/A2.png").resize((110, 150)))
    ImagenAC3 = ImageTk.PhotoImage(Image.open(r"C:/Avatar App/Imagenes/Accesorios/A3.png").resize((110, 150))) 
    BotonAC1 = tk.Button(ventana, image = ImagenAC1, cursor= "hand2", command = lambda: muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, "Lentes", 0)) 
    BotonAC2 = tk.Button(ventana, image = ImagenAC2, cursor= "hand2", command = lambda: muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, "Piercing", 0))
    BotonAC3 = tk.Button(ventana, image = ImagenAC3, cursor= "hand2", command = lambda: muestra_accesorios_consultados(Personas, vestuarios, ventana, Obj_menu, Botones_anteriores, "Reloj", 0)) 
    Botones_anteriores = [BotonAC1, BotonAC2, BotonAC3] 
    for i in range(0, len(Botones_anteriores)):
        Botones_anteriores[i].grid(row= i+2, column= 0, padx = 3, pady = 4) 
    ventana.mainloop()
    return 

def Analista(Personas, vestuarios, ventana, Obj_menu):  
    """    Is the "Analista" user's function, it allows him to apply for statatistics and information of the country.
    The "Analista" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    """
    ventana.iconbitmap("C:/Avatar App/Imagenes/IconoAN.ico")
    Obj_menu.set_titulo("Analista")
    Obj_menu.set_texto("       ¿Cuál opción desea realizar?", 30, 2, "deep sky blue", "black", ["helvetica",15], 0, 0)  
    Boton_Consulta_acc = tk.Button(ventana, text= "Consultar accesorio", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "deep sky blue", font= ["helvetica", 15], command = lambda : Consultar_accesorio(Personas, vestuarios, ventana, Obj_menu, [Boton_Consulta_acc, Boton_Consulta_Ves, boton_regresar]))
    Boton_Consulta_acc.grid(row= 2, column= 0) 
    Boton_Consulta_Ves = tk.Button(ventana, text= "Consultar vestuario más utilizado", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "deep sky blue", font= ["helvetica", 15], command = lambda : Consultar_vestuario(Personas, vestuarios, ventana, Obj_menu, [Boton_Consulta_acc, Boton_Consulta_Ves, boton_regresar] )) 
    Boton_Consulta_Ves.grid(row= 5, column= 0)
    boton_regresar = tk.Button(ventana, text= "Regresar", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [Boton_Consulta_acc, Boton_Consulta_Ves, boton_regresar], 0 ,3)) 
    boton_regresar.grid(row = 8, column = 0)
    ventana.mainloop() 
    return

def validar_contrasena(Personas, vestuarios, ventana, Obj_menu, botones_anteriores, contrasena, comando): 
    """    Function that verify the user password, independently of which user was chosen ("Analista", or "Administrador").

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    ventana -- The graphical interface window.
    Obj_menu -- The "menu" object.
    botones_anteriores -- A list with the buttons that were used in the previous function. 
    contrasena -- A tk.Entry object where the password was typed.
    comando -- An integer (the identifier) that indicates which kind of user was selected.
    """
    Obj_menu.cerrar_botones(botones_anteriores)             #The "cerrar_botones" method is applied to the previous buttons
    Obj_menu.cerrar_texto()                                 #The "cerrar_texto" method is applied 
    if comando == 1 and contrasena.get()  == "admi123":   #If the password was correct, the respective function is called
        contrasena.destroy() 
        Administrador(Personas, vestuarios, ventana, Obj_menu)              
    elif comando == 2 and contrasena.get() == "ana456" :
        contrasena.destroy()  #Anyway, the tk.Entry object (in other words, the password) is destroyed
        Analista(Personas, vestuarios, ventana, Obj_menu)   
    else:
        contrasena.destroy()
        Ingresar_contrasena(Personas, vestuarios, False, comando, ventana, Obj_menu, botones_anteriores) #If the password was wrong, the "Ingresar_contrasena" function is called 
    return 

def Ingresar_contrasena(Personas, vestuarios, estado, comando, ventana, Obj_menu, botones_anteriores):
    """Function that allows the user to type his password. 

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    estado -- A boolean value that indicates if is the first time that the user is typing his password or if he typed a wrong password, so he is typing it again.
    comando -- An integer (the identifier) that indicates which kind of user was selected.
    ventana -- The graphical interface window.
    Obj_menu -- The "menu" object.
    botones_anteriores -- A list with the buttons that were used in the previous function. 
    """
    Obj_menu.cerrar_botones(botones_anteriores) #The "cerrar_botones" method is applied to the previous buttons
    Obj_menu.cerrar_texto()                     #The "cerrar_texto" method is applied 
    if estado == True:
        Obj_menu.set_texto("           Ingrese su contraseña:", 30, 2, "turquoise", "black", ["helvetica",15], 0, 0) 
    else:
        Obj_menu.set_texto("          Contraseña incorrecta,                 Vuelva a digitar su contraseña:", 30, 2, "turquoise", "black", ["helvetica",15], 0, 0)

    Obj_menu.set_titulo("Validar contraseña")
    contraseña = tk.Entry(ventana)
    contraseña.grid(row= 2, column= 0, pady= 2, ipadx= 103, ipady= 5)
    contraseña.config(show= "*")
    #If this button is pressed the function "Validar_contrasena" is called
    boton_continuar = tk.Button(ventana, text= "Continuar", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "turquoise", font= ["helvetica", 15], command = lambda : validar_contrasena(Personas, vestuarios, ventana, Obj_menu, [boton_continuar, boton_regresar], contraseña, comando))
    boton_continuar.grid(row = 5, column = 0)
    #If this button is pressed the function "regresar_usuario" is called 
    boton_regresar = tk.Button(ventana, text= "Regresar", cursor= "hand2",width= 30, height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda : regresar_usuario(Personas, vestuarios, ventana, Obj_menu, [boton_continuar, boton_regresar], contraseña ,3))
    boton_regresar.grid(row = 8, column = 0) 

    ventana.mainloop()
    return   

def regresar_usuario(Personas, vestuarios, ventana, Obj_menu, botones_anteriores, label, comando):
    """    Function that quit the previous: buttons, label or text, depending on an identifier. 
    Then, call an user's function ("Administrador" or "Analista"), call "login" function or return, depending on the received identifier. 

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    ventana -- The graphical interface window.
    Obj_menu -- The "menu" object.
    botones_anteriores -- A list with the buttons that were used in the previous function. 
    label -- The tk.Label object that will be destroyed, sometimes it could be a tk.Entry or an integer, depending on the received identifier.
    comando -- An integer (the identifier) that indicates which action will be performed.
    """
    Obj_menu.cerrar_botones(botones_anteriores) #Anyway the "cerrar_botones" method is applied to the previous buttons 
    if comando < 4:                             #Depending on the identifier the specific function is called
        Obj_menu.cerrar_texto()
        if comando == 1:
            Obj_menu.cerrar_label(label)   
            Administrador(Personas, vestuarios, ventana, Obj_menu) 
        elif comando == 2:
            if type(label) != int :
                Obj_menu.cerrar_label(label)  
            Analista(Personas, vestuarios, ventana, Obj_menu)
        else:
            if type(label) != int :
                label.destroy()
            login(Personas, vestuarios, ventana, Obj_menu)
    else:
        Obj_menu.cerrar_label(label)
        return

def salir(ventana, Obj_menu, botones_anteriores):
    """Function that finish the program, also shows a message about it and erases the file's information. 

    Keyword arguments:
    ventana -- The graphical interface window.
    Obj_menu -- The "menu" object.
    botones_anteriores -- A list with the buttons that were used in the previous function. 
    """
    archi = open("C:/Avatar App/Info_avatars.txt","w")  #the file's information is erased
    archi.writelines("")
    archi.close() 
    ventana.iconbitmap("C:/Avatar App/Imagenes/IconoE.ico") 
    Obj_menu.cerrar_botones(botones_anteriores)     #The "cerrar_botones" method is applied to the previous buttons
    Obj_menu.cerrar_texto()                         #The "cerrar_texto" method is applied
    Obj_menu.set_titulo("Salir")
    Obj_menu.set_fondo("black")
    Obj_menu.set_texto(" Desarrollado por: Harold Ramírez y Hugo Méndez ", 40, 1, "black", "cyan", ["times new roman",16], 4, 0)   

    caracter = "💡                                                                                💡"     #String that will be used to print the final message
    letras = [" ","¡", "H", "a", "s","t", "a", " ", "l", "u", "e", "g", "o", "!", "              ^_^ "]   #String that will be used to print the final message
    simbolos = []   #List that will contain three differents "tk.Text" objects that will be needed to print the final message.

    for x in range(0, 3):  #The three "tk.Text" objects are created and added to the "simbolos" list
        caracteres = tk.Text(ventana, width= 40, height= 1, bg= "black", fg= "cyan", font= ["times new roman", 16])
        if x == 0:
            caracteres.grid(row = 0, column = 0, padx = 3, pady= 3) 
        elif x == 1:
            caracteres.grid(row = 3, column = 0, padx = 3, pady= 3) 
        else:
            caracteres.grid(row = 5, column = 0, padx = 3, pady= 3)  
        caracteres.configure(state= "disabled") 
        simbolos.append(caracteres) 

    text = tk.Text(ventana, width= 13, height= 2, bg= "black", fg= "cyan", font= ["algerian",28]) #Another "tx.Text" object that will be used to print the final message
    text.grid(row = 1, column = 0, padx = 3, pady= 3)
    text.configure(state= "disabled")
    for l in range(0, len(letras)):  #The final message is printed 
        for j  in simbolos:
            j.configure(state= "normal")
            j.insert(tk.END, caracter)
            j.configure(state= "disabled")
        ventana.update()
        text.configure(state= "normal")
        text.insert(tk.END, letras[l])
        text.configure(state= "disabled")
        ventana.update()
        time.sleep(0.5)   #The system is interrupted throught the "sleep method" in order to give the impression of blinking
        for j in simbolos:
            j.configure(state= "normal")
            j.delete("1.0", tk.END)
            j.configure(state= "disabled")
        ventana.update() 
        time.sleep(0.5) 
    time.sleep(0.6)
    ventana.destroy()   #The graphical interface window is destroyed
    return  

def login(Personas, vestuarios, ventana, Obj_menu):
    """Function that allows select the kind of user in order to log in as that user. 

    Keyword arguments:
    Personas -- The list with "Persona" objects.
    vestuarios -- Dictionary that contains dictionaries, which ones, contain the: "Accesorios", "Ropa" and "Calzado" objects.
    ventana -- The graphical interface window.
    Obj_menu -- The "menu" object.
    """
    ventana.iconbitmap("C:/Avatar App/Imagenes/Icono.ico") 
    Obj_menu.set_titulo("LOGIN")
    Obj_menu.set_texto("       Seleccione el tipo de usuario", 30, 2, "turquoise", "black", ["helvetica",15], 0, 0)
    
    #If this button is pressed the function "Ingresar_contrasena" is called
    boton_admi = tk.Button(ventana, text= "Administrador", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "turquoise", font= ["helvetica", 15], command = lambda : Ingresar_contrasena(Personas, vestuarios, True, 1, ventana, Obj_menu, [boton_admi, boton_ana, boton_salir]))
    boton_admi.grid(row = 2, column = 0)
    
    #If this button is pressed the function "Ingresar_contrasena" is called
    boton_ana = tk.Button(ventana, text= "Analista", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "turquoise", font= ["helvetica", 15], command = lambda : Ingresar_contrasena(Personas, vestuarios, True, 2, ventana, Obj_menu, [boton_admi, boton_ana, boton_salir]))
    boton_ana.grid(row = 5, column = 0)
    
    #If this button is pressed the function "salir" is called
    boton_salir = tk.Button(ventana, text= "Salir", cursor= "hand2", width= 30, height= 1, bg= "black", fg = "firebrick1", font= ["helvetica", 15], command = lambda: salir(ventana, Obj_menu, [boton_admi, boton_ana, boton_salir])) 
    boton_salir.grid(row = 8, column = 0)
    ventana.mainloop()
    return

def Crea_personas_pordefecto():
    """Function that creates a initial quantity of persons."""
    vestuarios = Crea_vestuario()                                                             #The "Crea_Vestuario" function is called to store the dictionary that it returns, in a variable
    Personas = Crea_Personas(Crea_cedulas(10), Crea_provincias(), vestuarios ,Crea_genero())  #The "Crea_Personas" function is called and the list that it returns is saved in a variable (Personas)
    Grabar_informacion_avatars(Personas, False)                                               #The "Grabar_informacion_avatars" function is called to store the persons's information in the ".txt" file
    ventana = tk.Tk()                                              #The graphical interface window is created
    Obj_menu = menu(ventana)                                       #The "menu" object is instantiated for working on the window previusly created
    Obj_menu.set_fondo("grey30")                                #The "set_fondo" method is applied
    login(Personas, vestuarios, ventana, Obj_menu)          #"login" function is called
    return 
Crea_personas_pordefecto()  