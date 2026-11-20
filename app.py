from flask import Flask, render_template

app = Flask(__name__)

# Proyectos destacados a nivel global para compartirlos entre rutas
proyectos = [
    {
        "id": "react-flow-payment",
        "nombre": "React Flow Payment Integration",
        "descripcion": "Prueba de concepto para integración de flujos de pago en interfaces modernas.",
        "tecnologias": ["React", "JavaScript"],
        "github_url": "https://github.com/gel32/react-flow-payment-integration/blob/main/README.md",
        "detalle_completo": "Prueba de concepto desarrollada en React y JavaScript enfocada en la integración de pasarelas y flujos de pago (Flow) dentro de interfaces web modernas. Incluye manejo de estados transaccionales, redirecciones de pago y vistas de resultado para ofrecer una experiencia clara y confiable al usuario final."
    },
    {
        "id": "asistente-emma",
        "nombre": "Asistente Virtual IA 'Emma'",
        "descripcion": "Construcción y despliegue de un asistente virtual corporativo inteligente para inge.cl utilizando servicios en la nube.",
        "tecnologias": ["TypeScript", "Azure OpenAI", "Azure Logic Apps", "Azure Functions"],
        "github_url": "https://github.com/gel32/asistente-virtual-ia-react-azure/blob/main/README.md",
        "detalle_completo": "Diseño, construcción y puesta en producción de 'Emma', el asistente virtual corporativo inteligente para inge.cl. La arquitectura se apoyó en el ecosistema cloud de Microsoft Azure: Azure OpenAI para el procesamiento de lenguaje natural y respuestas contextualizadas, Azure Logic Apps para la orquestación de flujos de negocio y derivación de consultas, y Azure Functions para la ejecución de lógica serverless de integración."
    },
    {
        "id": "factoring-sii-certificados",
        "nombre": "Herramienta Factoring SII & Certificados",
        "descripcion": "Desarrollo de utilidades web para el registro de datos del SII, búsqueda de empresas y generación masiva de certificados de crédito.",
        "tecnologias": ["Python", "Flask", "Azure App Service"],
        "github_url": "https://github.com/gel32/herramienta-factoring-sii/blob/main/README.md",
        "detalle_completo": "Creación y despliegue en producción de aplicaciones web internas desarrolladas con Python y Flask, alojadas en Azure App Service. Estas herramientas agilizaron la operación diaria del área comercial y de factoring, permitiendo el registro estructurado de credenciales y datos del SII, búsqueda histórica de empresas con ordenamiento dinámico de columnas y la emisión automatizada de certificados de crédito."
    },
    {
        "id": "login-usuario",
        "nombre": "Login Usuario",
        "descripcion": "Módulo base de autenticación y gestión de sesiones.",
        "tecnologias": ["PHP", "MySQL", "Frontend", "Backend"],
        "github_url": "https://github.com/gel32/LoginUsuario/blob/main/README.md",
        "detalle_completo": "Módulo base diseñado para la autenticación de usuarios y administración de sesiones. Implementa la estructura fundamental de validación de credenciales, manejo de estados de acceso y protección de rutas tanto en frontend como en backend."
    }
]

@app.route('/')
def home():
    # Sección de contacto
    contacto = {
        "telefono": "+56 9 4035 6059",
        "email": "lriverol32@gmail.com",
        "linkedin": "https://www.linkedin.com/in/luisrivero3232",
        "ubicacion": "Puente Alto, RM, Chile"
    }
    
    # Sección sobre ti
    sobre_mi = "En búsqueda de nuevos desafíos que me permitan aplicar y expandir mi formación académica en un entorno colaborativo. Aporto experiencia en equipos ágiles (Scrum), donde he liderado la administración de incidencias y validación de requerimientos. Mi enfoque se centra en la calidad del software, participando en etapas clave de desarrollo a través de testing funcional y estático."

    # Habilidades categorizadas y ampliadas para coincidir con Devicon
    habilidades = [
        {"categoria": "Lenguajes & Backend", "lista": ["Python", "C#", "PHP", ".NET", "Codelgniter"]},
        {"categoria": "Frontend", "lista": ["React", "Angular", "TypeScript", "JavaScript (DOM, Ajax, JQuery)", "HTML"]},
        {"categoria": "Bases de Datos", "lista": ["SQL Server", "MySQL", "MongoDB", "Sybase SQL", "Scripts & SPs"]},
        {"categoria": "Herramientas & Cloud", "lista": ["Azure", "Docker", "Git", "Jenkins (Pipelines)", "n8n", "SFTP", "Microservicios"]},
        {"categoria": "Metodologías", "lista": ["Scrum", "UML", "Métricas SLA"]}
    ]

    # Sección de experiencia laboral
    experiencia = [
        {
            "cargo": "Ingeniero de software",
            "empresa": "Inge!",
            "periodo": "Nov 2025 - Actualidad",
            "detalle": "Desarrollo y mantenimiento de microservicios y APIs REST en entorno Cloud (Azure). Migración de módulos desde sistemas monolíticos y construcción de herramientas para el análisis de datos financieros en portal de autoatención."
        },
        {
            "cargo": "Junior System Engineer",
            "empresa": "Indra Company",
            "periodo": "Jun 2025 - Oct 2025",
            "detalle": "Mantenimiento de sistemas y plataformas tecnológicas para cliente coordinador eléctrico nacional. Monitoreo de infraestructura e integración de sistemas en pruebas y pasos a producción."
        },
        {
            "cargo": "Analista Desarrollador",
            "empresa": "Imaginasoft",
            "periodo": "Abr 2023 - Nov 2023",
            "detalle": "Desarrollo de mejoras correctivas en PHP7.4 y MySQL. Creación de Procedimientos Almacenados (SP) y soporte evolutivo Frontend/Backend."
        },
        {
            "cargo": "Analista Mesa de Servicios",
            "empresa": "In Motion Chile",
            "periodo": "Mar 2017 - Abr 2020",
            "detalle": "Creación de Formularios Web, manejo del DOM a través de JavaScript, e implementación de editor integrado en CodeIgniter. Despliegues mediante SFTP y configuración de pipelines en Jenkins."
        }
    ]
    
    estudios = [
        {"titulo": "Ingeniería en Informática", "estado": "Proceso de titulación (2026)"},
        {"titulo": "Analista Programador", "estado": "Titulado (2023)"}
    ]

    return render_template('index.html', contacto=contacto, sobre_mi=sobre_mi, habilidades=habilidades, experiencia=experiencia, proyectos=proyectos, estudios=estudios)

@app.route('/proyecto/<proyecto_id>')
def proyecto_detalle(proyecto_id):
    proyecto = next((p for p in proyectos if p['id'] == proyecto_id), None)
    if not proyecto:
        return "Proyecto no encontrado", 404
    return render_template('proyecto.html', proyecto=proyecto)

if __name__ == '__main__':
    app.run(debug=True, port=5001)