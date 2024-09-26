# Cotação de Moedas com RPA em Python

## Descrição do Projeto

Este projeto consiste em um aplicativo de desktop que permite buscar cotações de diversas moedas usando um processo de Automação de Processos Robóticos (RPA). O aplicativo é desenvolvido em Python, utilizando a biblioteca Tkinter para a interface gráfica e Selenium para realizar a automação da busca de cotações no Google.

## Tecnologias Envolvidas

- **Python**: Linguagem de programação versátil, utilizada para o desenvolvimento do aplicativo.
- **Tkinter**: Biblioteca padrão do Python para a criação de interfaces gráficas, permitindo uma experiência de usuário amigável.
- **Selenium**: Ferramenta de automação que simula a interação com um navegador web, permitindo a busca de informações em tempo real.
- **ChromeDriver**: Driver que permite ao Selenium controlar o navegador Google Chrome.

## RPA e Busca de Cotações

### O que é RPA?

RPA (Robotic Process Automation) é uma tecnologia que permite automatizar tarefas repetitivas e baseadas em regras, utilizando robôs de software. O RPA pode ser utilizado para interagir com interfaces de usuário, extrair e manipular dados, e executar processos de forma eficiente.

### Aplicação no Projeto

Neste projeto, utilizamos RPA para automatizar o processo de busca de cotações de moedas. O aplicativo permite ao usuário selecionar uma moeda de uma lista suspensa e, ao clicar em "Pesquisar", o Selenium simula a entrada de dados no Google e captura o resultado da cotação.

### Conceitos Técnicos

1. **Web Scraping**: Técnica de extração de dados de websites. Utilizamos o Selenium para buscar informações sobre cotações diretamente no Google.
2. **Automação**: O uso de scripts para realizar tarefas que normalmente requerem intervenção humana. Neste caso, a busca e a extração de cotações.
3. **Tratamento de Exceções**: Utilizamos `try-except` para lidar com possíveis erros durante a extração de dados, garantindo que o usuário receba feedback adequado em caso de falhas.

## Conclusão

Este projeto demonstra a aplicação de RPA para buscar cotações de moedas de forma rápida e eficiente. A combinação de Tkinter e Selenium oferece uma solução robusta para automação de processos de coleta de dados, evidenciando o potencial do Python como uma ferramenta poderosa para desenvolvimento de aplicações de automação.
