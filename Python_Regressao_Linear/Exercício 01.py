"""
Exercício equação da reta y = a * x + b
"""
import numpy as np
import matplotlib.pyplot as plt
a = float(input("Entre com o coeficiente angular, a: "))
b = float(input("Entre com o intercepto, b: "))
x = np.linspace(-2, 2, 50)  # Faixa de valores de x
y = a * x + b  # construção da reta
txt = f"y ={a} * x + {b}"
plt.plot(x, y, c="b")
plt.text(x=-1.8, y=max(y)*.9, s=txt, c="b")
plt.text(x=-1.8, y=max(y)*.9, s=txt, c="b")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(y=0, color="k")  # Eixo x
plt.axvline(x=0, color="k")  # Eixo y
plt.grid(True)
plt.show()
