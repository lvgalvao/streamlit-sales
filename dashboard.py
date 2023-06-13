import streamlit as st
import pandas as pd

# Função para calcular insights e visualizações dos dados
def calcular_informacoes_vendas(df):
    # Cálculo das estatísticas de vendas
    total_vendas = df['Vendas'].sum()
    media_vendas = df['Vendas'].mean()
    max_vendas = df['Vendas'].max()
    min_vendas = df['Vendas'].min()

    # Display dos insights
    st.write('Total de Vendas:', total_vendas)
    st.write('Média de Vendas:', media_vendas)
    st.write('Maior Venda:', max_vendas)
    st.write('Menor Venda:', min_vendas)

    # Visualização do gráfico de vendas
    st.subheader('Gráfico de Vendas')
    st.bar_chart(df['Vendas'])

# Streamlit app
st.title('Análise de Vendas')

# Carregamento dos dados
st.header('Carregar Dados')
data_file = st.file_uploader('Upload de arquivo CSV', type=['csv'])

if data_file is not None:
    # Leitura do arquivo CSV
    df = pd.read_csv(data_file)

    # Display dos dados carregados
    st.subheader('Dados Carregados')
    st.write(df)

    # Cálculo das informações de vendas e exibição
    st.header('Informações de Vendas')
    calcular_informacoes_vendas(df)
