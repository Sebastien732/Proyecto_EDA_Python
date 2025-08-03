# Proyecto_EDA_Python
The Power - proyecto 4 




# Análisis Exploratorio de Datos — Campañas de Marketing Bancarias

## 🎯 Objetivo del proyecto
Este proyecto consiste en realizar un análisis exploratorio sobre datos de campañas de marketing telefónico realizados por un banco portugués, con el fin de comprender mejor el perfil de los clientes y el rendimiento de las campañas.


## 📁 Estructura del repositorio
Ruta: https://github.com/Sebastien732/Proyecto_EDA_Python.git
- `datos/`: Contiene los datasets originales (`CSV` y `Excel`) y los datos transformados.
- `notebooks/`: Archivos Jupyter Notebook con el desarrollo del análisis.
- `scripts/`: Código auxiliar para limpieza y transformación.
- `README.md`: Documento explicativo del proyecto y hallazgos.

'''


📁 tu-proyecto/  
├─ README.md  
├─ 📁 datos/  
│ .. ├─ bank-additional.csv  
│ .. ├─ customer-details.xlsx  
├─ 📁 notebooks/  
│ .. ├─ exploracion.ipynb  
└─ 📁 scripts/  
. . . └─ limpieza_transformacion.py  



'''

## 🛠 Herramientas utilizadas
- Python
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook
- Visual Studio Code

## 🗂 Fuente de datos
- `bank-additional.csv`: Detalles sobre interacciones en campañas de marketing.
- `customer-details.xlsx`: Información demográfica y de comportamiento de clientes.

## 🗂 Descripcion de los datos brutos

### 'bank-additional.csv':  
●	**age:** La edad del cliente.  
●	**job:** La ocupación o profesión del cliente.  
●	**marital:** El estado civil del cliente.  
●	**education:** El nivel educativo del cliente.  
●	**default:** Indica si el cliente tiene algún historial de incumplimiento de pagos (1: Sí, 0: No).  
●	**housing:** Indica si el cliente tiene un préstamo hipotecario (1: Sí, 0: No).  
●	**loan:** Indica si el cliente tiene algún otro tipo de préstamo (1: Sí, 0: No).  
●	**contact:** El método de contacto utilizado para comunicarse con el cliente.  
●	**duration:** La duración en segundos de la última interacción con el cliente.  
●	**campaign:** El número de contactos realizados durante esta campaña para este cliente.  
●	**pdays:** Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña.  
●	**previous:** Número de veces que se ha contactado con el cliente antes de esta campaña.  
●	**poutcome:** Resultado de la campaña de marketing anterior.  
●	**emp.var.rate:** La tasa de variación del empleo.  
●	**cons.price.idx:** El índice de precios al consumidor.  
●	**cons.conf.idx:** El índice de confianza del consumidor.  
●	**euribor3m:** La tasa de interés de referencia a tres meses.  
●	**nr.employed:** El número de empleados.  
●	**y:** Indica si el cliente ha suscrito un producto o servicio (Sí/No).  
●	**date:** La fecha en la que se realizó la interacción con el cliente.  
●	**contact_month:** Mes en el que se realizó la interacción con el cliente durante la campaña de marketing.  
●	**contact_year:** Año en el que se realizó la interacción con el cliente durante la campaña de marketing.  
●	**id_:** Un identificador único para cada registro en el dataset.  

### 'customer-details.xlsx  
 
●	**Income:** Representa el ingreso anual del cliente en términos monetarios.  
●	**Kidhome:** Indica el número de niños en el hogar del cliente.  
●	**Teenhome:** Indica el número de adolescentes en el hogar del cliente.  
●	**Dt_Customer:** Representa la fecha en que el cliente se convirtió en cliente de la empresa.  
●	**NumWebVisitsMonth:** Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa.  
●	**ID:** Identificador único del cliente.  


## ✅ Pasos realizados
1.  ## Carga de datos desde archivos `.csv` y `.xlsx`.  

-El archivo `bank-additional.csv` esta asignado a la variable `bank_df`.  
-Las paginas del archivo customer-dtails.xlsx estan asignadas a las variables `customer_df_2012`, `customer_df_2013` y `customer_df_2014`.





2. ## Inspección Inicial de los Archivos:
*estructura, tipos de datos, valores nulos*  

Se realizó una inspección preliminar de ambos archivos utilizando los siguientes métodos de análisis:

```python
.sample(), .shape(), .columns(), .dtypes(), .info(), .isnull().sum(), .describe()
```

### Análisis del DataFrame `bank_df`

- El DataFrame `bank_df` contiene **43 300 entradas** y **24 columnas**.
- Se detectaron tipos de datos incorrectos en algunas columnas, los cuales serán detallados y corregidos en la siguiente etapa.
- Se observaron valores nulos significativos en las columnas `age`, `default` y `euribor3m`, representando entre el 10% y el 20% del total de los datos.
- Se propone:
  - **Rellenar los valores faltantes** en las columnas con alta proporción de nulos.
  - **Eliminar filas** con menos del **5% de valores nulos**, para mantener la calidad del conjunto de datos.

