import streamlit as st
import requests

extender = False
virgula = False
str_fronteira = "Países com Fronteira: "
st.title("Informações do País")

pais = st.text_input("Nome do País")
if st.button("Pesquisar País"):
    response = requests.get(f"https://restcountries.com/v3.1/name/{pais}?fullText=true")
    response = response.json()
    nomeOf = response[0]['name']['official']
    fronteiras = response[0]['borders']
    for paises in fronteiras:
        if virgula == False:
            str_fronteira += paises
            virgula = True
        str_fronteira += "," + " " + paises
    latlng = response[0]['latlng']
    brasao = response[0]["coatOfArms"]['png']
    bandeira = response[0]["flags"]['png']
    extender = True
else:
    pass

if extender:
    with st.expander("See explanation"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(nomeOf)
            st.write(str_fronteira)
            st.write(f"Latitude: {round(latlng[0])}, Longitude: {round(latlng[1])}")

        with col2:
            st.image(brasao, use_column_width=True, caption= "Brasão de Armas")
        st.image(bandeira, use_column_width=True, caption= "Bandeira do País")