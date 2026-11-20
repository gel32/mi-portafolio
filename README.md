# Mi Portafolio Web — Luis Felipe Rivero Lagos

Portafolio web personal desarrollado con **Python (Flask)**, diseño **Dark Mode con Glassmorphism** y preparado para despliegue en contenedores con **Docker**, **Gunicorn** y **Google Cloud Run**.

---

## Características

- **Contenido centralizado:** Toda la información personal, experiencia, habilidades, proyectos y estudios se gestiona desde `app.py` y se renderiza dinámicamente con **Jinja2**.
- **Diseño moderno y responsivo:** Tema oscuro con efecto *Glassmorphism*, panel lateral fijo (*sticky sidebar*) en escritorio y adaptación automática para dispositivos móviles (`<= 900px`).
- **Descarga de documentos:** Acceso directo al currículum (`CV_LuisFelipeRiveroLagos.pdf`) y certificados (`certificados.pdf`).
- **Iconografía tecnológica:** Integración de etiquetas con iconos mediante **Devicon** y **Simple Icons**.
- **Listo para producción:** Configurado con **Gunicorn** y **Dockerfile** compatible con **Google Cloud Run** (puerto `8080` configurable vía variable `PORT`).

---

## Secciones incluidas

- **Panel lateral:** Foto de perfil, nombre, título profesional, ubicación y accesos directos a Email, Teléfono y LinkedIn.
- **Sobre Mí:** Resumen del perfil profesional.
- **Habilidades Técnicas:** Organizadas por categorías (Lenguajes & Backend, Frontend, Bases de Datos, Herramientas & Cloud y Metodologías).
- **Experiencia Laboral:** Línea de tiempo cronológica con cargos, empresas y detalle de responsabilidades.
- **Proyectos Destacados y Personales:** Tarjetas con descripción, stack tecnológico y enlaces a repositorios de GitHub.
- **Formación Académica:** Títulos y estado de estudios.

---

## Tecnologías utilizadas

- **Backend:** Python 3.11, Flask 3.0.0, Jinja2
- **Servidor WSGI:** Gunicorn 21.2.0
- **Frontend:** HTML5, CSS3 (Flexbox, CSS Grid, Glassmorphism, Media Queries)
- **Iconos:** [Devicon](https://devicon.dev/) y [Simple Icons](https://simpleicons.org/)
- **Contenedores y Despliegue:** Docker (`python:3.11-slim`), Google Cloud Run

---

## Estructura del proyecto

```text
mi-portafolio/
├── app.py                               # Aplicación Flask y estructura de datos del portafolio
├── requirements.txt                     # Dependencias Python (Flask, Gunicorn)
├── Dockerfile                           # Configuración de imagen para Docker / Cloud Run
├── .gitignore                           # Exclusiones de Git
├── templates/
│   └── index.html                       # Plantilla principal Jinja2
└── static/
    ├── css/
    │   └── style.css                    # Estilos Dark Mode, Glassmorphism y responsive
    ├── docs/
    │   ├── CV_LuisFelipeRiveroLagos.pdf # Currículum descargable
    │   └── certificados.pdf             # Certificados y diplomas
    └── img/
        ├── foto-mia.jpeg                # Foto de perfil
        └── portada-codigo.jpg           # Imagen de portada superior
```

---

## Ejecución local

### Opción 1: Con Python y entorno virtual

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/gel32/mi-portafolio.git
   cd mi-portafolio
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS / Linux
   # venv\Scripts\activate       # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar la aplicación:**
   ```bash
   python app.py
   ```

5. Abrir en el navegador: `http://127.0.0.1:5001`

---

### Opción 2: Con Docker

1. **Construir la imagen:**
   ```bash
   docker build -t mi-portafolio .
   ```

2. **Ejecutar el contenedor:**
   ```bash
   docker run -p 8080:8080 mi-portafolio
   ```

3. Abrir en el navegador: `http://localhost:8080`

---

## Despliegue en Google Cloud Run

El `Dockerfile` utiliza `gunicorn` escuchando en la variable de entorno `$PORT` (por defecto `8080`), listo para desplegarse directamente en Cloud Run:

```bash
gcloud run deploy mi-portafolio \
  --source . \
  --region southamerica-west1 \
  --allow-unauthenticated
```

---

## Personalización

- **Textos, experiencia, habilidades y proyectos:** Edita los diccionarios y listas dentro de `home()` en `app.py`.
- **Imágenes y documentos:** Reemplaza los archivos dentro de `static/img/` y `static/docs/`.
- **Estilos:** Modifica `static/css/style.css` (si actualizas estilos en producción, recuerda incrementar el parámetro de versión `?v=...` en `templates/index.html` para evitar caché del navegador).

---

## Contacto

- **Autor:** Luis Felipe Rivero Lagos
- **LinkedIn:** [linkedin.com/in/luisrivero3232](https://www.linkedin.com/in/luisrivero3232)
- **GitHub:** [github.com/gel32](https://github.com/gel32)
