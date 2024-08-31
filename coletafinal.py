import streamlit as st
import numpy as np

diametro = 7
raio = diametro/2
valores_iniciais = 0
valores_finais = 0

def ler_dados_arquivo():
    try:
        with open('dados_recebidos.txt', 'r') as arquivo:
            dados = arquivo.readlines()
        return [int(dado.strip()) for dado in dados]
    except FileNotFoundError:
        return ["Arquivo não encontrado."]
    
def calcular_media(counter_aux):
    valores = 0
    dados_recebidos = ler_dados_arquivo()
    for i in range(10):
        if counter_aux < 10:
            valores = valores + dados_recebidos[i]
        if counter_aux >= 10:
            valores = valores + dados_recebidos[i + 10]
        if counter_aux == 9:
            break
        if counter_aux == 19:
            break 
        counter_aux+=1
        i+=1
    return (valores/10)

st.title('Calculo da densidade de um corpo')

massa = st.text_input("Insira a massa do corpo:")

if st.button('Calcular densidade'):
    media_inicial = (calcular_media(0))
    media_final = (calcular_media(10))
    Densidade = int(massa) / (np.pi * raio**2 * (media_final - media_inicial))
    st.text(f"A densidade do corpo imergido no líquido é de: {Densidade}")
