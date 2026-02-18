# 🤖 Chatbot con contexto de documentos

Chatbot conversacional con historial y soporte de documentos de contexto (PDF, ODT, TXT).
Construido con FastAPI (Python) en el backend y JavaScript + Bootstrap en el frontend.

## 🚀 Tecnologías

- **Backend:** Python, FastAPI, Groq API (LLaMA 3.3)
- **Frontend:** HTML, JavaScript, Bootstrap 5
- **Librerías:** pypdf, odfpy, python-dotenv

## ⚙️ Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/CarlosBertomeuM/chatbot-project.git
cd chatbot-project
```

### 2. Crea el entorno virtual
```bash
py -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```
GROQ_API_KEY=tu_clave_aqui
```

### 5. Arranca el servidor
```bash
uvicorn main:app --reload
```

### 6. Abre el frontend
Abre `index.html` con Live Server en VS Code.

## 💡 Uso

1. Sube un documento PDF, ODT o TXT desde el botón **Cargar**
2. El chatbot usará ese documento como contexto para responder
3. Si no subes documento, funciona como asistente general

## 📁 Estructura del proyecto
```
chatbot-project/
├── main.py              # Backend FastAPI
├── chat.py              # Chatbot de consola (Fase 2)
├── context_loader.py    # Lector de documentos
├── index.html           # Frontend
├── requirements.txt     # Dependencias
├── .env                 # API Key (no se sube a GitHub)
└── .gitignore
```

## ⚠️ Seguridad

- La API key nunca se sube a GitHub (está en `.env` y en `.gitignore`)
- El CORS está configurado para permitir solo peticiones locales en producción
- 

## 🚫 Limitaciones

- **Límite de tokens:** Debido al plan gratuito de Groq, solo se leen los primeros 8.000 
  caracteres del documento. Puedes ampliar o eliminar este límite con un plan de pago.
- **Límite de peticiones:** El plan gratuito permite 12.000 tokens por minuto. 
  Si haces muchas preguntas rapidamente o tienes muchos usuarios simultanios puede dar error temporalmente.
