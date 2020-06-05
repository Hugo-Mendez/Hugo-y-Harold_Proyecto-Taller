
#Authors: Hugo Méndez and Harold Ramírez
#Date: May 24th 2020

import random
from datetime import date

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
    return provincias

def Crea_accesorios():
    """Function that creates a dictionary which stores the accessories, then returns the dictionary."""
    accesorios = {1: "Lentes  ", 2: "Aretes  ", 3: "Piercing", 4: "Ninguno "}
    return accesorios

def Crea_genero():
    """Function that creates a dictionary which stores the two possible genres (female or male), then returns the dictionary."""
    genero = {1: "Femenino ", 2: "Masculino"}
    return  genero

def Crea_color_piel():
    """Function that creates a dictionary which stores diferent skin colors (just five, in this case), then returns the dictionary."""
    colorpiel = {1: "Negra ", 2: "Marrón", 3: "Morena", 4: "Clara ", 5: "Blanca"}
    return colorpiel

def Crea_rostro():
    """Function that creates a dictionary which stores diferent face shapes (just six, in this case), then returns the dictionary."""
    rostro = {1: "Redondo    ", 2: "Alargado   ", 3: "Corazón    ", 4: "Cuadrado   ", 5: "Ovalado    ", 6: "Rectangular"}
    return rostro

def Crea_emociones():
    """Function that creates a dictionary which stores diferent expressions (just eight, in this case), then returns the dictionary."""
    emociones = {1: "Enfado   ", 2: "Desprecio", 3: "Disgusto ", 4: "Miedo    ", 5: "Sorpresa ", 6: "Alegría  ", 7: "Neutral  ", 8: "Tristeza "}
    return emociones

def Crea_Atributos_Cabello():
    """    Function that creates a dictionary (with three dictionaries inside).
    These dictionaries stores diferent hair attributes (such as: color, density or texture), then returns the dictionary.
    """
    Atr_cabello = {1: {1:"Negro    ", 2:"Rubio    ", 3:"Café     ", 4:"Castaño  ", 5:"Gris     ", 6:"Invisible"},
                   2: {1:"Escaso   ", 2:"Moderado ", 3:"Abundante"}, 3: {1:"Lacio   ", 2:"Ondulado", 3:"Rizado  "}}
    return Atr_cabello

def Crea_Atributos_Ojos():
    """    Function that creates a dictionary (with two dictionaries inside).
    Both dictionaries stores diferent eye characteristics (the first one stores shapes and the second one stores colors).
    After, returns the dictionary.
    """
    Atr_ojos = {1: {1: "Almendrados", 2: "Separados  ", 3: "Redondos   ", 4: "Caídos     ", 5: "Saltones   ", 6: "Juntos     ", 7: "Profundos  ", 8: "Asiáticos  "},
                2: {1: "Negro   ", 2: "Castaño ", 3: "Ámbar   ", 4: "Avellana", 5: "Verde   ", 6: "Azul    ", 7: "Gris    "}}       
    return Atr_ojos

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

