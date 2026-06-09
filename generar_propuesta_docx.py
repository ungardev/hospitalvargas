#!/usr/bin/env python3
"""
PROPUESTA DE PROYECTO - FORMATO DOCX
===================================
Sitio Web Institucional - Hospital Vargas de Caracas
Dirigido a: Junta Directiva del Hospital Vargas y Ministerio del Poder Popular para la Salud

Autor: Ungar Villamizar Mirabal
Fecha: Junio 2026
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import datetime

# =============================================================================
# CONFIGURACIÓN DE COLORES INSTITUCIONALES
# =============================================================================
AZUL_INSTITUCIONAL = RGBColor(0x1E, 0x3A, 0x5F)
AZUL_CLARO = RGBColor(0x2C, 0x52, 0x82)
GRIS_OSCURO = RGBColor(0x2D, 0x37, 0x48)
GRIS_CLARO = RGBColor(0x71, 0x80, 0x96)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

# =============================================================================
# DATOS DEL DOCUMENTO
# =============================================================================

AUTORIDADES = {
    "ministra": "Dra. Nuramy Josefa Gutierrez Gonzalez",
    "viceministra_integral": "GB. Dra. Rosalbina Hurtado Ruiz",
    "director_hospital": "Dr. Jose Gregorio Rincon",
    "viceministerio_hospitales": "Mauricio Erasmo Vega Mendez",
    "viceministerio_ambulatoria": "Dra. Noly Fernandez Hernandez",
    "viceministerio_colectiva": "Dra. Magda Mara Magris Crestini",
    "viceministerio_tecnologia": "Alexandra Josefina Hernandez de Castillo",
}

HOSPITAL_INFO = {
    "nombre": "Hospital Vargas de Caracas",
    "nombre_completo": "Hospital Vargas de Caracas",
    "fundacion": "5 de julio de 1891",
    "annos_historia": "134",
    "categoria": "Hospital Tipo 4",
    "ubicacion": "Monte Carmelo a San Pirito, Esq. del Hospital, Parroquia San Jose, Caracas",
    "telefono": "(0212) 862-9965",
    "email": "hospitalvargas@gmail.com",
    "area_influencia": "400 mil habitantes",
    "especialidades": "35+",
    "programas_postgrado": "132",
}

DESARROLLADOR = {
    "nombre": "Ungar Villamizar Mirabal",
    "cedula": "25.575.601",
    "telefono": "+58 4241898413",
    "email": "ungardev@outlook.com",
    "rif": "V255756016",
}

INVERSION_TOTAL_DESARROLLO = 7000
INVERSION_TOTAL_ANUAL = 2400

STACK = {
    "framework": "Astro v5.5.3",
    "lenguaje": "TypeScript",
    "estilos": "Tailwind CSS v4",
    "iconos": "Lucide Icons",
    "despliegue": "Vercel (CDN Global)",
    "rendimiento": "< 2 segundos carga, < 20 requests",
    "dominio_propuesto": "hospitalvargas.gob.ve",
}

PAGINAS_SITIO = [
    ("/", "Inicio", "Hero, estadisticas, servicios destacados"),
    ("/historia", "Historia", "Linea de tiempo desde 1891, figuras historicas"),
    ("/servicios", "Servicios", "32 especialidades medicas categorizadas"),
    (
        "/banco-de-sangre",
        "Banco de Sangre",
        "Centro de referencia nacional, requisitos, tipos",
    ),
    ("/pregrado", "Pregrado", "Programas de la Escuela de Medicina UCV"),
    ("/postgrado", "Postgrado", "132 programas de especializacion/maestria/doctorado"),
    ("/estadisticas", "Estadisticas", "Indicadores de gestion hospitalaria"),
    ("/noticias", "Noticias", "Novedades y eventos"),
    ("/contacto", "Contacto", "Informacion de contacto, ubicacion"),
    ("/404", "404", "Pagina de error"),
]

# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================


def set_cell_shading(cell, color):
    """Establece el color de fondo de una celda"""
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), color)
    cell._tc.get_or_add_tcPr().append(shading)


def add_heading_formatted(doc, text, level=1, color=AZUL_INSTITUCIONAL):
    """Agrega un titulo con formato"""
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.color.rgb = color
    return heading


def add_paragraph_formatted(
    doc,
    text,
    bold=False,
    color=GRIS_OSCURO,
    size=11,
    alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
):
    """Agrega un parrafo con formato"""
    p = doc.add_paragraph()
    p.alignment = alignment
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.bold = bold
    return p


def add_bullet_point(doc, text):
    """Agrega un punto de lista"""
    p = doc.add_paragraph(text, style="List Bullet")
    return p


def add_table_authorities(doc):
    """Crea tabla de autoridades"""
    table = doc.add_table(rows=8, cols=2)
    table.style = "Table Grid"

    # Header
    header_cells = table.rows[0].cells
    header_cells[0].text = "CARGO"
    header_cells[1].text = "TITULAR"
    set_cell_shading(header_cells[0], "1E3A5F")
    set_cell_shading(header_cells[1], "1E3A5F")
    for cell in header_cells:
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = BLANCO
                run.bold = True

    # Data rows
    data = [
        ("Ministra del Poder Popular para la Salud", AUTORIDADES["ministra"]),
        ("Viceministra de Salud Integral", AUTORIDADES["viceministra_integral"]),
        ("Director General del Hospital Vargas", AUTORIDADES["director_hospital"]),
        ("Viceministro de Hospitales (E)", AUTORIDADES["viceministerio_hospitales"]),
        (
            "Viceminista de Redes de Atencion Ambulatoria (E)",
            AUTORIDADES["viceministerio_ambulatoria"],
        ),
        (
            "Viceminista de Redes de Salud Colectiva (E)",
            AUTORIDADES["viceministerio_colectiva"],
        ),
        (
            "Viceminista de Recursos, Tecnologia y Regulacion (E)",
            AUTORIDADES["viceministerio_tecnologia"],
        ),
    ]

    for i, (cargo, titular) in enumerate(data, 1):
        row = table.rows[i]
        row.cells[0].text = cargo
        row.cells[1].text = titular

    return table


def add_table_stack(doc):
    """Crea tabla del stack tecnologico"""
    table = doc.add_table(rows=7, cols=3)
    table.style = "Table Grid"

    # Header
    header = table.rows[0].cells
    header[0].text = "COMPONENTE"
    header[1].text = "TECNOLOGIA"
    header[2].text = "BENEFICIO"
    for cell in header:
        set_cell_shading(cell, "2C5282")
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = BLANCO
                run.bold = True

    # Data
    data = [
        ("Framework", STACK["framework"], "Alto rendimiento, build estatico"),
        ("Lenguaje", STACK["lenguaje"], "Tipado, menos errores, mejor mantenibilidad"),
        ("Estilos", STACK["estilos"], "Diseño responsivo y consistente"),
        ("Iconos", STACK["iconos"], "Graficos vectoriales optimizados"),
        ("Despliegue", STACK["despliegue"], "CDN global, alta disponibilidad"),
        ("Rendimiento", STACK["rendimiento"], "Carga rapida, mejor SEO"),
    ]

    for i, (comp, tech, benef) in enumerate(data, 1):
        row = table.rows[i]
        row.cells[0].text = comp
        row.cells[1].text = tech
        row.cells[2].text = benef

    return table


def add_table_paginas(doc):
    """Crea tabla de paginas del sitio"""
    table = doc.add_table(rows=11, cols=3)
    table.style = "Table Grid"

    header = table.rows[0].cells
    header[0].text = "RUTA"
    header[1].text = "PAGINA"
    header[2].text = "DESCRIPCION"
    for cell in header:
        set_cell_shading(cell, "1E3A5F")
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = BLANCO
                run.bold = True

    for i, (ruta, pagina, desc) in enumerate(PAGINAS_SITIO, 1):
        row = table.rows[i]
        row.cells[0].text = ruta
        row.cells[1].text = pagina
        row.cells[2].text = desc

    return table


def add_table_inversion(doc):
    """Crea tabla de inversion"""
    table = doc.add_table(rows=7, cols=3)
    table.style = "Table Grid"

    header = table.rows[0].cells
    header[0].text = "CONCEPTO"
    header[1].text = "DESCRIPCION"
    header[2].text = "MONTO (USD)"
    for cell in header:
        set_cell_shading(cell, "1E3A5F")
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = BLANCO
                run.bold = True

    data = [
        (
            "Desarrollo Web",
            "Desarrollo del sitio web institucional completo",
            "$7,000.00",
        ),
        ("Dominio (anual)", "Dominio hospitalvargas.gob.ve (gestion CONATEL)", "$0.00"),
        ("Hosting (anual)", "Alojamiento en servidores del MPPS", "$0.00"),
        ("Mantenimiento (anual)", "Mantenimiento y actualizaciones", "$2,400.00"),
        ("Capacitacion", "Capacitacion al personal del hospital (Cortesia)", "$0.00"),
    ]

    for i, (concepto, desc, monto) in enumerate(data, 1):
        row = table.rows[i]
        row.cells[0].text = concepto
        row.cells[1].text = desc
        row.cells[2].text = monto

    # Total row
    total_row = table.add_row()
    total_row.cells[0].text = "TOTAL DESARROLLO"
    total_row.cells[1].text = ""
    total_row.cells[2].text = "$7,000.00"
    set_cell_shading(total_row.cells[0], "E2E8F0")
    set_cell_shading(total_row.cells[1], "E2E8F0")
    set_cell_shading(total_row.cells[2], "E2E8F0")

    return table


def add_table_cronograma(doc):
    """Crea tabla del cronograma"""
    table = doc.add_table(rows=5, cols=6)
    table.style = "Table Grid"

    header = table.rows[0].cells
    headers = [
        "FASE",
        "SEMANA 1-2",
        "SEMANA 3-4",
        "SEMANA 5-6",
        "SEMANA 7-8",
        "SEMANA 9",
    ]
    for i, h in enumerate(headers):
        header[i].text = h
        set_cell_shading(header[i], "1E3A5F")
        for paragraph in header[i].paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = BLANCO
                run.bold = True

    data = [
        ("Planificacion", "XXX", "", "", "", ""),
        ("Desarrollo", "", "XXXX", "XXXX", "", ""),
        ("Pruebas", "", "", "", "XXX", ""),
        ("Despliegue", "", "", "", "", "XXX"),
    ]

    for i, row_data in enumerate(data, 1):
        row = table.rows[i]
        for j, cell_data in enumerate(row_data):
            row.cells[j].text = cell_data

    return table


def add_table_contacto_dev(doc):
    """Crea tabla de contacto del desarrollador"""
    table = doc.add_table(rows=6, cols=1)
    table.style = "Table Grid"

    header = table.rows[0].cells
    header[0].text = "DATOS DEL DESARROLLADOR/EJECUTOR"
    set_cell_shading(header[0], "2C5282")
    for paragraph in header[0].paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = BLANCO
            run.bold = True

    data = [
        f"Nombre: {DESARROLLADOR['nombre']}",
        f"C.I.: {DESARROLLADOR['cedula']}",
        f"Telefono: {DESARROLLADOR['telefono']}",
        f"Email: {DESARROLLADOR['email']}",
        f"RIF: {DESARROLLADOR['rif']}",
    ]

    for i, text in enumerate(data, 1):
        row = table.rows[i]
        row.cells[0].text = text

    return table


# =============================================================================
# CONSTRUCCION DEL DOCUMENTO
# =============================================================================


def generar_propuesta_docx():
    """Genera el documento DOCX de la propuesta"""

    doc = Document()

    # Configurar margenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(2.54)
        section.right_margin = Cm(2.54)

    # =============================================================================
    # PAGINA 1 - PORTADA
    # =============================================================================
    doc.add_paragraph()
    add_paragraph_formatted(
        doc,
        "REPUBLICA BOLIVARIANA DE VENEZUELA",
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=14,
    )
    doc.add_paragraph()
    add_paragraph_formatted(
        doc,
        "Ministerio del Poder Popular para la Salud",
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=12,
    )
    doc.add_paragraph()
    add_paragraph_formatted(
        doc,
        "Hospital Vargas de Caracas",
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=12,
    )
    doc.add_paragraph()
    doc.add_paragraph()

    # Titulo principal
    title = doc.add_heading("PROPUESTA DE PROYECTO", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in title.runs:
        run.font.color.rgb = AZUL_INSTITUCIONAL

    doc.add_paragraph()
    add_paragraph_formatted(
        doc,
        "Sitio Web Institucional",
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=16,
    )
    add_paragraph_formatted(
        doc,
        "Hospital Vargas de Caracas",
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=14,
    )
    doc.add_paragraph()
    doc.add_paragraph()

    # Linea separadora
    doc.add_paragraph("_" * 80)
    doc.add_paragraph()

    # Fecha y destinatario
    fecha_actual = datetime.now().strftime("%d de %B de %Y")
    add_paragraph_formatted(
        doc, f"Fecha: {fecha_actual}", alignment=WD_ALIGN_PARAGRAPH.CENTER
    )
    add_paragraph_formatted(
        doc,
        "Dirigido a: Junta Directiva del Hospital Vargas y Ministerio del Poder Popular para la Salud",
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
    )
    doc.add_paragraph()

    # Datos del desarrollador
    add_paragraph_formatted(
        doc,
        "EL DESARROLLADOR/EJECUTOR DEL PROYECTO",
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=12,
        color=AZUL_INSTITUCIONAL,
    )
    doc.add_paragraph()

    datos_dev = f"""
Nombre:    {DESARROLLADOR["nombre"]}
C.I.:      {DESARROLLADOR["cedula"]}
Telefono:  {DESARROLLADOR["telefono"]}
Email:     {DESARROLLADOR["email"]}
RIF:       {DESARROLLADOR["rif"]}
    """
    add_paragraph_formatted(doc, datos_dev.strip(), alignment=WD_ALIGN_PARAGRAPH.CENTER)

    doc.add_page_break()

    # =============================================================================
    # PAGINA 2 - AUTORIDADES
    # =============================================================================
    doc.add_paragraph()
    add_heading_formatted(doc, "AUTORIDADES INSTITUCIONALES", level=1)
    doc.add_paragraph()
    add_table_authorities(doc)

    doc.add_page_break()

    # =============================================================================
    # PAGINA 3 - INDICE
    # =============================================================================
    doc.add_paragraph()
    add_heading_formatted(doc, "INDICE", level=1)
    doc.add_paragraph()

    indice_items = [
        "I. RESUMEN EJECUTIVO",
        "II. INTRODUCCION Y JUSTIFICACION",
        "III. DESCRIPCION DEL PROYECTO",
        "    3.1 Objetivos",
        "    3.2 Alcance",
        "    3.3 Beneficios Esperados",
        "IV. ESPECIFICACIONES TECNICAS",
        "    4.1 Arquitectura Tecnologica",
        "    4.2 Stack Tecnologico",
        "    4.3 Caracteristicas de Rendimiento",
        "    4.4 Seguridad y Disponibilidad",
        "    4.5 Portabilidad del Sistema",
        "    4.6 Mapa del Sitio",
        "CUMPLIMIENTO LEGAL - LEY DE INFOGOBIERNO",
        "IMPACTO SOCIAL - REDUCCION DE COLAS",
        "V. IDENTIDAD INSTITUCIONAL",
        "VI. PLAN DE IMPLEMENTACION",
        "    6.1 Fases del Proyecto",
        "    6.2 Cronograma",
        "    6.3 Recursos y Entregables",
        "VII. INVERSION Y PRESUPUESTO",
        "VIII. SOSTENIBILIDAD Y MANTENIMIENTO",
        "IX. CONCLUSIONES Y RECOMENDACIONES",
        "ANEXOS",
    ]

    for item in indice_items:
        add_paragraph_formatted(doc, item, size=11)

    doc.add_page_break()

    # =============================================================================
    # I. RESUMEN EJECUTIVO
    # =============================================================================
    add_heading_formatted(doc, "I. RESUMEN EJECUTIVO", level=1)
    doc.add_paragraph()

    resumen_text = f"""El presente documento propone el desarrollo e implementacion del Sitio Web Institucional del Hospital Vargas de Caracas, como plataforma digital oficial del segundo centro hospitalario mas importante de Venezuela.

Fundado el {HOSPITAL_INFO["fundacion"]}, el Hospital Vargas de Caracas cuenta con {HOSPITAL_INFO["annos_historia"]} años de historia y atiende a un area de influencia de mas de {HOSPITAL_INFO["area_influencia"]}. Con {HOSPITAL_INFO["especialidades"]} especialidades medicas y {HOSPITAL_INFO["programas_postgrado"]} programas de postgrado, es referente nacional en formacion medica.

La propuesta contempla la creacion de un sitio web de alto rendimiento, accesible desde cualquier dispositivo, que permita a la ciudadania acceder a informacion sobre servicios medicos, historia institucional, programas academicos y estadisticas de gestion hospitalaria."""

    add_paragraph_formatted(doc, resumen_text.strip())
    doc.add_paragraph()

    add_paragraph_formatted(doc, "Puntos clave:", bold=True)
    add_bullet_point(
        doc, f"Inversion total de desarrollo: ${INVERSION_TOTAL_DESARROLLO:,.2f}"
    )
    add_bullet_point(
        doc, f"Costo anual de mantenimiento: ${INVERSION_TOTAL_ANUAL:,.2f}"
    )
    add_bullet_point(
        doc, "Sitio web con 10 paginas de contenido institucional completo"
    )
    add_bullet_point(doc, "Tiempo de carga menor a 2 segundos")
    add_bullet_point(doc, "Arquitectura de seguridad robusta con SSL y CDN global")

    doc.add_page_break()

    # =============================================================================
    # II. INTRODUCCION Y JUSTIFICACION
    # =============================================================================
    add_heading_formatted(doc, "II. INTRODUCCION Y JUSTIFICACION", level=1)
    doc.add_paragraph()

    intro_text = """En la era digital, la presencia en linea de las instituciones de salud publica es fundamental para garantizar la transparencia, accesibilidad y calidad de la informacion提供给 ciudadanos.

