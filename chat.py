import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = "Eres un asistente útil y amable. Responde siempre en castellano de forma clara y concisa."


historial = []

print("Chatbot iniciat. Escriu 'sortir' per acabar.\n")

while True:
    pregunta = input("Tu: ").strip()
    
    if pregunta.lower() in ["sortir", "quit", "exit"]:
        print("Fins aviat!")
        break

    historial.append({"role": "user", "content": pregunta})

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + historial
    )

    text = resposta.choices[0].message.content
    historial.append({"role": "assistant", "content": text})

    print(f"Bot: {text}\n")