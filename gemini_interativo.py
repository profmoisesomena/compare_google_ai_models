import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do Google Generative AI com sua chave de API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    # Inicializar o chat com o modelo Gemini
    modelo = genai.GenerativeModel('gemini-2.0-flash')
    chat = modelo.start_chat(history=[])
    
    print("=" * 50)
    print("Assistente Gemini - Digite 'sair' para encerrar")
    print("=" * 50)
    
    # Loop de conversa
    while True:
        # Obter pergunta do usuário
        pergunta = input("\nVocê: ")
        
        # Verificar se o usuário quer sair
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            print("\nObrigado por conversar comigo! Até logo!")
            break
        
        try:
            # Enviar pergunta para o Gemini
            resposta = chat.send_message(pergunta)
            
            # Exibir resposta
            print(f"\nGemini: {resposta.text}")
            
        except Exception as e:
            print(f"\nErro: {str(e)}")

if __name__ == "__main__":
    main()