Justificacion del proyecto:

1. Transparencia Institucional: Un sitio web oficial permite a la ciudadania acceder a informacion actualizada sobre servicios, horarios, especialidades y estadisticas de gestion del hospital.

2. Mejora en la Comunicacion: Facilita la comunicacion entre el hospital y la poblacion, permitiendo la difusion de noticias, alertas epidemiologicas y campañas de salud.

3. Referencia Nacional: Como Hospital Tipo 4, el Hospital Vargas requiere una presencia digital que refleje su importancia y liderazgo en el sistema de salud venezolano.

4. Modernizacion: La implementacion de tecnologia web de ultima generacion posiciona al hospital como institucion moderna y comprometida con la excelencia.

5. Accesibilidad: El sitio web permitira que pacientes y familiares accedan a informacion desde cualquier lugar y dispositivo, mejorando la experiencia del usuario."""

    add_paragraph_formatted(doc, intro_text.strip())

    doc.add_page_break()

    # =============================================================================
    # III. DESCRIPCION DEL PROYECTO
    # =============================================================================
    add_heading_formatted(doc, "III. DESCRIPCION DEL PROYECTO", level=1)
    doc.add_paragraph()

    add_heading_formatted(doc, "3.1 Objetivos", level=2)
    add_paragraph_formatted(doc, "Objetivo General:", bold=True)
    add_paragraph_formatted(
        doc,
        "Desarrollar e implementar el sitio web institucional del Hospital Vargas de Caracas como plataforma digital oficial, que permita a la ciudadania acceder a informacion sobre servicios medicos, programas academicos e institucionales del hospital.",
    )
    doc.add_paragraph()

    add_paragraph_formatted(doc, "Objetivos Especificos:", bold=True)
    objetivos = [
        "Crear un sitio web responsivo y accesible desde cualquier dispositivo",
        "Publicar informacion completa sobre las 35+ especialidades medicas",
        "Mostrar los 132 programas de postgrado disponibles",
        "Proporcionar informacion sobre el Banco Municipal de Sangre",
        "Implementar canales de comunicacion para contacto y consultas",
        "Garantizar alto rendimiento y tiempos de carga rapidos",
        "Optimizar para motores de busqueda (SEO)",
        "Cumplir con estandares de accesibilidad web",
    ]
    for obj in objetivos:
        add_bullet_point(doc, obj)

    doc.add_paragraph()
    add_heading_formatted(doc, "3.2 Alcance", level=2)
    alcance_text = "El proyecto comprende el desarrollo completo del sitio web institucional, incluyendo:"
    add_paragraph_formatted(doc, alcance_text)

    alcance_items = [
        "Diseño y desarrollo de 10 paginas web completas",
        "Sistema de gestion de contenidos estatico (sin base de datos)",
        "Integracion con mapa del sitio y SEO",
        "Responsive design para moviles, tablets y escritorio",
        "Iconografia medica personalizada",
        "Formulario de contacto funcional",
        "Despliegue en infraestructura CDN",
        "Capacitacion al personal del hospital",
    ]
    for item in alcance_items:
        add_bullet_point(doc, item)

    doc.add_paragraph()
    add_heading_formatted(doc, "3.3 Beneficios Esperados", level=2)

    beneficios = [
        (
            "Mejor atencion al ciudadano",
            "Informacion accesible 24/7 sobre servicios hospitalarios",
        ),
        ("Transparencia", "Datos abiertos sobre estadisticas e indicadores de gestion"),
        (
            "Eficiencia",
            "Reduccion de consultas presenciales mediante informacion digital",
        ),
        (
            "Imagen institucional",
            "Presencia digital profesional que refleja calidad medica",
        ),
        ("Educacion", "Difusion de programas de pregrado y postgrado"),
        ("Comunicacion", "Canal oficial para noticias y alertas epidemiologicas"),
    ]
    for benef, desc in beneficios:
        add_paragraph_formatted(doc, f"- {benef}: {desc}")

    doc.add_page_break()

    # =============================================================================
    # IV. ESPECIFICACIONES TECNICAS
    # =============================================================================
    add_heading_formatted(doc, "IV. ESPECIFICACIONES TECNICAS", level=1)
    doc.add_paragraph()

    add_heading_formatted(doc, "4.1 Arquitectura Tecnologica", level=2)
    arch_text = """El sitio web utiliza una arquitectura moderna de generacion estatica que permite maximo rendimiento y minima dependencia de infraestructura:

