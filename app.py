import requests
import pandas as pd
import streamlit as st

def get_data():
    url = "https://mindicador.cl/api/dolar"
    r = requests.get(url, timeout=20)
    data = r.json()
    df = pd.DataFrame(data["serie"])
    df["fecha"] = pd.to_datetime(df["fecha"])
    df = df.rename(columns={"valor": "dolar"})
    return df.sort_values("fecha")

st.set_page_config(page_title="Dólar Chile")
st.title("Indicadores Económicos - Dólar en Chile")
st.write("Datos obtenidos desde [mindicador.cl](https://mindicador.cl/api)")

df = get_data()
dias = st.slider("Seleccione número de días", 10, 90, 30)
df_filtrado = df.tail(dias)

st.line_chart(df_filtrado.set_index("fecha")["dolar"])
st.dataframe(df_filtrado)
