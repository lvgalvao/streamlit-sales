import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk

def main():
    st.title("Fotográfia do sucesso - Key Account")
    st.write("Coleta dia 27/05, Brasil, Ifood")
    
    # Ler arquivo CSV
    df = pd.read_csv("key_account_fake_store_locations.csv")
    
    # Exibir dados do CSV como uma tabela
    st.subheader("Dados do CSV")
    st.dataframe(df)

    # Obter as marcas de lojas únicas
    marcas_unicas = df['STORE_BRAND'].unique()

    # Checkbox para selecionar todas as marcas de lojas
    selecionar_todas = st.checkbox("Selecionar Todas")
    
    # Criar checkboxes para seleção de marcas
    if selecionar_todas:
        marcas_selecionadas = st.multiselect('Selecione as Marcas de Lojas', marcas_unicas, default=marcas_unicas)
    else:
        marcas_selecionadas = st.multiselect('Selecione as Marcas de Lojas', marcas_unicas)

    # Filtrar o dataframe com base nas marcas selecionadas
    df_filtrado = df[df['STORE_BRAND'].isin(marcas_selecionadas)]

    # Definir os dados para cada eixo
    x = df_filtrado['AVG_COMBO']
    y = df_filtrado['AVG_OCURRENCE_TITLE']
    raio = df_filtrado['COUNT_STORES'] * 2  # Ajustar o fator de escala conforme necessário

    # Criar o gráfico de dispersão
    st.subheader("Gráfico de Dispersão")
    st.markdown("O gráfico de dispersão mostra a relação entre 'AVG_COMBO' e 'AVG_OCURRENCE_TITLE', sendo o raio do círculo indicativo da contagem de marcas de lojas.")
    fig, ax = plt.subplots(figsize=(8, 6))
    dispersao = ax.scatter(x, y, s=raio, alpha=0.5)

    # Definir os rótulos e título
    ax.set_xlabel('AVG_COMBO')
    ax.set_ylabel('AVG_OCURRENCE_TITLE')
    ax.set_title('Gráfico de Dispersão com Raio do Círculo como Contagem')

    # Adicionar uma legenda de barra de cores
    barra_cores = fig.colorbar(dispersao)
    barra_cores.set_label('Contagem de Marca de Loja')

    # Obter as 3 principais marcas de lojas
    top_marcas = df_filtrado.nlargest(3, 'COUNT_STORES')
    top_x = top_marcas['AVG_COMBO']
    top_y = top_marcas['AVG_OCURRENCE_TITLE']
    top_raio = top_marcas['COUNT_STORES'] * 2
    top_marcas_lojas = top_marcas['STORE_BRAND']

    # Criar um gráfico de dispersão separado para as principais marcas de lojas com círculos maiores e rótulos
    ax.scatter(top_x, top_y, s=top_raio, color='red', alpha=0.5)
    for i, marca in enumerate(top_marcas_lojas):
        ax.annotate(marca, (top_x.iloc[i], top_y.iloc[i]), fontsize=8, ha='center')

    # Exibir o gráfico
    st.pyplot(fig)

    # Mapa do Brasil com as localizações das lojas usando pydeck
    st.subheader("Localizações das Lojas no Mapa")
    st.markdown("O mapa mostra as localizações das lojas no Brasil.")
    latitudes = df_filtrado['LATITUDE']
    longitudes = df_filtrado['LONGITUDE']

    # Criar a camada de gráfico de dispersão do pydeck
    camada = pdk.Layer(
        "ScatterplotLayer",
        data=df,  # Usar o dataframe original em vez de df_filtrado
        get_position=["LONGITUDE", "LATITUDE"],
        get_color=[255, 0, 0],  # Cor vermelha para os pontos
        get_radius=50000,  # Ajustar o tamanho do raio conforme necessário
        pickable=True,
    )

    # Definir a vista inicial para o mapa
    estado_visualizacao = pdk.ViewState(latitude=-14.235004, longitude=-51.92528, zoom=4)

    # Criar o deck pydeck
    deck = pdk.Deck(layers=[camada], initial_view_state=estado_visualizacao)

    # Exibir o mapa
    st.pydeck_chart(deck)

    # Seção de Tarefas com 5 recomendações geradas pelo ChatGPT
    st.subheader("Tarefas")

    # Recomendação 1
    recomendacao1 = "- Entrar em contato com o gerente da marca McDonald's para discutir a falta de combos disponíveis."
    recomendacao1_checkbox = st.checkbox("Recomendação Insight Team", value=False)
    if recomendacao1_checkbox:
        st.markdown(f"<s>{recomendacao1}</s>", unsafe_allow_html=True)
    else:
        st.markdown(recomendacao1)

    # Recomendação 2
    recomendacao2 = "- Explorar a distribuição das marcas de lojas em diferentes regiões do Brasil."
    recomendacao2_checkbox = st.checkbox("Recomendação Insight Team 2", value=False)
    if recomendacao2_checkbox:
        st.markdown(f"<s>{recomendacao2}</s>", unsafe_allow_html=True)
    else:
        st.markdown(recomendacao2)

    # Recomendação 3
    recomendacao3 = "- Investigar a correlação entre o número de lojas e a média do combo."
    recomendacao3_checkbox = st.checkbox("Dica do Vini", value=False)
    if recomendacao3_checkbox:
        st.markdown(f"<s>{recomendacao3}</s>", unsafe_allow_html=True)
    else:
        st.markdown(recomendacao3)

    # Recomendação 4
    recomendacao4 = "- Comparar o desempenho das diferentes marcas de lojas com base na contagem de marcas."
    recomendacao4_checkbox = st.checkbox("Dica do Vini 2", value=False)
    if recomendacao4_checkbox:
        st.markdown(f"<s>{recomendacao4}</s>", unsafe_allow_html=True)
    else:
        st.markdown(recomendacao4)


    # Botão para download do arquivo CSV
    st.subheader("Download do Arquivo CSV")
    st.write("Faça o download do arquivo 'key_account_fake_store_locations.csv'")
    st.markdown(get_csv_download_link(df_filtrado), unsafe_allow_html=True)

def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    href = f'<a href="data:file/csv;base64,{csv}" download="key_account_fake_store_locations.csv">Download CSV</a>'
    return href

if __name__ == "__main__":
    main()
