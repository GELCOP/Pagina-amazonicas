import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import random
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Amazonicas XI",
    page_icon="🌿",
    layout="wide"
)

col1, col2, col3 = st.columns([1,3,1], gap="small")
with col2:
    st.image("logo_amazonicas.png", width=1500)
    #st.image("banner_amazonicas.png", width=1800)
        
#st.markdown(f'<h1 style="font-size: 60px; text-align: center; color: green">Amazonicas XI</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Selectbox */
    div[data-baseweb="select"] > div {
        color: black !important;
        background-color: white !important;
        border: 1px solid #555 !important;
    }

    /* Opciones desplegables */
    div[role="option"] {
        color: black !important;
        background-color: white !important;
    }

    /* Texto dentro del select */
    div[data-baseweb="select"] span {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

idioma = st.selectbox(
    "",
    ["Español", "English", "Português"],
    label_visibility="collapsed"
)

menus = { "Español": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programación", "Organizadores": "Organizadores", 
                      "Convocatoria": "Convocatoria de resúmenes", "Cursos": "Cursos", "Información": "Información"}, 
         "English": {"Evento": "Event", "Amazonicas": "Amazonicas", "Programación": "Program", "Organizadores": "Organizers",
                     "Convocatoria": "Call for abstracts", "Cursos": "Courses", "Información": "Information"}, 
         "Português": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programação", "Organizadores": "Organizadores",
                       "Convocatoria": "Chamada submissão de resumos", "Cursos": "Coursos", "Información": "Informações"} }

opciones_menu = [
    menus[idioma]["Evento"],
    menus[idioma]["Amazonicas"],
    menus[idioma]["Programación"],
    menus[idioma]["Organizadores"],
    menus[idioma]["Convocatoria"],
    menus[idioma]["Cursos"],
    menus[idioma]["Información"]
]


evento = {
    "Español": {
        "Evento": "AMAZONICAS XI — Congreso Internacional sobre Lenguas Amazónicas",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima",
        "Fechas": "Del 15 al 18 de junio de 2027",
        "Temas": [
            "Fonología: prosodia y entonación",
            "Morfosintaxis: oraciones complejas",
            "Lengua y sociedad: revitalización lingüística en contextos de alta obsolescencia",
            "Sesión general: tema libre"
        ],
        "Correo": "amazonicasXI@gmail.com",
        "Lugar_label": "Lugar",
        "Fechas_label": "Fechas",
        "Correo_label": "Correo",
        "Temas_label": "Temas"
    },

    "English": {
        "Evento": "AMAZONICAS XI — International Conference on Amazonian Languages",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima",
        "Fechas": "June 15–18, 2027",
        "Temas": [
            "Phonology: prosody and intonation",
            "Morphosyntax: complex sentences",
            "Language and Society: language revitalization in high obsolescence contexts",
            "General Session: free topic"
        ],
        "Correo": "amazonicasXI@gmail.com",
        "Lugar_label": "Location",
        "Fechas_label": "Dates",
        "Correo_label": "Email",
        "Temas_label": "Topics"
    },

    "Português": {
        "Evento": "AMAZONICAS XI — Conferência Internacional sobre Línguas Amazónicas",
        "Lugar": "Pontifícia Universidade Católica do Peru, Lima",
        "Fechas": "15 a 18 de junho de 2027",
        "Temas": [
            "Fonologia: prosódia e entoação",
            "Morfossintaxe: cláusulas complexas",
            "Língua e sociedade: revitalização linguística em contextos de elevada obsolescência",
            "Sessão geral: tema livre"
        ],
        "Correo": "amazonicasXI@gmail.com",
        "Lugar_label": "Local",
        "Fechas_label": "Datas",
        "Correo_label": "E-mail",
        "Temas_label": "Temas"
    }
}

