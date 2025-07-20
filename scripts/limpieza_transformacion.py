
import pandas as pd
import numpy as np
# Cargar los DataFrames
bank_df = pd.read_csv('Proyecto_EDA_Python/Proyecto_EDA_Python/data/bank.csv')
customer_df_2012 = pd.read_csv('Proyecto_EDA_Python/Proyecto_EDA_Python/data/customer_2012.csv')
customer_df_2013 = pd.read_csv('Proyecto_EDA_Python/Proyecto_EDA_Python/data/customer_2013.csv')
customer_df_2014 = pd.read_csv('Proyecto_EDA_Python/Proyecto_EDA_Python/data/customer_2014.csv')
# Combinar los DataFrames de clientes
df_customer_combinados = pd.concat([customer_df_2012, customer_df_2013, customer_df_2014], ignore_index=True)

