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
        from hyphen import Hyphenator
h = Hyphenator('pt_BR')

palavra = 'casa'
silabas = h.syllables(palavra)
print(silabas)  # ['ca', 'sa']

import streamlit as st
from hyphen import Hyphenator

# Lista de consoantes comuns
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']

# Gerar todos os grupos de sílabas C+V
grupos = [c+v for c in consoantes for v in vogais]

h = Hyphenator('pt_BR')

st.title("Alfabetizador - Método Paulo Freire (Português)")
palavra = st.text_input("Digite uma palavra:")

if palavra:
    silabas = h.syllables(palavra)
    st.write("Sílabas:", silabas)
    st.write("Grupos de sílabas (C+V):", grupos)
    grupos_da_palavra = [g for g in grupos if g in silabas]
    st.write("Grupo de sílabas da palavra:", grupos_da_palavra)

        if grupo:
            st.write(f"Sílaba '{s}': grupo {grupo}")
        else:
            st.write(f"Sílaba '{s}': não pertence a grupo cadastrado")
