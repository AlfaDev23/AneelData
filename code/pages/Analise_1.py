import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
# Carregar os dados
# Carregar os dados
df = pd.read_csv(r"C:\Users\Lincon Vinicius\OneDrive\Documentos\Faculdade\BIT\DadosLimpos\ConjuntosDeDados\Acréscimo anual da potência instalada\acrescimo-anual-potencia-instalada.csv", sep=';')
# Verificar os dados
st.write("Dados carregados:")
st.write(df.head())  # Exibir as primeiras linhas do DataFrame para depuração

# Criar a figura com Plotly
fig = go.Figure()

# Adicionar a primeira linha (MdaPotenciaMW)
fig.add_trace(go.Scatter(
    x=df["AnoReferencia"],
    y=df["MdaPotenciaMW"],
    mode='lines+markers',
    name='MdaPotencia (MW)',
    line=dict(color='blue'),
    marker=dict(color='blue')
))

# Adicionar a segunda linha (MdaAcrescimoPotenciaMW)
fig.add_trace(go.Scatter(
    x=df["AnoReferencia"],
    y=df["MdaAcrescimoPotenciaMW"],
    mode='lines+markers',
    name='MdaAcrescimoPotencia (MW)',
    line=dict(color='red'),
    marker=dict(color='red', symbol='square'),
    yaxis='y2'  # Mapear para o segundo eixo Y
))

# Layout do gráfico
fig.update_layout(
    title="Comparação de Dados",
    xaxis=dict(title="AnoReferencia", range=[min(df['AnoReferencia']), max(df['AnoReferencia'])]),
    yaxis=dict(title=dict(text='MdaPotencia (MW)', font=dict(color='blue')), tickfont=dict(color='blue'), range=[0, 200000]),
    yaxis2=dict(title=dict(text='MdaAcrescimoPotencia (MW)', font=dict(color='red')), tickfont=dict(color='red'),
                overlaying='y', side='right')
)

# Exibir no Streamlit
st.title("Análise de Capacidade Instalada e Acréscimos")
st.plotly_chart(fig)
def plot_comparacao_duplo_eixo(df, coluna_x, coluna_y1, coluna_y2, 
                               label_y1, label_y2,
                               titulo="Comparação de Dados",
                               cor_y1="blue", cor_y2="red"):

    fig, ax1 = plt.subplots(figsize=(10, 5))  # Criando a figura e eixo primário

    # Primeiro eixo Y (esquerda)
    ax1.set_xlabel(coluna_x)
    ax1.set_ylabel(label_y1, color=cor_y1)
    ax1.plot(df[coluna_x], df[coluna_y1], marker='o', linestyle='-', label=label_y1, color=cor_y1)
    ax1.tick_params(axis='y', labelcolor=cor_y1)
    ax1.grid(True, linestyle='--', alpha=0.5)  # Adiciona grid com transparência

    # Segundo eixo Y (direita)
    ax2 = ax1.twinx()  # Criando um segundo eixo Y
    ax2.set_ylabel(label_y2, color=cor_y2)
    ax2.plot(df[coluna_x], df[coluna_y2], marker='s', linestyle='--', label=label_y2, color=cor_y2)
    ax2.tick_params(axis='y', labelcolor=cor_y2)

    plt.title(titulo)
    fig.tight_layout()  # Ajusta layout para evitar sobreposição
    return fig

x = "AnoReferencia"
y_1 = "MdaPotenciaMW"
y_2 = "MdaAcrescimoPotenciaMW"
label_1 = "MdaPotencia (MW)"
label_2 = "MdaAcrescimoPotencia (MW)"

figura = plot_comparacao_duplo_eixo(df,x,y_1,y_2, label_y1= label_1, label_y2=label_2)

st.write(figura)