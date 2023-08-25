class Herramientas:
    def __init__(self,listaNumeros):
        self.lista=listaNumeros
    
    def Primo (self,num):
        esPrimo= False
        for n in range(2,num):
            if (num%2!=0) and (num%3!=0):
                esPrimo= True
            else:
                esPrimo= False
        return esPrimo

    def Repetidos(self,listaNum):
        caja=[]
        cantidad=[]
        caja[0]=listaNum[0]
        k=0
        r=0
        while n < len(listaNum):
            if listaNum[n]== caja[k]:
                cantidad.append(1)
                n+=0
            else:
                caja[k]=listaNum[n]
                n+=0
                k+=0
        print(listaNum)

    def Grados(self,valor,origen,destino):
        if (origen== "Celsius"):            #analizar segun destino celsius
            if (destino=="Kelvin"):       
                Kelvin= (valor + 273.15)        #conversion celsius a kelvin
                return Kelvin
            elif (destino=="Farenheit"):
                Farenheit=(valor * 9/5) + 32    #conversion de celsius a farenheit
                return Farenheit
            else:
                return valor                   #si no se dan las anteriores, se devuelve
    
        if (origen== "Kelvin"):            #analizar segun destino kelvin
            if (destino=="Celsius"):       
                Celsius= (valor - 273.15)        #conversion de kelvin a celsius
                return Celsius
            elif (destino=="Farenheit"):
                Farenheit=((valor - 273.15) * 9 / 5) + 32    #conversion de kelvin a farenheit
                return Farenheit
            else:
                return valor                   #si no se dan las anteriores, se devuelve
        if (origen== "Farenheit"):            #analizar segun destino farenheit
            if (destino=="Celsius"):       
                Celsius= (valor - 32) * 5 / 9        #conversion de farenheit a celsius
                return Celsius
            elif (destino=="Kelvin"):
                Farenheit=((valor - 32) * 5 / 9) + 273.15   #conversion de farenheit a kelvin
                return Farenheit
            else:
                return valor                   #si no se dan las anteriores, se devuelve

    def factorial(self,num):
        if (num-num !=0) or (type(num)==float):
            return ("numero incorrecto")
        else:
            if (numero > 1):
                numero = numero * num(numero - 1)
            return numero