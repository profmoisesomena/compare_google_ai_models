import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do Google Generative AI com sua chave de API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
lista_modelos=[]
def mostrar_modelos_disponiveis():
    """Mostra os modelos Gemini disponíveis"""
    print("Modelos Gemini disponíveis:")
    for model in genai.list_models():
        if "gemini" in model.name.lower():
            print(f"- {model.name}")
            lista_modelos.append(model.name)
    print()
    return lista_modelos

# Lista de modelos Gemini para comparar
modelos = [
    "gemini-1.5-pro",
    "gemini-1.5-flash",
    "gemini-2.0-flash"
]

# Perguntas para testar


def comparar_modelos(perguntas):
    """Compara as respostas de diferentes modelos Gemini"""
    print("Comparando respostas de diferentes modelos Gemini:\n")
    
    for pergunta in perguntas:
        print(f"Pergunta: {pergunta}\n")
        print("-" * 80)
        
        for modelo_nome in modelos:
            try:
                print(f"\n=== Resposta do {modelo_nome} ===\n")
                
                # Registrar o tempo de início
                inicio = time.time()
                
                # Inicializar o modelo Gemini
                modelo = genai.GenerativeModel(modelo_nome)
                
                # Gerar resposta
                resposta = modelo.generate_content(pergunta)
                
                # Calcular o tempo de resposta
                tempo = time.time() - inicio
                
                # Exibir a resposta
                print(resposta.text)
                print(f"\nTempo de resposta: {tempo:.2f} segundos")
                
            except Exception as e:
                print(f"Erro com {modelo_nome}: {str(e)}")
            
            print("-" * 80)
        
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    # Mostrar modelos disponíveis
    lista_modelos = mostrar_modelos_disponiveis()
    
    perguntas = [
    """Quais são as 3 melhores modelos llms do google in """ + str(lista_modelos) + """ e por quê?""",
    """Explique o conceito de inteligência artificial para uma criança de 5 anos"""
]
    # Comparar modelos
    comparar_modelos(perguntas)
