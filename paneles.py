#Quizz

#Entradas
print("bienvenido  al proframa de calculo de paneles solares")
import math
Consumo_anual = float(input("Ingrese el consumo anual de energía en KWh: "))
Eficiencia_Panel = float(input("Ingrese la eficiencia del panel solar: "))
Superficie_Panel = float(input("Ingrese la superficie del panel solar en m2: "))
Horas_sol = float(input("Ingrese las horas de sol al día: "))
Radiacion_solar = float(input("Ingrese la radiación solar en KWh/m2: "))


#Calculos
potencia_diaria = Superficie_Panel * Radiacion_solar * Eficiencia_Panel
potencia_anual = potencia_diaria * 365
Cantidad_paneles = Consumo_anual / potencia_anual
superficie_total = Cantidad_paneles * Superficie_Panel