def Crea_Personas(cedulas,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
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
        dic_persona = {1: cedulas[random.randint(1,len(cedulas))], 2: provincias[random.randint(1,len(provincias))], 3: accesorios[random.randint(1,len(accesorios))],
                       4: genero[random.randint(1,len(genero))], 5: colores_de_piel[random.randint(1,len(colores_de_piel))],
                       6: rostro[random.randint(1,len(rostro))], 7: emociones[random.randint(1,len(emociones))],
                       8: atri_cabello[1][random.randint(1,6)], 9: atri_cabello[2][random.randint(1,3)],
                       10: atri_cabello[3][random.randint(1,3)], 11: atri_ojos[1][random.randint(1,8)], 
                       12: atri_ojos[2][random.randint(1,7)], 13: Edad_Años} #The attributes are randomly selected and saved in a dictionary
        Lista_Personas.append(dic_persona) #It is appended each dictionary to the person's list
    return Lista_Personas

def Crear_Persona_Auto(Personas,nueva_cedula,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
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
    dic_persona = {1: nueva_cedula[1], 2: provincias[random.randint(1,len(provincias))], 3: accesorios[random.randint(1,len(accesorios))],
                   4: genero[random.randint(1,len(genero))], 5: colores_de_piel[random.randint(1,len(colores_de_piel))],
                   6: rostro[random.randint(1,len(rostro))], 7: emociones[random.randint(1,len(emociones))],
                   8: atri_cabello[1][random.randint(1,6)], 9: atri_cabello[2][random.randint(1,3)],
                   10: atri_cabello[3][random.randint(1,3)], 11: atri_ojos[1][random.randint(1,8)], 
                   12: atri_ojos[2][random.randint(1,7)], 13: Edad_Años}  #The attributes are randomly selected and saved in a dictionary
    Personas.append(dic_persona)                                          #The dictionary is appended to the person's list
    print("\nPersona creada y agregada a la lista satisfactoriamente")
    return Personas

def Crear_Persona_Manual(Personas,nueva_cedula,provincias,accesorios,genero,colores_de_piel,rostro,emociones,atri_cabello,atri_ojos):
    """    Function that creates a person and add him to the list of persons, after that, returns the list. 
    The attributes of this person are selected by the administrator user.

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
    print("\nPara crear una persona manualmente por favor indica cada uno de los siguientes atributos:")

    print("\nIngrese su fecha de nacimiento, en formato dd(1-30)/mm(1-12)/aaaa(1920-2019)")
    dia = 0
    mes = 0
    año = 0
    while dia not in range(1, 31) or mes not in range(1,13) or año not in range(1920, 2020):
        dia = int(input("\nIngrese el día de nacimiento: ")) #The administrator types the new person's date of birth
        mes = int(input("\nIngrese el mes de nacimiento: "))
        año = int(input("\nIngrese el año de nacimiento: "))
        if dia not in range(1, 31) or mes not in range(1,13) or año not in range(1920, 2020): 
            print("\nError: día, mes o año fuera del rango establecido") #If the date isn't in range, the administrator should type it again
    fecha_naci = {1: dia, 2: mes, 3: año} #The day, month and year are saved in a dictionary, in that order 

    F_rostro = 0
    while F_rostro not in range(1,7): #There is a menu for each attribute
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
        print("****************************************\n") #The administrator selects the option that he wants
        F_rostro = int(input("Digite un número correspondiente con el menú: ")) 
        if F_rostro not in range(1,7):
            print("\nDigito incorrecto, por favor digite un número correspondiente con el menú.") 
    
    Color_piel = 0
    while Color_piel not in range(1,6): #The same way for the next menus
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
    
    Edad_Años = Calcula_Edad(fecha_naci)  #The function "Calcula_Edad" is called to calculate the person's age
    dic_persona = {1: nueva_cedula[1], 2: provincias[provincia], 3: accesorios[accesorio],
                   4: genero[Genero], 5: colores_de_piel[Color_piel],
                   6: rostro[F_rostro], 7: emociones[emocion],
                   8: atri_cabello[1][color_cabello], 9: atri_cabello[2][densidad_cabello],
                   10: atri_cabello[3][textura_cabello], 11: atri_ojos[1][Forma_ojos], 
                   12: atri_ojos[2][Color_ojos], 13: Edad_Años}  #It is created a dictionary with each attribute, previously selected by the administrator                                       
    Personas.append(dic_persona)                                 #The dictionary is appended to the person's list
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
            Personas = Crear_Persona_Auto(Personas,Crea_cedulas(1),Crea_provincias(),Crea_accesorios(),Crea_genero(),Crea_color_piel(),Crea_rostro(),Crea_emociones(),Crea_Atributos_Cabello(),Crea_Atributos_Ojos())
        elif comando == 2:                                                     #Option number 2: Create a person manually
            Personas = Crear_Persona_Manual(Personas,Crea_cedulas(1),Crea_provincias(),Crea_accesorios(),Crea_genero(),Crea_color_piel(),Crea_rostro(),Crea_emociones(),Crea_Atributos_Cabello(),Crea_Atributos_Ojos())
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
    provincia -- An specific province indicated.
    """
    Grupos_Etarios = {1: "Bebés          " , 2: "Niños          ", 3: "Adolescentes   ", 4: "Adultos        ", 5: "Adultos mayores"}
    Grupo_Etario = 0                     #Quantity of persons from the province and age group, previously stablished
    for i in range(0, (len(Personas))):  #The list of persons is toured, looking for those persons
        if Personas[i][2] == provincia and Personas[i][13] < Rango_edades[comando] and Personas[i][13] > Rango_edades[comando -1]:
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
    Rango_edades = {0: 0, 1: 4, 2: 12, 3: 18, 4: 60, 5: 99}        #Dictionary that contains the limits for belong to an specific age group.
    print("\n _________________________________________________")
    print("|     Estadística por provincia en Costa Rica     |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for e in range(1,(len(Provincias)+1)):     #For each province the list of persons will be toured.
        print("\n ___________")
        print("|",Provincias[e])
        print(" ¯¯¯¯¯¯¯¯¯¯¯")
        PersonasProvi = 0                      #Quantity of persons per province.
        contador = 1                           #Number that represents an specific age group(since babies to older adults).
        while contador < len(Rango_edades):    #For each age group, the function "Cuenta_Grupos_Etarios" is called.
            Cuenta_Grupos_Etarios(Rango_edades, contador, Personas, Provincias[e])
            for i in range(0, (len(Personas))):         #The list of persons is toured.
                if Personas[i][2] == Provincias[e]:     #If someone from that province and that age group is found, his imformation is printed. 
                    if Personas[i][13] < Rango_edades[contador] and Personas[i][13] > Rango_edades[contador -1]:       
                        print(" ___________________________________________________________________________ ")
                        print("| Cédula        | Edad     | Provincia      | Género        | Emoción       |")
                        if Personas[i][13] < 10:
                            print("|", Personas[i][1],"    |",str(Personas[i][13])+" ","      |",Personas[i][2],"    |", Personas[i][4],"    |",Personas[i][7],"    |")
                        else:
                            print("|", Personas[i][1],"    |",Personas[i][13],"      |",Personas[i][2],"    |", Personas[i][4],"    |",Personas[i][7],"    |")
                        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")    
                        print("|___________________________________________________________________________|")
                        print("| Color de piel   | Forma del rostro   | Forma de ojos   | Color de ojos    |")
                        print("|", Personas[i][5],"         |",Personas[i][6],"       |",Personas[i][11],"    |",Personas[i][12],"        |")
                        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
                        print("|___________________________________________________________________________|")
                        print("| Color cabello     | Densidad cabello    | Textura cabello    | Accesorio  |")
                        print("|", Personas[i][8], "        |", Personas[i][9], "          |", Personas[i][10], "          |", Personas[i][3],"  |")
                        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                        print("---------------------------------------------------------------------------------")
                        PersonasProvi += 1                                     #The quantity of persons from that province increases.
            contador += 1                                                      #The "contador" increases, looking for the next age group.
        print("\nTotal de personas en ",Provincias[e],":",PersonasProvi,"\n")  #The quantity of persons for each province is printed.
        print("---------------------------------------------------------------------------------")
    return

def Informes_Grupos_Etarios(Personas):
    """    Function that shows the statistics per age group in Costa Rica.

    Keyword arguments:
    Personas -- The list with persons.
    """
    Grupos_Etarios = {1: "Bebés          " , 2: "Niños          ", 3: "Adolescentes   ", 4: "Adultos        ", 5: "Adultos mayores"}
    Rango_edades = {0: 0, 1: 4, 2: 12, 3: 18, 4: 60, 5: 99}       #Dictionary that contains the limits for belong to an specific age group.
    print("\n ____________________________________________________")
    print("|     Estadística por grupo etario en Costa Rica     |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for i in range(1, len(Rango_edades)):    #For each age group the list of persons will be toured.
        Total_etarios = 0                    #Quantity of persons per age group.
        for j in range(0, len(Personas)):    #The list of persons is toured.
            if Personas[j][13] < Rango_edades[i] and Personas[j][13] > Rango_edades[i-1]: 
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
            if Personas[j][7] == Emociones[i]:
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
    print("             |",Emociones[Lista_Claves_Ordenadas[0]],"|",Emociones[Lista_Claves_Ordenadas[1]],"|",Emociones[Lista_Claves_Ordenadas[2]],"|",
          Emociones[Lista_Claves_Ordenadas[3]],"|",Emociones[Lista_Claves_Ordenadas[4]],"|",Emociones[Lista_Claves_Ordenadas[5]],"|",
          Emociones[Lista_Claves_Ordenadas[6]],"|",Emociones[Lista_Claves_Ordenadas[7]],"|")
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

def Impresion_Datos_Usuario(usuario,mensaje):
    """Function that shows the "Usuario" user's personal information.

    Keyword arguments:
    usuario -- Dictionary that contains all the information (attributes) of the selected user.
    mensaje -- String with a message that is wished to print.
    """
    #The message and "Usuario" user's personal information are printed.
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
    """Allows to the "Usuario" user modify his emotion.

    Keyword arguments:
    usuario -- Dictionary that contains all the information (attributes) of the selected user.
    emociones -- Dictionary that contains the emotions.
    """
    emocion = 0
    while emocion not in range(1,9):                  #There is a menu, where the "Usuario" can select the emotion that he wants.
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
    usuario[7] = emociones[emocion]                                        #The previous emotion is replaced by the chosen emotion.
    Impresion_Datos_Usuario(usuario,"Ahora esta es su nueva información")  #The "Impresion_Datos_Usuario" function is called.
    return 

def Modificar_provincia(usuario, provincias):
    """Allows to the "Usuario" user modify his province.

    Keyword arguments:
    usuario -- Dictionary that contains all the information (attributes) of the selected user.
    provincias -- Dictionary that contains the provinces.
    """
    provincia = 0
    while provincia not in range(1,8):       #There is a menu, where the "Usuario" can select the province that he wants.
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
    usuario[2] = provincias[provincia]                                    #The previous province is replaced by the chosen province.
    Impresion_Datos_Usuario(usuario,"Ahora esta es su nueva información") #The "Impresion_Datos_Usuario" function is called.
    return

def Usuario(Personas,emociones,provincias):
    """    Is the "Usuario" user's function, it allows him to modify his province and emotion.
    The "Usuario" user can do this process as many times as he wants.

    Keyword arguments:
    Personas -- The list with persons.
    emociones -- Dictionary that contains the emotions.
    provincias -- Dictionary that contains the provinces.
    """
    usuario = random.choice(Personas)   #The user is randomly selected from the persons's list.
    comando = 0
    Impresion_Datos_Usuario(usuario,"Esta es su información actual     ")   #The "Impresion_Datos_Usuario" function is called.
    while comando < 3:                              #There is a menu, where the "Usuario" can select the option that he wants.
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
        if comando == 1:                                       #Option number 1: Modify his emotion.
            Modificar_emocion(usuario,emociones)
        elif comando == 2:                                     #Option number 2: Modify his province.
            Modificar_provincia(usuario,provincias)
    return Personas

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

    else :
        while contraseña != "usu789" :  #If the typed password was incorrect, the user has to type it again or return to the menu
            contraseña = input("\nContraseña incorrecta: vuelva a digitar su contraseña o digite: 0 para regresar ")
            if contraseña == "0" :
                return
        print("\nIngresó como Usuario")
        Usuario(Personas,  Crea_emociones(), Crea_provincias()) #If the typed password was correct, the "Usuario" function is called
    return 

def login():
    """Is the main function, allows select as which user login."""
    comando = 0
    #The "Crea_Personas" function is called and the list that it returns is saved in a variable (Personas).
    Personas = Crea_Personas(Crea_cedulas(100), Crea_provincias(), Crea_accesorios(),Crea_genero(), Crea_color_piel(), Crea_rostro(), Crea_emociones(),Crea_Atributos_Cabello(), Crea_Atributos_Ojos())
    while comando < 4 :
        print("\n*******************************************************")
        print("*                                                     *")  #There is a menu for select as which user login
        print("* Digite:  1     para ingresar como Administrador     *")
        print("* Digite:  2     para ingresar como Analista          *")
        print("* Digite:  3     para ingresar como Usuario           *")
        print("* Digite: #>3    para salir                           *")
        print("*                                                     *")
        print("*******************************************************\n")
        comando=int(input("Digite un número correspondiente con el menú: "))
        if comando < 4 :
            contraseña = input("\nDigite su contraseña: ")    #The password is typed, even if it's incorrect
            validar_contraseña(contraseña,comando,Personas)   #The "validar_contraseña" function is called
        else :
            print("\n********************\n*   Hasta luego!   *\n********************")
            return
login()