import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Base de dados simples (simulada)
np.random.seed(42)
n = 30
produtos = np.random.randint(1, 15, n)
valor_venda = 15 + produtos * 22 + np.random.normal(0, 10, n)

df = pd.DataFrame({"produtos": produtos, "valor_venda": valor_venda.round(2)})

# 2. Preparação mínima dos dados
X = df[["produtos"]]   # entrada
y = df["valor_venda"]  # alvo

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 3. Criação e treino do modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. Previsão
y_pred = modelo.predict(X_test)

# 5. Resultados
a = modelo.intercept_
b = modelo.coef_[0]
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Equação: valor_venda = {a:.2f} + {b:.2f} * produtos")
print(f"R² (teste): {r2:.3f}")
print(f"RMSE (teste): {rmse:.2f}")

novo_produto = pd.DataFrame({"produtos": [8]})
previsao = modelo.predict(novo_produto)[0]
print(f"Previsão para 8 produtos: R$ {previsao:.2f}")