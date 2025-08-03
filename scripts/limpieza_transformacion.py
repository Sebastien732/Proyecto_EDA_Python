
import pandas as pd
import numpy as np
# Cargar los DataFrames
bank_df = pd.read_csv('../datos/bank-additional.csv', sep=',')
customer_df_2012 = pd.read_excel('../datos/customer-details.xlsx', sheet_name='2012')
customer_df_2013 = pd.read_excel('../datos/customer-details.xlsx', sheet_name='2013')
customer_df_2014 = pd.read_excel('../datos/customer-details.xlsx', sheet_name='2014')
# Combinar los DataFrames de clientes
df_customer_combinados = pd.concat([customer_df_2012, customer_df_2013, customer_df_2014], ignore_index=True)

# Normalizar las variables categóricas
# gestionde nulos de la columna age
# paso 1: Agrupamos por 'job' y 'education' y rellenamos los valores nulos en 'age' con la media del grupo redoneando a 0 para luego convertir en int
# esto asegura que los valores nulos se imputen con la media del grupo correspondiente
bank_df['age'] = bank_df.groupby(['job', 'education'])['age'].transform(lambda x: x.fillna(round(x.mean(), 0)))
# Paso 2: Imputar los que siguen siendo NaN (grupos sin edad registrada) con la media global
bank_df['age'] = bank_df['age'].fillna(round(bank_df['age'].mean(), 0))
#convertimos la columna age de formato float a int
bank_df['age'] = bank_df['age'].astype(int)

# cambiamos el tipo de dato de las columnas 
bank_df[['default', 'housing', 'loan']] = bank_df[['default', 'housing', 'loan']].astype(bool)



# Realizamos el merge para obtener solo las entradas que tienen coincidencia en ambos DataFrames
# en la exploracion previa se confirmo que el valor comun tiene el mismo formato

bank_cust_df = pd.merge(
    bank_df, 
    df_customer_combinados, 
    left_on='id_', 
    right_on='ID', 
    how='inner'  # Esta opción conserva solo las coincidencias
)

#Eliminacion de lineas sin valores de los atributos 'job', 'marital' y 'date' que representan menos de 1% del data frame
bank_cust_df = bank_cust_df.dropna(subset=['job', 'marital', 'date'])
# Por la columna 'education' replazamos las lineas sin valores por el valor "unknown"
bank_cust_df['education'] = bank_cust_df['education'].fillna('unknown')

# cambiamos el tipo de la columna 'y' a booleano
bank_cust_df['y'] = bank_cust_df['y'].astype(bool)

# Renombrar la columna 'y' a 'subscribed'
bank_cust_df = bank_cust_df.rename(columns={'y': 'subscribed'})
