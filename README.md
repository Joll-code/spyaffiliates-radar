# 🕵️‍♂️ SpyAffiliates - Radar de Produtos Gringos

O **SpyAffiliates** é uma plataforma analítica desenvolvida em Python para garimpar, ranquear e analisar infoprodutos e softwares das principais redes de afiliados do mundo. 

O objetivo do sistema é cruzar dados de vendas com o volume de buscas no Google Trends, permitindo que afiliados de tráfego pago encontrem "oceanos azuis" e produtos com alto potencial de escala antes da concorrência.

---

## 🎯 Redes Monitoradas

O radar simula e filtra ofertas focadas no mercado internacional através das seguintes plataformas:
* ClickBank
* Digistore24
* BuyGoods
* MediaScalers
* Adcom

---

## 🚀 Funcionalidades Principais

* **🏆 Top Infoprodutos:** Tabela ranqueada com as ofertas digitais de maior conversão e comissão no momento.
* **📈 Inteligência de Busca (Google Trends):** Integração direta que gera links dinâmicos para analisar o volume de pesquisa exato de cada produto nos Estados Unidos (compatível com a extensão Glimpse).
* **🚀 Radar de Oportunidades:** Algoritmo que filtra e isola ofertas com mais de 50% de chance de crescimento (escala).
* **👻 Garimpo Diamante (Oceano Azul):** Filtro rigoroso que oculta produtos saturados e revela apenas ofertas com baixíssima concorrência (menos de 300 vendas) e alta comissão.
* **🌐 Filtro por Plataforma:** Sistema de abas para isolar a análise de acordo com a sua rede de preferência.

---

## 💻 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes bibliotecas e frameworks:
* **Python 3+** (Linguagem base)
* **Streamlit** (Criação do servidor web e interface gráfica)
* **Pandas** (Manipulação e estruturação de dados em DataFrames)
* **Requests / Urllib** (Comunicação com a internet e formatação de URLs)

---

## ⚙️ Como Rodar o Projeto Localmente

Se você quiser baixar o código e rodar na sua própria máquina, siga os passos abaixo:

1. Clone este repositório no seu computador.
2. Abra o terminal na pasta do projeto.
3. Instale as dependências executando o comando:
   `pip install -r requirements.txt`
4. Inicie o servidor local do Streamlit executando:
   `streamlit run consulta.py`
5. O painel abrirá automaticamente no seu navegador.
