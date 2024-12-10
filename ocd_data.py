import pandas as pd
import streamlit as st
import plotly.express as px
import upload


def classify_certificado(certificado):
    certificado_str = str(certificado)

    if certificado_str.isdigit() and 1 <= int(certificado_str) <= 150000:
        return "IBRACE"
    elif len(certificado_str) == 9 and certificado_str[3] == "-" and certificado_str[6] == "-" or "ACERT" in certificado_str or "CCT" in certificado_str:
        return "ACERT"
    elif "/" in certificado_str and certificado_str.replace("/", "").replace(".", "").isdigit():
        return "ACERT"
    elif "OCD" in certificado_str and "ABCP" not in certificado_str:
        return "BRICS"
    elif "ABCP" in certificado_str:
        return "ABCP"
    elif "MODERNA" in certificado_str:
        return "MODERNA"
    elif "ICC" in certificado_str:
        return "ICC"
    elif "TÜV" in certificado_str:
        return "TUV"
    elif "TEL" in certificado_str:
        return "ACTA"
    elif "BRA" in certificado_str:
        return "BR APPROVAL"
    elif "BRC" in certificado_str:
        return "BRACERT"
    elif "CCPE" in certificado_str:
        return "CCPE"
    elif "CPQD" in certificado_str:
        return "CPQD"
    elif "CTCP" in certificado_str:
        return "CTCP"
    elif "DEKRA" in certificado_str:
        return "DEKRA"
    elif "ELD" in certificado_str:
        return "ELDORADO"
    elif "IBR" in certificado_str:
        return "IBR TECH"
    elif "TELECOM" in certificado_str:
        return "INTERTEK"
    elif "LMP" in certificado_str:
        return "LMP"
    elif "MT" in certificado_str:
        return "MASTER"
    elif "NCC" in certificado_str:
        return "NCC"
    elif "OCP" in certificado_str:
        return "OCPTELLI"
    elif "PCN" in certificado_str:
        return "PCN"
    elif "QC" in certificado_str:
        return "QCCERT"
    elif "7C" in certificado_str:
        return "SEVEN COMPLIANCE"
    elif "UL-BR" in certificado_str:
        return "UL"
    elif "Versys" in certificado_str:
        return "VERSYS"
    elif len(certificado_str) == 8 and certificado_str.startswith("100"):
        return "TECPAR CERT"
    else:
        return "OUTROS"
def main():
    # Título da aplicação
    st.title("Análise Nome Comercial e OCD")

    # Upload do arquivo
    uploaded_file = upload.upload()

    if uploaded_file:
        # Carregar os dados
        data = upload.load_data(uploaded_file)

        # Verificar se as colunas necessárias existem
        if "Data da Homologação" in data.columns and "Certificado de Conformidade Técnica" in data.columns:
            # Garantir que a coluna Data da Homologação está no formato de data
            data["Data da Homologação"] = pd.to_datetime(data["Data da Homologação"], errors='coerce')

            # Remover linhas com datas inválidas
            data = data.dropna(subset=["Data da Homologação"])

            # Aplicar a função de classificação
            data["OCD Classificação"] = data["Certificado de Conformidade Técnica"].apply(classify_certificado)

            # Selecionar intervalo de datas
            st.sidebar.header("Selecione o intervalo de datas")
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

                # Contagem de certificações por OCD
                ocd_counts = filtered_data["OCD Classificação"].value_counts().reset_index()
                ocd_counts.columns = ["OCD", "Count"]

                # Exibir os resultados
                st.subheader(f"Certificações por OCD ({start_date} a {end_date})")

                # Gráfico de barras
                st.bar_chart(ocd_counts.set_index("OCD"))

                # Gráfico de Pizza Interativo
                st.subheader("Distribuição de Certificações por OCD (Gráfico Interativo)")
                fig = px.pie(ocd_counts, values="Count", names="OCD", title="Distribuição por OCD")
                st.plotly_chart(fig)

                st.dataframe(filtered_data)

                # Tentativa final para salvar o arquivo em um local padrão acessível
                #output_path = "Produtos_Homologados_Classificado_Final.xlsx"

                # Salvando novamente
                #filtered_data.to_excel(output_path, index=False)



        else:
            st.error("As colunas necessárias ('Data da Homologação', 'Certificado de Conformidade Técnica') não foram encontradas no arquivo.")
    else:
        st.info("Aguardando o upload do arquivo Excel.")
if __name__ == "__main__":
    main()