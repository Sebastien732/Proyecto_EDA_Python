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


📁 Proyecto_EDA_Python  
├─ README.md  
├─ 📁 datos/  
│ .. ├─ bank-additional.csv  
│ .. ├─ customer-details.xlsx  
│ .. └─ df_bank_cust.csv  
├─ 📁 notebooks/  
│ .. └─ exploracion.ipynb  
└─ 📁 scripts/  
 ..... └─ limpieza_transformacion.py  



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
- `df_bank_cust.csv`: data frame final obtenido tras limpieza y transformacion de los datos anteriores

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
●	**~~y:~~** titulo de columna cambiado a **subscribed**: Indica si el cliente ha suscrito un producto o servicio (Sí/No).  
●	**date:** La fecha en la que se realizó la interacción con el cliente.  
●	**latitude:** coordenadas de latitude de la ubicacion del cliente.  
●	**longitude:** coordenadas de longitud de la ubicacion del cliente.  
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
- las columnas Latitude and Longitud no constaban en la descripcion original y la fecha de contacto aparece en una sola columna y no separadas en columna individuales por dia, mes y año. se actualizo la descripcion y se convierto la columna fecha en 3 columnas.
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

- El formato del campo `ID` en `bank_df` y en los DataFrames de clientes es **similar**.
- Se utilizó el método `.isin()` para verificar que los valores de `ID` están presentes en ambos conjuntos de datos.
- Se confirma que el campo `ID` puede ser utilizado como **clave común** para consolidar los DataFrames.

---





3. ## Limpieza y transformación: 

**Procesos aplicados:** *normalización de variables categóricas, tratamiento de fechas, codificación de valores booleanos*

#### Tratamiento de valores faltantes

- En la columna `age`, aproximadamente el **12% de los valores están ausentes**. Dado que esta variable es crucial, no se eliminan las filas. En su lugar, se imputan los valores faltantes utilizando la **edad promedio de clientes con perfiles similares**, definidos por los atributos `job` y `education`.

- Se eliminan las filas con valores faltantes en las columnas `job`, `marital`, `housing`, `loan` y `date`, ya que representan **menos del 3% del DataFrame**.

- Para la columna `education`, los valores faltantes se reemplazan por el valor `"unknown"`.

#### Observaciones adicionales

- Al revisar una muestra del DataFrame, se detecta una posible **correspondencia entre los valores únicos** de las columnas `cons.price.idx` y `cons.conf.idx`.

- Se confirma esta relación y se procede a **rellenar los valores faltantes en `cons.price.idx`** utilizando los valores correspondientes de `cons.conf.idx`.



### 🔍 Análisis de valores nulos en la columna `euribor3m`

Se han detectado valores nulos en la columna `euribor3m`, que representan **más del 20%** del total de registros disponibles. Dado este volumen significativo de datos faltantes, se considera adecuado aplicar técnicas de imputación para estimar dichos valores.

Tras evaluar distintos métodos —**media**, **mediana**, **moda** y un **modelo de regresión lineal**— se opta por este último. La decisión se basa en la **fuerte correlación** observada entre `euribor3m` y `emp.var.rate`, con un coeficiente de **0.9724**, lo que sugiere que el modelo de regresión puede proporcionar estimaciones precisas y coherentes.

---

### 🛠️ Transformación de tipos de datos

Durante la fase de exploración de datos se identificaron varias columnas con tipos incorrectos. Se realizaron las siguientes transformaciones:

| Columna            | Tipo original | Tipo corregido     |
|--------------------|---------------|---------------------|
| `age`              | `float64`     | `int`               |
| `default`          | `float64`     | `bool`              |
| `housing`          | `float64`     | `bool`              |
| `loan`             | `float64`     | `bool`              |
| `cons.price.idx`   | `object`      | `float`             |
| `cons.conf.idx`    | `object`      | `float`             |
| `euribor3m`        | `object`      | `float`             |
| `nr.employed`      | `object`      | `int` (formato uniforme) |
| `y` → `subscribed` | `object`      | `bool`              |
| `date`             | `object`      | `datetime`          |

