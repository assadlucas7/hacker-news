# Hacker News Top Stories Visualization

## Descrição

Este projeto busca e visualiza as principais histórias do site Hacker News. Utilizando a API do Hacker News, o script recupera as histórias mais discutidas no momento e as exibe em um gráfico de barras.

## Funcionalidades

- Busca as 30 principais histórias do site Hacker News.
- Ordena as histórias com base no número de comentários.
- Visualiza os resultados em um gráfico de barras, com links clicáveis para cada história.

## Pré-requisitos

Você precisará do seguinte para executar este projeto:

- Python instalado em sua máquina.
- Bibliotecas: `requests`, `pygal`.

## Instalação

1. **Instalação das Bibliotecas**:
   - Use o comando abaixo para instalar as bibliotecas necessárias:
     ```bash
     pip install requests pygal
     ```

## Como Usar

1. **Execução do Programa**:
   - Execute o programa com o comando:
     ```bash
     python nome_do_seu_arquivo.py
     ```
   - Após executar o programa, ainda no terminal, irá mostrar o status_code de cada chamada de API. '200' informa que a chamada foi bem sucedida.

2. **Visualização do Gráfico**:
   - Após executar o programa, você encontrará um arquivo chamado `hn_submissions.svg` no diretório atual.
   - Abra este arquivo em um navegador de sua escolha para visualizar o gráfico das histórias mais discutidas do Hacker News.

## Contribuição

Para contribuir com este projeto, faça um fork, realize suas alterações e abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` no repositório para obter mais detalhes.


