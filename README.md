# Consulta OpenAI via Terminal

Este projeto permite que você faça perguntas para a API da OpenAI diretamente pelo terminal, recebendo respostas em texto e salvando as conversas em arquivos `.txt`.

---

## Como funciona

1. O programa pede que você digite uma pergunta.
2. Envia essa pergunta para a API da OpenAI (modelo GPT-3.5-turbo).
3. Recebe a resposta da IA e exibe no terminal.
4. Salva a pergunta e a resposta em arquivos de texto (`pergunta1.txt`, `pergunta2.txt`, etc).
5. Você pode continuar perguntando até digitar `sair`.

---

## Como usar

### Pré-requisitos

- Python 3.7 ou superior
- Conta na OpenAI com chave de API válida (é necessário criar uma conta no site da OpenAI e adicionar sua chave)
- É importante lembrar que o uso da API da OpenAI é pago conforme o consumo, então você deve ter créditos ou um plano ativo para usar o serviço.

### Passos para rodar o projeto

1. Clone este repositório ou baixe os arquivos do projeto.
2. Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da OpenAI nesse formato:
OPENAI_API_KEY=sk-xxxxxSeuTokenAquixxxxx
3. Instale as dependências do projeto com:
pip install -r requirements.txt
4. Execute o script principal:
python perguntas_ia.py
5. Digite sua pergunta e pressione Enter.
6. Para sair, digite:
sair