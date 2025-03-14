import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar os dados
# Carregar os dados
df= pd.read_csv(r"C:\Users\Lincon Vinicius\OneDrive\Documentos\Faculdade\BIT\DadosLimpos\ConjuntosDeDados\Atos de Outorgas de Geração\atos-outorgas-aneel.csv", sep=',')
# Converter a coluna de datas para o formato datetime
df['Ano'] = pd.to_datetime(df['DatPublicacao']).dt.year
# Agrupar por Ano e Tipo de Geração
df_grouped = df.groupby(["Ano", "SigTipoGeracao"]).size().unstack(fill_value=0)
df_pivot = df_grouped
# Verificar os dados
st.write("Dados carregados:")
st.write(df.head())  # Exibir as primeiras linhas do DataFrame para depuração


# Criar a figura com Plotly
fig = go.Figure()



# Criar gráfico de barras empilhado
fig = px.bar(
    df_pivot,
    title="Atos de outorgas ao longo dos anos",
    labels={"value": "Quantidade de Autorizações", "index": "Ano"},
    barmode='stack'
    
)

# Adicionar os valores no topo das barras
totais = df_pivot.sum(axis=1)
for i, total in enumerate(totais):
    fig.add_annotation(
        x=df_pivot.index[i],
        y=total,
        text=str(int(total)),
        showarrow=False,
        font=dict(size=10, color="black"),
        yshift=10,
    )
fig.update_layout(template='plotly_white')
st.plotly_chart(fig)
#fig.show()

#--------------------------------------------------------------------------


# Criar o gráfico de barras empilhadas
fig, ax = plt.subplots(figsize=(12, 6))

df_grouped.plot(kind='bar', stacked=True, ax=ax, colormap='tab10')

# Adicionar rótulos e título
plt.xlabel("Ano")
plt.ylabel("Quantidade de Usinas")
plt.title("Distribuição de Usinas por Ano e Tipo")
plt.legend(title="Tipo de Usina")
plt.xticks(rotation=45)

# Adicionar os valores no topo das barras
for i, year in enumerate(df_grouped.index):
    total = df_grouped.loc[year].sum()
    ax.text(i, total + 5, str(total), ha='center', fontsize=9)
    
st.pyplot(plt)