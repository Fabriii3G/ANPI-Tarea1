import sympy as sp 
import matplotlib.pyplot as plt
import numpy as np

#En este caso se hace el análisis completo de una función real utilizando la librería sympy, dominio real, intersecciones con los ejes coordenados, asintotas, derivadas f'(x) y f''(x), monotonía y concavidad.

x= sp.Symbol('x')
funcion = (x**3-3*x**2+3*x-1)/(x**2-2*x)

#Dominio Real 
denominador = sp.denom(funcion) 
restricciones = sp.solve(denominador, x)
dominio = f"R - {{ {', '.join(map(str, restricciones))} }}"
print(f"El dominio de la función es: {dominio}")


#Intersecciones con los ejes coordenados 
interseccion_x= sp.solve(funcion,x)
print("intersección con el eje x:", (interseccion_x,0))

interseccion_y= funcion.subs(x,0)
print("No hay intersecciones con el eje y", interseccion_y)


#Asíntotas 
#horizontales 
limite_infinito_pos=sp.limit(funcion,x,sp.oo) 
print("El límite cuando x tiende a infinito =",limite_infinito_pos, "por lo que no posee asintota horizontal en +∞")
limite_infinito_neg= sp.limit(funcion,x,-sp.oo) 
print("El límite cuando x tiende a menos infinito =",limite_infinito_neg,"por lo que no posee asintota horizontal en -∞")

#Oblicuas
m = sp.limit(funcion/x, x, sp.oo)
b = sp.limit(funcion - m*x, x, sp.oo)
print("Asíntota oblicua en +∞ y =",m,"x +",b)
m2 = sp.limit(funcion/x, x, -sp.oo)
b2 = sp.limit(funcion - m2*x, x, sp.oo)
print("Asíntota oblicua en -∞ y =",m2,"x +",b2)

#Verticales
asintotas_verticales = [p for p in restricciones if sp.limit(funcion, x, p, dir="+") == sp.oo or sp.limit(funcion, x, p, dir="-") == -sp.oo]
asintotas_str = f"x = {asintotas_verticales[0]} y x = {asintotas_verticales[1]}" 
print(f"Asintotas verticales en: {asintotas_str}")

#Derivadas de la función 
primera_derivada= sp.diff(funcion, x)
print("Primera derivada",primera_derivada)

segunda_derivada= sp.diff(funcion,x,2)
print("Segunda derivada:", segunda_derivada)

#Gráfica de las funciones f(x), f'(x) y f''(x)
grafica_funcion= sp.lambdify(x,funcion, 'numpy')
grafica_primer_deriv= sp.lambdify(x, primera_derivada, 'numpy')
grafica_segunda_deriv= sp.lambdify(x,segunda_derivada, 'numpy')

#Configuración de la ventana para graficar f(x) y sus derivadas 
x_vals = np.linspace(-10, 10, 400)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, grafica_funcion(x_vals), label='f(x)', color= 'blue')
plt.plot(x_vals, grafica_primer_deriv(x_vals), label="f'(x)", color= 'red')
plt.plot(x_vals, grafica_segunda_deriv(x_vals), label="f''(x)", color= 'green')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-10, 10)  
plt.ylim(-20, 20)  
plt.title("Análisis de f(x) y sus derivadas")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#Intervalos de monotonía
Decreciente= sp.solve_univariate_inequality(primera_derivada < 0, x)
print("Intervalos donde la función es decreciente:", Decreciente)

Creciente= sp.solve_univariate_inequality(primera_derivada > 0, x)
print("Intervalos donde la función es creciente:", Creciente)

#Intervalos de Concavidad 
Concava_abajo= sp.solve_univariate_inequality(segunda_derivada < 0, x)
print("Intervalos donde la función es concava hacia abajo:", Concava_abajo)

Concava_arriba= sp.solve_univariate_inequality(segunda_derivada > 0, x)
print("Intervalos donde la función es concava hacia arriba:", Concava_arriba)