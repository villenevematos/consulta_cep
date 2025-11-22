import pandas as pd
import requests

# Nome do arquivo Excel que já existe e será lido
arquivo_excel = 'dados.xlsx'

try:
    # Tenta ler o arquivo Excel e carregar os dados em um DataFrame
    df_cep = pd.read_excel(arquivo_excel)

    # Se a leitura for bem-sucedida, imprime mensagem de confirmação
    print("Dados lidos do Excel com sucesso:")

except FileNotFoundError:
    # Caso o arquivo não seja encontrado, imprime mensagem de erro
    print(f"ERRO: O arquivo '{arquivo_excel}' não foi encontrado.")
except Exception as e:
    # Captura qualquer outro erro inesperado e imprime a mensagem
    print(f"Ocorreu um erro: {e}")

# Define a Unidade Federativa (estado) e a cidade para consulta
uf = 'SP'
cidade = 'São Paulo'

# Monta a URL da API ViaCEP para buscar endereços da região "Centro" da cidade
url = f'https://viacep.com.br/ws/{uf}/{cidade}/Centro/json/'

# Faz a requisição HTTP para a API e já converte a resposta para JSON
response = requests.get(url).json()

# Cria um dicionário vazio para armazenar os dados de CEPs
dict_dados = {}

# Itera sobre cada item retornado pela API (cada item é um dicionário com informações do CEP)
for dicinario_cep in response:
    # Extrai o CEP, removendo o hífen e convertendo para inteiro
    cep = int(dicinario_cep['cep'].replace('-', ''))
    # Extrai o logradouro (endereço)
    endereco = dicinario_cep['logradouro']
    # Extrai o bairro
    bairro = dicinario_cep['bairro']
    # Adiciona os dados ao dicionário, usando o CEP como chave
    dict_dados[cep] = {'endereco': endereco, 'bairro': bairro}

# Imprime o dicionário com os dados coletados
print(dict_dados)

# Converte o dicionário em um DataFrame do pandas
# orient='index' indica que as chaves do dicionário (CEPs) serão usadas como índice
# rename_axis renomeia o índice para "CEP"
# reset_index transforma o índice em uma coluna normal
df_cep_novo = pd.DataFrame.from_dict(dict_dados, orient='index').rename_axis('CEP').reset_index()

# Concatena os dados lidos do Excel (df_cep) com os novos dados obtidos da API (df_cep_novo)
# ignore_index=True faz com que o índice seja reordenado de forma sequencial
df_final = pd.concat([df_cep, df_cep_novo], ignore_index=True)

# Salva o DataFrame final em um novo arquivo Excel chamado "dados_atualizados.xlsx"
# index=False evita que o índice seja salvo como coluna no Excel
df_final.to_excel('dados_atualizados.xlsx', index=False)