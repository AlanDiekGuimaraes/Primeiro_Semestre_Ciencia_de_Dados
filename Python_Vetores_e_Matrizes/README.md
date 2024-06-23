# Meus exercícios Python CST em Ciência de Dados


01 - Crie uma função, mult(v, N), que recebe um vetor v e um número N e retorna cada elemento do vetor multiplicado por esse número.

02 - Implemente a função dot(v1, v2) que retorna o produto escalar dos vetores v1 e v2. Cheque em sua implementação que os vetores tenham o mesmo tamanho.

03 - Implemente a função transp(mat) que recebe uma matriz mat e retorna sua transposta.

04 - Crie um vetor numpy com os números pares de 1 a 20. Dica: use np.arange().

05 - Crie uma matriz numpy 3x3 com valores aleatórios entre 0 e 10. Dica: use np.random.rand().

06 - Multiplique todos os elementos de um vetor por 2. Use broadcasting para evitar loop.
Exemplo: Seja `vetor = np.array([1, 2, 3, 4])`. O resultado esperado: `array([2, 4, 6, 8]).

07 - Calcule a soma cumulativa de um vetor. Dica: usar np.cumsum()
Exemplo: Seja `vetor = np.array([1, 2, 3, 4])`, o resultado seria `array([ 1, 3, 6, 10]).

08 - Transponha uma matriz.
Exemplo: Seja `matriz = np.array([[1, 2], [3, 4], [5, 6]])`, o resultado seria `array([[1, 3, 5], [2, 4, 6]]).

09 - Converta uma matriz em um vetor unidimensional.
Exemplo: Seja `matriz = np.array([[1, 2, 3], [4, 5, 6]])`, o resultado seria `array([1, 2, 3, 4, 5, 6]).

10 - Multiplicação matricial: multiplique uma matriz (𝑚 × 𝑛) por um vetor (𝑛 × 1).
Exemplo: Seja `matriz = np.array([[1, 2], [3, 4]])` e `vetor = np.array([[5], [6]]),
o resultado seria `array([[17], [39]]).

11 - Encontre os índices dos valores máximos em cada linha de uma matriz.
Dica: use np.argmax(). Exemplo: Seja `matriz = np.array([[1, 9, 6], [8, 2, 3], [4, 7, 5]])`,
o resultado seria `array([1, 0, 1]).

12 - Calcule a raiz quadrada de todos os elementos de um vetor.
Exemplo: Seja `vetor = np.array([4, 9, 16, 25])`, o resultado seria `array([2., 3., 4., 5.]).

13 - Substitua todos os valores negativos em um vetor por 0. Exemplo: Seja `vetor = np.array([-1, 2, -3, 4, -5])`,
o resultado seria `array([0, 2, 0, 4, 0]).

14 - Reshape um vetor unidimensional em uma matriz 3x3. Exemplo: Seja `vetor =
np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])`, o resultado seria `array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).

15 - Adicione um valor constante a todos os elementos de um vetor.
Exemplo: Seja `vetor = np.array([1, 2, 3, 4])` e `constante = 5`, o resultado seria array([6, 7, 8, 9]).

16 - Determine uma constante que ao multiplicar todos os elementos de uma matriz por
essa constante, a soma dos elementos da matriz resultante será 1. Não usar loops.
Exemplo: Seja `matriz = np.array([[1, 2], [3, 4]])`, o resultado seria `array([[0.1, 0.2], [0.3,
0.4]])`, pois 0.1+0.2+0.3+0.4 = 1.

17 - Gere uma matriz identidade 3x3. Dica: use np.eye().

18 - Concatene duas matrizes horizontalmente. Dica: use np.hstack()
Exemplo: matriz_1 = ([1,2,3],[4,5,6]) matriz_2([7,8,9],[10,11,12])
Matriz concatenada [[1,2,3,7,8,9],[4,5,6,10,11,12]].

19 - Encontre o produto escalar entre os vetores [1, 2, 3] e [4, 5, 6]. Dica: use np.dot() e
também o operador @ para conferir o outro resultado.

20 - Calcule a média e o desvio padrão de cada linha de uma matriz. Dica: use np.mean() e
np.std(). Exemplo: `matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`. O resultado deve ser:
média por linha: [2. 5. 8.], desvio padrão por linha: [0.8165, 0.8165, 0.8165].

21 - Calcule a média e o desvio padrão de cada coluna de uma matriz. Dica: use np.mean()
e np.std(). Exemplo: matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). O resultado deve ser:
média por coluna: [4. 5. 6.], desvio padrão por coluna: [2.4495, 2.4495, 2.4495].

22 - Calcule a média de cada coluna de uma matriz e as subtraia das respectivas colunas.
Exemplo: Seja `matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, o resultado seria
array([[-3., -3., -3.], [ 0., 0., 0.], [ 3., 3., 3.]])`. Use broadcasting para evitar loops.

23 - Calcule a média de cada linha de uma matriz e as subtraia das respectivas linhas.
Exemplo: Seja `matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, o resultado seria
array([[-1., 0., 1.], [-1., 0., 1.], [-1., 0., 1.]])`. Use broadcasting para evitar loops.

24 - Uma operação comum em ciência de dados ou aprendizado de máquina é a normalização dos dados. Os
dados estão dispostos em uma matriz e cada característica de interesse ao longo das colunas. Por exemplo,
uma matriz em que cada linha corresponde a uma pessoa, teremos a coluna das idades, a coluna das
alturas, a coluna da renda mensal, etc. A normalização consiste em, para cada ponto na matriz, subtrair a
média da coluna e dividir pelo desvio padrão da respectiva coluna.
Normalize os dados da seguinte matriz X, onde cada linha corresponde a uma amostra (e.g. pessoa) e cada
coluna corresponde a uma característica dela. Para normalizar os dados, você pode usar broadcasting para
subtrair a média de cada coluna e dividir pelo desvio padrão, evitando a necessidade de loops explícitos.
Dica: use os métodos mean(), std() para os cálculos da média e desvio padrão, respectivamente.

25 - Encontre a solução para o seguinte problema. Arredondar todos os valores em uma
matriz para o inteiro mais próximo. Dica: analise np.floor(), np.ceil(), np.fix() e np.round()
Exemplo:

26 - Dada a matriz A, encontre sua inversa A
−1
Então, comprove que A A
−1 = I, onde I é
a matriz identidade, com elementos da diagonal unitários e o restante zero.

27 - Suponha que você seja um corretor imobiliário e deseja prever o preço de uma casa com base em diferentes
características, como área construída, número de quartos, número de banheiros e idade da casa. Você coletou
dados de venda de casas nos últimos seis meses e registrou essas características para cada venda.
Os dados coletados estão disponíveis na forma de uma matriz, onde cada linha representa uma casa vendida e
cada coluna representa uma característica. Além disso, você tem um vetor com os preços de venda
correspondentes das casas.
Tarefa:
Encontrar os coeficientes ideais que relacionam as características das casas com
os preços de venda. Em seguida, preveja o preço de uma nova casa com as
 seguintes características:
• Área construída: 180 metros quadrados
• Número de quartos: 3
• Número de banheiros: 2
• Idade da casa: 10 anos
(Resposta: 355000).
