#Quizz
#adrian Cañon
#brayan Ladino
#andres Ramirez

#Entradas #Se pide al usuario que ingrese los datos necesarios para realizar los calculos
print("bienvenido  al protaforma de calculo de paneles solares")
import math
Consumo_anual = float(input("Ingrese el consumo anual de energía en KWh: ")) 
Eficiencia_Panel = float(input("Ingrese la eficiencia del panel solar: "))
Superficie_Panel = float(input("Ingrese la superficie del panel solar en m2: "))
Horas_sol = float(input("Ingrese las horas de sol al día: "))
Radiacion_solar = float(input("Ingrese la radiación solar en KWh/m2: "))


#Calculos #Se realizan los calculos necesarios para obtener los resultados pedidos
Eficiencia_Pane2 = Eficiencia_Panel / 100
potencia_diaria = Superficie_Panel * Radiacion_solar * Eficiencia_Pane2
potencia_anual = potencia_diaria * 365
Cantidad_paneles=math.ceil(Consumo_anual / potencia_anual) # se usa el math.ceil para redondear 
superficie_total = Cantidad_paneles * Superficie_Panel



#salidas #Se imprime los resultados de los calculos
print("La potencia diaria es: ", potencia_diaria, "KWh")
print("La potencia anual es: ", potencia_anual, "KWh")
print("La cantidad de paneles necesarios es: ", Cantidad_paneles)