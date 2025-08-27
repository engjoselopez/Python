import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Cargar el dataset (ajusta el path si es necesario)
df = pd.read_csv('brent_prices.csv')

# Preprocesamiento
df.columns = df.columns.str.strip()  # Limpia espacios en nombres de columnas
df['Date'] = pd.to_datetime(df['Date'])  # Asegura que la columna Date sea tipo datetime
df.set_index('Date', inplace=True)

# Filtrar columnas relevantes
df = df[['Open', 'High', 'Low', 'Close']].dropna()

# Variables independientes y dependiente
X = df[['Open', 'High', 'Low']]
y = df['Close']

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Entrenamiento del modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Nuevos datos para predicción (simulados)
X_pred = pd.DataFrame({
    "Open":  [66.25, 66.80, 66.14, 65.76, 66.87],
    "High":  [67.13, 67.06, 66.33, 66.99, 67.06],
    "Low":   [65.81, 65.98, 65.01, 65.55, 65.73]
})

# Predicción
y_pred = model.predict(X_pred)

# Visualización: comparar predicción con valores reales
# Para evitar confusión, graficamos solo los valores predichos junto a sus fechas simuladas
fechas_pred = pd.date_range(start="2025-08-10", periods=len(y_pred), freq="D")

plt.figure(figsize=(10, 5))
plt.plot(df.index, y, label='Actual', marker='o', alpha=0.5)
plt.plot(fechas_pred, y_pred, label='Predicted', marker='x', color='orange')
plt.title('Brent Crude Price Prediction')
plt.xlabel('Fecha')
plt.ylabel('Precio (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Evaluación del modelo con datos de prueba reales
y_test_pred = model.predict(X_test)
r2 = r2_score(y_test, y_test_pred)
print(f"R² del modelo sobre el conjunto de prueba: {r2:.4f}")