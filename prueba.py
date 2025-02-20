import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Conteo de Votos')

# Función para contar votos
def contar_votos(df):
    nombres_candidatos = ['Noboa', 'Luisa']
    votos = {candidato: 0 for candidato in nombres_candidatos}
    votos['Nulos'] = 0
    
    for columna in df.columns:
        for candidato in nombres_candidatos:
            votos[candidato] += df[columna].astype(str).str.contains(candidato, case=False, na=False).sum()
        
        votos['Nulos'] += df[columna].astype(str).str.contains('Nulo', case=False, na=False).sum()
    
    return votos

# Cargar archivo
uploaded_file = st.file_uploader('Sube un archivo Excel o CSV', type=['xls', 'xlsx', 'csv'])

if uploaded_file:
    if uploaded_file.name.endswith(('xls', 'xlsx')):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    
    # Contar votos
    resultado = contar_votos(df)
    
    # Mostrar resultados inmediatamente después de cargar el archivo
    st.write("### Resultados del Conteo")
    st.write(f"- **Noboa:** {resultado['Noboa']} votos")
    st.write(f"- **Luisa:** {resultado['Luisa']} votos")
    st.write(f"- **Nulos:** {resultado['Nulos']} votos")
    
    # Crear gráfico de barras
    st.write("### Gráfico de Votos")
    fig, ax = plt.subplots()
    ax.bar(resultado.keys(), resultado.values(), color=['blue', 'red', 'gray'])
    ax.set_ylabel("Cantidad de Votos")
    ax.set_title("Distribución de Votos")
    st.pyplot(fig)
