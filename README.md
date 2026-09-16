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

5. PARTE III – ANÁLISE E SELEÇÃO 

1. Classifique as quatro situações como regressão ou classificação e justifique. 

RESPOSTA:

A - Previsão de vendas: Regressão, pois a variável-alvo a ser prevista é quantitativa e contínua.

B - Previsão com várias informações: Regressão, pois a variável-alvo a ser prevista é quantitativa e contínua.

C - Compra ou não compra: Classificação, pois a variável-alvo é categórica, discreta e binária (1 sim, 0 não)

D - Clientes semelhantes: Classificação, pois o objetivo é determinar a qual grupo ou categoria discreta um novo cliente pertence, com base nos perfis já existentes.

2. Indique o modelo mais adequado para cada situação. 

RESPOSTA:

Já resolvida na parte II da atividade, mas aqui está a solução novamente

Situação A: Regressão Linear Simples.  
Situação B: Regressão Linear Múltipla.  
Situação C: Regressão Logística.  
Situação D: KNN (K-Nearest Neighbors)

3. Explique por que pelo menos um dos outros modelos seria menos adequado em cada situação.

RESPOSTA:

A - Não seria possível utilizar Regressão Logística, pois ela não serve diretamente para estimar um valor contínuo monetário em uma reta de tendência.

B - A regressão linear simples não é adequada, pois aceita apenas uma variável indepentende.

C - A regressão linear simples não seria adequada, pois ela pode prever valores numéricos fora do intervalo definido (binário).

D - Regressão Logística pode ser menos adequada do que o KNN quando a fronteira de decisão entre os grupos de clientes é altamente complexa ou não linear, já que o KNN se adapta localmente à geometria dos dados por proximidade.

4. Se novas variáveis forem acrescentadas à Situação A, isso necessariamente transforma o problema em regressão linear múltipla? Explique. 

RESPOSTA:

Sim, se novas variáveis forem utilizadas para prever a mesma variável-alvo a situação se tornaria uma Regressão Linear Múltipla.

5. Na Situação C, por que não basta usar regressão linear e arredondar o resultado para 0 ou 1?

RESPOSTA:

Não há como garantir que o arredondamento seria confiável, já que qualquer uma das extremidades pode prejudicar o resultado. As regressões lineares têm como resultado uma linha reta contínua, já a regressão logística tem como resultado uma curva sigmóide (S).

6. Na Situação D, quais consequências podem ocorrer se K for escolhido inadequadamente?

RESPOSTA:

Se K for muito pequeno, o modelo se torna extremamente sensível a ruídos, dados incorretos ou outliers na vizinhança imediata. Se K for muito alto, o modelo tenderá a prever sempre a classe majoritária do conjunto de dados, ignorando os padrões e peculiaridades locais do novo cliente.

7. PARTE V – ANÁLISE CRÍTICA 

É possível afirmar que um modelo é melhor apenas porque apresentou um resultado numérico melhor? Justifique. Cite e explique pelo menos dois fatores a considerar antes de usar um modelo real. 
Indique uma limitação ou cuidado importante do modelo escolhido. 

RESPOSTA:

Não. Um valor numérico superior em uma métrica de treino ou validação não garante que o modelo seja realmente melhor. Essa métrica isolada pode ser fruto de overfitting (quando o modelo decora os dados de treino, mas perde a capacidade de generalizar para novos dados reais) ou de um conjunto de dados com viés. Além disso, a escolha do melhor modelo deve ponderar a complexidade do algoritmo, o custo computacional, a velocidade de resposta e a interpretabilidade das decisões no contexto de negócio.
