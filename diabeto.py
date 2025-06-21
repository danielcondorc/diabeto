import streamlit as st
import pandas as pd
import joblib
import requests
import json
import os

st.set_page_config(page_title="Detector de Diabetes", layout="centered")
def obtener_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except:
        return "IP no disponible"

def registrar_visita(ip, archivo='visitas_por_ip.json'):
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            json.dump({}, f)

    with open(archivo, 'r') as f:
        data = json.load(f)

    if ip not in data:
        data[ip] = 1
    else:
        data[ip] += 1

    with open(archivo, 'w') as f:
        json.dump(data, f)

    return len(data)

st.title("Diabeto: Detecta si tienes o eres candidato a tener Diabetes")
st.markdown(
    """
    Ingresa la información de cada campo y al final podrás conocer si tienes o eres candidato de tener Diabetes.
    **Todos los campos deben ser numéricos** según la escala indicada.
    La aplicación Diabeto, predice la probabilidad de una persona de tener diabetes tipo 2 a través un modelo de machine learning con un 74% de precisión. 
    """
)

ip_usuario = obtener_ip()
total_ips = registrar_visita(ip_usuario)
st.sidebar.markdown(f"🌎 Visitas únicas: **{total_ips}**")

# Botón para seleccionar modelo
modelo_opcion = st.selectbox("Selecciona el modelo que deseas usar:",
                             ["adaboost_model.pkl", "best_adaboost_model.pkl"])

# Diccionario para almacenar la entrada del usuario
inputs = {}

st.subheader("Completa la siguiente información:")

# Lista de variables y sus descripciones traducidas
campos = [
    ("Presión arterial alta", "HighBP", "0 = no, 1 = sí"),
    ("Colesterol alto", "HighChol", "0 = no, 1 = sí"),
    ("Control de colesterol en los últimos 5 años", "CholCheck", "0 = no, 1 = sí"),
    ("Índice de masa corporal", "BMI", "1 = Bajo peso, 2 = Peso normal, 3 = Sobrepeso, 4 = Obesidad"),
    ("Fumador", "Smoker", "0 = no, 1 = sí"),
    ("Tuvo un derrame cerebral", "Stroke", "0 = no, 1 = sí"),
    ("Enfermedad cardíaca", "HeartDiseaseorAttack", "0 = no, 1 = sí"),
    ("Actividad física", "PhysActivity", "0 = no, 1 = sí"),
    ("Consume frutas", "Fruits", "0 = no, 1 = sí"),
    ("Consume vegetales", "Veggies", "0 = no, 1 = sí"),
    ("Alto consumo de alcohol", "HvyAlcoholConsump", "0 = no, 1 = sí"),
    ("Seguro de salud (SIS, EsSalud, Privado)", "AnyHealthcare", "0 = no, 1 = sí"),
    ("No pudo ir al médico por costo", "NoDocbcCost", "0 = no, 1 = sí"),
    ("Salud general (1 = excelente a 5 = mala)", "GenHlth", "1 a 5"),
    ("Días de mala salud mental (últimos 30 días)", "MentHlth", "0 a 30"),
    ("Días de mala salud física (últimos 30 días)", "PhysHlth", "0 a 30"),
    ("Dificultad para caminar", "DiffWalk", "0 = no, 1 = sí"),
    ("Sexo", "Sex", "0 = mujer, 1 = varón"),
    ("Edad", "Age", "1=31–40, 2=41–50, 3=51–60, 4=61–70, 5=71–80, 6=81+"),
    ("Educación", "Education", "1 = no secundaria, 2 = secundaria, 3 = universitaria incompleta, 4 = universidad completa"),
    ("Ingresos anuales", "Income", "1=<10k, 2=10-14k, 3=15-19k, 4=20-24k, 5=25-34k, 6=35-49k, 7=50-75k, 8=>75k")
]

# Crear los campos de entrada
for etiqueta, clave, ayuda in campos:
    valor = st.number_input(f"{etiqueta} ({ayuda})", min_value=0, step=1, format="%d")
    inputs[clave] = valor

# Botón para predecir
if st.button("Detectar Diabetes"):
    try:
        # Cargar el modelo
        modelo = joblib.load(modelo_opcion)

        # Crear el DataFrame para predicción
        input_df = pd.DataFrame([inputs])
        prediccion = modelo.predict(input_df)[0]

        if prediccion == 0:
            resultado = "No Diabetes"
        else:
            resultado = "Pre Diabetes o Diabetes"

        st.success(f"Resultado del análisis: **{resultado}**")

    except Exception as e:
        st.error(f"Ocurrió un error al cargar el modelo o hacer la predicción: {e}")
