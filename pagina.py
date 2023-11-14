import streamlit as st
import requests

#Alguns verificadores que julguei nescessario
extender = False # Caso eh nescessario ou nao o extender
virgula = False # Se preciso ou nao adicionar virgula na lista de paises que fazem fronteiras

str_fronteira = "Países com Fronteira: "
st.title("Informações do País")

pais = st.text_input("Nome do País")
if st.button("Pesquisar País"):
    # Try Except para fazer verificacao de erro
    # Neste caso se o nome do pais existe
    try:
        # Requisicao https
        response = requests.get(f"https://restcountries.com/v3.1/name/{pais}?fullText=true")
        response = response.json()

        #Tratando as Variaveis nescessarias
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
    except:
        # Mensagem de erro
        st.warning("Achou que não teria mensagem de erro?")
        st.warning("Escreve ai um pais que existe fazendo favor")

# Verifico a nescessidade do Extender
if extender:
    with st.expander("See explanation"):
        col1, col2 = st.columns(2)
        with col1:
            # Informacoes Primeira Coluna
            st.write(nomeOf)
            st.write(str_fronteira)
            st.write(f"Latitude: {round(latlng[0])}, Longitude: {round(latlng[1])}")

        with col2:
            # Informacoes Segunda Coluna
            st.image(brasao, use_column_width=True, caption= "Brasão de Armas")

        # Fora das Colunas mas Dentro do Extender
        st.image(bandeira, use_column_width=True, caption= "Bandeira do País")