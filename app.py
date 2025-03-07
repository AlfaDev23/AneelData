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
        Page(r"code\pages\Analise_5.py", "Capacidade instalada por UF", "📚", in_section=True)
    ]
)

hide_pages(["Thank you"])

st.markdown("### Análise de dados com Streamlit e Plotly")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(r"imagens\image.png", width=300)
    

st.markdown("---")



hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 