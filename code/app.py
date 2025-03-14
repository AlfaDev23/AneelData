import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()

show_pages(
    [   
        Page("code/app.py", "Dados Aneel 2024", "💻"),
        # # 2024 Content
        Section("Análises: ", "🧙‍♂️"),
        Page(r"code\pages\Analise_1.py", "Acréscimo da potência instalada", "📚", in_section=True),
        Page(r"code\pages\Analise_2.py", "Distribuição de usinas nos estados", "📚", in_section=True),
        Page(r"code\pages\Analise_3.py", "Atos de outorga", "📚", in_section=True),
        Page(r"code\pages\Analise_4.py", "Bandeiras Tarifárias", "📚", in_section=True),
        Page(r"code\pages\Analise_5.py", "Capacidade instalada por UF", "📚", in_section=True),
        Page(r"code\pages\Analise_6.py", "Liberação para operação comercial", "📚", in_section=True)
    ]
)

hide_pages(["Thank you"])

st.markdown("### Análise de dados com Streamlit e Plotly")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(r"imagens\image.png", width=300)
    

st.markdown("---")


st.markdown(
    """
    <p style="margin-bottom: 20px;text-indent: 30px;">A análise da geração e do consumo de energia no Brasil é fundamental para garantir o planejamento eficiente do setor elétrico, a segurança do abastecimento e a adoção de estratégias sustentáveis. O país possui uma matriz energética diversificada, com grande participação de fontes renováveis, como hidrelétricas, eólicas e solares. No entanto, oscilações climáticas, variações na demanda e mudanças regulatórias podem impactar significativamente o equilíbrio entre oferta e consumo. Ferramentas como Python permitem o processamento e a visualização de grandes volumes de dados, possibilitando uma compreensão mais aprofundada dos padrões de geração e consumo ao longo do tempo.</p>
    <p style="margin-bottom: 20px;text-indent: 30px;">Com bibliotecas como Pandas, NumPy e Plotly, é possível explorar séries históricas, identificar tendências e correlacionar variáveis como capacidade instalada, bandeiras tarifárias e fatores climáticos. A utilização de Python facilita a criação de modelos preditivos que ajudam na tomada de decisões estratégicas, tanto para órgãos reguladores quanto para empresas do setor. Além disso, a análise automatizada permite detectar anomalias e avaliar o impacto de políticas públicas e investimentos em novas fontes de geração.</p>
    <p style="margin-bottom: 20px;text-indent: 30px;">Outro benefício do uso de Python na análise energética é a integração com bases de dados públicas, como aquelas fornecidas pela Agência Nacional de Energia Elétrica (ANEEL) e pelo Operador Nacional do Sistema Elétrico (ONS). Isso possibilita a elaboração de estudos mais precisos sobre a expansão da infraestrutura energética e sua relação com o crescimento econômico e ambiental do Brasil. Assim, a aplicação de técnicas de ciência de dados no setor elétrico contribui para um planejamento mais eficiente e resiliente diante dos desafios do futuro.</p>
    """,
    unsafe_allow_html=True
)


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 