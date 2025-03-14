import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar os dados
# Carregar os dados
df= pd.read_csv(r"C:\Users\Lincon Vinicius\OneDrive\Documentos\Faculdade\BIT\DadosLimpos\ConjuntosDeDados\Agentes de Geração de Energia Elétrica\agentes-geracao-energia-eletrica.csv", sep=';')
df['UF'] = df['CodCEG'].apply(lambda x: x[7:9])
df = df[df['DscFaseUsina'] == 'Operação']
df_pivot = df.groupby(['UF', 'SigTipoGeracao']).size().unstack()


# Verificar os dados
st.write("Dados carregados:")
st.write(df)  # Exibir as primeiras linhas do DataFrame para depuração


# Criar a figura com Plotly
fig = go.Figure()



# Criar gráfico de barras empilhado
fig = px.bar(
    df_pivot,
    x=df_pivot.index,
    y=df_pivot.columns,
    title="Distribuição de Usinas por Tipo e Estado (Escala Logarítmica)",
    labels={"value": "Quantidade de Usinas", "index": "Estado"},
    barmode='stack'
    
)
fig.update_layout(template='plotly_white')

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

st.plotly_chart(fig)


#--------------------------------------------------------------------------

# Transformar os dados para gráfico empilhado
df_reset = df.reset_index()

df_pivot = df_reset.pivot_table(index="UF", columns="SigTipoGeracao", aggfunc="size", fill_value=0)

# Criar o gráfico empilhado
ax = df_pivot.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="tab10")

# Calcular a magnitude total de cada barra
totais = df_pivot.sum(axis=1)  # Soma todas as colunas para cada estado

# Adicionar os valores no topo das barras
for i, total in enumerate(totais):
    ax.text(i, total + 1, f"{int(total)}", ha="center", fontsize=12)

# Configuração do gráfico
plt.xlabel("Estado")
plt.ylabel("Quantidade de Usinas")
plt.title("Distribuição de Usinas por Tipo e Estado")
plt.xticks(rotation=0)
plt.legend(title="Tipo de Usina")

st.pyplot(plt)