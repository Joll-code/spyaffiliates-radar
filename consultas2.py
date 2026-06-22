import streamlit as st
import pandas as pd
import urllib.parse
import random

st.set_page_config(page_title="SpyAffiliates - Plataforma Completa", layout="wide")

# ==========================================
# 1. MOTOR DE DADOS
# ==========================================
@st.cache_data(ttl=60)
def buscar_dados_das_redes():
    banco_redes = [
        {"Rede": "ClickBank", "Produto": "Custom Keto Diet"},
        {"Rede": "Digistore24", "Produto": "Tube Mastery"},
        {"Rede": "MediaScalers", "Produto": "AI Video Creator SaaS"},
        {"Rede": "Adcom", "Produto": "Forex Trading Masterclass"},
        {"Rede": "ClickBank", "Produto": "Neuro-Focus Brain Wave Audio"},
        {"Rede": "Digistore24", "Produto": "Faceless YouTube AI Automator"},
        {"Rede": "BuyGoods", "Produto": "Quantum Wealth Frequency"},
        {"Rede": "Adcom", "Produto": "TikTok Shop Dropship Blueprint"},
        {"Rede": "MediaScalers", "Produto": "Local SEO Agency In A Box"}
    ]
    
    lista = []
    for item in banco_redes:
        nome_url = urllib.parse.quote(item["Produto"])
        link_trends = f"https://trends.google.com/trends/explore?geo=US&q={nome_url}"
        
        vendas = random.randint(10, 9500)
        chance = random.randint(10, 98)
        
        if vendas < 300:
            status_concorrencia = "👻 Oculto / Oceano Azul"
        elif vendas < 2000:
            status_concorrencia = "🟢 Baixa Concorrência"
        elif vendas < 6000:
            status_concorrencia = "🟡 Média (Aquecendo)"
        else:
            status_concorrencia = "🔴 Saturado / Tubarões"
            
        score_ouro = (vendas * 0.3) + (chance * 100)
        
        lista.append({
            "Plataforma": item["Rede"],
            "Produto": item["Produto"],
            "Comissão": round(random.uniform(50.00, 299.00), 2),
            "Vendas": vendas,
            "Chance de Alta (%)": chance,
            "Concorrência": status_concorrencia,
            "Score Ouro": score_ouro,
            "Análise": link_trends # A URL crua fica armazenada aqui
        })
        
    return pd.DataFrame(lista)

df_redes = buscar_dados_das_redes()

# ==========================================
# 2. MENU LATERAL
# ==========================================
st.sidebar.title("🕵️ SpyAffiliates")
st.sidebar.markdown("Filtro Ativo: **Produtos Digitais**")

pagina_selecionada = st.sidebar.radio(
    "Navegação:",
    [
        "🏆 Top Digitais Vendidos", 
        "🚀 Oportunidades Ocultas",
        "🌐 Top 5 Redes Gringas",
        "👻 Garimpo de Ocultos"
    ]
)

st.sidebar.divider()
if st.sidebar.button("🔄 Atualizar Servidor"):
    st.cache_data.clear()

# ==========================================
# 3. REGRAS VISUAIS UNIVERSAIS (CORRIGIDO)
# ==========================================
# Aqui nós definimos como as colunas devem aparecer em TODAS as páginas
config_colunas = {
    "Plataforma": st.column_config.TextColumn("Rede"),
    "Análise": st.column_config.LinkColumn("📈 Trends", display_text="Analisar ↗"),
    "Comissão": st.column_config.NumberColumn("Comissão (USD)", format="$%.2f"),
    "Chance de Alta (%)": st.column_config.ProgressColumn("Escala / Chance", format="%f%%", min_value=0, max_value=100)
}

# ==========================================
# 4. EXIBIÇÃO DAS PÁGINAS
# ==========================================
if pagina_selecionada == "🏆 Top Digitais Vendidos":
    st.title("🏆 Top Infoprodutos")
    df_top = df_redes.sort_values(by="Vendas", ascending=False).drop(columns=["Score Ouro"])
    # Passando a regra visual para a tabela
    st.dataframe(df_top, use_container_width=True, hide_index=True, column_config=config_colunas)

elif pagina_selecionada == "🚀 Oportunidades Ocultas":
    st.title("🚀 Radar de Lançamentos")
    df_op = df_redes[df_redes["Chance de Alta (%)"] >= 50].sort_values(by="Chance de Alta (%)", ascending=False).drop(columns=["Score Ouro"])
    st.dataframe(df_op, use_container_width=True, hide_index=True, column_config=config_colunas)

elif pagina_selecionada == "🌐 Top 5 Redes Gringas":
    st.title("🌐 Painel Exclusivo de Redes")
    df_plataformas = df_redes.sort_values(by="Score Ouro", ascending=False).drop(columns=["Score Ouro"])
    rede_escolhida = st.selectbox("Selecione a Plataforma:", ["Todas"] + list(df_plataformas["Plataforma"].unique()))
    
    if rede_escolhida != "Todas":
        df_plataformas = df_plataformas[df_plataformas["Plataforma"] == rede_escolhida]
        
    st.dataframe(df_plataformas, use_container_width=True, hide_index=True, column_config=config_colunas)

elif pagina_selecionada == "👻 Garimpo de Ocultos":
    st.title("👻 Garimpo Diamante (Oceano Azul)")
    df_ocultos = df_redes[df_redes["Concorrência"] == "👻 Oculto / Oceano Azul"].sort_values(by="Comissão", ascending=False).drop(columns=["Score Ouro"])
    
    col1, col2 = st.columns(2)
    col1.metric("Produtos Ocultos", len(df_ocultos))
    if not df_ocultos.empty:
        col2.metric("Maior Comissão Oculta", f"${df_ocultos.iloc[0]['Comissão']:.2f}")
    
    st.divider()
    if not df_ocultos.empty:
        st.dataframe(df_ocultos, use_container_width=True, hide_index=True, height=400, column_config=config_colunas)
    else:
        st.info("Nenhum produto oculto detectado. Atualize o servidor.")