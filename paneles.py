"quiz 1"
print("bienvenido  al proframa de calculo de paneles solares")
import math
consumoenergia = float(input("ingrese el consumo de energia en kWh: "))
horas = float(input("ingrese el numero de horas de sol: "))
eficiencia = float(input("ingrese la eficiencia del panel: "))
efinciencia1 = eficiencia/100
anchopanel = float(input("ingrese el ancho del panel: "))
largopanel = float(input("ingrese el largo del panel: "))
areapanel = anchopanel*largopanel
print(f"el area del panel es: {areapanel} m^2")
radiacionpromedio=float(input("ingrese la radiacion promedio por metro cuadrado: "))
potenciadia=areapanel*radiacionpromedio*efinciencia1
print(f"la potencia diaria del panel es: {potenciadia} kWh")
potenciaño=potenciadia*365
print(f"la potencia anual del panel es: {potenciaño} kWh")
numpaneles=math.ceil(consumoenergia/potenciaño)
print(f"el numero de paneles necesarios es: {numpaneles}")
