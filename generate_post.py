import os
import re
from datetime import datetime
from dotenv import load_dotenv
import openai

# Cargar env variables
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
NICHO = os.getenv('NICHO')
AFFILIATES = []
with open(os.path.join(os.getcwd(), '.env')) as envfile:
    env_content = envfile.read()
for item in re.findall(r"- name: (.*)\s+url: '(.*)'", env_content):
    AFFILIATES.append({'name': item[0], 'url': item[1]})

openai.api_key = API_KEY

def generar_articulo(nicho):
    prompt = (
        f"Escribe un artículo SEO de 800-1000 palabras sobre '{nicho}'. "
        "Incluye al menos 3 recomendaciones de productos con enlaces de afiliado genéricos. "
        "Genera un título atractivo y separa en secciones con subtítulos."
    )
    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{'role':'user','content':prompt}]
    )
    contenido = resp.choices[0].message.content.strip()
    return contenido

if __name__ == '__main__':
    contenido = generar_articulo(NICHO)
    today = datetime.utcnow().strftime('%Y-%m-%d')
    title_match = re.match(r"^#\s*(.*)", contenido)
    if title_match:
        title = title_match.group(1)
        body = contenido[len(title_match.group(0)):].strip()
    else:
        title = f"Artículo sobre {NICHO}"
        body = contenido
    filename = f"{today}-{title.lower().replace(' ', '-')}.md"
    filepath = os.path.join('_posts', filename)
    os.makedirs('_posts', exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f"title: "{title}"\n")
        f.write(f"date: {today} 10:00:00 +0000\n")
        f.write(f"categories: {NICHO.split()[0]}\n")
        f.write('---\n\n')
        f.write(body + '\n\n---\n')
        for aff in AFFILIATES:
            f.write(f"[{aff['name']}]({aff['url']})\n")
    print(f"Artículo generado: {filepath}")
