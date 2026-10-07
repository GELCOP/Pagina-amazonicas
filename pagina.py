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

st.markdown("""
<style>
div.stButton > button {
    color: black !important;
    background-color: white !important;
    border: 1px solid #cccccc;
}

div.stButton > button:hover {
    color: black !important;
    border-color: black;
}
</style>
""", unsafe_allow_html=True)

if "idioma" not in st.session_state:
    st.session_state.idioma = "English"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Español", use_container_width=True):
        st.session_state.idioma = "Español"

with col2:
    if st.button("English", use_container_width=True):
        st.session_state.idioma = "English"

with col3:
    if st.button("Português", use_container_width=True):
        st.session_state.idioma = "Português"


idioma = st.session_state.idioma

menus = { "Español": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programación", "Organizadores": "Organizadores", 
                      "Convocatoria": "Convocatoria de resúmenes", "Cursos": "Cursos", "Información": "Información"}, 
         "English": {"Evento": "Event", "Amazonicas": "Amazonicas", "Programación": "Program", "Organizadores": "Organizers",
                     "Convocatoria": "Call for abstracts", "Cursos": "Courses", "Información": "Information"}, 
         "Português": {"Evento": "Evento", "Amazonicas": "Amazonicas", "Programación": "Programação", "Organizadores": "Organizadores",
                       "Convocatoria": "Chamada para resumos", "Cursos": "Coursos", "Información": "Informações"} }

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
        Envío de resúmenes: Un documento en formato PDF, máximo 1 página excluyendo las referencias,
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

