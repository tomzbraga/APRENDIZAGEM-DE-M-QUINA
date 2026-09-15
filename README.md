# APRENDIZAGEM-DE-MAQUINA

4. PARTE II – CASO REAL
Uma empresa de comércio eletrônico possui dados históricos de clientes e vendas e identificou quatro necessidades:

A – Previsão de vendas
Prever o valor de uma venda usando apenas o número de produtos adquiridos.
Pergunta: Qual modelo é mais adequado? Justifique.

RESPOSTA: 

O modelo mais adequado é a Regressão Linear Simples, pois a situação descrita contém uma variável dependente (o valor da venda) subordinada à apenas uma variável independente (número de produtos adquiridos). O valor da compra é a variável alvo e seu valor é contínuo, porém depende da quantidade de produtos adquiridos.

B – Previsão com várias informações
Prever o valor de uma venda usando quantidade de produtos, valor médio, visitas, tempo de permanência e compras
anteriores.
Pergunta: Qual modelo é mais adequado? Explique.

RESPOSTA: 

O modelo mais adequado é a Regressão Linear Múltipla, pois há várias variáveis independentes influenciando no valor da variável alvo, que é contínua. Esse modelo isola o efeito de cada uma sobre o valor da venda, mantendo as demais constantes

C – Compra ou não compra
Prever se o cliente comprará: 1 = sim; 0 = não.
Pergunta: Qual técnica é mais adequada? Explique por que é classificação binária.

RESPOSTA: 

A técnica mais adequada é a Regressão Logística, pois a sua variável dependente é categórica. Seu resultado depende de coeficientes que se relacionam com a razão de chances. A questão expõe uma classificação binária, pois há apenas 2 resultados possíveis (0 ou 1).

D – Clientes semelhantes
Classificar um novo cliente com base em clientes anteriores semelhantes.
Pergunta: Qual técnica pode ser usada? Explique como a proximidade participa da decisão.

RESPOSTA: 

A técnica a ser utilizada é o KNN (K-Nearest Neighbors). Após escolher o valor de K, o algoritmo calcula a distância entre o novo cliente e todos os clientes já classificados, com base nas características relevantes. Os K clientes mais próximos são selecionados, e a classificação do novo cliente é definida pela classe mais frequente entre esses vizinhos (votação da maioria). Assim, a proximidade determina quais exemplos passados têm influência na decisão — quanto mais parecido o cliente for de um grupo, maior o peso desse grupo na previsão
