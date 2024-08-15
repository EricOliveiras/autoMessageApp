# Auto Message App

## Sobre o projeto

Este projeto surge como resultado do curso "Atividades de Extensão: Integração de Competências em Engenharia de Software
III", na UNICID | Universidade Cidade de São Paulo. Ele foi concebido com o propósito de oferecer uma solução prática e
relevante para a minha comunidade, alinhada com os conhecimentos adquiridos durante o curso.

A aplicação consiste em uma plataforma desenvolvida em Flask, projetada para simplificar o processo de comunicação em
larga escala através do WhatsApp. Seu desenvolvimento abrange uma ampla gama de conceitos de Engenharia de Software,
desde o desenvolvimento web com Python até a manipulação de dados, automação de tarefas e integração com APIs.

Essa iniciativa não apenas visa cumprir os requisitos acadêmicos do curso, mas também busca impactar positivamente a
comunidade, oferecendo uma solução eficiente e acessível para as necessidades de comunicação em massa.

## Problema x Solução

Vi a necessidade de resolver o problema da ONG em questão de enviar mensagem para um número grande de contatos de forma
eficiente e automatizada. Manualmente, o processo de enviar mensagens para cada contato seria demorado e suscetível a
erros. Além disso, manter o controle sobre quais contatos já receberam as mensagens também seria desafiador.

Para solucionar esse problema, desenvolvi esta aplicação Flask que automatiza o processo de envio de mensagens em massa
pelo WhatsApp. A aplicação permite carregar os contatos a partir de um arquivo Excel, enviar mensagens personalizadas
para cada contato e manter o controle sobre quais mensagens foram enviadas com sucesso.

Essa solução oferece uma abordagem mais eficiente e confiável para a ONG alcançar seus contatos de forma rápida e
eficaz, economizando tempo e minimizando erros. Além disso, fornece uma maneira de rastrear e gerenciar o status das
mensagens enviadas, facilitando o acompanhamento e a comunicação com a comunidade.

## Requisitos

- Python 3.6 ou superior.

## Funcionalidades

- Carregar contatos a partir de um arquivo Excel.
- Enviar mensagens personalizadas para os contatos.
- Atualizar o status de mensagens enviadas.

## Observações

Este projeto foi desenvolvido sob medida para atender às necessidades específicas da ONG, seguindo rigorosamente o
padrão estabelecido no arquivo xlsx fornecido por eles.

É importante ressaltar que a automação de mensagens via WhatsApp pode estar sujeita às políticas e diretrizes da empresa
WhatsApp. Portanto, é crucial agir com responsabilidade e ética ao utilizar esta ferramenta, garantindo o cumprimento de
todas as políticas de uso e evitando qualquer atividade que possa violar os termos de serviço.

Além disso, este projeto foi desenvolvido com foco na segurança e privacidade dos usuários. Todas as informações e dados
pessoais dos contatos são tratados com o máximo cuidado e proteção, garantindo a conformidade com as regulamentações de
privacidade vigentes.

Por fim, este projeto é uma demonstração do compromisso em aplicar os conhecimentos adquiridos em Engenharia de Software
para resolver problemas do mundo real e fazer uma diferença positiva na comunidade.

## Utilizando o projeto

- Clone este repositório:

```bash
  git clone https://github.com/EricOliveiras/autoMessageApp.git
```

- Abra o terminal ou prompt de comando e navegue até o diretório raiz do projeto auto-message-app.

- Execute o seguinte comando para criar a venv:

```bash
  python -m venv venv
```

- Após a criação da venv, ative-a executando o seguinte comando:
- No Windows:

```bash
  venv\Scripts\activate
```

- No macOS e Linux:

```bash
  source venv/bin/activate
```

- Com a venv ativada, instale as dependências do projeto a partir do arquivo requirements.txt usando o seguinte comando:

```bash
  pip install -r requirements.txt
```

- Para iniciar o projeto após criar e ativar a virtual environment, siga estas etapas:

- Certifique-se de estar com a venv ativada (como descrito acima).
- Navegue até o diretório raiz do projeto auto-message-app no terminal.
- Execute o seguinte comando para iniciar o aplicativo Flask:

```bash
  python app.py
```

- Após a execução bem-sucedida do comando acima, aguarde alguns segundos enquanto a aplicação inicia. Ela irá
  automaticamente abrir uma aba no seu navegador padrão.