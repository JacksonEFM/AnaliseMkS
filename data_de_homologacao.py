import streamlit as st
import pandas as pd

@st.cache_data


def main():
    # Título da aplicação
    st.title("Análise de Homologações por Data")

    # Upload do arquivo
    uploaded_file = st.file_uploader("Faça o upload da planilha Excel", type=["xlsx"])

    if uploaded_file:
        # Carregar os dados
        data = upload.load_data(uploaded_file)

        # Verificar se a coluna "Data de Homologação" existe
        if "Data da Homologação" in data.columns:
            # Converter a coluna para o formato de data
            data["Data da Homologação"] = pd.to_datetime(data["Data da Homologação"], errors='coerce')

            # Exibir as primeiras linhas
            st.write("Prévia dos dados carregados:")
            st.dataframe(data.head())

            # Intervalo de datas
            st.sidebar.header("Filtro por Datas")
            min_date = data["Data da Homologação"].min()
            max_date = data["Data da Homologação"].max()

            # Seleção de intervalo
            date_range = st.sidebar.date_input("Selecione o intervalo de datas",
                                               [min_date, max_date],
                                               min_value=min_date,
                                               max_value=max_date)

            if len(date_range) == 2:
                start_date, end_date = date_range
                filtered_data = data[(data["Data da Homologação"] >= pd.Timestamp(start_date)) &
                                     (data["Data da Homologação"] <= pd.Timestamp(end_date))]

                # Mostrar os dados filtrados
                st.write(f"Dados filtrados entre {start_date} e {end_date}:")
                st.dataframe(filtered_data)

                # Estatísticas
                st.write("Estatísticas:")
                st.write(f"Total de homologações no período: {filtered_data.shape[0]}")

                # Gráfico (opcional)
                st.write("Distribuição por Data da Homologação:")
                st.bar_chart(filtered_data["Data da Homologação"].value_counts().sort_index())
        else:
            st.error("A coluna 'Data da Homologação' não foi encontrada no arquivo.")
    else:
        st.info("Aguardando o upload do arquivo Excel.")
if __name__ == "__main__":
    main()