convocatoria_2 = {
    "Español": {
        "Subtitulo": "AMAZONICAS XI – Sesión de Morfosintaxis: Oraciones complejas",
        "Organizadores": "Organizadoras: Luciana Storto (Universidade de São Paulo) y Suzi Lima (University of Toronto y PPGL-UFRR)",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "15 al 18 de junio de 2027",

        "Descripcion": """
        Las <strong>oraciones complejas</strong> pueden definirse de distintas maneras según los
        diferentes marcos lingüísticos, pero todas comparten una estrategia que
        implica el uso de más de un verbo en una oración. Se invita a lingüistas
        que trabajan con lenguas amazónicas a presentar resúmenes que describan,
        analicen o expliquen fenómenos de coordinación, cláusulas relativas,
        adverbiales o de complemento desde una perspectiva sincrónica o diacrónica.
        La coordinación implica dos cláusulas independientes, mientras que las
        cláusulas relativas, adverbiales y de complemento dependen de una cláusula
        independiente. Desde el marco tipológico de la subordinación de Cristofaro
        (2005), esta dependencia debe ser, como mínimo, semántica, mientras que
        en los marcos formales debe ser sintáctica.
        También se invita especialmente a presentar trabajos sobre las metodologías
        utilizadas para identificar, clasificar y describir estos fenómenos.
        """,

        "Coordinacion": """
        Según Haspelmath (2007), las <strong>cláusulas coordinadas</strong> pueden presentar un
        elemento coordinador (coordinación sindética) o no presentarlo
        (coordinación asindética). La coordinación sindética puede clasificarse
        en ocho tipos según el número de elementos coordinadores y su posición
        respecto de las cláusulas. Semánticamente, los elementos coordinadores
        pueden expresar conjunción (y), disyunción (o) o coordinación adversativa
        (pero).
        """,

        "Relativas": """
        Las <strong>cláusulas relativas</strong> suelen funcionar como modificadores de un nombre.
        Entre las estrategias utilizadas para formar relativas se encuentran el
        uso de un relativizador y la nominalización. Camacho y Giménez (2017)
        señalan que 18 de las 30 lenguas indígenas analizadas en su estudio
        utilizaban nominalizaciones.
        Las relativas también pueden clasificarse según la posición del núcleo.
        Las relativas externas al núcleo pueden ser prenominales (Relativa N),
        como en mandarín, o posnominales (N Relativa), como en inglés. Dryer et al.
        (2013) analizaron 824 lenguas y encontraron 579 lenguas con relativas
        posnominales, 141 con relativas prenominales y 24 con relativas internas
        al núcleo.
        Otra clasificación tipológica (Payne 1997) distingue entre una estrategia
        de omisión (gap), en la que el sintagma nominal correferencial con el
        núcleo no se expresa dentro de la relativa, y una estrategia explícita,
        en la que dicho sintagma nominal presenta una realización fonológica.
        """,

        "Adverbiales": """
        Las <strong>cláusulas adverbiales</strong> funcionan como modificadores o adjuntos de
        cláusulas independientes y pueden expresar nociones como tiempo,
        condición, razón, propósito u objetivo.
        """,

        "Complemento": """
        Las <strong>cláusulas de complemento</strong> funcionan como complementos del verbo de la
        cláusula independiente. Los verbos que seleccionan estas cláusulas pueden
        expresar modalidad (obligación, posibilidad, capacidad), fase (comenzar,
        detener, continuar), manipulación (ordenar, persuadir), deseo (querer,
        desear), percepción (oír, ver), conocimiento (saber, percibir), actitud
        proposicional (pensar, creer) y enunciación (decir, hablar).
        """,

        "Envio": """
        Envío de resúmenes: Un documento en formato PDF, de una página como máximo
        sin contar las referencias, con márgenes de 1 pulgada, fuente de 12 puntos
        y espacio sencillo. Incluya un título.
        Las referencias y los ejemplos pueden proporcionarse en una página adicional.
        No incluya los nombres de los autores ni otra información identificativa
        en el resumen.
        """,

        "Limite": "Se permite un resumen de autor único y un resumen en coautoría.",

        "Idiomas": "El resumen y la ponencia pueden ser en español, portugués o inglés.",

        "Deadline": "Fecha límite de envío: 6 de diciembre de 2026",

        "Aceptacion": "Notificación de aceptación: 4 de enero de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Enlace para envío de resúmenes"
    },


    "English": {
        "Subtitulo": "AMAZONICAS XI – Morphosyntax Session: Complex sentences",
        "Organizadores": "Organizers: Luciana Storto (Universidade de São Paulo) & Suzi Lima (University of Toronto and PPGL-UFRR)",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "June 15 to 18, 2027",

        "Descripcion": """
        <strong>Complex sentences</strong> can be defined differently across linguistic frameworks,
        but they all share a strategy involving the use of more than one verb in
        a sentence. Linguists working on Amazonian languages are invited to submit
        abstracts describing, analyzing, or explaining coordination, relative
        clauses, adverbial clauses, or complement clauses from a synchronic or
        diachronic perspective.
        Coordination involves two independent clauses, whereas relative, adverbial,
        and complement clauses depend on an independent clause. In Cristofaro's
        (2005) typological framework of subordination, this dependency must be at
        least semantic, whereas in formal frameworks it must be syntactic.
        Contributions discussing methodologies used to identify, classify, and
        describe these phenomena are also especially encouraged.
        """,

        "Coordinacion": """
        According to Haspelmath (2007), <strong>coordinate clauses</strong> may contain a coordinating
        element (syndetic coordination) or not (asyndetic coordination). Syndetic
        coordination can be divided into eight types depending on the number of
        coordinating elements and their position with respect to each clause.
        Semantically, coordinating elements may express conjunction (and),
        disjunction (or), or adversative coordination (but).
        """,

        "Relativas": """
        <strong>Relative clauses</strong> frequently function as modifiers of nouns. Two strategies
        are commonly used to form relatives: the use of a relativizer and
        nominalization. Camacho & Gimenez (2017) report that 18 of the 30
        Indigenous languages analyzed in their study used nominalizations.
        Relative clauses can also be classified according to the position of the
        head. Head-external relatives may be prenominal (Relative N), as in
        Mandarin, or postnominal (N Relative), as in English. Dryer et al. (2013)
        analyzed 824 languages and found 579 postnominal, 141 prenominal, and
        24 head-internal relative clauses.
        Another typological classification (Payne 1997) distinguishes between a
        gap strategy, in which the noun phrase coreferential with the head is not
        expressed inside the relative clause, and an overt strategy, in which the
        noun phrase is phonologically expressed.
        """,

        "Adverbiales": """
        <strong>Adverbial clauses</strong> function as modifiers or adjuncts of independent clauses
        and may express notions such as time, condition, reason, or purpose/goal.
        """,

        "Complemento": """
        <strong>Complement clauses</strong> function as complements of the verb in the independent
        clause. These verbs may express Modality (obligation, possibility,
        capacity), Phase (start, stop, continue), Manipulation (order, persuade),
        Desideratives (want, desire), Perception (hear, see), Knowledge (know,
        perceive), Propositional Attitude (think, believe), and Enunciation
        (say, speak).
        """,

        "Envio": """
        Abstract submission: One document in PDF format, at most 1 page excluding
        references, with 1-inch margins, 12pt font, and single spacing. Include a
        title.
        References and examples can be provided on an additional page. Do not
        include author names or other identifying information in the abstract.
        """,

        "Limite": "One single-authored and one co-authored abstract are allowed.",

        "Idiomas": "The abstract and the talk can be in Spanish, Portuguese, or English.",

        "Deadline": "Deadline for submission: December 6, 2026",

        "Aceptacion": "Notification of acceptance: January 4, 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Abstract submission link"
    },


    "Português": {
        "Subtitulo": "AMAZONICAS XI – Sessão de Morfossintaxe: Orações complexas",
        "Organizadores": "Organizadoras: Luciana Storto (Universidade de São Paulo) e Suzi Lima (University of Toronto e PPGL-UFRR)",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "15 a 18 de junho de 2027",

        "Descripcion": """
        As <strong>orações complexas</strong> podem ser definidas de diferentes formas nos diversos
        quadros linguísticos, mas todas compartilham uma estratégia que envolve o
        uso de mais de um verbo em uma oração. Convidamos linguistas que trabalham
        com línguas amazônicas a apresentar resumos que descrevam, analisem ou
        expliquem fenômenos de coordenação, orações relativas, adverbiais ou
        completivas, numa perspectiva sincrônica ou diacrônica.
        A coordenação envolve duas orações independentes, enquanto as orações
        relativas, adverbiais e completivas dependem de uma oração independente.
        No quadro tipológico da subordinação de Cristofaro (2005), essa dependência
        deve ser, no mínimo, semântica, enquanto nos quadros formais deve ser
        sintática.
        Trabalhos que discutam as metodologias utilizadas para identificar,
        classificar e descrever esses fenômenos também são especialmente
        incentivados.""",

        "Coordinacion": """
        Segundo Haspelmath (2007), as <strong>orações coordenadas</strong> podem apresentar um
        elemento coordenador (coordenação sindética) ou não (coordenação assindética).
        A coordenação sindética pode ser dividida em oito tipos, dependendo do
        número de elementos coordenadores e de sua posição em relação a cada oração.
        Semanticamente, os elementos coordenadores podem expressar conjunção (e),
        disjunção (ou) ou coordenação adversativa (mas).""",

        "Relativas": """
        As <strong>orações relativas</strong> frequentemente funcionam como modificadores de nomes.
        Duas estratégias são utilizadas com frequência para formar relativas:
        o uso de um relativizador e a nominalização. Camacho e Giménez (2017)
        relatam que 18 das 30 línguas indígenas analisadas em seu estudo utilizavam
        nominalizações.
        As orações relativas também podem ser classificadas de acordo com a posição
        do núcleo. As relativas externas ao núcleo podem ser pré-nominais
        (Relativa N), como no mandarim, ou pós-nominais (N Relativa), como no inglês.
        Dryer et al. (2013) analisaram 824 línguas e encontraram 579 relativas
        pós-nominais, 141 pré-nominais e 24 internas ao núcleo.
        Outra classificação tipológica (Payne 1997) distingue entre uma estratégia
        de omissão (gap), na qual o sintagma nominal correferente ao núcleo não é
        expresso dentro da oração relativa, e uma estratégia explícita, na qual o
        sintagma nominal é realizado fonologicamente.""",

        "Adverbiales": """
        As <strong>orações adverbiais</strong> funcionam como modificadores ou adjuntos de orações
        independentes e podem expressar noções como tempo, condição, razão ou
        propósito/objetivo.""",

        "Complemento": """
        As <strong>orações completivas</strong> funcionam como complementos do verbo na oração
        independente. Esses verbos podem expressar modalidade (obrigação,
        possibilidade, capacidade), fase (começar, parar, continuar), manipulação
        (ordenar, persuadir), desejo (querer, desejar), percepção (ouvir, ver),
        conhecimento (saber, perceber), atitude proposicional (pensar, acreditar)
        e enunciação (dizer, falar).""",

        "Envio": """
        Submissão de resumos: Um documento em formato PDF, com no máximo uma página,
        sem contar as referências, com margens de 1 polegada (2,54 cm), fonte de
        12 pontos e espaçamento simples. Incluir um título.
        As referências e os exemplos podem constar em uma página separada. Não
        incluir os nomes dos autores ou outras informações de identificação no
        resumo.
        """,

        "Limite": "É permitido um resumo de autoria única e um resumo em coautoria.",

        "Idiomas": "O resumo e a apresentação podem ser em espanhol, português ou inglês.",

        "Deadline": "Prazo para submissão: 6 de dezembro de 2026",

        "Aceptacion": "Notificação de aceitação: 4 de janeiro de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Link para submissão de resumos"
    }
}

