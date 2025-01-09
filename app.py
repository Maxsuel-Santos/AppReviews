# execute o comando 'streamlit run nomedoarquivo.py' para executar a aplicação no localhost
import streamlit as st # importa a biblioteca streamlit
import pandas as pd # importa a biblioteca pandas
import plotly.express as px # importa a função 'express' da biblioteca 'plotly'

st.set_page_config(layout="wide") # Define o layout em tela inteira por padrão

df_reviews = pd.read_csv("datasets/customerReviews.csv") # Carrega e ler um arquivo csv e armazena em uma variável
df_top100_books = pd.read_csv("datasets/Top-100TrendingBooks.csv") # Carrega e ler um arquivo csv e armazena em uma variável

price_max = df_top100_books["book price"].max() # Pega o valor máximo da coluna 'book price' e armazena em uma variável
price_min = df_top100_books["book price"].min() # Pega o valor mínimo da coluna 'book price' e armazena em uma variável

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max) # Usa o valor máximo e mínimo da coluna 'book price' do arquivo csv para criar um slider para o usuário alternar entre esses valores como filtro
df_books = df_top100_books[df_top100_books["book price"] <= max_price] # Mostra todos os intens do csv que tenham o preço igual ou menos do que o valor máximo
df_books

fig = px.bar(df_books["year of publication"].value_counts()) # Põe em uma variável quantas vezes (uma contagem) um determinado ano de publicação em um livro tem (conta as ocorrências de ano de lançamento dos livros em forma de barras)
fig2 = px.histogram(df_books["rating"]) # Põe em uma variável quantas vezes (uma contagem) um determinado rating de um livro (conta as ocorrências de rating dos livros em forma de histograma)

st.plotly_chart(fig) # Exibe o gráfico em barra (bar) em coluna
st.plotly_chart(fig2) # Exibe o gráfico em histograma (histogram) em coluna