# APRENDIZAGEM-DE-MAQUINA
# APRENDIZAGEM-DE-MAQUINA
Faculdade iesb
2.1 Regressão Linear Simples : Regressão Linear Simples é utilizada quando o objetivo é prever uma variável numérica contínua (variável-alvo $Y$) a partir de uma única variável explicativa (variável de entrada $X$).
Variável Explicativa ($X$): É o dado de entrada independente que utilizamos para estimar o resultado.
Variável-Alvo ($Y$): É o valor numérico contínuo que pretendemos prever.
Aplicações: Prever o valor final de uma venda com base apenas na quantidade de itens comprados, prever o consumo de combustível baseado na distância percorrida, entre outros
Ideia da Equação da Reta ($Y = \beta_0 + \beta_1 X + \epsilon$):$\beta_0$ (Intercepto): O valor onde a reta intercepta o eixo $Y$ quando $X = 0$.$\beta_1$ (Coeficiente Angular): Representa a taxa de variação esperada em $Y$ para cada unidade acrescida em $X$.$\epsilon$ (Erro de Resíduo): A diferença entre o valor real observado e o valor estimado pelo modelo.Exemplo: Prever o valor total gasto por um cliente ($Y$) utilizando apenas o total de produtos adicionados ao carrinho ($X$).Por que é "Simples"? É chamada de simples por utilizar estritamente uma única variável independente para construir a previsão
.2 Regressão Linear MúltiplaA Regressão Linear Múltipla expande o modelo simples para situações onde duas ou mais variáveis explicativas ($X_1, X_2, \dots, X_n$) são necessárias para projetar a variável-alvo contínua ($Y$).
Diferença para a Regressão Simples: Enquanto a regressão simples traça uma reta em um plano de duas dimensões, a múltipla cria um plano ou hiperplano para relacionar múltiplos fatores ao mesmo tempo.Papel das Variáveis Explicativas: Capturar o impacto combinado de diferentes aspectos do problema (por exemplo, tempo no site, número de visitas e compras passadas).Por que mais variáveis não garantem um modelo melhor? Incluir variáveis sem critérios adequados pode gerar multicolinearidade (variáveis fortemente correlacionadas que trazem informação redundante) ou causar overfitting (quando o modelo decora ruídos do histórico e perde o poder de generalização).
3 Regressão LogísticaDiferente das regressões lineares, a Regressão Logística é focada em problemas de classificação binária, onde a variável-alvo assume apenas duas opções possíveis (ex.: Sim/Não, 0/1).Valor Numérico vs. Probabilidade: O algoritmo aplica a função sigmóide para converter os cálculos numéricos em uma escala de probabilidade contida entre $0$ e $1$ ($0\%$ a $100\%$).Exemplo 0/1: Prever se um acesso a uma conta é legítimo ($0$) ou uma tentativa de invasão ($1$).Papel do Limiar (Threshold): É o ponto de corte (frequentemente fixado em $0.5$). Se a probabilidade estimada for superior ou igual a $0.5$, o registro é classificado como $1$; caso contrário, recebe a classificação $0$
.4 KNN - K-Nearest Neighbors (K-Vizinhos Mais Próximos)O KNN é uma técnica baseada em instâncias que realiza previsões através da comparação do novo dado com os registros históricos mais próximos.Técnica Baseada em Instâncias: O algoritmo não gera uma fórmula matemática durante o treinamento; ele armazena a base de dados e efetua os cálculos de proximidade no momento exato de efetuar a classificação.Significado do K: Refere-se à quantidade de vizinhos históricos mais próximos que serão consultados para a decisão.Vizinhança e Distância: O algoritmo mede a distância (como a distância Euclidiana) entre o novo ponto e todos os registros antigos.Definição da Classe: A classe do novo elemento é determinada pela votação majoritária entre seus $K$ vizinhos mais próximos.Influência do K:$K$ muito pequeno ($K=1$): Torna o modelo excessivamente sensível a ruídos ou dados fora do padrão (causando overfitting).$K$ muito grande: Faz com que o modelo considere vizinhos distantes e irrelevantes, suavizando excessivamente as fronteiras e priorizando sempre a classe majoritária (causando underfitting).

 



 



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