convocatoria_3 = {
    "Español": {
        "Titulo": "Convocatoria de resúmenes",
        "Subtitulo": "AMAZONICAS XI 2027 – Simposio de Fonología",
        "Organizadores": "Organizadores: Spike Gildea, Uli Reich, Sebastian Drude",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "15 al 18 de junio de 2027",

        "Descripcion": """<div style="color: #7f3213;">
        <strong>Fonología – con especial énfasis en la prosodia y la entonación</strong>
        <p>Invitamos a presentar resúmenes sobre cualquier tema relacionado con la
        fonética y la fonología de las lenguas indígenas de la Amazonía: fenómenos
        segmentales y suprasegmentales, tono, acento y nasalidad, morfofonología y
        las interfaces con la morfología y la sintaxis, variación y cambio,
        fonología histórica y comparativa, tipología, contacto lingüístico, así
        como enfoques experimentales, computacionales o documentales.</p>
        <p>Se aceptan contribuciones de todos los marcos teóricos, desde estudios de
        caso en profundidad de una sola lengua hasta trabajos comparativos entre
        familias y regiones.</p>
        <p>Dentro de este amplio alcance, damos especial bienvenida a las
        contribuciones sobre prosodia, y sobre la entonación en particular,
        entendida en sentido amplio para abarcar no solo las melodías, los
        contornos tonales y de altura, sino también la temporalidad, el ritmo y
        la prominencia.</p>
        <p>Si bien las lenguas amazónicas son bien conocidas por sus ricos sistemas
        de tono y acento a nivel de palabra, el funcionamiento de la melodía y la
        prominencia más allá de la palabra sigue siendo en gran medida
        inexplorado.</p>
        <p>Entre las preguntas que nos gustaría abordar se incluyen:</p>
        <ul>
            <li>¿Cuáles son los hallazgos y los retos más importantes o inusuales en el estudio de la prosodia de las lenguas amazónicas?</li>
            <li>¿Cómo interactúa la entonación con el tono léxico y el acento de altura, y cómo funciona en las lenguas tonales?</li>
            <li>¿Cómo se utiliza la prosodia para marcar tipos de oraciones, la estructura de la información (tema, foco) o categorías como el modo y la evidencialidad?</li>
            <li>¿Cómo utilizan los hablantes los recursos melódicos en la conversación cotidiana y qué sucede con ellos en comunidades multilingües?</li>
            <li>¿Existen patrones regionales o transferencia prosódica entre lenguas?</li>
        </ul>
        <p>Se acogen explícitamente los hallazgos preliminares y los trabajos en curso.
        Durante el simposio se pretende examinar conjuntamente los datos, discutir
        métodos y análisis y, posiblemente, convertir las presentaciones en una
        propuesta para un volumen editado sobre la prosodia de las lenguas
        indígenas amazónicas.</p></div>""",
        
        "Temas": """
        Los trabajos pueden abordar fenómenos segmentales y suprasegmentales,
        tono, acento, nasalidad, morfofonología, interfaces con la morfología y
        la sintaxis, variación y cambio, fonología histórica y comparativa,
        tipología, contacto lingüístico y enfoques experimentales,
        computacionales o documentales.
        """,

        "Prosodia": """
        Se presta especial atención a la prosodia y, particularmente, a la
        entonación, incluyendo melodía, contornos tonales, temporalidad, ritmo
        y prominencia. También se invita a abordar la interacción entre
        entonación, tono léxico y acento de altura, así como el papel de la
        prosodia en los tipos de oración, la estructura informativa, el modo,
        la evidencialidad, la conversación cotidiana y las comunidades
        multilingües.
        """,

        "Envio": """
        Envío de resúmenes: Un documento en formato PDF, de un máximo de 1 página
        sin contar las referencias, con márgenes de 1 pulgada, fuente de 12 puntos
        y a espacio sencillo. Incluya un título.
        Las referencias y los ejemplos pueden proporcionarse en una página adicional.
        No incluya los nombres de los autores ni otra información identificativa
        en el resumen.
        """,

        "Limite": "Se permite un resumen de autor único y otro en coautoría.",

        "Idiomas": "El resumen y la ponencia pueden estar en español, portugués o inglés.",

        "Deadline": "Fecha límite de presentación: 6 de diciembre de 2026",

        "Aceptacion": "Notificación de aceptación: 4 de enero de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Enlace para envío de resúmenes"
    },


    "English": {
        "Titulo": "Call for abstracts",
        "Subtitulo": "AMAZONICAS XI 2027 – Symposium Phonology",
        "Organizadores": "Organizers: Spike Gildea, Uli Reich, Sebastian Drude",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "June 15 to 18, 2027",

        "Descripcion": """<div style="color: #7f3213;">
        <strong>Phonology – with a special focus on Prosody and Intonation</strong>
        <p>We invite abstracts on any topic in the phonetics and phonology of the
        Indigenous languages of Amazonia: segmental and suprasegmental phenomena,
        tone, stress and nasality, morphophonology and the interfaces with
        morphology and syntax, variation and change, historical and comparative
        phonology, typology, language contact, and experimental, computational
        or documentary approaches.</p>
        <p>Contributions from all theoretical frameworks are welcome, from in-depth
        case studies of a single language to comparative work across families
        and regions.</p>
        <p>Within this broad scope, we especially welcome contributions on prosody,
        and intonation in particular, understood broadly to cover not only
        tunes, melody and pitch contours but also timing, rhythm and prominence.
        While Amazonian languages are well known for their rich word-level tone
        and accent systems, how melody and prominence work beyond the word remains
        largely unexplored.</p>
        <p>Questions we would like to address include:</p>
        <ul>
            <li>What are the most important or unusual findings and challenges in
          studying prosody in Amazonian languages?</li>
            <li>How does intonation interact with lexical tone and pitch accent, and
          how does it work in tonal languages?</li>
            <li>How is prosody used to mark sentence types, information structure
          (topic, focus), or categories such as mood and evidentiality?</li>
            <li>How do speakers deploy melodic resources in everyday conversation,
          and what happens to them in multilingual communities?</li>
            <li>Are there areal patterns or prosodic transfer between languages?</li></ul>
        <p>Preliminary findings and work in progress are explicitly welcome. During
        the symposium, we intend to examine each other's data, discuss methods
        and analyses, and possibly develop the presentations into a proposal
        for an edited volume on the prosody of Amazonian Indigenous languages.</p></div>""",

        "Temas": """
        Contributions may address segmental and suprasegmental phenomena, tone,
        stress, nasality, morphophonology, interfaces with morphology and syntax,
        variation and change, historical and comparative phonology, typology,
        language contact, and experimental, computational or documentary
        approaches.
        """,

        "Prosodia": """
        Particular attention is given to prosody and, especially, intonation,
        including melody, pitch contours, timing, rhythm and prominence.
        Contributions may also address the interaction between intonation,
        lexical tone and pitch accent, as well as the role of prosody in sentence
        types, information structure, mood, evidentiality, everyday conversation,
        and multilingual communities.
        """,

        "Envio": """
        Abstract submission: One document in PDF format, at most 1 page excluding
        references, with 1-inch margins, 12pt font, and single spacing. Include
        a title.
        References and examples can be provided in an additional page. Do not
        include author names or other identifying information in the abstract.
        """,

        "Limite": "One single-authored and one co-authored abstract are allowed.",

        "Idiomas": "The abstract and the talk can be in Spanish, Portuguese, or English.",

        "Deadline": "Deadline for submission: December 6, 2026",

        "Aceptacion": "Notification of acceptance: January 4, 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Abstract submission link"
    },


    "Português": {
        "Titulo": "Chamada para submissão de resumos",
        "Subtitulo": "AMAZONICAS XI 2027 – Simpósio de Fonologia",
        "Organizadores": "Organizadores: Spike Gildea, Uli Reich, Sebastian Drude",
        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Peru",
        "Fecha_evento": "15 a 18 de junho de 2027",

        "Descripcion": """<div style="color: #7f3213;">
        <strong>Fonologia – com ênfase especial em prosódia e entonação</strong>
        <p>Convidamos o envio de resumos sobre qualquer tema relacionado à fonética
        e à fonologia das línguas indígenas da Amazônia: fenômenos segmentais e
        suprassegmentais, tom, acento e nasalidade, morfofonologia e as interfaces
        com a morfologia e a sintaxe, variação e mudança, fonologia histórica e
        comparativa, tipologia, contato linguístico e abordagens experimentais,
        computacionais ou documentais.</p>
        <p>São bem-vindas contribuições de todos os marcos teóricos, desde estudos
        de caso aprofundados de uma única língua até trabalhos comparativos entre
        famílias e regiões.</p>
        <p>Dentro desse amplo escopo, acolhemos especialmente contribuições sobre
        prosódia e, em particular, entonação, entendidas de forma ampla para
        abranger não apenas melodias e contornos de tom, mas também temporização,
        ritmo e proeminência.</p>
        <p>Embora as línguas amazônicas sejam bem conhecidas por seus ricos sistemas
        de tom e acento no nível da palavra, a forma como a melodia e a
        proeminência funcionam além da palavra permanece amplamente inexplorada.</p>
        <p>As questões que gostaríamos de abordar incluem:</p>
        <ul>
            <il>Quais são as descobertas e os desafios mais importantes ou incomuns
          no estudo da prosódia nas línguas amazônicas?</il>
            <il>Como a entonação interage com o tom lexical e o acento de altura, e
          como ela funciona em línguas tonais?</il>
            <il>Como a prosódia é utilizada para marcar tipos de frases, estrutura
          informacional (tópico, foco) ou categorias como modo e evidencialidade?</il>
            <il>Como os falantes utilizam recursos melódicos na conversa cotidiana e
          o que ocorre com eles em comunidades multilíngues?</il>
            <il>Existem padrões regionais ou transferência prosódica entre as línguas?</il>
        <p>Resultados preliminares e trabalhos em andamento são explicitamente
        bem-vindos. Durante o simpósio, pretendemos examinar conjuntamente os
        dados, discutir métodos e análises e, possivelmente, desenvolver as
        apresentações em uma proposta para um volume coletivo sobre a prosódia
        das línguas indígenas amazônicas.</p></div>""",

        "Temas": """
        As contribuições podem abordar fenômenos segmentais e suprassegmentais,
        tom, acento, nasalidade, morfofonologia, interfaces com a morfologia e
        a sintaxe, variação e mudança, fonologia histórica e comparativa,
        tipologia, contato linguístico e abordagens experimentais,
        computacionais ou documentais.
        """,

        "Prosodia": """
        É dada especial atenção à prosódia e, particularmente, à entonação,
        incluindo melodia, contornos de tom, temporização, ritmo e proeminência.
        Também são bem-vindos trabalhos sobre a interação entre entonação,
        tom lexical e acento de altura, bem como sobre o papel da prosódia nos
        tipos de frases, estrutura informacional, modo, evidencialidade,
        conversação cotidiana e comunidades multilíngues.
        """,

        "Envio": """
        Envio de resumos: Um documento em formato PDF, com no máximo 1 página,
        excluindo as referências, com margens de 1 polegada, fonte 12pt e
        espaçamento simples. Inclua um título.
        Referências e exemplos podem ser fornecidos em uma página adicional.
        Não inclua nomes de autores ou outras informações de identificação
        no resumo.
        """,

        "Limite": "São permitidos um resumo de autoria única e um de autoria conjunta.",

        "Idiomas": "O resumo e a palestra podem ser em espanhol, português ou inglês.",

        "Deadline": "Prazo para envio: 6 de dezembro de 2026",

        "Aceptacion": "Notificação de aceitação: 4 de janeiro de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Link para envio de resumos"
    }
}

