# Projeto de Automação de Preços de Criptomoedas

Este projeto tem como objetivo automatizar a coleta de preços de criptomoedas de diferentes rotas do site CoinMarketCap. Utilizando o Selenium para interagir com a página web, o script busca os preços atualizados e armazena esses dados em um arquivo JSON. Além disso, foi desenvolvido um front-end com Flask que exibe esses preços em uma interface web.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

1. **coin_fetcher.py**: Contém as funções que realizam a coleta de preços das criptomoedas.
2. **config.json**: Um arquivo de configuração que armazena a URL base do CoinMarketCap e as rotas específicas para as criptomoedas que serão monitoradas.
3. **main.py**: O arquivo principal que executa a função de coleta de preços em intervalos regulares.
4. **app.py**: Um aplicativo Flask que serve uma interface web para exibir os preços das criptomoedas.
5. **prices.html**: A página HTML que apresenta os preços de forma organizada.

## Dependências

O projeto utiliza o Selenium e Flask. As dependências estão listadas no arquivo `requirements.txt`:

- selenium==4.25.0
- Flask
- flask-cors

## Instalação

1. Clone o repositório:
   - `git clone <URL_DO_REPOSITORIO>`
   - `cd <NOME_DO_REPOSITORIO>`

2. Instale as dependências necessárias:
   - `pip install -r requirements.txt`

3. Certifique-se de que o Chrome WebDriver esteja disponível no seu PATH ou modifique o código para incluir o caminho correto.

## Como Usar

1. Configure o arquivo `config.json` com as rotas das criptomoedas que você deseja monitorar. O formato padrão já está incluído no projeto.
2. Execute o aplicativo Flask:
   - `python app.py`
3. Acesse a interface web no navegador:
   - `http://127.0.0.1:3000/prices`
4. O script fará a coleta de preços a cada 60 segundos e os armazenará no arquivo `moeda_precos.json`.

## Funções Principais

### fetch_coins()

- Função principal que inicia o loop de coleta de preços.
- Chama a função `fetch_prices()` a cada 10 segundos.

### fetch_prices()

- Carrega as configurações do arquivo `config.json`.
- Inicia o WebDriver do Selenium e navega até a URL base.
- Para cada rota de criptomoeda, coleta o preço atual, adiciona um timestamp e armazena os dados.
- Salva os preços coletados em `moeda_precos.json`.

### load_prices()

- Carrega os preços armazenados em `moeda_precos.json` para exibição na interface web.

### app.py

- Inicia um aplicativo Flask que roda em uma porta específica e fornece uma rota para a página de preços.
- Utiliza uma thread para buscar preços periodicamente.

### prices.html

- Interface HTML que exibe os preços das criptomoedas em uma lista, com atualizações em tempo real.

## Contribuições

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões, sinta-se à vontade para abrir uma issue ou fazer um pull request.

### Contribuintes

- **Thor Galli**: [GitHub](https://github.com/ThorGalli)  
  ![Thor Galli](https://avatars.githubusercontent.com/u/95541125?v=4)

- **Pedro Lobato**: [GitHub](https://github.com/Pedrossl/)  
  ![Pedro Lobato](https://avatars.githubusercontent.com/u/116649671?v=4)