- Navegador -> CDN Vercel -> Archivos estaticos (HTML/CSS/JS)
- Sin servidor de aplicaciones
- Sin base de datos
- Generacion en build time
- Despliegue global automatico"""
    add_paragraph_formatted(doc, arch_text.strip())

    doc.add_paragraph()
    add_heading_formatted(doc, "4.2 Stack Tecnologico", level=2)
    doc.add_paragraph()
    add_table_stack(doc)

    doc.add_paragraph()
    add_heading_formatted(doc, "4.3 Caracteristicas de Rendimiento", level=2)
    rendimiento_items = [
        "Tiempo de carga: < 2 segundos",
        "Solicitudes HTTP: < 20 por pagina",
        "Build estatico: HTML pre-generado",
        "Sin JavaScript del cliente: Rendering en servidor",
        "CDN Global: Archivos distribuidos mundialment",
        "Compresion Gzip: Activada por defecto",
        "SSL/TLS: HTTPS obligatorio",
    ]
    for item in rendimiento_items:
        add_bullet_point(doc, item)

    doc.add_paragraph()
    add_heading_formatted(doc, "4.4 Seguridad y Disponibilidad", level=2)
    seguridad_items = [
        "SSL/TLS: Conexion encriptada HTTPS (obligatorio)",
        "Backups: Versionamiento git con commits automaticos",
        "Monitoreo: Uptime monitoring 24/7 en servidores del MPPS",
        "Infraestructura: Servidores nacionales del Ministerio de Salud",
    ]
    for item in seguridad_items:
        add_bullet_point(doc, item)

    doc.add_paragraph()
    add_heading_formatted(doc, "4.5 Portabilidad del Sistema", level=2)
    portabilidad_items = [
        "Tecnologia Astro: Genera HTML/CSS/JS estatico puro",
        "Sin dependencias: No requiere Node.js en servidor de produccion",
        "Flexible: Puede alojarse en cualquier servidor web (Apache, Nginx, IIS)",
        "Servidores nacionales: Compatible con infraestructura MPPS/CANTV",
        "Migracion sencilla: Deployment en un solo paso",
    ]
    for item in portabilidad_items:
        add_bullet_point(doc, item)

    doc.add_paragraph()
    add_heading_formatted(doc, "4.6 Mapa del Sitio", level=2)
    doc.add_paragraph()
    add_table_paginas(doc)

    doc.add_page_break()

    # =============================================================================
    # CUMPLIMIENTO LEGAL - LEY DE INFOGOBIERNO
    # =============================================================================
    add_heading_formatted(doc, "CUMPLIMIENTO LEGAL - LEY DE INFOGOBIERNO", level=1)
    doc.add_paragraph()

    legal_text = """El presente proyecto se alinea con las normativas nacionales de tecnologia e informacion gubernamental:

1. Ley de Infogobierno (2013):
   - Promueve el uso de software libre y estandares abiertos en la administracion publica
   - Fomenta la transparencia y acceso a la informacion ciudadana
   - Las tecnologias seleccionadas (Astro, TypeScript, Tailwind CSS) son software libre

2. Gestion de Dominio .gob.ve:
   - Los dominios institucionales publicos son gestionados por CONATEL
   - El tramite se realizara en coordinacion con la Oficina de Tecnologia del MPPS
   - Costo de dominio: $0 (gestion institucional gratuita)

3. Infraestructura Nacional:
   - El sitio esta disenado para ser alojado en servidores del Ministerio de Salud
   - Cumple con las directrices de SUSCERTE y CNTI para plataformas gubernamentales
   - Puede ser exportado como HTML/CSS puro para cualquier servidor nacional

4. Consideraciones:
   - No se requieren pagos recurrentes a proveedores externos
   - El mantenimiento tecnico puede realizarse con personal del area de informatica del hospital
   - Se entrega con manuales de administracion y contenido"""

    add_paragraph_formatted(doc, legal_text.strip())

    doc.add_page_break()

    # =============================================================================
    # IMPACTO SOCIAL - REDUCCION DE COLAS
    # =============================================================================
    add_heading_formatted(doc, "IMPACTO SOCIAL - REDUCCION DE COLAS", level=1)
    doc.add_paragraph()

    impacto_text = """Una de las principales ventajas de la implementacion del sitio web institucional es la reduccion de la congestion fisica en las instalaciones del hospital:

1. Problema Actual:
   - Familiares y pacientes realizan colas extensas para obtener informacion basica
   - Consultas sobre requisitos del Banco de Sangre requieren presencia fisica
   - Horarios de especialistas y disponibilidad no son accesibles remotamente
   - El personal administrativo dedica tiempo excesivo a responder consultas repetitivas

2. Solucion Propuesta:
   - El ciudadano puede consultar desde su telefono o computadora:
      - Requisitos para donacion de sangre
      - Horarios de consulta de especialidades
      - Ubicacion de servicios dentro del hospital
      - Programas de pregrado y postgrado disponibles
      - Estadisticas de gestion hospitalaria

3. Beneficios Cuantificables:
   - Reduccion estimada del 30% en consultas presenciales por informacion
   - Ahorro de tiempo para familiares en sectores populares (Catia, Petara, Caracas Este)
   - Mejora en la eficiencia operativa del personal administrativo
   - Disponibilidad de informacion 24/7 durante todo el ano

4. Impacto en Poblaciones Vulnerables:
   - Personas de la tercera edad evitaran desplazamientos innecesarios
   - Familias de sectores populares con acceso limitado a transporte
   - Madres con ninos pequenos que pueden consultar desde casa
   - Pacientes con enfermedades cronicas que requieren seguimiento constante"""

    add_paragraph_formatted(doc, impacto_text.strip())

    doc.add_page_break()

    # =============================================================================
    # V. IDENTIDAD INSTITUCIONAL
    # =============================================================================
    add_heading_formatted(doc, "V. IDENTIDAD INSTITUCIONAL", level=1)
    doc.add_paragraph()

    identidad_text = """El diseno del sitio web refleja la identidad institucional del Hospital Vargas de Caracas:

Paleta de colores:
- Azul institucional: #1E3A5F (principal)
- Azul claro: #2C5282 (secundario)
- Blanco: #FFFFFF (textos sobre fondo oscuro)
- Dorado: #B8860B (acentos)

Tipografia:
- Titulos: Helvetica Bold / Arial Bold
- Cuerpo: Helvetica / Arial
- Lectura optimizada para pantallas

Logotipo:
- Uso del logotipo oficial del Hospital Vargas
- Version horizontal para header
- Version compactada para movil

Tono de comunicacion:
- Profesional y formal
- Accesible para todo publico
- Informacion clara y concisa
- Espanol oficial (espanol neutro)"""

    add_paragraph_formatted(doc, identidad_text.strip())

    doc.add_page_break()

    # =============================================================================
    # VI. PLAN DE IMPLEMENTACION
    # =============================================================================
    add_heading_formatted(doc, "VI. PLAN DE IMPLEMENTACION", level=1)
    doc.add_paragraph()

    add_heading_formatted(doc, "6.1 Fases del Proyecto", level=2)

    fases = [
        (
            "Fase 1: Analisis y Planificacion",
            "2 semanas",
            [
                "Reuniones con autoridades del hospital",
                "Recopilacion de contenido existente",
                "Definicion de estructura de informacion",
                "Aprobacion de mockups y wireframes",
            ],
        ),
        (
            "Fase 2: Desarrollo",
            "4 semanas",
            [
                "Disenio de interfaces",
                "Implementacion de codigo",
                "Integracion de contenido",
                "Pruebas de rendimiento",
            ],
        ),
        (
            "Fase 3: Pruebas y Ajustes",
            "2 semanas",
            [
                "Pruebas en multiples navegadores",
                "Pruebas de responsividad",
                "Validacion de accesibilidad",
                "Correccion de errores",
            ],
        ),
        (
            "Fase 4: Despliegue",
            "1 semana",
            [
                "Configuracion de dominio",
                "Despliegue a produccion",
                "Monitoreo de errores",
                "Capacitacion al personal",
            ],
        ),
    ]

    for fase, duracion, tareas in fases:
        add_paragraph_formatted(doc, f"{fase} ({duracion})", bold=True)
        for tarea in tareas:
            add_paragraph_formatted(doc, f"   - {tarea}", size=10)
        doc.add_paragraph()

    add_heading_formatted(doc, "6.2 Cronograma", level=2)
    add_paragraph_formatted(
        doc, "Duracion total estimada: 9 semanas (aproximadamente 2 meses)", bold=True
    )
    doc.add_paragraph()
    add_table_cronograma(doc)

    doc.add_paragraph()
    add_heading_formatted(doc, "6.3 Recursos y Entregables", level=2)
    recursos = [
        ("Recurso humano", "1 desarrollador web senior, 1 disenador"),
        ("Infraestructura", "Hosting en Vercel, dominio .gob.ve"),
        ("Contenido", "Textos, imagenes y datos proporcionados por el hospital"),
        ("Entregable final", "Sitio web en produccion, documentacion, capacitacion"),
    ]
    for recurso, desc in recursos:
        add_paragraph_formatted(doc, f"- {recurso}: {desc}")

    doc.add_page_break()

    # =============================================================================
    # VII. INVERSION Y PRESUPUESTO
    # =============================================================================
    add_heading_formatted(doc, "VII. INVERSION Y PRESUPUESTO", level=1)
    doc.add_paragraph()

    add_paragraph_formatted(
        doc,
        "A continuacion se presenta el presupuesto estimado para el desarrollo e implementacion del sitio web institucional:",
    )
    doc.add_paragraph()
    add_paragraph_formatted(
        doc,
        "La inversion se divide en dos categorias: desarrollo (una vez) y mantenimiento anual (recurrente).",
    )
    doc.add_paragraph()

    add_table_inversion(doc)

    doc.add_paragraph()
    notas_text = """Notas importantes:
- Los costos de desarrollo incluyen disenio, desarrollo, pruebas y capacitacion
- El dominio requiere registro oficial a traves de los canales correspondientes del MPPS
- El hosting en Vercel incluye SSL, CDN, y soporte tecnico
- El mantenimiento anual incluye actualizaciones de seguridad y contenido
- Los costos pueden variar segun necesidades especificas del proyecto

