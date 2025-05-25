import os
import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

contador = 1

while True:
    pergunta = input("Digite sua pergunta (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        break

    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}]
        )
        conteudo = resposta.choices[0].message.content.strip()
        print("\nResposta da IA:\n", conteudo)

        nome_arquivo = f"pergunta{contador}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(f"Pergunta: {pergunta}\n\nResposta: {conteudo}")

        contador += 1

    except Exception as e:
        print("\nErro ao consultar a IA:\n", e)
