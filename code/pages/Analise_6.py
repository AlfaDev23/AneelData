import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px


# Carregar os dados
df = pd.read_csv(r"C:\Users\Lincon Vinicius\OneDrive\Documentos\Faculdade\BIT\DadosLimpos\ConjuntosDeDados\Liberação para operação comercial de empreendimentos de geração\unidades-geradoras-liberadas-operacao-comercial-resumido.csv")
df1 = pd.read_csv(r'C:\Users\Lincon Vinicius\OneDrive\Documentos\Faculdade\BIT\DadosLimpos\ConjuntosDeDados\Liberação para operação comercial de empreendimentos de geração\unidades-geradoras-liberadas-operacao-comercial-detalhado.csv')
st.write(df.head())  # Exibir as primeiras linhas do DataFrame para depuração


df_grouped = df[df['AnoReferencia'] > 2011].groupby(["AnoReferencia", "DescOrigemCombustivel"])["MdaSomaPotenciaMW"].sum().reset_index()

# Criar o gráfico de linhas
fig = px.line(
    df_grouped,
    x="AnoReferencia",
    y="MdaSomaPotenciaMW",
    color="DescOrigemCombustivel",
    markers=True,  # Adiciona os pontos no gráfico
    labels={"AnoReferencia": "Ano de Referência", "MdaSomaPotenciaMW": "Potência Instalada (MW)"},
    title="Evolução da Potência Instalada por Tipo de Geração"
)

# Personalizar layout
fig.update_layout(
    xaxis=dict(dtick=1),  # Garante que todos os anos sejam exibidos
    yaxis=dict(title="Potência Instalada (MW)"),
    legend_title="Tipo de Geração"
)

st.plotly_chart(fig)
# Exibir no Streamlit

#----------------------------------------------------------------------------------------------


# Converter a coluna de data para datetime
df1["DatUGInicioOpComerOutorgado"] = pd.to_datetime(df1["DatUGInicioOpComerOutorgado"], errors='coerce')

# Criar uma nova coluna com o ano de liberação
df1["Ano"] = df1["DatUGInicioOpComerOutorgado"].dt.year

# Contar o número de usinas por ano
usinas_por_ano = df1['Ano'][df1['Ano'] > 2000].value_counts().sort_index().reset_index()
usinas_por_ano.columns = ['Ano', 'Numero de Usinas']

# Criar o gráfico de barras no Plotly
fig = px.bar(
    usinas_por_ano,
    x="Ano",
    y="Numero de Usinas",
    labels={"Ano": "Ano de início das operações", "Numero de Usinas": "Número de Usinas"},
    title="Número de Usinas Liberadas para Operação Comercial por Ano",
    color_discrete_sequence=["royalblue"]
)

# Personalizar layout
fig.update_layout(
    xaxis=dict(dtick=1),  # Garante que todos os anos sejam exibidos
    yaxis=dict(gridcolor="lightgray"),
    bargap=0.1  # Ajusta espaçamento entre as barras
)

st.plotly_chart(fig)