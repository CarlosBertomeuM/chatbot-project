import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from context_loader import cargar_documento

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

CONTEXTO = ""

BASE_PROMPT = "Eres un asistente útil y amable. Responde siempre en castellano de forma clara y concisa."


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Limitaciones debido a el uso de la version gratuita de grok, ya que tiene un limite maximo de tokens que puede leer
#cuando subes un archivo lee los primeros 8000 caracteres, son embargo funciona a modo de prueba
#Eliminar o modificar en caso de ampliar el plan 
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

MAX_CHARS = 8000  

def construir_system_prompt():
    if CONTEXTO:
        contexto_truncado = CONTEXTO[:MAX_CHARS]
        if len(CONTEXTO) > MAX_CHARS:
            contexto_truncado += "\n\n[Documento truncado por límite de tokens]"
        return f"{BASE_PROMPT}\n\nUsa el siguiente documento como base para responder:\n\n{contexto_truncado}"
    return BASE_PROMPT

@app.post("/subir-documento")
async def subir_documento(archivo: UploadFile = File(...)):
    global CONTEXTO

    os.makedirs("docs", exist_ok=True)
    ruta = f"docs/{archivo.filename}"

    with open(ruta, "wb") as f:
        shutil.copyfileobj(archivo.file, f)

    CONTEXTO = cargar_documento(ruta)
    print(f"✅ Documento cargado: {archivo.filename}")
    return {"mensaje": f"Documento '{archivo.filename}' cargado correctamente"}

class Mensaje(BaseModel):
    historial: list
    pregunta: str

@app.post("/chat")
def chat(datos: Mensaje):
    mensajes = [{"role": "system", "content": construir_system_prompt()}]
    mensajes += datos.historial
    mensajes.append({"role": "user", "content": datos.pregunta})

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=mensajes
    )

    texto = respuesta.choices[0].message.content
    return {"respuesta": texto}