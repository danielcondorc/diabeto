La dataset utilizada Procede de la encuesta BRFSS 2015 del CDC, un muestreo telefónico en EE. UU. de más de 70 mil adultos. La variable objetivo “Diabetes_binary” tiene 2 clases. 0 es para no tener diabetes y 1 es para prediabetes o diabetes. Este conjunto de datos tiene 21 variables y está equilibrado.
La creación de una app sobre riesgos para presentar diabetes se justifica en la creciente prevalencia de esta enfermedad a nivel mundial, la cual representa un grave problema de salud pública debido a sus complicaciones y altos costos de tratamiento. Esta aplicación permitiría a los usuarios identificar de manera temprana y personalizada sus factores de riesgo sobre esta enfermedad.
Asimismo, la contribución que tendría en el campo del Machine learning sería contribuir en el diseño para construir y evaluar modelos de predicción de riesgo de diabetes.

La aplicación Diabeto, permite utilizar un modelo de machine learning entrenado para predecir la probabilidad de diabetes tipo 2 a partir de datos clínicos ingresados por el usuario. 
Modo de uso:
El usuario accede a la aplicación web a través del enlace https://diabeto.streamlit.app.
El usuario debe responder a cada uno de los campos a través de números, cada campo tiene los números para su respuesta.
Una vez completados los campos, el usuario presiona el botón para generar la predicción.
La aplicación evalúa los datos mediante un modelo previamente entrenado (modelo de regresión logística y Ada Boost) con una precisión del 74%. El usuario recibe al final un mensaje que indica si el paciente tiene o no diabetes tipo 2.

URL data set: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv
