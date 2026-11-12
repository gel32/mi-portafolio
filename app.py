from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Nueva sección de contacto
    contacto = {
        "telefono": "+56 9 4035 6059",
        "email": "lriverol32@gmail.com",
        "linkedin": "https://www.linkedin.com/in/luisrivero3232",
        "ubicacion": "Puente Alto, RM, Chile"
    }
    
    # Nueva sección sobre ti
    sobre_mi = "En búsqueda de nuevos desafíos que me permitan aplicar y expandir mi formación académica en un entorno colaborativo. Aporto experiencia en equipos ágiles (Scrum), donde he liderado la administración de incidencias y validación de requerimientos. Mi enfoque se centra en la calidad del software, participando en etapas clave de desarrollo a través de testing funcional y estático."

    # Nuevas habilidades categorizadas (CORREGIDO: 'lista' en lugar de 'items')
    habilidades = [
        {"categoria": "Lenguajes & Backend", "lista": ["Python", "PHP", ".NET", "Codelgniter"]},
        {"categoria": "Frontend", "lista": ["JavaScript (DOM, Ajax, JQuery)", "HTML"]},
        {"categoria": "Bases de Datos", "lista": ["SQL Server", "Sybase SQL", "MySQL","MongoDB", "Scripts & SPs"]},
        {"categoria": "Herramientas & Cloud", "lista": ["Azure", "Jenkins (Pipelines)", "SFTP", "Microservicios"]},
        {"categoria": "Metodologías", "lista": ["Scrum", "UML", "Métricas SLA"]}
    ]

    # Nueva sección de experiencia laboral
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

    # Proyectos existentes
    proyectos = [
        {
            "nombre": "Portal Privado InGe!",
            "descripcion": "Desarrollo frontend y backend de servicios, implementación de actualización de perfiles, modales de enlace con clave tributaria del SII y vistas de gestión de garantías.",
            "tecnologias": ["Web APIs", "Bases de Datos", "Frontend"]
        },
        {
            "nombre": "Asistente Virtual IA 'Emma'",
            "descripcion": "Construcción y despliegue de un asistente virtual corporativo inteligente para inge.cl utilizando servicios en la nube.",
            "tecnologias": ["Azure OpenAI", "Azure Logic Apps", "Azure Functions"]
        },
        {
            "nombre": "Herramienta Factoring SII & Certificados",
            "descripcion": "Desarrollo de utilidades web para el registro de datos del SII, búsqueda de empresas y generación masiva de certificados de crédito.",
            "tecnologias": ["Python", "Flask", "Azure App Service"]
        },
        {
            "nombre": "Integración Pasarela de Pagos Getnet",
            "descripcion": "Integración de la API de la pasarela de pagos Getnet en los servicios backend para el procesamiento transaccional.",
            "tecnologias": [".NET", "API Rest"]
        }
    ]
    
    proyectos_personales = [
        {
            "nombre": "Herramienta Factoring SII",
            "descripcion": "Versión open-source del registro de datos del SII.",
            "tecnologias": ["Python", "Flask"],
            "url": "https://github.com/gel32/herramienta-factoring-sii"
        },
        {
            "nombre": "React Flow Payment Integration",
            "descripcion": "Prueba de concepto para integración de flujos de pago en interfaces modernas.",
            "tecnologias": ["React", "JavaScript"],
            "url": "https://github.com/gel32/react-flow-payment-integration"
        },
        {
            "nombre": "Login Usuario",
            "descripcion": "Módulo base de autenticación y gestión de sesiones.",
            "tecnologias": ["Frontend", "Backend"],
            "url": "https://github.com/gel32/LoginUsuario"
        },
        {
            "nombre": "Testing",
            "descripcion": "Entorno de pruebas y automatización de procesos.",
            "tecnologias": ["QA", "Scripts"],
            "url": "https://github.com/gel32/Testing"
        }
    ]
    
    estudios = [
        {"titulo": "Ingeniería en Informática", "estado": "Proceso de titulación (2026)"},
        {"titulo": "Analista Programador", "estado": "Titulado (2023)"}
    ]

    return render_template('index.html', contacto=contacto, sobre_mi=sobre_mi, habilidades=habilidades, experiencia=experiencia, proyectos=proyectos, proyectos_personales=proyectos_personales, estudios=estudios)

if __name__ == '__main__':
    app.run(debug=True, port=5001)