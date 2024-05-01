# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fc3xrDrOYfhwM23oTpQ2fpQDeE8QpjYV
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

#Datos ha generar
cantidad_datos=2000

def main():

  def generar_edad():
    return np.random.randint(18, 80, cantidad_datos)

  def generar_peso(edad):
    sobrepeso = np.random.choice([0, 1], cantidad_datos, p=[0.9, 0.1])
    peso_base = np.random.normal(70, 15, cantidad_datos)
    peso = peso_base + sobrepeso * 20
    peso = np.where((edad >= 40) & (edad <= 60), peso + 5, peso)
    return peso

  def generar_altura():
    return np.random.normal(170, 10, cantidad_datos)

  def calcular_imc(peso, altura):
    return peso / ((altura / 100) ** 2)

  def generar_circunferencia_cintura():
    return np.random.normal(90, 10, cantidad_datos)

  def generar_circunferencia_cadera():
    return np.random.normal(100, 10, cantidad_datos)

  def generar_porcentaje_grasa_corporal():
    return np.random.normal(25, 5, cantidad_datos)

  def generar_historial_medico_familiar():
    enfermedades = ['Diabetes', 'Hipertensión', 'Cáncer', 'Enfermedades cardiovasculares']
    return [', '.join(np.random.choice(enfermedades, np.random.randint(0, len(enfermedades)), replace=False)) for _ in range(cantidad_datos)]

  def generar_nivel_actividad_fisica():
    return np.random.choice(['Sedentario', 'Ligero', 'Moderado', 'Intenso'], cantidad_datos)

  def generar_habitos_alimenticios():
    habitos = ['Vegetariano', 'Omnívoro', 'Vegano', 'Pescetariano', 'Keto', 'Paleo']
    return np.random.choice(habitos, cantidad_datos)

  def generar_horas_sueño_noche():
    return np.random.normal(7, 2, cantidad_datos)

  def generar_nivel_estres_percibido():
    return np.random.randint(1, 11, cantidad_datos)

  def generar_consumo_agua_diario():
    return np.random.normal(2, 0.5, cantidad_datos)

  def generar_consumo_alcohol():
    return np.random.normal(5, 3, cantidad_datos)

  def generar_consumo_tabaco():
    return np.random.normal(5, 2, cantidad_datos)

  def generar_consumo_cafeina():
    return np.random.normal(200, 100, cantidad_datos)

  def generar_enfermedades_cronicas():
    enfermedades = ['Diabetes', 'Hipertensión', 'Cáncer', 'Enfermedades cardiovasculares', 'Enfermedad renal crónica', 'Enfermedad pulmonar crónica']
    return [', '.join(np.random.choice(enfermedades, np.random.randint(0, len(enfermedades)), replace=False)) for _ in range(cantidad_datos)]

  def generar_medicamentos_actuales():
    medicamentos = ['Aspirina', 'Insulina', 'Losartán', 'Atorvastatina', 'Metformina', 'Omeprazol', 'Salbutamol']
    dosis = ['10 mg', '50 mg', '100 mg', '20 mg', '200 UI', '500 mg', '1 tableta']
    return ['{}, {}'.format(np.random.choice(medicamentos), np.random.choice(dosis)) for _ in range(cantidad_datos)]

  def generar_metas_perdida_peso():
    return np.random.normal(5, 3, cantidad_datos)

  def generar_frecuencia_cardiaca_reposo():
    return np.random.normal(70, 10, cantidad_datos)

  def generar_presion_arterial_sistolica():
    return np.random.normal(120, 10, cantidad_datos)

  def generar_presion_arterial_diastolica():
    return np.random.normal(80, 8, cantidad_datos)

  def generar_niveles_colesterol():
    ldl = np.random.normal(100, 20, cantidad_datos)
    hdl = np.random.normal(50, 10, cantidad_datos)
    trigliceridos = np.random.normal(150, 30, cantidad_datos)
    return ldl, hdl, trigliceridos

  def generar_niveles_glucosa_sangre():
    ayunas = np.random.normal(90, 10, cantidad_datos)
    postprandial = np.random.normal(120, 20, cantidad_datos)
    return ayunas, postprandial

  def generar_sensibilidad_alimentos():
    alimentos = ['Lactosa', 'Gluten', 'Nueces', 'Mariscos', 'Huevo', 'Soja']
    return [', '.join(np.random.choice(alimentos, np.random.randint(0, len(alimentos)), replace=False)) for _ in range(cantidad_datos)]

  def generar_nivel_satisfaccion_dieta_actual():
    return np.random.randint(1, 11, cantidad_datos)

  def generar_cumplimiento_plan_nutricional():
    return np.random.randint(1, 11, cantidad_datos)

  def generar_actividades_fisicas_realizadas():
    actividades = ['Caminar', 'Correr', 'Nadar', 'Bailar', 'Levantamiento de pesas', 'Yoga']
    return [', '.join(np.random.choice(actividades, np.random.randint(1, 4), replace=False)) for _ in range(cantidad_datos)]

  def generar_consumo_frutas_verduras():
    return np.random.normal(5, 2, cantidad_datos)

  def generar_nivel_conocimiento_nutricion():
    return np.random.choice(['Bajo', 'Medio', 'Alto'], cantidad_datos)


