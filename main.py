#Processos que deverão ser atendidos:
#1 OCDs - Total de certificados
#2 OCDs - Modelos certificados
#3 Solicitante - Total de certificados
#4 Campos a adicionar na tabela - OCD e Tipo de certificado




# Reimportar as bibliotecas necessárias
import pandas as pd

# Recarregar o arquivo Excel enviado
file_path = "Produtos_Homologados_Anatel.xlsx"
data = pd.read_excel(file_path)

# Lista de OCDs para separação
ocds = ["Moderna", "NCC", "IBRACE", "CPQD", "MASTER", "UL", "OCPTELLI", "ICC"]

# Criar um dicionário para armazenar os dados filtrados por OCD
dados_por_ocd = {ocd: data[data['Certificado de Conformidade Técnica'].str.contains(ocd, na=False, case=False)]
                 for ocd in ocds}

# Contar o número de registros por OCD
contagem_por_ocd = {ocd: len(dados) for ocd, dados in dados_por_ocd.items()}

print(contagem_por_ocd)
