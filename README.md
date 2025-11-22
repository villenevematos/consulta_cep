# Conector de API (Excel + API)

* **O que ele faz?** <br>
Este script lê uma lista de CEPs de uma planilha Excel, conecta-se a uma API pública (ViaCEP) para consultar cada um deles e exibe o endereço completo (Rua, Bairro, Cidade, UF) no terminal. É um exemplo clássico de automação de consulta em lote.
* **Habilidades:** <br>
Consumo de APIs REST (`requests`)<br>
Manipulação de dados em planilhas (`pandas`)<br>
Integração de sistemas (Excel -> Python -> Web -> Python)<br>
Tratamento de dados JSON

* **Como Usar:** <br>

1. Crie um arquivo `dados.xlsx` com uma coluna chamada "CEP" e insira alguns números de CEP.<br>
2. Execute o script (`python consulta_cep.py`).<br>
3. O script lerá cada linha, buscará os dados na internet e mostrará o resultado logradouro no terminal.