### Análisis de los DataFrames `customer_df_2012`, `customer_df_2013` y `customer_df_2014`

- Los tres DataFrames presentan la misma estructura de datos, lo que permite su **unificación** en una sola tabla para facilitar la limpieza y transformación en etapas posteriores. los 3 DataFrames combinados contienen **43 170 entradas** y **7 columnas**
- No se encontraron valores nulos en ninguno de los tres DataFrames.
- Los tipos de datos en cada columna están correctamente alineados con los valores que contienen.

### Relación entre `bank_df` y los DataFrames de clientes

- El formato del campo `ID` en `bank_df` y en los DataFrames de clientes es **muy similar**.
- Se utilizó el método `.isin()` para verificar que los valores de `ID` están presentes en ambos conjuntos de datos.
- Se confirma que el campo `ID` puede ser utilizado como **clave común** para consolidar los DataFrames.

---






3. ## Limpieza y transformación: 
*normalización de variables categóricas, tratamiento de fechas, codificación de valores booleanos*


En la columna `age` nos falta cerca de 12% de los valores. Este dato parece crucial por lo cual no podemos eliminarlo. Procedemos a remplazar los valores faltante por una edad promedia correspondiente a otros clientes con perfiles similar usando los atributos `job` & `education` 

Se procede a la eliminacion de lineas sin valores de los atributos 'job', 'marital' y 'date' que representan menos de 1% del data frame. 
Por la columna 'education' replazamos las lineas sin valores por el valor "unknown"

Tras observar sample del data frame se observa una posible correspondencia de valores unicos entre las columnas 'cons.price.idx' y 'cons.conf.idx'.
Confirmamos esta teoria y rellenanos los valores faltantes de la columna 'cons.price.idx'

Quedan valores nulos por en 'euribor3m'. Representan mas de 20% de los datos disponibles. Se sospecha que se podria calcular estos valores faltantes. Lo dejamos de  momento y lo estudiaremos mas adelante.


Durante la fase de exploracion de datos se identifico varias columnas de tipo incorrecto que vamos a transformar de la manera siguiente:  
 1   age             float64 ==> inter  
 5   default         float64 ==> bool  
 6   housing         float64 ==> bool  
 7   loan            float64 ==> bool  
 8   contact         object  
 9   duration        int64   
 10  campaign        int64   
 11  pdays           int64   
 12  previous        int64   
 13  poutcome        object  
 14  emp.var.rate    float64  
 15  cons.price.idx  object ==> float  
 16  cons.conf.idx   object ==> float  
 17  euribor3m       object ==> float  
 18  nr.employed     object ==> inter  
 19  ~~y~~ subscribed    object ==> bool  
 20  date            object ==> object date  
 21  latitude        float64  
 22  longitude       float64  
 23  id_             object  


Ademas del cambio de tipo de dato de la columna "age", se ha reemplazado los valores nulos por un promedio usando valores "job" y "education".
En la columna "pdays" el valor 999 es un valor ficticio que se usa cuando el cliente nunca fue contactado ya el calculo desde la ultima llamada no se puede hacer. Cambiaremos este valor por NaN para poder excluirlo de calculo posteriores (promedio ect..)
por las columnas 15, 16 y 17 se reemplazo la coma por un punto antes de convertir los valores a float
por la columna 18 "nr.employed" se uniformisa el formato usando el mismo metodo y un par de cambio de formato para añadir un decimal y quitar el punto. Se obtiene una referencia de 5 digitos.
Se renombra la columna "y" a "subscribed", cambiamos los valores "yes" a "True" y "no" a "False" y finalmente cambiamos el tipo de dato a boleano.
En la columna date, convertimos los meses en numero usando un diccionario y luego se convirtio en formato date_time mostrando el valore como dd-mm-aa.







Se combina de forma vertical los 3 dataframes de clientes en uno nuevo asignado a la variable `df_customer_combinados` 
se cambia los datos de la columna Dt_Customer a fecha con formato dd-mm-aa
Se combinan los data frame `bank_df` y `df_customer_combinados` usando la columna `ID` como clave comun y se assigna el nombre `df_bank_cust`. el DF contiene 42332 entradas y 29 columnas.
En el proceso perdemos 170 endradas del dataframe de clientes. Estos datos parecen innecesarios ya que estos clientes no participaron a la camapaña que estudiamos.



4. ## Análisis descriptivo:
 *estadísticas, distribuciones, correlaciones entre variables*




5. ## Visualización de datos: 
*gráficos para detectar patrones y relaciones entre variables*




6. ## Conclusiones:
 *hallazgos significativos, propuestas de mejora en las campañas*







## 📌 Nota
Este proyecto está diseñado como un ejercicio académico dentro del módulo *Python for Data*. El objetivo es aplicar conocimientos prácticos en la manipulación y análisis de datos.

---