# Generar datos simulados
edad = generar_edad()
peso = generar_peso(edad)
altura = generar_altura()
imc = calcular_imc(peso, altura)
circunferencia_cintura = generar_circunferencia_cintura()
circunferencia_cadera = generar_circunferencia_cadera()
porcentaje_grasa_corporal = generar_porcentaje_grasa_corporal()
historial_medico_familiar = generar_historial_medico_familiar()
enfermedades_cronicas = generar_enfermedades_cronicas()
nivel_actividad_fisica = generar_nivel_actividad_fisica()
habitos_alimenticios = generar_habitos_alimenticios()
horas_sueño_noche = generar_horas_sueño_noche()
nivel_estres_percibido = generar_nivel_estres_percibido()
consumo_agua_diario = generar_consumo_agua_diario()
consumo_alcohol = generar_consumo_alcohol()
consumo_tabaco = generar_consumo_tabaco()
consumo_cafeina = generar_consumo_cafeina()
ldl, hdl, trigliceridos = generar_niveles_colesterol()
glucosa_ayunas, glucosa_postprandial = generar_niveles_glucosa_sangre()
sensibilidad_alimentos = generar_sensibilidad_alimentos()
nivel_satisfaccion_dieta_actual = generar_nivel_satisfaccion_dieta_actual()
cumplimiento_plan_nutricional = generar_cumplimiento_plan_nutricional()
actividades_fisicas_realizadas = generar_actividades_fisicas_realizadas()
consumo_frutas_verduras = generar_consumo_frutas_verduras()
nivel_conocimiento_nutricion = generar_nivel_conocimiento_nutricion()

# Crear un diccionario con los datos generados
data = {
    'Edad': edad,
    'Peso': peso,
    'Altura': altura,
    'IMC': imc,
    'Circunferencia de cintura': circunferencia_cintura,
    'Circunferencia de cadera': circunferencia_cadera,
    'Porcentaje de grasa corporal': porcentaje_grasa_corporal,
    'Historial médico familiar': historial_medico_familiar,
    'Enfermedades crónicas': enfermedades_cronicas,
    'Nivel de actividad física': nivel_actividad_fisica,
    'Hábitos alimenticios': habitos_alimenticios,
    'Horas de sueño por noche': horas_sueño_noche,
    'Nivel de estrés percibido': nivel_estres_percibido,
    'Consumo de agua diario (litros)': consumo_agua_diario,
    'Consumo de alcohol (unidades por semana)': consumo_alcohol,
    'Consumo de tabaco (cigarrillos por día)': consumo_tabaco,
    'Consumo de cafeína (mg por día)': consumo_cafeina,
    'Niveles de colesterol LDL (mg/dL)': ldl,
    'Niveles de colesterol HDL (mg/dL)': hdl,
    'Niveles de triglicéridos (mg/dL)': trigliceridos,
    'Niveles de glucosa en sangre en ayunas (mg/dL)': glucosa_ayunas,
    'Niveles de glucosa en sangre postprandial (mg/dL)': glucosa_postprandial,
    'Sensibilidad a alimentos': sensibilidad_alimentos,
    'Nivel de satisfacción con la dieta actual': nivel_satisfaccion_dieta_actual,
    'Cumplimiento del plan nutricional': cumplimiento_plan_nutricional,
    'Actividades físicas realizadas': actividades_fisicas_realizadas,
    'Consumo de frutas y verduras por día': consumo_frutas_verduras,
    'Nivel de conocimiento en nutrición': nivel_conocimiento_nutricion
}

# Crear un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificar y corregir valores nulos o inconsistentes
for columna in df.columns:
    print(f"Longitud de {columna}: {len(df[columna])}")

# Manejar valores nulos imputándoles NaN
longitud_maxima = max(len(df[columna]) for columna in df.columns)
for columna in df.columns:
    if len(df[columna]) < longitud_maxima:
        df[columna] = df[columna].append(pd.Series([np.nan] * (longitud_maxima - len(df[columna]))), ignore_index=True)

# Verificar nuevamente las longitudes después de imputar NaN
print("\nDespués de imputar NaN:\n")
for columna in df.columns:
    print(f"Longitud de {columna}: {len(df[columna])}")

# Separar el DataFrame en dos basado en la lógica de los datos
datos_con_logica_real = df[['Niveles de colesterol LDL (mg/dL)', 'Niveles de colesterol HDL (mg/dL)', 'Niveles de triglicéridos (mg/dL)',
                            'Niveles de glucosa en sangre en ayunas (mg/dL)', 'Niveles de glucosa en sangre postprandial (mg/dL)']]

datos_aleatorios = df.drop(columns=['Niveles de colesterol LDL (mg/dL)', 'Niveles de colesterol HDL (mg/dL)', 'Niveles de triglicéridos (mg/dL)',
                                     'Niveles de glucosa en sangre en ayunas (mg/dL)', 'Niveles de glucosa en sangre postprandial (mg/dL)'])

# Explicar los DataFrames resultantes
print("\nDataFrame con lógica real:\n")
print(datos_con_logica_real.head())

print("\nDataFrame con datos aleatorios:\n")
print(datos_aleatorios.head())

# Define las características (features) y la variable objetivo
X = df.drop(columns=['Enfermedades crónicas'])  # Características
y = df['Enfermedades crónicas']  # Variable objetivo

# Aplicar codificación one-hot a las variables categóricas
X_encoded = pd.get_dummies(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Definir los hiperparámetros a ajustar
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Inicializar el clasificador RandomForest
rf_classifier = RandomForestClassifier(random_state=42)

# Realizar la búsqueda de cuadrícula (grid search) para encontrar los mejores hiperparámetros
grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=5, scoring='accuracy', verbose=2)
grid_search.fit(X_train, y_train)

# Obtener el mejor modelo con los mejores hiperparámetros
best_rf_model = grid_search.best_estimator_

# Hacer predicciones en el conjunto de prueba
y_pred = best_rf_model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy after GridSearchCV:", accuracy)

# Imprimir el reporte de clasificación y la matriz de confusión
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    main()