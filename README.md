# Mi Portafolio Web — Luis Felipe Rivero Lagos

Portafolio web personal desarrollado con **Python (Flask)**, diseño **Dark Mode con Glassmorphism** y preparado para despliegue en contenedores con **Docker**, **Gunicorn** y **Google Cloud Run**.

---

## Características

- **Contenido centralizado:** Toda la información personal, experiencia, habilidades, proyectos y estudios se gestiona desde `app.py` y se renderiza dinámicamente con **Jinja2**.
- **Sistema de diseño:** Tema oscuro con efecto *Glassmorphism*; colores, espaciado (escala de 4px), radios, sombras y tipografía definidos como variables CSS en `:root`. Todo el texto cumple contraste WCAG AA.
- **Tipografía:** **Inter** para el texto y **JetBrains Mono** para fechas y etiquetas (Google Fonts), con escala fluida (`clamp()`).
- **Diseño responsivo:** CSS Grid con panel lateral y menú fijos en escritorio; en móvil, una columna (portada → perfil → menú → contenido) con menú de scroll horizontal. Puntos de corte: `1100px`, `900px`, `600px` y `480px`.
- **Fondo animado:** Campo 3D de partículas de luz dibujado con WebGL (`static/js/fondo.js`) que rota suavemente siguiendo al mouse; toma sus colores de las variables CSS, se atenúa en pantallas táctiles y queda estático con `prefers-reduced-motion`. Sin WebGL, se muestran los halos de fondo en CSS.
- **Páginas de detalle:** Cada proyecto tiene su propia página (`/proyecto/<id>`) con descripción completa y enlace a GitHub.
- **Accesibilidad:** Jerarquía de encabezados h1 → h2 → h3, foto con texto alternativo, foco visible con teclado, enlace "Saltar al contenido" y soporte para `prefers-reduced-motion`.
- **Descarga de documentos:** Acceso directo al currículum (`CV_LuisFelipeRiveroLagos.pdf`) y certificados (`certificados.pdf`).
- **Iconografía tecnológica:** Integración de etiquetas con iconos mediante **Devicon** (versión fijada) y **Simple Icons**.
- **Listo para producción:** Configurado con **Gunicorn** y **Dockerfile** compatible con **Google Cloud Run** (puerto `8080` configurable vía variable `PORT`).

---

## Secciones incluidas

- **Panel lateral:** Foto de perfil, nombre, título profesional, ubicación y accesos directos a Email, Teléfono y LinkedIn.
- **Sobre Mí:** Resumen del perfil profesional.
- **Habilidades Técnicas:** Organizadas por categorías (Lenguajes & Backend, Frontend, Bases de Datos, Herramientas & Cloud y Metodologías).
- **Experiencia Laboral:** Línea de tiempo cronológica con cargos, empresas y detalle de responsabilidades.
- **Proyectos Destacados y Personales:** Tarjetas con icono del stack principal, descripción, tecnologías, enlace a la página de detalle y al repositorio de GitHub.
- **Formación Académica:** Títulos con insignia de estado (titulado / en proceso).

---

## Tecnologías utilizadas

- **Backend:** Python 3.11, Flask 3.0.0, Jinja2
- **Servidor WSGI:** Gunicorn 21.2.0
- **Frontend:** HTML5, CSS3 (variables CSS, Flexbox, CSS Grid, Glassmorphism, Media Queries)
- **Tipografías:** [Inter](https://fonts.google.com/specimen/Inter) y [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)
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
│   ├── base.html                        # Estructura común (<head>, fuentes, CSS)
│   ├── _macros.html                     # Mapa de iconos y macros de etiquetas/iconos
│   ├── index.html                       # Página principal
│   └── proyecto.html                    # Página de detalle de cada proyecto
└── static/
    ├── css/
    │   └── style.css                    # Sistema de diseño, componentes y responsive
    ├── js/
    │   └── fondo.js                     # Fondo animado de partículas (WebGL) que sigue al mouse
    ├── docs/
    │   ├── CV_LuisFelipeRiveroLagos.pdf # Currículum descargable
    │   └── certificados.pdf             # Certificados y diplomas
    └── img/
        ├── foto-mia.jpeg                # Foto de perfil (original)
        ├── foto-mia-400.jpg             # Foto de perfil optimizada (la que usa el sitio)
        ├── portada-codigo.jpg           # Imagen de portada (original)
        └── portada-codigo-2400.jpg      # Portada optimizada (la que usa el sitio)
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

- **Textos, experiencia, habilidades y proyectos:** Edita los diccionarios y listas dentro de `home()` en `app.py` (los proyectos están en la lista global `proyectos`).
  - El puesto que contenga "Actualidad" en su periodo se resalta automáticamente en la línea de tiempo.
  - Los estudios con "Titulado" en su estado muestran la insignia verde; el resto, la azul.
  - El icono de cada tarjeta de proyecto es el de su primera tecnología con icono en `templates/_macros.html`.
- **Iconos de tecnologías:** Agrega nuevas entradas al mapa `icon_map` en `templates/_macros.html` (nombres de clase de [Devicon](https://devicon.dev/)).
- **Imágenes y documentos:** Reemplaza los archivos dentro de `static/img/` y `static/docs/`. Si cambias la foto o la portada, genera también su versión optimizada (`foto-mia-400.jpg`, ~400px; `portada-codigo-2400.jpg`, ~2400px de ancho) o ajusta las rutas en `templates/index.html` y `static/css/style.css`.
- **Estilos:** Los colores, espaciados y tipografía se cambian desde las variables de `:root` al inicio de `static/css/style.css`. Si actualizas estilos en producción, incrementa el parámetro de versión `?v=...` en `templates/base.html` para evitar la caché del navegador.

---

## Contacto

- **Autor:** Luis Felipe Rivero Lagos
- **LinkedIn:** [linkedin.com/in/luisrivero3232](https://www.linkedin.com/in/luisrivero3232)
- **GitHub:** [github.com/gel32](https://github.com/gel32)
