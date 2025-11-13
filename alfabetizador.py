import streamlit as st
from hyphen import Hyphenator

# Definindo lista de consoantes e vogais
consoantes = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z'
]
vogais = ['a', 'e', 'i', 'o', 'u']

# Gerando todos os grupos de sílabas C+V
grupos_c_v = [c + v for c in consoantes for v in vogais]

# Inicializando separador de sílabas para português
h = Hyphenator('pt_BR')

st.title("Alfabetizador - Método Paulo Freire")
palavra = st.text_input("Digite uma palavra:")

if palavra:
    silabas = h.syllables(palavra.lower())
    st.write("**Sílabas separadas:**", silabas)
    st.write("**Todos os grupos C+V:**", grupos_c_v)
    # Grupos usados na palavra
    grupos_da_palavra = [s for s in silabas if s in grupos_c_v]
    st.write("**Grupos presentes na palavra:**", grupos_da_palavra)
    
    st.markdown("---")
    st.write("**Como funciona?**")
    st.write("- Digite qualquer palavra no campo acima.")
    st.write("- O programa separa corretamente as sílabas.")
    st.write("- Mostra todos os grupos de sílabas C+V do português.")
    st.write("- Destaca quais desses grupos aparecem na palavra digitada.")

    st.markdown("---")
    st.write("Se quiser explorar sílabas mais complexas ou outros tipos de agrupamento, fale comigo!")
