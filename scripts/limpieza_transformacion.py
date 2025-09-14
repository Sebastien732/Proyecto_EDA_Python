# importar las librerías necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Configuración de rutas para cargar y guardar datos desde/hacia la carpeta "datos"
# Ruta al directorio del script actual
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Ruta al directorio 'datos'
ruta_datos = os.path.join(ruta_script, '..', 'datos')

# Cargar el CSV principal
bank_df = pd.read_csv(os.path.join(ruta_datos, 'bank-additional.csv'), sep=',')

# Cargar las hojas del Excel
customer_df_2012 = pd.read_excel(os.path.join(ruta_datos, 'customer-details.xlsx'), sheet_name='2012')
customer_df_2013 = pd.read_excel(os.path.join(ruta_datos, 'customer-details.xlsx'), sheet_name='2013')
customer_df_2014 = pd.read_excel(os.path.join(ruta_datos, 'customer-details.xlsx'), sheet_name='2014')


# limpieza y transformación de bank_df
# quitar columna innecesaria de indice
bank_df = bank_df.drop(bank_df.columns[0], axis=1)
# convertir las columnas 'default', 'housing' y 'loan' a tipo booleano
bank_df[['default', 'housing', 'loan']] = bank_df[['default', 'housing', 'loan']].astype(bool)

# gestion de nulos de la columna age
# paso 1: Agrupamos por 'job' y 'education' y rellenamos los valores nulos en 'age' con la media del grupo
bank_df['age'] = bank_df.groupby(['job', 'education'])['age'].transform(lambda x: x.fillna(round(x.mean(), 0)))
# Paso 2: Imputar los que siguen siendo NaN (grupos sin edad registrada) con la media global
bank_df['age'] = bank_df['age'].fillna(round(bank_df['age'].mean(), 0))
#convertimos la columna age de formato float a int
bank_df['age'] = bank_df['age'].astype(int)

# Eliminacion de lineas sin valores de los atributos 'job', 'marital' ,'housing', 'loan' y 'date'
bank_df = bank_df.dropna(subset=['job', 'marital', 'housing', 'loan','date'])

# Se añade el valor "unknown" a los valores nulos de la columna 'education'
bank_df['education'] = bank_df['education'].fillna('unknown')

# cambio del valor "999" de la columna 'pdays' por "NaN"
bank_df.loc[bank_df['pdays'] == 999, 'pdays'] = pd.NA

# convertir la columna 'pdays' a tipo Int64 (permite NaN)
bank_df['pdays'] = bank_df['pdays'].astype('Int64')
# convertir la columna 'age' a tipo Int64
bank_df['age'] = bank_df['age'].astype('Int64')

# convertir las columnas 'cons.price.idx', 'cons.conf.idx' y 'euribor3m' a tipo float
columns_to_convert = ['cons.price.idx', 'cons.conf.idx', 'euribor3m']
# Reemplazar comas por puntos y convertir a float
for col in columns_to_convert:
    bank_df[col] = bank_df[col].astype(str).str.replace(',', '.')
    bank_df[col] = bank_df[col].astype(float)

# gestion de nulos de la columna cons.price.idx
# Crear un diccionario de mapeo desde 'cons.conf.idx' a 'cons.price.idx'
mapping = bank_df.dropna(subset=['cons.price.idx']).drop_duplicates(subset=['cons.conf.idx'])\
    .set_index('cons.conf.idx')['cons.price.idx'].to_dict()

# Rellenar los valores faltantes en 'cons.price.idx' usando el mapeo
bank_df['cons.price.idx'] = bank_df.apply(
    lambda row: mapping[row['cons.conf.idx']] if pd.isna(row['cons.price.idx']) else row['cons.price.idx'],
    axis=1)

