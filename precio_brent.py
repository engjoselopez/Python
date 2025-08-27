# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 14:52:22 2025

@author: USER
"""

import pandas as pd

# Datos de ejemplo extraídos manualmente (puedes automatizarlo con Selenium si lo deseas)
data = {
    'Date': ['2025-08-14', '2025-08-13', '2025-08-12', '2025-08-11', '2025-08-10'],
    'Open': [66.87, 65.76, 66.14, 66.80, 66.25],
    'High': [67.06, 66.99, 66.33, 67.06, 67.13],
    'Low': [65.73, 65.55, 65.01, 65.98, 65.81],
    'Close': [65.85, 66.84, 65.63, 66.12, 66.63]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como CSV
df.to_csv('brent_prices.csv', index=False)
