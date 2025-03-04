import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do Google Generative AI com sua chave de API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Inicializar o modelo Gemini
modelo = genai.GenerativeModel('gemini-1.5-pro')

def obter_resposta(pergunta):
    """Função simples para obter resposta do Gemini"""
    resposta = modelo.generate_content(pergunta)
    print(f"\n=== Pergunta: {pergunta} ===\n")
    print(resposta.text)
    print("\n" + "-"*50 + "\n")

# Exemplo 1: Pergunta simples
obter_resposta("Qual é a capital do Brasil?")

# Exemplo 2: Criatividade
obter_resposta("Escreva uma pequena poesia sobre tecnologia")

# Exemplo 3: Explicação
obter_resposta("Explique de forma simples como funciona a inteligência artificial")

# Exemplo 4: Código
obter_resposta("Escreva um código Python simples que calcule a sequência de Fibonacci")
