import streamlit as st
import pandas as pd
import upload



def main():
    # Título da aplicação
    st.title("Análise por Nome do Solicitante")

    # Upload do arquivo
    uploaded_file = st.file_uploader("Faça o upload da planilha Excel", type=["xlsx"])

    if uploaded_file:
        # Carregar os dados
        data = upload.load_data(uploaded_file)

        # Verificar se a coluna "Nome do Solicitante" existe
        if "Nome do Solicitante" in data.columns:
            # Exibir uma prévia dos dados
            st.write("Prévia dos dados carregados:")
            st.dataframe(data.head())

            # Estatísticas gerais
            st.subheader("Estatísticas Gerais")
            solicitante_counts = data["Nome do Solicitante"].value_counts()
            st.write(f"Total de solicitantes distintos: {solicitante_counts.shape[0]}")
            st.write(f"Distribuição dos solicitantes:")
            st.dataframe(solicitante_counts)

            # Gráfico de barras
            st.subheader("Gráfico de Distribuição dos Solicitantes")
            st.bar_chart(solicitante_counts.head(10))  # Mostrar os 10 solicitantes mais frequentes

            # Filtrar por um solicitante específico
            st.sidebar.header("Filtrar por Nome do Solicitante")
            selected_solicitante = st.sidebar.selectbox("Selecione um solicitante", solicitante_counts.index)

            if selected_solicitante:
                filtered_data = data[data["Nome do Solicitante"] == selected_solicitante]
                st.write(f"Dados filtrados para o solicitante: {selected_solicitante}")
                st.dataframe(filtered_data)
                st.write(f"Total de registros para {selected_solicitante}: {filtered_data.shape[0]}")

        else:
            st.error("A coluna 'Nome do Solicitante' não foi encontrada no arquivo.")
    else:
        st.info("Aguardando o upload do arquivo Excel.")
if __name__ == "__main__":
    main()