Forma de pago propuesta:
- 40% al inicio del proyecto (aprobacion de propuesta)
- 30% al completar fase de desarrollo
- 30% al entregar sitio web en produccion"""
    add_paragraph_formatted(doc, notas_text.strip())

    doc.add_page_break()

    # =============================================================================
    # VIII. SOSTENIBILIDAD Y MANTENIMIENTO
    # =============================================================================
    add_heading_formatted(doc, "VIII. SOSTENIBILIDAD Y MANTENIMIENTO", level=1)
    doc.add_paragraph()

    sostenibilidad_text = """Para garantizar la sostenibilidad del sitio web a largo plazo, se proponen las siguientes acciones:

1. Mantenimiento Tecnico:
   - Actualizaciones de seguridad mensuales
   - Monitoreo de uptime 24/7
   - Respaldo automatico de codigo
   - Actualizaciones del framework Astro

2. Actualizacion de Contenido:
   - El personal del hospital puede actualizar textos e imagenes
   - Se proporcionara manual de usuario detallado
   - Soporte tecnico remoto disponible

3. Capacitacion:
   - Sesion de formacion para personal responsable
   - Documentacion de procedimientos
   - Videos tutoriales de uso

4. Metricas de Exito:
   - Numero de visitantes unicos
   - Tiempo promedio en pagina
   - Tasa de rebote
   - Posicionamiento en buscadores (SEO)"""

    add_paragraph_formatted(doc, sostenibilidad_text.strip())

    doc.add_page_break()

    # =============================================================================
    # IX. CONCLUSIONES Y RECOMENDACIONES
    # =============================================================================
    add_heading_formatted(doc, "IX. CONCLUSIONES Y RECOMENDACIONES", level=1)
    doc.add_paragraph()

    conclusiones_text = f"""El Hospital Vargas de Caracas, con sus {HOSPITAL_INFO["annos_historia"]} años de historia y su posicion como segundo centro hospitalario mas importante de Venezuela, requiere una presencia digital que refleje su importancia y compromiso con la salud publica.

Conclusiones:
- El sitio web propuesto cumplira con los mas altos estandares de rendimiento y accesibilidad
- La inversion de ${INVERSION_TOTAL_DESARROLLO:,.2f} es competitiva para un proyecto de esta envergadura
- El mantenimiento anual de ${INVERSION_TOTAL_ANUAL:,.2f} asegura la sostenibilidad del proyecto

Recomendaciones:
1. Aprobar el proyecto para iniciar la fase de planificacion
2. Designar un equipo del hospital para coordinar con el desarrollador
3. Priorizar el registro del dominio hospitalvargas.gob.ve
4. Considerar la integracion con sistemas internos del hospital a futuro"""

    add_paragraph_formatted(doc, conclusiones_text.strip())

    doc.add_page_break()

    # =============================================================================
    # ANEXOS
    # =============================================================================
    add_heading_formatted(doc, "ANEXOS", level=1)
    doc.add_paragraph()

    add_heading_formatted(doc, "Anexo A: Capturas del Prototipo", level=2)
    capturas_text = """[PLACEHOLDER] Se incluiran capturas de pantalla del prototipo desarrollado accesible en: https://hospital-vargas.vercel.app

Capturas planificadas:
- Pagina de inicio (Hero, estadisticas, servicios)
- Pagina de Historia (linea de tiempo)
- Pagina de Servicios (grid de especialidades)
- Pagina del Banco de Sangre
- Pagina de Postgrado
- Pagina de Estadisticas
- Pagina de Contacto"""
    add_paragraph_formatted(doc, capturas_text.strip())

    doc.add_paragraph()
    add_heading_formatted(doc, "Anexo B: Datos de Contacto del Desarrollador", level=2)
    doc.add_paragraph()
    add_table_contacto_dev(doc)

    doc.add_paragraph()
    doc.add_paragraph()
    add_paragraph_formatted(
        doc,
        f"Documento elaborado en {datetime.now().strftime('%B de %Y')}",
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=10,
    )
    add_paragraph_formatted(
        doc,
        "Hospital Vargas de Caracas | Caracas, Venezuela",
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        size=10,
    )

    # =============================================================================
    # GUARDAR DOCUMENTO
    # =============================================================================
    doc.save("Propuesta_Hospital_Vargas.docx")
    print("[OK] Documento DOCX generado exitosamente: Propuesta_Hospital_Vargas.docx")


# =============================================================================
# EJECUCION
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("PROPUESTA DE PROYECTO")
    print("Sitio Web Institucional - Hospital Vargas de Caracas")
    print("=" * 60)
    print()

    # Verificar que python-docx esté instalado
    try:
        from docx import Document

        print("[OK] python-docx instalado correctamente")
    except ImportError:
        print("[ERROR] python-docx no está instalado")
        print("   Instalar con: pip install python-docx")
        exit(1)

    print()
    print("Generando documento DOCX...")
    print()

    generar_propuesta_docx()

    print()
    print("=" * 60)
    print("PROCESO COMPLETADO")
    print("=" * 60)
