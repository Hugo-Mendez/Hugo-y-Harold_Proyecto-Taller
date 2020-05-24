def login():
    comando = 0
    while comando < 4 :
        print("\n*********************************************************")
        print("*                                                       *") 
        print("* Digite:  1      para: ingresar como Administrador     *")   
        print("* Digite:  2      para: ingresar como Analista          *")
        print("* Digite:  3      para: ingresar como Usuario           *") 
        print("* Digite: #>3:    para Salir                            *")  
        print("*                                                       *")  
        print("*********************************************************\n")
        comando=int(input("Digite un numero correspondiente: "))
        if comando < 4 :
            if comando == 1 :
                print("\nEsta en usuario Administrador")
            elif comando == 2 :
                print("\nEsta en usuario Analista")
            elif comando == 3 :
                print("\nEsta en usuario Usuario")
        else :
            print("Chao")
login()    