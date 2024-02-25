##print("Hello world!")

import pandas as pd

datos = {
   'Nombre': ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'],
   'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Año': [2019, 2003, 1991, 2019, 1990],
    'Kilometraje': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Cero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}


dataset = pd.read_csv("db.csv", sep=";")

print(dataset.to_html())