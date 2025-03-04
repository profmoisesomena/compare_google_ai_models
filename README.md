# compare_google_ai_models

This is a simple sample project demonstrating how to use Gemini models.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure your API keys in the `.env` file:
   ```
   GOOGLE_API_KEY="your-google-api-key"


There are 3 basic examples of using Gemini with the Google API:

1) gemini_simples.py: An extremely basic example that asks a single question to Gemini.

2) gemini_interativo.py: An interactive chat example where you can have a real-time conversation with Gemini.

3) gemini_exemplos.py: An example that shows how to use Gemini for different types of tasks (simple questions, creativity, explanations, and code).

 
1️⃣ gemini_simple.py
A script that compares responses from different Gemini models to the same set of questions.

Features:

Lists and displays available Gemini models.
Defines example questions and compares responses from each model.
Shows the response time of each model.
Models used for comparison:

gemini-1.5-pro
gemini-1.5-flash
gemini-2.0-flash
Example usage: python3 gemini_simple.py


2️⃣ gemini_interactive.py
A terminal-based chatbot using the gemini-2.0-flash model to chat with the user in real-time.

How it works:

You type your questions in the terminal.
The assistant responds instantly.
To exit, type sair (or exit / quit).
Example usage:

bash
Copiar
Editar
python gemini_interactive.py


3️⃣ gemini_examples.py
Demonstrates practical examples using the gemini-1.5-pro model to answer specific types of questions.

Included examples:

Factual question ("What is the capital of Brazil?")
Creative writing (a short poem about technology)
Simple explanation (how artificial intelligence works)
Code generation (Python code for the Fibonacci sequence)
Example usage: python3 gemini_examples.py