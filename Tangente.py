import math
angulo_g = float(input("Ingrese angulo: "))
angulo_rad = math.radians(angulo_g)
tangente = math.tan(angulo_rad)
print(f"La tangente de {angulo_g}° es: {tangente:.4f}")
