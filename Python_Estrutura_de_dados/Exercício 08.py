"""
[Opcional] Tente melhorar os resultados obtidos na classificação
dos dígitos manuscritos. Faça isso estudando as funções que
treinam os modelos e teste com combinações diferentes dos
parâmetros de treinamento. Note que modelos treinados por
Convolutional Neural Networks chegam a acurácias acima de 99%.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix


# Carregar os dados do arquivo CSV
df_train = pd.read_csv("mnist_train_small.csv", header=None)
df_test = pd.read_csv("mnist_test.csv", header= None)

# Dividir os dados em features (X) e rótulos(y)
X_train = df_train.iloc[:, 1:]
y_train = df_train.iloc[:, 0]
X_test = df_test.iloc[:, 1:]
y_test = df_test.iloc[:, 0]

# Treinamento do modulo de árvore de decisão (clf: Classifier)
tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train, y_train)

# Fazer previsões nos dados de teste
tree_predictions = tree_clf.predict(X_test)

# Avaliar o desempenho do modelo de árvore de decisão
tree_accuracy = accuracy_score(y_test, tree_predictions)
print("Árvore de Decisão - Acurácia", tree_predictions)
print("Relatório de Classificação: ")
print(classification_report(y_test, tree_predictions))
print("Matriz de Confusão: ")
print(confusion_matrix(y_test, tree_predictions))