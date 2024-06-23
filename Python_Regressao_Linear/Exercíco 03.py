import numpy as np
import matplotlib.pyplot as plt

# Ler dados do arquivo .csv | delimiter=',' informando que o delimitador é a virgula | skip_header=1 pula a 1ª linha.
dados = np.genfromtxt("Dados_descarbonizacao.csv", delimiter=',', skip_header=1)

x = dados[0:,:4]
y = dados[:,-1:]


x = np.hstack((np.ones((len(x), 1)), x))
betas, res, _, _ = np.linalg.lstsq(x, y, rcond=None)

y_predito = x @ betas
y_medio = np.mean(y)  # Calcula o valor medio de y


tss = sum((y - y_medio) ** 2)
rss = sum((y_predito -y) ** 2)
r_quadrado = 1 - (rss / tss)



id = np.arange(1, len(y)+ 1)

plt.title("Previsão das Emissões de Carbono em Regiões Urbanas")
plt.xlabel("Id das amostras")
plt.ylabel("Emissão de carbonos")
#""plt.legend("reais", y_predito)""
plt.scatter(id, y, c="b", label="Reais")
plt.scatter(id, y_predito, c="g", label="Estimados" )
plt.grid()
plt.show()

 
print(f"Intercepto, {betas[0]} ")
print(f"Coeficiente angular, {betas[1]} ")
print(f"R-quadrado, {r_quadrado}")
print(f"Residuo calculado:{rss} ")
