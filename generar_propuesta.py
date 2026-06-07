#!/usr/bin/env python3
"""
PROPUESTA DE PROYECTO
=====================
Sitio Web Institucional - Hospital José María Vargas
Dirigido a: Junta Directiva del Hospital Vargas y Ministerio del Poder Popular para la Salud

Autor: Desarrollo Web Hospital Vargas
Fecha: Junio 2026
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
    ListFlowable,
    ListItem,
    KeepTogether,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import Image
from reportlab.lib import colors
import os
from datetime import datetime

# =============================================================================
# CONFIGURACIÓN DE COLORES INSTITUCIONALES
# =============================================================================
AZUL_INSTITUCIONAL = HexColor("#1E3A5F")
AZUL_CLARO = HexColor("#2C5282")
GRIS_OSCURO = HexColor("#2D3748")
GRIS_CLARO = HexColor("#718096")
BLANCO = HexColor("#FFFFFF")
DORADO = HexColor("#B8860B")

# =============================================================================
# ESTILOS DEL DOCUMENTO
# =============================================================================
styles = getSampleStyleSheet()

# Estilo para título principal
style_titulo_principal = ParagraphStyle(
    "TituloPrincipal",
    parent=styles["Heading1"],
    fontSize=28,
    textColor=AZUL_INSTITUCIONAL,
    alignment=TA_CENTER,
    spaceAfter=20,
    fontName="Helvetica-Bold",
    leading=34,
)

# Estilo para subtítulo
style_subtitulo = ParagraphStyle(
    "Subtitulo",
    parent=styles["Heading2"],
    fontSize=18,
    textColor=AZUL_CLARO,
    alignment=TA_CENTER,
    spaceAfter=12,
    fontName="Helvetica",
)

# Estilo para nombres de autoridades
style_nombre_autoridad = ParagraphStyle(
    "NombreAutoridad",
    parent=styles["Heading2"],
    fontSize=14,
    textColor=AZUL_INSTITUCIONAL,
    alignment=TA_CENTER,
    spaceAfter=6,
    fontName="Helvetica-Bold",
)

# Estilo para títulos de sección
style_seccion = ParagraphStyle(
    "Seccion",
    parent=styles["Heading1"],
    fontSize=16,
    textColor=AZUL_INSTITUCIONAL,
    spaceBefore=20,
    spaceAfter=12,
    fontName="Helvetica-Bold",
    borderPadding=5,
)

# Estilo para subsección
style_subseccion = ParagraphStyle(
    "Subseccion",
    parent=styles["Heading2"],
    fontSize=13,
    textColor=AZUL_CLARO,
    spaceBefore=14,
    spaceAfter=8,
    fontName="Helvetica-Bold",
)

# Estilo para texto normal
style_texto = ParagraphStyle(
    "TextoNormal",
    parent=styles["Normal"],
    fontSize=11,
    textColor=GRIS_OSCURO,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    fontName="Helvetica",
    leading=14,
)

# Estilo para texto de cuerpo
style_cuerpo = ParagraphStyle(
    "Cuerpo",
    parent=styles["Normal"],
    fontSize=11,
    textColor=GRIS_OSCURO,
    alignment=TA_LEFT,
    spaceAfter=6,
    fontName="Helvetica",
    leading=13,
)

# Estilo para listas
style_lista = ParagraphStyle(
    "Lista",
    parent=styles["Normal"],
    fontSize=11,
    textColor=GRIS_OSCURO,
    alignment=TA_LEFT,
    spaceAfter=4,
    fontName="Helvetica",
    leftIndent=20,
    leading=13,
)

# Estilo para tablas
style_tabla_header = ParagraphStyle(
    "TablaHeader",
    parent=styles["Normal"],
    fontSize=10,
    textColor=BLANCO,
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
)

style_tabla_celda = ParagraphStyle(
    "TablaCelda",
    parent=styles["Normal"],
    fontSize=9,
    textColor=GRIS_OSCURO,
    alignment=TA_LEFT,
    fontName="Helvetica",
)

# =============================================================================
# CONTENIDO DEL DOCUMENTO
# =============================================================================

# AUTORIDADES INSTITUCIONALES
AUTORIDADES = {
    "ministra": "Dra. Nuramy Josefa Gutiérrez González",
    "viceministra_integral": "GB. Dra. Rosalbina Hurtado Ruiz",
    "director_hospital": "Dr. José Gregorio Rincón",
    "viceministerio_hospitales": "Mauricio Erasmo Vega Méndez",
    "viceministerio_ambulatoria": "Dra. Noly Fernández Hernández",
    "viceministerio_colectiva": "Dra. Magda Mara Magris Crestini",
    "viceministerio_tecnologia": "Alexandra Josefina Hernández de Castillo",
}

# INFORMACIÓN DEL HOSPITAL
HOSPITAL_INFO = {
    "nombre": "Hospital José María Vargas",
    "nombre_completo": "Hospital José María Vargas de Caracas",
    "fundacion": "5 de julio de 1891",
    "annos_historia": "134",
    "categoria": "Hospital Tipo 4",
    "ubicacion": "Monte Carmelo a San Pirito, Esq. del Hospital, Parroquia San José, Caracas",
    "telefono": "(0212) 862-9965",
    "email": "hospitalvargas@gmail.com",
    "area_influencia": "400 mil habitantes",
    "especialidades": "35+",
    "programas_postgrado": "132",
}

# STACK TECNOLÓGICO
STACK = {
    "framework": "Astro v5.5.3",
    "lenguaje": "TypeScript",
    "estilos": "Tailwind CSS v4",
    "iconos": "Lucide Icons",
    "despliegue": "Vercel (CDN Global)",
    "rendimiento": "< 2 segundos carga, < 20 requests",
    "dominio_propuesto": "hospitalvargas.gob.ve",
}

# PÁGINAS DEL SITIO
PAGINAS_SITIO = [
    ("/", "Inicio", "Hero, estadísticas, servicios destacados"),
    ("/historia", "Historia", "Línea de tiempo desde 1891, figuras históricas"),
    ("/servicios", "Servicios", "32 especialidades médicas categorizadas"),
    (
        "/banco-de-sangre",
        "Banco de Sangre",
        "Centro de referencia nacional, requisitos, tipos",
    ),
    ("/pregrado", "Pregrado", "Programas de la Escuela de Medicina UCV"),
    ("/postgrado", "Postgrado", "132 programas de especialización/maestría/doctorado"),
    ("/estadisticas", "Estadísticas", "Indicadores de gestión hospitalaria"),
    ("/noticias", "Noticias", "Novedades y eventos"),
    ("/contacto", "Contacto", "Información de contacto, ubicación"),
    ("/404", "404", "Página de error"),
]

# ESPECIALIDADES MÉDICAS
ESPECIALIDADES = [
    "Cuidados Intensivos",
    "Anatomía Patológica",
    "Anestesiología",
    "Cirugía Cardiovascular",
    "Cirugía Experimental",
    "Cirugía General",
    "Cirugía Plástica",
    "Dermatología",
    "Endocrinología",
    "Farmacia",
    "Hematología",
    "Infectología",
    "Medicina Interna",
    "Medicina Nuclear",
    "Nefrología",
    "Neurocirugía",
    "Neurología",
    "Nutrición y Dietética",
    "O.R.L. (Otorrinolaringología)",
    "Odontología",
    "Oftalmología",
    "Oncología",
    "Pediatría",
    "Psiquiatría",
    "Radiología y Diagnóstico por Imágenes",
    "Reumatología",
    "Tórax y Neumonología",
    "Traumatología",
    "Urología",
    "Unidad de Diabetes",
    "Unidad del Dolor",
    "Unidad de Emergencia",
]

# INVERSIÓN ESTIMADA
INVERSION = {
    "desarrollo_web": {
        "descripcion": "Desarrollo del sitio web institucional completo",
        "monto": 7000,
        "notas": "Incluye diseño, desarrollo, pruebas y manuales de usuario",
    },
    "dominio_anual": {
        "descripcion": "Dominio hospitalvargas.gob.ve (gestión CONATEL)",
        "monto": 0,
        "notas": "Dominios .gob.ve gestionados gratuitamente por CONATEL",
    },
    "hosting_anual": {
        "descripcion": "Alojamiento en servidores del MPPS",
        "monto": 0,
        "notas": "Infraestructura nacional - Ley de Infogobierno",
    },
    "mantenimiento_anual": {
        "descripcion": "Mantenimiento y actualizaciones (anual)",
        "monto": 2400,
        "notas": "Soporte técnico, actualizaciones de seguridad y contenido",
    },
    "capacitacion": {
        "descripcion": "Capacitación al personal del hospital",
        "monto": 0,
        "notas": "Cortesía del proyecto - Manual de usuario incluido",
    },
}

INVERSION_TOTAL_DESARROLLO = 7000 + 0 + 0 + 0  # 7000
INVERSION_TOTAL_ANUAL = 0 + 0 + 2400  # 2400

# =============================================================================
# FUNCIONES DE CONSTRUCCIÓN DEL DOCUMENTO
# =============================================================================


def build_header_footer(canvas, doc):
    """Encabezado y pie de página"""
    canvas.saveState()

    # Header
    canvas.setFillColor(AZUL_INSTITUCIONAL)
    canvas.rect(0, letter[1] - 50, letter[0], 50, fill=1)
    canvas.setFillColor(BLANCO)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(
        72,
        letter[1] - 32,
        "PROPUESTA: Sitio Web Institucional - Hospital José María Vargas",
    )
    canvas.drawRightString(
        letter[0] - 72, letter[1] - 32, datetime.now().strftime("%d/%m/%Y")
    )

    # Footer
    canvas.setFillColor(AZUL_INSTITUCIONAL)
    canvas.rect(0, 0, letter[0], 40, fill=1)
    canvas.setFillColor(BLANCO)
    canvas.setFont("Helvetica", 9)
    canvas.drawString(72, 15, "Hospital José María Vargas | Caracas, Venezuela")
    canvas.drawRightString(letter[0] - 72, 15, f"Página {doc.page}")

    canvas.restoreState()


def crear_tabla_autoridades():
    """Tabla con las autoridades institucionales"""
    data = [
        ["CARGO", "TITULAR"],
        ["Ministra del Poder Popular para la Salud", AUTORIDADES["ministra"]],
        ["Viceministra de Salud Integral", AUTORIDADES["viceministra_integral"]],
        ["Director General del Hospital Vargas", AUTORIDADES["director_hospital"]],
        ["Viceministro de Hospitales (E)", AUTORIDADES["viceministerio_hospitales"]],
        [
            "Viceminista de Redes de Atención Ambulatoria (E)",
            AUTORIDADES["viceministerio_ambulatoria"],
        ],
        [
            "Viceminista de Redes de Salud Colectiva (E)",
            AUTORIDADES["viceministerio_colectiva"],
        ],
        [
            "Viceminista de Recursos, Tecnología y Regulación (E)",
            AUTORIDADES["viceministerio_tecnologia"],
        ],
    ]

    table = Table(data, colWidths=[250, 280])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_INSTITUCIONAL),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    return table


def crear_tabla_stack():
    """Tabla con el stack tecnológico"""
    data = [
        ["COMPONENTE", "TECNOLOGÍA", "BENEFICIO"],
        ["Framework", STACK["framework"], "Alto rendimiento, build estático"],
        ["Lenguaje", STACK["lenguaje"], "Tipado, menos errores, mejor mantenibilidad"],
        ["Estilos", STACK["estilos"], "Diseño responsivo y consistente"],
        ["Iconos", STACK["iconos"], "Gráficos vectoriales optimizados"],
        ["Despliegue", STACK["despliegue"], "CDN global, alta disponibilidad"],
        ["Rendimiento", STACK["rendimiento"], "Carga rápida, mejor SEO"],
    ]

    table = Table(data, colWidths=[100, 140, 200])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_CLARO),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    return table


def crear_tabla_paginas():
    """Tabla con las páginas del sitio"""
    data = [["RUTA", "PÁGINA", "DESCRIPCIÓN"]]
    for pagina in PAGINAS_SITIO:
        data.append([pagina[0], pagina[1], pagina[2]])

    table = Table(data, colWidths=[80, 100, 250])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_INSTITUCIONAL),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    return table


def crear_tabla_inversion():
    """Tabla con la inversión estimada"""
    data = [
        ["CONCEPTO", "DESCRIPCIÓN", "MONTO (USD)"],
        [
            "Desarrollo Web",
            INVERSION["desarrollo_web"]["descripcion"],
            f"${INVERSION['desarrollo_web']['monto']:,.2f}",
        ],
        [
            "Dominio (anual)",
            INVERSION["dominio_anual"]["descripcion"],
            f"${INVERSION['dominio_anual']['monto']:,.2f}",
        ],
        [
            "Hosting (anual)",
            INVERSION["hosting_anual"]["descripcion"],
            f"${INVERSION['hosting_anual']['monto']:,.2f}",
        ],
        [
            "Mantenimiento (anual)",
            INVERSION["mantenimiento_anual"]["descripcion"],
            f"${INVERSION['mantenimiento_anual']['monto']:,.2f}",
        ],
        [
            "Capacitación",
            INVERSION["capacitacion"]["descripcion"],
            f"${INVERSION['capacitacion']['monto']:,.2f}",
        ],
        ["TOTAL DESARROLLO", "", f"${INVERSION_TOTAL_DESARROLLO:,.2f}"],
        ["TOTAL ANUAL (recurrente)", "", f"${INVERSION_TOTAL_ANUAL:,.2f}"],
    ]

    table = Table(data, colWidths=[130, 220, 90])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_INSTITUCIONAL),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, -2), (-1, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
                ("BACKGROUND", (0, -2), (-1, -1), HexColor("#E2E8F0")),
                ("BACKGROUND", (0, 1), (-1, -3), HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -3),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    return table


def crear_tabla_especialidades():
    """Tabla con las especialidades médicas"""
    items = []
    row = []
    for i, esp in enumerate(ESPECIALIDADES):
        row.append(esp)
        if len(row) == 3:
            items.append(row)
            row = []
    if row:
        while len(row) < 3:
            row.append("")
        items.append(row)

    data = [["ESPECIALIDADES MÉDICAS"]]
    for row in items:
        data.append(row)

    table = Table(data, colWidths=[180, 180, 180])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_CLARO),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 11),
                ("FONTSIZE", (0, 1), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("TOPPADDING", (0, 0), (-1, 0), 8),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
                ("TOPPADDING", (0, 1), (-1, -1), 4),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    return table


def crear_seccion(nombre, contenido, story):
    """Crea una sección con título y contenido"""
    story.append(Spacer(1, 15))
    story.append(Paragraph(nombre, style_seccion))
    story.append(HRFlowable(width="100%", thickness=2, color=AZUL_INSTITUCIONAL))
    story.append(Spacer(1, 10))
    for item in contenido:
        if isinstance(item, str):
            story.append(Paragraph(item, style_texto))
        else:
            story.append(item)
    story.append(Spacer(1, 10))


# =============================================================================
# CONSTRUCCIÓN DEL DOCUMENTO
# =============================================================================


def generar_propuesta():
    """Genera el documento PDF de la propuesta"""

    page_width, page_height = letter

    doc = SimpleDocTemplate(
        "Propuesta_Hospital_Vargas.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=80,
        bottomMargin=60,
    )

    story = []

    # =============================================================================
    # PORTADA
    # =============================================================================
    story.append(Spacer(1, 80))
    story.append(Paragraph("REPUBLICA BOLIVARIANA DE VENEZUELA", style_subtitulo))
    story.append(Spacer(1, 10))
    story.append(
        Paragraph("Ministerio del Poder Popular para la Salud", style_nombre_autoridad)
    )
    story.append(Spacer(1, 10))
    story.append(Paragraph("Hospital José María Vargas", style_nombre_autoridad))
    story.append(Spacer(1, 40))

    # Título principal
    story.append(Paragraph("PROPUESTA DE PROYECTO", style_titulo_principal))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Sitio Web Institucional", style_subtitulo))
    story.append(
        Paragraph(f"<b>{HOSPITAL_INFO['nombre_completo']}</b>", style_subtitulo)
    )
    story.append(Spacer(1, 30))

    # Información del proyecto
    story.append(
        HRFlowable(width="60%", thickness=1, color=GRIS_CLARO, hAlign="CENTER")
    )
    story.append(Spacer(1, 20))

    info_proyecto = f"""
    <b>Fecha:</b> {datetime.now().strftime("%d de %B de %Y")}<br/>
    <b>Elaborado por:</b> Equipo de Desarrollo Web<br/>
    <b>Dirigido a:</b> Junta Directiva del Hospital Vargas y Ministerio del Poder Popular para la Salud
    """
    story.append(
        Paragraph(
            info_proyecto,
            ParagraphStyle(
                "InfoProyecto",
                parent=styles["Normal"],
                fontSize=11,
                textColor=GRIS_OSCURO,
                alignment=TA_CENTER,
                leading=16,
            ),
        )
    )

    story.append(Spacer(1, 60))

    # Tabla de autoridades
    story.append(crear_tabla_autoridades())

    story.append(PageBreak())

    # =============================================================================
    # ÍNDICE
    # =============================================================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("ÍNDICE", style_titulo_principal))
    story.append(HRFlowable(width="100%", thickness=2, color=AZUL_INSTITUCIONAL))
    story.append(Spacer(1, 20))

    indice_items = [
        "I. RESUMEN EJECUTIVO",
        "II. INTRODUCCIÓN Y JUSTIFICACIÓN",
        "III. DESCRIPCIÓN DEL PROYECTO",
        "    3.1 Objetivos",
        "    3.2 Alcance",
        "    3.3 Beneficios Esperados",
        "IV. ESPECIFICACIONES TÉCNICAS",
        "    4.1 Arquitectura Tecnológica",
        "    4.2 Stack Tecnológico",
        "    4.3 Características de Rendimiento",
        "    4.4 Seguridad y Disponibilidad",
        "    4.5 Portabilidad del Sistema",
        "    4.6 Mapa del Sitio",
        "CUMPLIMIENTO LEGAL - LEY DE INFOGOBIERNO",
        "IMPACTO SOCIAL - REDUCCIÓN DE COLAS",
        "V. IDENTIDAD INSTITUCIONAL",
        "VI. PLAN DE IMPLEMENTACIÓN",
        "    6.1 Fases del Proyecto",
        "    6.2 Cronograma",
        "    6.3 Recursos y Entregables",
        "VII. INVERSIÓN Y PRESUPUESTO",
        "VIII. SOSTENIBILIDAD Y MANTENIMIENTO",
        "IX. CONCLUSIONES Y RECOMENDACIONES",
        "ANEXOS",
    ]

    for item in indice_items:
        story.append(Paragraph(item, style_cuerpo))

    story.append(PageBreak())

    # =============================================================================
    # I. RESUMEN EJECUTIVO
    # =============================================================================
    crear_seccion(
        "I. RESUMEN EJECUTIVO",
        [
            f"El presente documento propone el desarrollo e implementación del <b>Sitio Web Institucional del Hospital José María Vargas</b>, "
            f"como plataforma digital oficial del segundo centro hospitalario más importante de Venezuela.",
            "",
            f"Fundado el {HOSPITAL_INFO['fundacion']}, el Hospital José María Vargas cuenta con <b>{HOSPITAL_INFO['annos_historia']} años de historia</b> "
            f"y atiende a un área de influencia de más de <b>{HOSPITAL_INFO['area_influencia']}</b>. Con <b>{HOSPITAL_INFO['especialidades']} especialidades médicas</b> "
            f"y <b>{HOSPITAL_INFO['programas_postgrado']} programas de postgrado</b>, es referente nacional en formación médica.",
            "",
            "La propuesta contempla la creación de un sitio web de alto rendimiento, accesible desde cualquier dispositivo, "
            "que permita a la ciudadanía acceder a información sobre servicios médicos, historia institucional, programas "
            "académicos y统计数据 de gestión hospitalaria.",
            "",
            "<b>Puntos clave:</b>",
            "• Sitio web con 10 páginas de contenido institucional completo",
            "• Tiempo de carga menor a 2 segundos",
            "• Arquitectura de seguridad robusta con SSL y CDN global",
            f"• Inversión total de desarrollo: <b>${INVERSION_TOTAL_DESARROLLO:,.2f}</b>",
            f"• Costo anual de mantenimiento: <b>${INVERSION_TOTAL_ANUAL:,.2f}</b>",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # II. INTRODUCCIÓN Y JUSTIFICACIÓN
    # =============================================================================
    crear_seccion(
        "II. INTRODUCCIÓN Y JUSTIFICACIÓN",
        [
            "En la era digital, la presencia en línea de las instituciones de salud pública es fundamental para garantizar "
            "la transparencia, accessibility y calidad de la información提供给 ciudadanos.",
            "",
            "<b>Justificación del proyecto:</b>",
            "",
            "1. <b>Transparencia Institucional:</b> Un sitio web oficial permite a la ciudadanía acceder a información "
            "actualizada sobre servicios, horarios, especialidades y统计数据 de gestión del hospital.",
            "",
            "2. <b>Mejora en la Comunicación:</b> Facilita la comunicación entre el hospital y la población, permitiendo "
            "la difusión de noticias, alertas epidemiológicas y campañas de salud.",
            "",
            f"3. <b>Referencia Nacional:</b> Como {HOSPITAL_INFO['categoria']}, el Hospital Vargas requiere una "
            "presencia digital que refleje su importancia y liderazgo en el sistema de salud venezolano.",
            "",
            "4. <b>Modernización:</b> La implementación de tecnología web de última generación posiciona al hospital "
            "como institución moderna y comprometida con la excelencia.",
            "",
            "5. <b>Accesibilidad:</b> El sitio web permitirá que pacientes y familiares accedan a información desde "
            "cualquier lugar y dispositivo, mejorando la experiencia del usuario.",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # III. DESCRIPCIÓN DEL PROYECTO
    # =============================================================================
    crear_seccion("III. DESCRIPCIÓN DEL PROYECTO", [], story)

    story.append(Paragraph("3.1 Objetivos", style_subseccion))
    story.append(Paragraph("<b>Objetivo General:</b>", style_cuerpo))
    story.append(
        Paragraph(
            "Desarrollar e implementar el sitio web institucional del Hospital José María Vargas como plataforma "
            "digital oficial, que permita a la ciudadanía acceder a información sobre servicios médicos, programas "
            "académicos e institucionales del hospital.",
            style_texto,
        )
    )

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Objetivos Específicos:</b>", style_cuerpo))
    objetivos = [
        "Crear un sitio web responsivo y accesible desde cualquier dispositivo",
        "Publicar información completa sobre las 35+ especialidades médicas",
        "Mostrar los 132 programas de postgrado disponibles",
        "Proporcionar información sobre el Banco Municipal de Sangre",
        "Implementar canales de comunicación para contacto y consultas",
        "Garantizar alto rendimiento y tiempos de carga rápidos",
        "Optimizar para motores de búsqueda (SEO)",
        "Cumplir con estándares de accesibilidad web",
    ]
    for obj in objetivos:
        story.append(Paragraph(f"• {obj}", style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("3.2 Alcance", style_subseccion))
    story.append(
        Paragraph(
            "El proyecto comprende el desarrollo completo del sitio web institucional, incluyendo:",
            style_texto,
        )
    )
    alcance = [
        "Diseño y desarrollo de 10 páginas web completas",
        "Sistema de gestión de contenidos estático (sin base de datos)",
        "Integración con mapa del sitio y SEO",
        "Responsive design para móviles, tablets y escritorio",
        "Iconografía médica personalizada",
        "Formulario de contacto funcional",
        "Despliegue en infraestructura CDN",
        "Capacitación al personal del hospital",
    ]
    for item in alcance:
        story.append(Paragraph(f"• {item}", style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("3.3 Beneficios Esperados", style_subseccion))
    beneficios = [
        (
            "Mejor atención al ciudadano",
            "Información accesible 24/7 sobre servicios hospitalarios",
        ),
        ("Transparencia", "Datos abiertos sobre estadísticas y indicadores de gestión"),
        (
            "Eficiencia",
            "Reducción de consultas presenciales mediante información digital",
        ),
        (
            "Imagen institucional",
            "Presencia digital profesional que refleja calidad médica",
        ),
        ("Educación", "difusión de programas de pregrado y postgrado"),
        ("Comunicación", "Canal oficial para noticias y alertas epidemiológicas"),
    ]
    for benef, desc in beneficios:
        story.append(Paragraph(f"• <b>{benef}:</b> {desc}", style_lista))

    story.append(PageBreak())

    # =============================================================================
    # IV. ESPECIFICACIONES TÉCNICAS
    # =============================================================================
    crear_seccion("IV. ESPECIFICACIONES TÉCNICAS", [], story)

    story.append(Paragraph("4.1 Arquitectura Tecnológica", style_subseccion))
    story.append(
        Paragraph(
            "El sitio web采用了 una arquitectura moderna de generación estática que permite máximo rendimiento "
            "y mínima dependencia de infraestructura:",
            style_texto,
        )
    )
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Diagrama de Arquitectura:</b>", style_cuerpo))
    arch = [
        "• Navegador → CDN Vercel → Archivos estáticos (HTML/CSS/JS)",
        "• Sin servidor de aplicaciones",
        "• Sin base de datos",
        "• Generación en build time",
        "• Despliegue global automático",
    ]
    for item in arch:
        story.append(Paragraph(item, style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("4.2 Stack Tecnológico", style_subseccion))
    story.append(Spacer(1, 5))
    story.append(crear_tabla_stack())

    story.append(Spacer(1, 15))
    story.append(Paragraph("4.3 Características de Rendimiento", style_subseccion))
    rendimiento = [
        f"• <b>Tiempo de carga:</b> < 2 segundos",
        f"• <b>Solicitudes HTTP:</b> < 20 por página",
        "• <b>Build estático:</b> HTML pre-generado",
        "• <b>Sin JavaScript del cliente:</b> Rendering en servidor",
        "• <b>CDN Global:</b> Archivos distribuidos mundialment",
        "• <b>Compresión Gzip:</b> Activada por defecto",
        "• <b>SSL/TLS:</b> HTTPS obligatorio",
    ]
    for item in rendimiento:
        story.append(Paragraph(item, style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("4.4 Seguridad y Disponibilidad", style_subseccion))
    seguridad = [
        "• <b>SSL/TLS:</b> Conexión encriptada HTTPS (obligatorio)",
        "• <b>Backups:</b> Versionamiento git con commits automáticos",
        "• <b>Monitoreo:</b> Uptime monitoring 24/7 en servidores del MPPS",
        "• <b>Infraestructura:</b> Servidores nacionales del Ministerio de Salud",
    ]
    for item in seguridad:
        story.append(Paragraph(item, style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("4.5 Portabilidad del Sistema", style_subseccion))
    portabilidad = [
        "• <b>Tecnología Astro:</b> Genera HTML/CSS/JS estático puro",
        "• <b>Sin dependencias:</b> No requiere Node.js en servidor de producción",
        "• <b>Flexible:</b> Puede alojarse en cualquier servidor web (Apache, Nginx, IIS)",
        "• <b>Servidores nacionales:</b> Compatible con infraestructura MPPS/CANTV",
        "• <b>Migración sencilla:</b> Deployment en un solo paso",
    ]
    for item in portabilidad:
        story.append(Paragraph(item, style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("4.5 Mapa del Sitio", style_subseccion))
    story.append(Spacer(1, 5))
    story.append(crear_tabla_paginas())

    story.append(PageBreak())

    # =============================================================================
    # CUMPLIMIENTO LEGAL - LEY DE INFOGOBIERNO
    # =============================================================================
    crear_seccion(
        "CUMPLIMIENTO LEGAL - LEY DE INFOGOBIERNO",
        [
            "El presente proyecto se alinea con las normativas nacionales de tecnología e información gubernamental:",
            "",
            "<b>1. Ley de Infogobierno (2013):</b>",
            "• Promueve el uso de software libre y estándares abiertos en la administración pública",
            "• Fomenta la transparencia y acceso a la información ciudadana",
            "• Las tecnologías seleccionadas (Astro, TypeScript, Tailwind CSS) son software libre",
            "",
            "<b>2. Gestión de Dominio .gob.ve:</b>",
            "• Los dominios institucionales públicos son gestionados por CONATEL",
            "• El trámite se realizará en coordinación con la Oficina de Tecnología del MPPS",
            "• Costo de dominio: $0 (gestión institucional gratuita)",
            "",
            "<b>3. Infraestructura Nacional:</b>",
            "• El sitio está diseñado para ser alojado en servidores del Ministerio de Salud",
            "• Cumple con las directrices de SUSCERTE y CNTI para plataformas gubernamentales",
            "• Puede ser exportado como HTML/CSS puro para cualquier servidor nacional",
            "",
            "<b>4. Aliases y Consideraciones:</b>",
            "• No se requieren pagos recurrentes a proveedores externos",
            "• El mantenimiento técnico puede realizarse con personal del área de informática del hospital",
            "• Se entrega con manuales de administración y contenido",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # IMPACTO SOCIAL - REDUCCIÓN DE COLAS
    # =============================================================================
    crear_seccion(
        "IMPACTO SOCIAL - REDUCCIÓN DE COLAS",
        [
            "Una de las principales ventajas de la implementación del sitio web institucional es la reducción de la congestión física en las instalaciones del hospital:",
            "",
            "<b>1. Problema Actual:</b>",
            "• Familiares y pacientes realizan colas extensas para obtener información básica",
            "• Consultas sobre requisitos del Banco de Sangre requieren presencia física",
            "• Horarios de especialistas y disponibilidad no son accesibles remotamente",
            "• El personal administrativo dedica tiempo excesivo a responder consultas repetitivas",
            "",
            "<b>2. Solución Propuesta:</b>",
            "• El ciudadano puede consultar desde su teléfono o computadora:",
            "   - Requisitos para donación de sangre",
            "   - Horarios de consulta de especialidades",
            "   - Ubicación de servicios dentro del hospital",
            "   - Programas de pregrado y postgrado disponibles",
            "   - Estadísticas de gestión hospitalaria",
            "",
            "<b>3. Beneficios Cuantificables:</b>",
            "• Reducción estimada del 30% en consultas presenciales por información",
            "• Ahorro de tiempo para familiares en sectores populares (Catia, Petare, Caracas Este)",
            "• Mejora en la eficiencia operativa del personal administrativo",
            "• Disponibilidad de información 24/7 durante todo el año",
            "",
            "<b>4. Impacto en Poblaciones Vulnerables:</b>",
            "• Personas de la tercera edad evitarán desplazamientos innecesarios",
            "• Familias de sectores populares con acceso limitado a transporte",
            "• Madres con niños pequeños que pueden consultar desde casa",
            "• Pacientes con enfermedades crónicas que requieren seguimiento constante",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # V. IDENTIDAD INSTITUCIONAL
    # =============================================================================
    crear_seccion(
        "V. IDENTIDAD INSTITUCIONAL",
        [
            "El diseño del sitio web reflection la identidad institucional del Hospital José María Vargas:",
            "",
            "<b>Paleta de colores:</b>",
            "• Azul institucional: #1E3A5F (principal)",
            "• Azul claro: #2C5282 (secundario)",
            "• Blanco: #FFFFFF (textos sobre fondo oscuro)",
            "• Dorado: #B8860B (acentos)",
            "",
            "<b>Tipografía:</b>",
            "• Títulos: Helvetica Bold / Arial Bold",
            "• Cuerpo: Helvetica / Arial",
            "• Lectura optimizada para pantallas",
            "",
            "<b>Logotipo:</b>",
            "• Uso del logotipo oficial del Hospital Vargas",
            "• Versión horizontal para header",
            "• Versión compactada para móvil",
            "",
            "<b>Tono de comunicación:</b>",
            "• Profesional y formal",
            "• Accesible para todo público",
            "• Información clara y concisa",
            "• Español oficial (español neutro)",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # VI. PLAN DE IMPLEMENTACIÓN
    # =============================================================================
    crear_seccion("VI. PLAN DE IMPLEMENTACIÓN", [], story)

    story.append(Paragraph("6.1 Fases del Proyecto", style_subseccion))
    fases = [
        (
            "Fase 1: Análisis y Planificación",
            "2 semanas",
            [
                "Reuniones con autoridades del hospital",
                "Recopilación de contenido existente",
                "Definición de estructura de información",
                "Aprobación de mockups y wireframes",
            ],
        ),
        (
            "Fase 2: Desarrollo",
            "4 semanas",
            [
                "Diseño de interfaces",
                "Implementación de código",
                "Integración de contenido",
                "Pruebas de rendimiento",
            ],
        ),
        (
            "Fase 3: Pruebas y Ajustes",
            "2 semanas",
            [
                "Pruebas en múltiples navegadores",
                "Pruebas de responsividad",
                "Validación de accesibilidad",
                "Corrección de errores",
            ],
        ),
        (
            "Fase 4: Despliegue",
            "1 semana",
            [
                "Configuración de dominio",
                "Despliegue a producción",
                "Monitoreo de errores",
                "Capacitación al personal",
            ],
        ),
    ]

    for fase, duracion, tareas in fases:
        story.append(Spacer(1, 8))
        story.append(Paragraph(f"<b>{fase}</b> ({duracion})", style_cuerpo))
        for tarea in tareas:
            story.append(Paragraph(f"   • {tarea}", style_lista))

    story.append(Spacer(1, 15))
    story.append(Paragraph("6.2 Cronograma", style_subseccion))
    story.append(
        Paragraph(
            f"<b>Duración total estimada: 9 semanas (aproximadamente 2 meses)</b>",
            style_texto,
        )
    )
    story.append(Spacer(1, 10))

    cronograma = [
        ["FASE", "SEMANA 1-2", "SEMANA 3-4", "SEMANA 5-6", "SEMANA 7-8", "SEMANA 9"],
        ["Planificación", "███", "", "", "", ""],
        ["Desarrollo", "", "████", "████", "", ""],
        ["Pruebas", "", "", "", "███", ""],
        ["Despliegue", "", "", "", "", "███"],
    ]

    table = Table(cronograma, colWidths=[100, 70, 70, 70, 70, 70])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_INSTITUCIONAL),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F7FAFC")),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    story.append(table)

    story.append(Spacer(1, 15))
    story.append(Paragraph("6.3 Recursos y Entregables", style_subseccion))
    recursos = [
        ("Recurso humano", "1 desarrollador web senior, 1 diseñador"),
        ("Infraestructura", "Hosting en Vercel, dominio .gob.ve"),
        ("Contenido", "Textos, imágenes y datos proporcionados por el hospital"),
        ("Entregable final", "Sitio web en producción, documentación, capacitación"),
    ]
    for recurso, desc in recursos:
        story.append(Paragraph(f"• <b>{recurso}:</b> {desc}", style_lista))

    story.append(PageBreak())

    # =============================================================================
    # VII. INVERSIÓN Y PRESUPUESTO
    # =============================================================================
    crear_seccion(
        "VII. INVERSIÓN Y PRESUPUESTO",
        [
            "A continuación se presenta el presupuesto estimado para el desarrollo e implementación del sitio web institucional:",
            "",
            "La inversión se divide en dos categorías: <b>desarrollo (una vez)</b> y <b>mantenimiento anual (recurrente)</b>.",
        ],
        story,
    )

    story.append(Spacer(1, 10))
    story.append(crear_tabla_inversion())

    story.append(Spacer(1, 20))

    notas_inversion = """
    <b>Notas importantes:</b><br/>
    • Los costos de desarrollo incluyen diseño, desarrollo, pruebas y capacitación<br/>
    • El dominio requiere registro oficial a través de los canales correspondientes del MPPS<br/>
    • El hosting en Vercel incluye SSL, CDN, y soporte técnico<br/>
    • El mantenimiento anual incluye actualizaciones de seguridad y contenido<br/>
    • Los costos pueden variar según necesidades específicas del proyecto
    """
    story.append(Paragraph(notas_inversion, style_texto))

    story.append(Spacer(1, 20))

    forma_pago = """
    <b>Forma de pago propuesta:</b><br/>
    • 40% al inicio del proyecto (aprobación de propuesta)<br/>
    • 30% al completar fase de desarrollo<br/>
    • 30% al entregar sitio web en producción
    """
    story.append(Paragraph(forma_pago, style_texto))

    story.append(PageBreak())

    # =============================================================================
    # VIII. SOSTENIBILIDAD Y MANTENIMIENTO
    # =============================================================================
    crear_seccion(
        "VIII. SOSTENIBILIDAD Y MANTENIMIENTO",
        [
            "Para garantizar la sostenibilidad del sitio web a largo plazo, se proponen las siguientes acciones:",
            "",
            "<b>1. Mantenimiento Técnico:</b>",
            "• Actualizaciones de seguridad mensuales",
            "• Monitoreo de uptime 24/7",
            "• Respaldo automático de código",
            "• Actualizaciones del framework Astro",
            "",
            "<b>2. Actualización de Contenido:</b>",
            "• El personal del hospital puede actualizar textos y imágenes",
            "• Se proporcionará manual de usuario detallado",
            "• Soporte técnico remoto disponible",
            "",
            "<b>3. Capacitación:</b>",
            "• Sesión de formación para personal responsable",
            "• Documentación de procedimientos",
            "• Videos tutoriales de uso",
            "",
            "<b>4. Métricas de Éxito:</b>",
            "• Número de visitantes únicos",
            "• Tiempo promedio en página",
            "• Tasa de rebote",
            "• Posicionamiento en buscadores (SEO)",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # IX. CONCLUSIONES Y RECOMENDACIONES
    # =============================================================================
    crear_seccion(
        "IX. CONCLUSIONES Y RECOMENDACIONES",
        [
            f"El Hospital José María Vargas, con sus <b>{HOSPITAL_INFO['annos_historia']} años de historia</b> y su posición "
            "como segundo centro hospitalario más importante de Venezuela, requiere una presencia digital que refleje "
            "su importancia y compromiso con la salud pública.",
            "",
            "<b>Conclusiones:</b>",
            "• El sitio web propuesto cumplirá con los más altos estándares de rendimiento y accesibilidad",
            f"• La inversión de <b>${INVERSION_TOTAL_DESARROLLO:,.2f}</b> es competitiva para un proyecto de esta envergadura",
            f"• El mantenimiento anual de <b>${INVERSION_TOTAL_ANUAL:,.2f}</b> asegura la sostenibilidad del proyecto",
            "",
            "<b>Recomendaciones:</b>",
            "1. Aprobar el proyecto para iniciar la fase de planificación",
            "2. Designar un equipo del hospital para coordinar con el desarrollador",
            "3. Priorizar el registro del dominio hospitalvargas.gob.ve",
            "4. Considerar la integración con sistemas internos del hospital a futuro",
        ],
        story,
    )

    story.append(PageBreak())

    # =============================================================================
    # ANEXOS
    # =============================================================================
    crear_seccion(
        "ANEXOS",
        ["A continuación se presentan los anexos complementarios a esta propuesta."],
        story,
    )

    story.append(Spacer(1, 15))
    story.append(Paragraph("Anexo A: Capturas del Prototipo", style_subseccion))
    story.append(
        Paragraph(
            "[PLACEHOLDER] Se incluirán capturas de pantalla del prototipo desarrollado "
            "accesible en: <b>https://hospital-vargas.vercel.app</b>",
            style_texto,
        )
    )

    capturas = [
        "• Página de inicio (Hero, estadísticas, servicios)",
        "• Página de Historia (línea de tiempo)",
        "• Página de Servicios (grid de especialidades)",
        "• Página del Banco de Sangre",
        "• Página de Postgrado",
        "• Página de Estadísticas",
        "• Página de Contacto",
    ]
    for cap in capturas:
        story.append(Paragraph(cap, style_lista))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Anexo B: Datos de Contacto", style_subseccion))

    contacto_data = [
        ["INFORMACIÓN DE CONTACTO"],
        [f"Hospital: {HOSPITAL_INFO['nombre']}"],
        [f"Director General: {AUTORIDADES['director_hospital']}"],
        [f"Dirección: {HOSPITAL_INFO['ubicacion']}"],
        [f"Teléfono: {HOSPITAL_INFO['telefono']}"],
        [f"Email: {HOSPITAL_INFO['email']}"],
    ]

    table = Table(contacto_data, colWidths=[400])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), AZUL_CLARO),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("TOPPADDING", (0, 0), (-1, 0), 8),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
                ("TOPPADDING", (0, 1), (-1, -1), 6),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, GRIS_CLARO),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [HexColor("#FFFFFF"), HexColor("#EDF2F7")],
                ),
            ]
        )
    )
    story.append(table)

    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=1, color=GRIS_CLARO))
    story.append(Spacer(1, 15))

    # Pie final
    story.append(
        Paragraph(
            "<b>Documento elaborado en junio de 2026</b><br/>"
            "Hospital José María Vargas | Caracas, Venezuela",
            ParagraphStyle(
                "PieFinal",
                parent=styles["Normal"],
                fontSize=10,
                alignment=TA_CENTER,
                textColor=GRIS_CLARO,
            ),
        )
    )

    # =============================================================================
    # CONSTRUCCIÓN DEL PDF
    # =============================================================================
    doc.build(story, onFirstPage=build_header_footer, onLaterPages=build_header_footer)
    print("[OK] PDF generado exitosamente: Propuesta_Hospital_Vargas.pdf")


# =============================================================================
# EJECUCIÓN
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("PROPUESTA DE PROYECTO")
    print("Sitio Web Institucional - Hospital José María Vargas")
    print("=" * 60)
    print()

    # Verificar que ReportLab esté instalado
    try:
        from reportlab.lib.pagesizes import letter

        print("[OK] ReportLab instalado correctamente")
    except ImportError:
        print("❌ ReportLab no está instalado")
        print("   Instalar con: pip install reportlab")
        exit(1)

    print()
    print("Generando documento PDF...")
    print()

    generar_propuesta()

    print()
    print("=" * 60)
    print("PROCESO COMPLETADO")
    print("=" * 60)