convocatoria_4 = {

    "Español": {
        "Subtitulo": "AMAZONICAS XI – Simposio de Lengua y Sociedad",

        "Organizadores": """
        <strong>Organizadores:</strong>
        Bernat Bardagil, Héloïse Calame, Carla Daniele Costa,
        Ana Vilacy Galúcio, Alba Hermida Rodríguez
        """,

        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Perú",

        "Fecha_evento": "15 al 18 de junio de 2027",

        "Descripcion": """
        <div style="color: #7f3213;">
        <strong>Lengua y Sociedad: Revitalización lingüística en contextos de alta obsolescencia</strong>
        <p>Las sociedades indígenas con un alto grado de obsolescencia lingüística
        son una realidad frecuente en la región de la Gran Amazonia, caracterizada
        por una enorme diversidad de situaciones y contextos de desplazamiento
        lingüístico, y también de iniciativas para abordar esas situaciones.
        Este simposio Amazónicas plantea una plataforma para que activistas e
        investigadores que trabajan específicamente en revitalización lingüística
        en contextos de alta obsolescencia puedan compartir experiencias y debatir
        perspectivas tanto teóricas como aplicadas.</p>
        <strong>¿Qué son los contextos de alta obsolescencia?</strong>
        <ul>
            <li><strong>Reducción del número de hablantes y dominios de uso:</strong>
            tendencia decreciente sostenida, no solo un número bajo estable.</li>
            <li><strong>Interrupción de la transmisión generacional (L1):</strong>
            predominan semi-hablantes o recordadores con un perfil demográfico envejecido.</li>
            <li><strong>Cambios estructurales internos:</strong>
            pérdidas de categorías gramaticales, convergencia con la lengua dominante,
            pérdida de vocabulario especializado, mayor variabilidad e inconsistencias.</li></ul>
        <strong>Los siguientes temas son de especial interés:</strong>
        <ul>
            <li>Las causas sociohistóricas del desplazamiento (violento o silencioso)
            y su efecto en la vitalidad lingüística.</li>
            <li>El concepto de hablante y su papel en la revitalización: tipologías
            (neohablantes, semi-hablantes, hablantes pasivos, recordadores),
            legitimidad/autoridad lingüística y tensiones entre grupos.</li>
            <li>Metodologías de trabajo con semi-hablantes y recordadores:
            reactivación y competencia latente, ética de investigación con
            hablantes vulnerables, revitalización de corpus.</li>
            <li>Variación lingüística y aspectos etnográficos: el papel de la
            etnografía en revitalización, el dilema entre homogeneización y la
            variación lingüística (registros situacionales, dialectales,
            generacionales), y/o criterios de priorización ante una u otra variabilidad.</li>
            <li>El impacto de la revitalización en el ámbito escolar y entre adultos:
            evaluación de resultados intra e intergrupales como programas de
            aprendices-maestros.</li>
            <li>Estrategias para ampliar los contextos de uso: competencia
            comunicativa real versus simbólica/identitaria, nuevos dominios digitales.</li>
            <li>Actitudes lingüísticas, evitación lingüística y disociación:
            desarrollar la ideología lingüística como marco teórico y determinar
            de qué manera condicionan la revitalización.</li>
            <li>Aspectos psicolingüísticos: lenguas de herencia, lengua-espíritu
            y transmisión epigenética/cultural como punto de partida de la
            revitalización lingüística.</li></ul></div>""",

        "Envio": """
        <div style="color: #7f3213;">

        <p><strong>Entrega de resúmenes:</strong></p>

        <p>Un documento en formato PDF, máximo 1 página excluyendo fuentes,
        márgenes de 1 pulgada, fuente de 12 puntos y espacio sencillo.
        Incluya título. Las referencias y ejemplos pueden ser entregados
        en una página separada.</p>

        <p>No incluya nombres o apellidos de autores ni otra información
        que identifique a los autores.</p>

        <p>Se pueden enviar máximo dos resúmenes, de los cuales solamente
        uno como autor único.</p>

        <p>El resumen y la ponencia pueden ser en español, portugués o inglés.</p>

        </div>
        """,

        "Limite": "Máximo dos resúmenes: uno como autor único y otro en coautoría.",

        "Idiomas": "El resumen y la ponencia pueden ser en español, portugués o inglés.",

        "Deadline": "Fecha límite de entrega: 6 de diciembre de 2026",

        "Aceptacion": "Notificación de aceptación: 4 de enero de 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Enlace para envío de resúmenes"
    },


    "English": {
        "Subtitulo": "AMAZONICAS XI – Language and Society Symposium",

        "Organizadores": """
        <strong>Organizers:</strong>
        Bernat Bardagil, Héloïse Calame, Carla Daniele Costa,
        Ana Vilacy Galúcio, Alba Hermida Rodríguez
        """,

        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Perú",

        "Fecha_evento": "June 15 to 18, 2027",

        "Descripcion": """<div style="color: #7f3213;">
        <strong>Language and Society: Language revitalization in high obsolescence contexts</strong>
        <p>Indigenous societies experiencing a high degree of language obsolescence
        are a frequent reality across the Greater Amazon region, which is
        characterised by an enormous diversity of situations and contexts of
        language shift, as well as by a wide range of initiatives aimed at
        addressing them. This Amazónicas symposium provides a platform for
        activists and researchers working specifically on language revitalisation
        in contexts of advanced language obsolescence to share experiences and
        discuss both theoretical and applied perspectives.</p>
        <strong>What are contexts of advanced language obsolescence?</strong>
        <ul>
            <li><strong>A reduction in the number of speakers and domains of use:</strong>
            a sustained downward trend, rather than simply a small but stable number
            of speakers.</li>
            <li><strong>An interruption of intergenerational transmission (L1):</strong>
            semi-speakers and rememberers predominate, with an ageing demographic profile.</li>
            <li><strong>Internal structural changes:</strong>
            loss of grammatical categories, convergence with the dominant language,
            loss of specialised vocabulary, and increasing variability and inconsistency.</li></ul>
        <strong>The following topics are of particular interest:</strong>
        <ul>
            <li>The sociohistorical causes of language shift (whether violent or
            more gradual/silent) and their effects on linguistic vitality.</li>
            <li>The concept of the speaker and its role in revitalisation:
            speaker typologies (new speakers, semi-speakers, passive speakers,
            rememberers), linguistic legitimacy and authority, and tensions
            between different speaker groups.</li>
            <li>Methodologies for working with semi-speakers and rememberers:
            reactivation and latent competence, research ethics when working
            with vulnerable speakers, and corpus revitalisation.</li>
            <li>Linguistic variation and ethnographic dimensions: the role of
            ethnography in revitalisation; the tension between homogenisation
            and linguistic variation (situational, dialectal, and generational
            registers); and/or criteria for prioritising one type of variation
            over another.</li>
            <li>The impact of revitalisation in educational settings and among
            adults: the evaluation of intra- and intergroup outcomes, including
            programmes based on learner–teacher models.</li>
            <li>Strategies for expanding contexts of use: genuine communicative
            competence versus symbolic/identity-based use, and the development
            of new digital domains.</li>
            <li>Language attitudes, language avoidance, and dissociation:
            developing language ideology as a theoretical framework and examining
            how these factors shape and constrain revitalisation efforts.</li>
            <li>Psycholinguistic dimensions: heritage languages, language as spirit
            or ancestral voice, and epigenetic/cultural transmission as potential
            starting points for language revitalisation.</li></ul></div>""",

        "Envio": """
        <div style="color: #7f3213;">

        <p><strong>Abstract submission:</strong></p>

        <p>One document in PDF format, at most 1 page excluding references,
        1-inch margins, 12pt font, and single-spaced. Include a title.
        References and examples can be provided on an additional page.</p>

        <p>Do not include author names or other identifying information
        in the abstract.</p>

        <p>One single-authored and one co-authored abstract are allowed.</p>

        <p>The abstract and the talk can be in Spanish, Portuguese, or English.</p>

        </div>
        """,

        "Limite": "One single-authored and one co-authored abstract are allowed.",

        "Idiomas": "The abstract and the talk can be in Spanish, Portuguese, or English.",

        "Deadline": "Deadline for submission: December 6, 2026",

        "Aceptacion": "Notification of acceptance: January 4, 2027",

        "Link": "https://app.oxfordabstracts.com/stages/83705/submitter",

        "Link_text": "Abstract submission link"
    },


    "Português": {
        "Subtitulo": "AMAZONICAS XI – Simpósio de Língua e Sociedade",

        "Organizadores": """
        <strong>Organizadores:</strong>
        Bernat Bardagil, Héloïse Calame, Carla Daniele Costa,
        Ana Vilacy Galúcio, Alba Hermida Rodríguez
        """,

        "Lugar": "Pontificia Universidad Católica del Perú, Lima, Perú",

        "Fecha_evento": "15 a 18 de junho de 2027",

        "Descripcion": """<div style="color: #7f3213;">
        <strong>Língua e Sociedade: Revitalização linguística em contextos de alta obsolescência</strong>
        <p>As sociedades indígenas que vivenciam um alto grau de deslocamento
        linguístico constituem uma realidade amplamente disseminada na Grande
        Amazônia. Essas sociedades apresentam uma enorme diversidade de situações
        e contextos de obsolescência linguística, bem como de iniciativas
        destinadas a enfrentar e reverter esses processos. Este simpósio do
        colóquio Amazônicas pretende constituir um espaço de diálogo entre
        ativistas e pesquisadores que atuam na área de revitalização linguística,
        com especial atenção aos contextos de alta obsolescência. O objetivo é
        promover o compartilhamento de experiências e a discussão de perspectivas
        teóricas e aplicadas relacionadas à revitalização de línguas indígenas.</p>
        <strong>O que são contextos de alta obsolescência?</strong>
        <ul>
            <li><strong>Redução do número de falantes e dos domínios de uso:</strong>
            há tendência ao decréscimo contínuo, não apenas a um número baixo e estável.</li>
            <li><strong>Interrupção da transmissão intergeracional (L1):</strong>
            predominância de semi-falantes ou pessoas que retêm memórias da língua
            (<em>rememberers</em>), com concentração desses perfis entre as gerações mais velhas.</li>
            <li><strong>Mudanças estruturais na língua:</strong>
            perda de categorias gramaticais, convergência com a língua dominante,
            perda de vocabulário especializado, maior variabilidade e inconsistência.</li></ul>
        <strong>Os seguintes temas são de especial interesse:</strong>
        <ul>
            <li>As causas sócio-históricas do deslocamento (violento ou silencioso)
            e seu efeito na vitalidade linguística.</li>
            <li>O conceito de falante e seu papel na revitalização: tipologias
            (neofalantes, semi-falantes, falantes passivos, pessoas que retêm
            memórias da língua), legitimidade/autoridade linguística e tensões
            entre grupos.</li>
            <li>Metodologias de trabalho junto a semi-falantes e pessoas que
            retêm memórias da língua: reativação linguística e desenvolvimento
            da competência latente, ética de pesquisa com falantes em situação
            de vulnerabilidade, e revitalização de <em>corpora</em> linguísticos.</li>
            <li>Variação linguística e aspectos etnográficos: o papel da
            etnografia nos processos de revitalização, o dilema entre
            homogeneização e preservação da variação linguística (situacional,
            dialetal e geracional), e os critérios de priorização diante de
            diferentes tipos de variabilidade.</li>
            <li>O impacto da revitalização no âmbito escolar e entre adultos:
            avaliação de resultados intra e intergrupais, como em programas
            de mestre-aprendiz.</li>
            <li>Estratégias para ampliar os contextos de uso: competência
            comunicativa efetiva <em>versus</em> usos simbólicos e identitários,
            criação de novos domínios de uso dentro e fora das comunidades,
            incluindo domínios digitais.</li>
            <li>Atitudes linguísticas, evitação linguística e dissociação:
            o desenvolvimento das ideologias linguísticas como referencial
            teórico e a maneira como elas condicionam a revitalização.</li>
            <li>Aspectos psicolinguísticos: línguas de herança, língua-espírito
            e transmissão epigenética/cultural como ponto de partida para a
            revitalização linguística.</li></ul></div>""",

        "Envio": """
        <div style="color: #7f3213;">

        <p><strong>Submissão de resumos:</strong></p>

        <p>O resumo deve ser submetido em formato PDF, com no máximo uma página,
        sem incluir as referências. O documento deve apresentar margens de
        1 polegada (2,54 cm), fonte tamanho 12 e espaçamento simples.</p>

        <p>O título deve ser incluído no documento. As referências e exemplos
        podem constar em uma página separada.</p>

        <p>Não incluir os nomes dos autores ou outras informações de identificação
        no resumo.</p>

        <p>Cada participante poderá submeter um resumo de autoria única e um
        resumo em coautoria.</p>

        <p>O resumo e a apresentação podem ser em espanhol, português ou inglês.</p>

        </div>
        """,

        "Limite": "Um resumo de autoria única e um resumo em coautoria.",

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
    st.markdown(f"""<h2 style="color:#7f3213; text-align:center; font-size:32px;">{convocatoria_3[idioma]["Titulo"]}</h2>""",unsafe_allow_html=True)

    st.markdown(f"""<h3 style="color:#7f3213; text-align:center;">{convocatoria_3[idioma]["Subtitulo"]}</h3>""",unsafe_allow_html=True)

    st.markdown(
        f"""
        <p style="color:#7f3213; text-align:center; font-size:18px;">
            <strong>{convocatoria_3[idioma]["Organizadores"]}</strong><br>
            {convocatoria_3[idioma]["Lugar"]}<br>
            {convocatoria_3[idioma]["Fecha_evento"]}
        </p>
        """,
        unsafe_allow_html=True)

    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_3[idioma]["Descripcion"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_3[idioma]["Temas"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_3[idioma]["Prosodia"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_3[idioma]["Envio"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria_3[idioma]["Limite"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria_3[idioma]["Idiomas"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_3[idioma]["Deadline"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_3[idioma]["Aceptacion"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="font-size:18px;">
            <a href="{convocatoria_3[idioma]["Link"]}"
               target="_blank"
               style="color:#7f3213; font-weight:bold;">
                {convocatoria_3[idioma]["Link_text"]}
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(f"""<h3 style="color:#7f3213; text-align:center;">{convocatoria_2[idioma]["Subtitulo"]}</h3>""",unsafe_allow_html=True)

    st.markdown(
        f"""
        <p style="color:#7f3213; text-align:center; font-size:18px;">
            <strong>{convocatoria_2[idioma]["Organizadores"]}</strong><br>
            {convocatoria_2[idioma]["Lugar"]}<br>
            {convocatoria_2[idioma]["Fecha_evento"]}
        </p>
        """,
        unsafe_allow_html=True)

    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_2[idioma]["Descripcion"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_2[idioma]["Coordinacion"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_2[idioma]["Relativas"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_2[idioma]["Adverbiales"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_2[idioma]["Complemento"]}</p>""",unsafe_allow_html=True)
    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_2[idioma]["Envio"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria_2[idioma]["Limite"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria_2[idioma]["Idiomas"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_2[idioma]["Deadline"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_2[idioma]["Aceptacion"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="font-size:18px;">
            <a href="{convocatoria_2[idioma]["Link"]}"
               target="_blank"
               style="color:#7f3213; font-weight:bold;">
                {convocatoria_2[idioma]["Link_text"]}
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(f"""<h3 style="color:#7f3213; text-align:center;">{convocatoria_4[idioma]["Subtitulo"]}</h3>""",unsafe_allow_html=True)

    st.markdown(
        f"""
        <p style="color:#7f3213; text-align:center; font-size:18px;">
            <strong>{convocatoria_4[idioma]["Organizadores"]}</strong><br>
            {convocatoria_4[idioma]["Lugar"]}<br>
            {convocatoria_4[idioma]["Fecha_evento"]}
        </p>
        """,
        unsafe_allow_html=True)

    st.markdown(f"""<p style="color: #7f3213;font-size: 18px;">{convocatoria_4[idioma]["Descripcion"]}</p>""",unsafe_allow_html=True)
    
    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_4[idioma]["Envio"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria_4[idioma]["Limite"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            {convocatoria_4[idioma]["Idiomas"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_4[idioma]["Deadline"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#7f3213; font-size:18px;">
            <strong>{convocatoria_4[idioma]["Aceptacion"]}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="font-size:18px;">
            <a href="{convocatoria_4[idioma]["Link"]}"
               target="_blank"
               style="color:#7f3213; font-weight:bold;">
                {convocatoria_4[idioma]["Link_text"]}
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()

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
