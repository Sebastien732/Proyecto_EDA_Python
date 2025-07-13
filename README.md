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
●	**id_: **Un identificador único para cada registro en el dataset.  

### 'customer-details.xlsx  
 
●	**Income:** Representa el ingreso anual del cliente en términos monetarios.  
●	**Kidhome:** Indica el número de niños en el hogar del cliente.  
●	**Teenhome:** Indica el número de adolescentes en el hogar del cliente.  
●	**Dt_Customer:** Representa la fecha en que el cliente se convirtió en cliente de la empresa.  
●	**NumWebVisitsMonth:** Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa.  
●	**ID:** Identificador único del cliente.  


## ✅ Pasos realizados
1. **Carga de datos** desde archivos `.csv` y `.xlsx`.

2. **Inspección inicial**: estructura, tipos de datos, valores nulos.





3. **Limpieza y transformación**: normalización de variables categóricas, tratamiento de fechas, codificación de valores booleanos.




4. **Análisis descriptivo**: estadísticas, distribuciones, correlaciones entre variables.




5. **Visualización de datos**: gráficos para detectar patrones y relaciones entre variables.




6. **Conclusiones**: hallazgos significativos, propuestas de mejora en las campañas.







## 📌 Nota
Este proyecto está diseñado como un ejercicio académico dentro del módulo *Python for Data*. El objetivo es aplicar conocimientos prácticos en la manipulación y análisis de datos.

---
