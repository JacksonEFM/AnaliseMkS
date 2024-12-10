
import streamlit as st
import pandas as pd
import upload

# Função para carregar o arquivo Excel

def main():
    st.title("Análise por Tipo do Produto")

    # Upload do arquivo
    uploaded_file = upload.upload()

    if uploaded_file:
        # Carregar os dados
        data = upload.load_data(uploaded_file)

        # Verificar se a coluna "Tipo do Produto" existe
        if "Tipo do Produto" in data.columns:
            # Exibir uma prévia dos dados
            st.write("Prévia dos dados carregados:")
            st.dataframe(data.head())

            # Estatísticas gerais
            st.subheader("Estatísticas Gerais")
            tipo_counts = data["Tipo do Produto"].value_counts()
            st.write(f"Total de tipos de produtos distintos: {tipo_counts.shape[0]}")
            st.write(f"Distribuição dos tipos de produtos:")
            st.dataframe(tipo_counts)

            # Gráfico de barras
            st.subheader("Gráfico de Distribuição dos Tipos de Produtos")
            st.bar_chart(tipo_counts)

            # Filtrar por um tipo específico
            st.sidebar.header("Filtrar por Tipo do Produto")
            selected_tipo = st.sidebar.selectbox("Selecione um tipo de produto", tipo_counts.index)

            if selected_tipo:
                filtered_data = data[data["Tipo do Produto"] == selected_tipo]
                st.write(f"Dados filtrados para o tipo de produto: {selected_tipo}")
                st.dataframe(filtered_data)
                st.write(f"Total de registros para {selected_tipo}: {filtered_data.shape[0]}")

        else:
            st.error("A coluna 'Tipo do Produto' não foi encontrada no arquivo.")
    else:
        st.info("Aguardando o upload do arquivo Excel.")
if __name__ == "__main__":
    main()