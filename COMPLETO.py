import pandas as pd
import streamlit as st
import ocd_data
import nome_solicitante
import tipo_de_produto
import tipo_de_certificado
import plotly.express as px
import ocd

# Menu de navegação aprimorado
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Selecione uma opção",
                         ["OCD X NOME COMERCIAL", "NOME DO SOLICITANTE", "TIPO DE PRODUTO", "TIPO DE CERTIFICADO","Certificados - OCD"])

if opcao == "OCD X NOME COMERCIAL":
    ocd_data.main()
elif opcao == "NOME DO SOLICITANTE":
    nome_solicitante.main()
elif opcao == "TIPO DE PRODUTO":
    tipo_de_produto.main()
elif opcao == "TIPO DE CERTIFICADO":
    tipo_de_certificado.main()
elif opcao == "Certificados - OCD":
    ocd.main()