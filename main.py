## Importa as bibliotecas necessárias para rodar a aplicação

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Calculadora de Análise de Portfólio Financeiro 📊')

base = st.number_input('Valor Inicial do Investimento', min_value=0.0, value=1000.0, step=100.0)
taxa_juros_anual = st.number_input('Taxa de Juros Anual (%)', min_value=0.0, value=5.0, step=0.1)
anos = st.number_input('Quantidade de Anos', min_value=1, value=10, step=1)

taxa_juros = taxa_juros_anual / 100
tempo = np.arange(1, anos + 1)
valor = base * (1+taxa_juros) ** tempo

data = pd.DataFrame({
    'Ano': tempo,
    'Valor do Investimento': valor.round(2)
})

st.subheader('Crescimento do investimento ao longo do tempo')
st.dataframe(data)

fig, ax = plt.subplots()
ax.plot(data['Ano'], data['Valor do Investimento'], marker='o')
ax.set_xlabel('Anos')
ax.set_ylabel('Valor do Investimento')
ax.set_title('Crescimento do investimento ao longo do tempo')
ax.grid(True)

st.pyplot(fig)