> Las columnas `contact`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`, `emp.var.rate`, `latitude`, `longitude`, `id_` mantienen sus tipos originales.

---

### 🧹 Limpieza y ajustes adicionales

- En la columna `age`, los valores nulos fueron reemplazados por el promedio calculado según las variables `job` y `education`.
- En `pdays`, el valor `999` representa clientes no contactados. Este valor fue reemplazado por `NaN` para excluirlo de cálculos estadísticos.
- En las columnas `cons.price.idx`, `cons.conf.idx` y `euribor3m`, se reemplazaron las comas por puntos antes de convertir los valores a tipo `float`.
- En `nr.employed`, se uniformizó el formato para obtener valores de 5 dígitos con un decimal.
- La columna `y` fue renombrada a `subscribed`, transformando `"yes"` en `True` y `"no"` en `False`, y cambiando su tipo a `bool`.
- En `date`, se tradujeron los nombres de los meses a números mediante un diccionario, y se convirtió la columna al formato `datetime` (`dd-mm-aa`). Se añadieron las columnas `contact_month` y `contact_year`, presentes en la descripción original pero ausentes en el archivo CSV.

---

### 🔗 Combinación de DataFrames

- Se combinaron verticalmente los tres DataFrames de clientes en uno nuevo llamado `df_customer_combinados`.
- La columna `Dt_Customer` fue convertida al formato de fecha `dd-mm-aa`.
- Finalmente, se fusionaron los DataFrames `bank_df` y `df_customer_combinados` usando la columna `ID` como clave común, generando el DataFrame final `df_bank_cust`, con **42,332 registros y 29 columnas**.

> Durante este proceso se perdieron 170 registros del DataFrame de clientes, correspondientes a personas que no participaron en la campaña analizada.

- Se reinició el índice y se eliminaron las columnas innecesarias como `'ID'`, `'_id'` y el índice original de `customer_df`.

---

### 💾 Exportación del DataFrame final

Tras la limpieza y transformación de los datos, se exportó el DataFrame final `df_bank_cust` a un archivo `.CSV` para su posterior análisis.

---






4. ## 📊 Análisis de suscripción: suscriptores vs. no suscriptores

Este análisis tiene como objetivo identificar los factores que influyen en el éxito de una campaña de marketing bancario, comparando las características de los clientes que se han suscrito frente a los que no lo han hecho.

## 🗺️ Ubicación geográfica
El mapa de coordenadas no revela focos geográficos significativos de éxito. La distribución de suscriptores es homogénea, lo que sugiere que la ubicación no es un factor determinante.

## 🎂 Edad
Los rangos de edad con mayor tasa de suscripción se encuentran en los extremos: menores de 24 años y mayores de 59 años.

## 👔 Ocupación
La tendencia observada en la edad se confirma al analizar la ocupación. Estudiantes y jubilados presentan las tasas más altas de suscripción.

## 💍 Estado civil
Los clientes solteros muestran una ligera ventaja en la tasa de suscripción respecto a otras categorías.

## 🎓 Nivel educativo
Excluyendo los casos con nivel educativo desconocido, se observa un mayor éxito en los clientes con educación universitaria y también entre los iletrados.

## 💳 Historial de impago
Los clientes sin incidencias de pago tienen una mayor tasa de suscripción.

## 🏠 Préstamos hipotecarios y personales
No se observan diferencias significativas entre suscriptores y no suscriptores en relación con la tenencia de préstamos.

## ☎️ Método de contacto
El contacto vía teléfono móvil es claramente más efectivo que el contacto por línea fija. Se recomienda priorizar la recopilación de números móviles para futuras campañas.

## ⏱️ Duración de la última llamada
Las llamadas a suscriptores tienden a ser más largas, posiblemente debido al tiempo necesario para completar el proceso de contratación.

## 🔁 Número de interacciones durante la campaña
Los suscriptores han recibido más contactos en promedio. Sería útil analizar el contenido de estas interacciones.

## 📆 Días desde la última interacción
No se observan diferencias entre suscriptores y no suscriptores.

## 📈 Resultados de campañas anteriores
Los clientes que ya habían suscrito en campañas anteriores tienen una probabilidad significativamente mayor de volver a hacerlo. El 65% de los suscriptores actuales ya habían participado en campañas previas.

---

# 💰 Parámetros financieros

## 📉 Tasa de variación del empleo (`emp.var.rate`)
Mayor tasa de suscripción cuando el valor es inferior a -0.2, con una excepción en -1.8.

## 🛒 Índice de precios al consumidor (`cons.price.idx`)
Mayor éxito en los extremos del índice (valores bajos y altos).

## 📉 Índice de confianza del consumidor (`cons.conf.idx`)
Menor éxito entre los rangos -47.1 a -41.8 y -36.4 a -36.1.

## 💶 Euribor a tres meses (`euribor3m`)
Menor éxito cuando el índice está entre 1.2 y 1.5, y también cuando supera 3.1.

## 👥 Número de empleados
Mayor tasa de suscripción en empresas con menor número de empleados.

---

# 📅 Temporalidad

- **Año**: La tasa de éxito es estable año tras año.
- **Mes**: Octubre destaca como el mes con mayor proporción de suscriptores.

---

# 📊 Otros factores

- **Ingresos anuales**: No se observa una correlación clara.
- **Número de hijos**: No hay impacto significativo.
- **Antigüedad del cliente**: Mayor éxito en clientes recientes (desde 2014).
- **Visitas a la web**: No se detecta una relación clara.

---




5. ## Visualización de datos: 
*gráficos para detectar patrones y relaciones entre variables*




6. ## Conclusiones:
 *hallazgos significativos, propuestas de mejora en las campañas*

# 🧑‍💼 Perfil medio del cliente suscriptor

- **Edad**: Menores de 24 o mayores de 59 años.
- **Ocupación**: Estudiantes y jubilados.
- **Estado civil**: Solteros.
- **Educación**: Universitaria o sin estudios formales.
- **Historial financiero**: Sin impagos.
- **Antigüedad**: Clientes recientes (desde 2014).
- **Método de contacto**: Teléfono móvil.
- **Interacción previa**: Participación en campañas anteriores.

---
# ✅ Recomendaciones para futuras campañas

1. **Segmentación precisa**: Priorizar clientes jóvenes, mayores, estudiantes y jubilados.
2. **Optimización del canal de contacto**: Usar preferentemente teléfonos móviles.
3. **Refuerzo en octubre**: Aumentar recursos humanos y horarios en este mes.
4. **Seguimiento de campañas anteriores**: Recontactar clientes que ya han suscrito antes.
5. **Análisis de contenido de llamadas**: Evaluar qué tipo de interacción genera mayor conversión.
6. **Cruce de variables financieras**: Analizar combinaciones de índices para identificar patrones más robustos.????????????????????



## 📌 Nota
Este proyecto está diseñado como un ejercicio académico dentro del módulo *Python for Data*. El objetivo es aplicar conocimientos prácticos en la manipulación y análisis de datos.

---
