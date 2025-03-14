import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar os dados
# Carregar os dados
df = pd.read_csv(r"C:\Users\Lincon Vinicius\OneDrive\Documentos\Faculdade\BIT\DadosLimpos\ConjuntosDeDados\Bandeiras Tarifárias\bandeira-tarifaria-acionamento.csv", sep = ',')
st.write(df.head())  # Exibir as primeiras linhas do DataFrame para depuração

df['DatCompetencia'] = pd.to_datetime(df['DatCompetencia'])
df["Mes"] = df["DatCompetencia"].dt.month

# Supondo que seu DataFrame df já esteja carregado
fig = px.box(
    df,
    x="Mes",
    y="NomBandeiraAcionada",
    color="NomBandeiraAcionada",  # Define cores para cada bandeira
    category_orders={"NomBandeiraAcionada": ["Verde", "Amarela", "Vermelha P1", "Vermelha P2", "Escassez Hídrica"]},
    color_discrete_sequence=px.colors.qualitative.Set2
)

# Personalizar layout
fig.update_layout(
    title="Distribuição das Bandeiras Tarifárias por Mês",
    xaxis_title="Mês",
    yaxis_title="Bandeira Tarifária",
    boxmode="overlay",  # Sobrepor caixas se necessário
    xaxis=dict(tickmode="linear", tick0=1, dtick=1)  # Garante que os meses fiquem bem distribuídos
)

# Exibir no Streamlit (se estiver usando)
# import streamlit as st
# st.plotly_chart(fig)

st.plotly_chart(fig)




#------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(x="Mes", y="NomBandeiraAcionada", data=df, palette="Set2")
plt.xlabel("Mês")
plt.ylabel("Bandeira Tarifária")
plt.title("Distribuição das Bandeiras Tarifárias por Mês")
plt.savefig("DistribuicaoBandeiraBoxplot.png", dpi=300, bbox_inches='tight')
plt.show()
st.pyplot(plt)