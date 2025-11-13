import streamlit as st
import re

# Função básica para separar sílabas (simples, para exemplo didático)
def separar_silabas(palavra):
    return re.findall(r'[^aeiou]*[aeiou]+[^aeiou]*', palavra.lower())

# Grupos de sílabas do método Paulo Freire (exemplo para C + V)
grupos = [
    ['ca', 'co', 'cu'],
    ['sa', 'se', 'si', 'so', 'su'],
    # Você pode adicionar outros grupos conforme necessário
]

def grupo_silaba(silaba):
    for grupo in grupos:
        if silaba in grupo:
            return grupo
    return []

st.title("Alfabetizador - Método Paulo Freire")

palavra = st.text_input("Digite uma palavra:")

if palavra:
    silabas = separar_silabas(palavra)
    st.write("Sílabas:", silabas)
    
    for s in silabas:
        grupo = grupo_silaba(s)
        if grupo:
            st.write(f"Sílaba '{s}': grupo {grupo}")
        else:
            st.write(f"Sílaba '{s}': não pertence a grupo cadastrado")