# cambio de formato de la columna 'nr.employed'
# Reemplazar comas por puntos antes de convertir a float
bank_df['nr.employed'] = bank_df['nr.employed'].astype(str).str.replace(',', '.')
bank_df['nr.employed'] = bank_df['nr.employed'].astype(float)
# Convertir a texto con 1 decimal, útil para visualización o comparación
bank_df['nr.employed'] = bank_df['nr.employed'].map(lambda x: f"{x:.1f}")
# Quitamos el punto de la columna nr.employed
bank_df['nr.employed'] = bank_df['nr.employed'].str.replace('.', '')
# Convertir a int
bank_df['nr.employed'] = bank_df['nr.employed'].astype(int)

# Cambio de nombre de la columna 'y'
bank_df.rename(columns={'y': 'subscribed'}, inplace=True)
# Reemplazar los valores de la columna 'subscribed' y convertir a booleano
bank_df['subscribed'] = bank_df['subscribed'].map({'yes': True, 'no': False})

# Cambio de valores de la columna 'date' al formato datetime y creación de nuevas columnas 'contact_year' 'contact_month' 
# Traduccion de los valores en ingles a traves de un diccionario

meses_es_en = {
    "enero": "January", "febrero": "February", "marzo": "March", "abril": "April",
    "mayo": "May", "junio": "June", "julio": "July", "agosto": "August",
    "septiembre": "September", "octubre": "October", "noviembre": "November", "diciembre": "December"
}

# Cambio de los nombres de los meses en español por inglés
for mes_es, mes_en in meses_es_en.items():
    bank_df['date'] = bank_df['date'].str.replace(mes_es, mes_en, regex=False)

# Conversion de la columna 'date' a datetime usando el formato adecuado
bank_df['date'] = pd.to_datetime(bank_df['date'], errors='coerce')
# Creacion de las columnas 'contact_year' y 'contact_month' antes de convertir a .dt.date
bank_df['contact_month'] = bank_df['date'].dt.month
bank_df['contact_year'] = bank_df['date'].dt.year
bank_df['date'] = bank_df['date'].dt.date

# gestion de nulos de la columna euribor3m
# Calcular la media de euribor3m
EURIBOR_MEAN = bank_df['euribor3m'].mean()
# Calcular la media de emp.var.rate
EMP_RATE_MEAN = bank_df['emp.var.rate'].mean()
# Calcular la correlación entre euribor3m y emp.var.rate
CORRELATION = bank_df['euribor3m'].corr(bank_df['emp.var.rate'])

# Imputar los valores nulos en 'euribor3m' usando un modelo de regresión lineal simple
bank_df['euribor3m'] = bank_df.apply(lambda row: 
    EURIBOR_MEAN + CORRELATION * (row['emp.var.rate'] - EMP_RATE_MEAN)
    if pd.isna(row['euribor3m']) else row['euribor3m'], axis=1)
# cambio de formato de la columna 'euribor3m' a 3 decimales
bank_df['euribor3m'] = bank_df['euribor3m'].round(3)

# combinacion de los dataframes customer_df_2012, customer_df_2013 y customer_df_2014 en un solo dataframe customer_df
customer_df = pd.concat([customer_df_2012, customer_df_2013, customer_df_2014], ignore_index=True)

# cammbio de formato de la columna 'Dt_Customer' a date
customer_df['Dt_Customer'] = customer_df['Dt_Customer'].dt.date

# eliminacion del indice innecesario de customer_df
customer_df = customer_df.reset_index(drop=True)   
# eliminacion del indice
customer_df = customer_df.drop(customer_df.columns[0], axis=1)

# Merge de los dataframes bank_df y customer_df en un solo dataframe df_bank_cust
df_bank_cust = pd.merge(
    bank_df, 
    customer_df, 
    left_on='id_', 
    right_on='ID', 
    how='inner'  # Esta opción conserva solo las coincidencias
)

# Eliminacion de las columnas innecesarias 'ID' y 'id_'
df_bank_cust = df_bank_cust.drop(columns=['id_'])
df_bank_cust = df_bank_cust.drop(columns=['ID'])


# reseteo del indice
df_bank_cust = df_bank_cust.reset_index(drop=True)


# creacion de un fichero .csv con el dataframe final df_bank_cust
df_bank_cust.to_csv(os.path.join(ruta_datos, 'df_bank_cust.csv'), index=False)
# fin del script de limpieza y transformacion