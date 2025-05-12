# Blog Automatizado de Nicho

Este repositorio crea un blog de nicho en Jekyll con contenido generado automáticamente por la API de OpenAI y monetizado con enlaces de afiliado.

## Pasos rápidos

1. Clona este repositorio.
2. Renombra `.env.example` a `.env` y añade tus claves:
   - `OPENAI_API_KEY`
   - `NICHO` (p.ej. "mejores accesorios para móviles gaming")
   - `affiliate_links` en el mismo `.env`
3. Sube tu repo a GitHub.
4. Configura tus GitHub Secrets: `OPENAI_API_KEY`, `NICHO`.
5. Asegúrate de que GitHub Pages esté habilitado en la rama `main` con carpeta `/(root)`

¡Cada semana se publicará un artículo automáticamente!
