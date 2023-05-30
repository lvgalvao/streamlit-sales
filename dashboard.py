import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Dados de exemplo
df = pd.DataFrame({
    'Tag': ['Python', 'Data Science', 'Machine Learning', 'Visualization', 'Big Data', 'Statistics'],
    'Count': [100, 80, 70, 60, 50, 40]
})

# Criação do gráfico de nuvem de tags
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(zip(df['Tag'], df['Count'])))

# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Gráfico de Nuvem de Tags')
plt.show()
st.pyplot()