convocatoria = {
    "Español": {
        "Titulo": "Convocatoria de resúmenes",
        "Subtitulo": "AMAZONICAS XI 2027 – Sesión General",
        "Organizadores": "Organizadores: Elder Lane, Kasia Wojtylak, Sidi Facundes",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Perú",
        "Fecha_evento": "15 al 18 de junio de 2027",

        "Descripcion": """
        La sesión general de AMAZONICAS proporciona un espacio para la presentación
        de trabajos sobre distintos aspectos de las lenguas amazónicas, incluyendo
        temas como la fonética, fonología, morfología, sintaxis, semántica,
        pragmática, estructura informativa, lingüística histórica, psicolingüística,
        tipología, documentación, revitalización, u otros temas lingüísticos no
        cubiertos por los simposios temáticos.
        """,

        "Envio": """
        Entrega de resúmenes: Un documento en formato PDF, máximo 1 página excluyendo las referencias,
        márgenes de 1 pulgada, fuente de 12 puntos y espacio sencillo. Incluya título.
        Las referencias y ejemplos pueden ser entregados en una página separada.
        No incluya nombres o apellidos de autores ni otra información que identifique
        a los autores.
        """,

        "Limite": "Se pueden enviar máximo dos resúmenes, de los cuales solamente uno puede ser como autor único.",

        "Idiomas": "El resumen y la ponencia pueden ser en español, portugués o inglés.",

        "Deadline": "Fecha límite de entrega: 6 de diciembre de 2026",

        "Aceptacion": "Notificación de aceptación: 4 de enero de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Enlace para envío de resúmenes"
    },

    "English": {
        "Titulo": "Call for abstracts",
        "Subtitulo": "AMAZONICAS XI 2027 – General Session",
        "Organizadores": "Organizers: Elder Lane, Kasia Wojtylak, Sidi Facundes",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "June 15 to 18, 2027",

        "Descripcion": """
        The general session of AMAZONICAS provides a forum for papers on diverse
        aspects of Amazonian languages, such as phonetics, phonology, morphology,
        syntax, semantics, pragmatics, information structure, historical linguistics,
        psycholinguistics, typology, documentation, revitalization, or other
        linguistic topics outside of the thematic symposia.
        """,

        "Envio": """
        Abstract submission: One document in PDF format, at most 1 page excluding references,
        1-inch margins, 12pt font, and single-spaced. Include a title.
        References and examples can be provided on an additional page.
        Do not include author names or other identifying information in the abstract.
        """,

        "Limite": "A maximum of two abstracts may be submitted, with only one being single-authored.",

        "Idiomas": "The abstract and the talk can be in Spanish, Portuguese, or English.",

        "Deadline": "Deadline for submission: December 6, 2026",

        "Aceptacion": "Notification of acceptance: January 4, 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Abstract submission link"
    },

    "Português": {
        "Titulo": "Chamada para submissão de resumos",
        "Subtitulo": "AMAZONICAS XI 2027 – Sessão Geral",
        "Organizadores": "Organizadores: Elder Lane, Kasia Wojtylak, Sidi Facundes",
        "Lugar": "Pontifícia Universidade Católica do Peru, Lima, Peru",
        "Fecha_evento": "15 a 18 de junho de 2027",

        "Descripcion": """
        A sessão geral de AMAZONICAS fornece um espaço para a apresentação de
        trabalhos sobre diversos aspectos das línguas amazônicas, incluindo tópicos
        como fonética, fonologia, morfologia, sintaxe, semântica, pragmática,
        estrutura informacional, linguística histórica, psicolinguística, tipologia,
        documentação, revitalização ou outros tópicos linguísticos não cobertos
        pelos simpósios temáticos.
        """,

        "Envio": """
        Submissão de resumos: Um documento em formato PDF, máximo de 1 página sem as referências,
        margens de 1 polegada (2,54 cm), fonte 12 e espaço simples.
        Incluir título. As referências e exemplos podem constar em uma página
        separada. Não incluir os nomes dos autores ou outras informações de
        identificação no resumo.
        """,

        "Limite": "Podem ser submetidos no máximo dois resumos, sendo apenas um deles de autoria única.",

        "Idiomas": "O resumo e a apresentação podem ser em espanhol, português ou inglês.",

        "Deadline": "Prazo para submissão: 6 de dezembro de 2026",

        "Aceptacion": "Notificação de aceitação: 4 de janeiro de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Link para submissão de resumos"
    }
}

opciones = option_menu(
    menu_title=None,
    options=opciones_menu,
    icons=[
        "calendar-event",
        "globe-americas",
        "calendar3",
        "people",
        "megaphone",
        "mortarboard",
        "info-circle"
    ],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if opciones == menus[idioma]["Evento"]: 
    st.markdown( f""" <h2 style=" font-size: 32px; text-align: center; color: #7f3213; "> {evento[idioma]["Evento"]} </h2> """, unsafe_allow_html=True ) 
    st.markdown( f""" <p style="color: #7f3213; font-size: 18px;"> 📍 <strong>{evento[idioma]["Lugar_label"]}:</strong> {evento[idioma]["Lugar"]} </p> <p style="color: #7f3213; font-size: 18px;"> 📅 <strong>{evento[idioma]["Fechas_label"]}:</strong> {evento[idioma]["Fechas"]} </p> <p style="color: #7f3213; font-size: 18px;"> 📧 <strong>{evento[idioma]["Correo_label"]}:</strong> {evento[idioma]["Correo"]} </p> <h3 style="color: #7f3213;"> {evento[idioma]["Temas_label"]} </h3> """, unsafe_allow_html=True ) 
    for tema in evento[idioma]["Temas"]: 
        st.markdown( f""" <p style=" color: #7f3213; font-size: 17px; margin-left: 20px; "> • {tema} </p> """, unsafe_allow_html=True )
        
elif opciones == menus[idioma]["Amazonicas"]: 
  st.header(menus[idioma]["Amazonicas"]) 
  st.write("Información sobre Amazonicas.") 

elif opciones == menus[idioma]["Programación"]: 
  st.header(menus[idioma]["Programación"]) 
  st.write("Información sobre Programación") 

elif opciones == menus[idioma]["Organizadores"]: 
  st.header(menus[idioma]["Organizadores"]) 
  st.write("Información sobre Organizadores") 
    
elif opciones == menus[idioma]["Convocatoria"]:
    st.markdown(f"""<h2 style="color:#7f3213; text-align:center; font-size:32px;">{convocatoria[idioma]["Titulo"]}</h2>""",unsafe_allow_html=True)

    st.markdown(f"""<h3 style="color:#7f3213; text-align:center;">{convocatoria[idioma]["Subtitulo"]}</h3>""",unsafe_allow_html=True)

    st.markdown(
        f"""
        <p style="color:#7f3213; text-align:center; font-size:18px;">
            <strong>{convocatoria[idioma]["Organizadores"]}</strong><br>
            {convocatoria[idioma]["Lugar"]}<br>
            {convocatoria[idioma]["Fecha_evento"]}
        </p>
        """,
        unsafe_allow_html=True)

    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria[idioma]["Descripcion"]}</p>""",unsafe_allow_html=True)

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria[idioma]["Envio"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria[idioma]["Limite"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria[idioma]["Idiomas"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria[idioma]["Deadline"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria[idioma]["Aceptacion"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="font-size:18px;">
            <a href="{convocatoria[idioma]["Link"]}"
               target="_blank"
               style="color:#7f3213; font-weight:bold;">
                {convocatoria[idioma]["Link_text"]}
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )
