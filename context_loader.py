import os
from pypdf import PdfReader
from odf import text, teletype
from odf.opendocument import load

def cargar_documento(ruta):
    extension = os.path.splitext(ruta)[1].lower()

    if extension == ".pdf":
        reader = PdfReader(ruta)
        contenido = ""
        for pagina in reader.pages:
            contenido += pagina.extract_text() + "\n"
        return contenido.strip()

    elif extension in [".odt", ".odf"]:
        doc = load(ruta)
        contenido = teletype.extractText(doc.text)
        return contenido.strip()

    elif extension == ".txt":
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read().strip()

    else:
        raise ValueError(f"Formato no soportado: {extension}")
        