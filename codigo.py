#titulo - sistema de vendas
# seção Cadastrar Vendas
    # Campo Data
    # CaMPO Vendedor - Ana, Bruno, Carla 
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
           # quando eu clicar no botao - adicionar a venda na tabela
# Seção Vendas Cadastradas
     # Tabela Com as Vendas
# Seção Dashboard 
        #Card/Metrica - Faturamento Total
        #Grafico De Barra/coluna - venda por vendedor
        # grafico de pizza - venda por produto

# pip install streamlit pandas plotly

import streamlit as st
import pandas as pd 
import plotly.express as px


# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")


st.write("# Sistema de Vendas")


# seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas") 
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", min_value=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

#logica de cadastro
if botao_cadastrar:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) #124 linhas
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")

# seção de visualizar as vendas 
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


# seção de dashboard
st.write("## Dashboard")

#Card/Metrica - Faturamento Total
faturamento = tabela_vendas ["valor"].sum()
st.metric("Faturamento Total", faturamento)

# Grafico De Barra/coluna - venda por vendedor
grafico1= px.bar(tabela_vendas, x="vendedor", y="valor")
st.plotly_chart(grafico1)

# Grafico de pizza - venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)