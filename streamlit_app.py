import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title= 'DataEx',
                   page_icon= ':globe_with_meridians:')

tab1, tab2, tab3 = st.tabs(['Nuestros servicios','Sobre nosotros','Contáctenos'])

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="clientes", usecols = [0,1,2,3])
df = df.dropna(how="all")

with tab1:
    st.title('DataEx')
    st.write('***Transformamos datos en descubrimientos***')
    st.header('Nuestros servicios')
    st.image(".\imagenes\page1.jpg")
    st.caption("Photo by Clay Banks on Unsplash")
    st.write('Nuestro enfoque integral pretende brindar un servicio integral con una fuerte influencia cuantitativa, junto con la tecnología más moderna del mercado.')
    # SERVICIOS 
    with st.container(border= True):
        st.header('Diseño Muestral')
    with st.container(border= True):
        st.header('Metodología')
    with st.container(border= True):
        st.header('Análisis de datos')
    
with tab2: 
    # Quienes somos
    st.header('Nuestro equipo')
    with st.container(border= True):
        st.subheader("Marco Espinoza")
        st.image(".\imagenes\marco.jpeg")
        st.write("Estadístico con dos años de experiencia laboral en el mundo de la consultoría en análisis de datos. Apasionado por la investigación y durante sus ratos libres por el montañismo.")

    # Misión
    st.header('Misión')
    st.write('Nuestro propósito es ser un agente mediador entre la estadística y el o la investigadora para traer una armonía metodológica y que a su vez, sea comunicada de la mejor manera.')
    # Visión
    st.header('Visión')
    st.write('Consolidarnos como la mejor consultora en investigaciones en múltiples disciplinas.')
    # Valores
    st.header('Valores')
    st.write('Como empresa familiar, nuestros valores significan lo que nos ha caracterizado por generaciones. Estos valores no solo definen quiénes somos como empresa, sino que también informan nuestras acciones y decisiones en cada interacción con nuestros clientes, socios y colegas. Con disciplina, organización y excelencia como pilares fundamentales, estamos comprometidos a alcanzar nuevas alturas de éxito y hacer una diferencia significativa en el mundo que nos rodea.')
    st.subheader('Disciplina')
    st.write('La disciplina es el cimiento sobre el cual construimos nuestro éxito. Con la que demostramos nuestra dedicación y determinación para alcanzar la excelencia en todo lo que hacemos.')
    st.subheader('Organización')
    st.write('Nos esforzamos por mantener un entorno de trabajo ordenado y estructurado, donde cada tarea y proceso esté claramente definido y coordinado. Al priorizar la organización, optimizamos nuestro rendimiento y garantizamos resultados consistentes y confiables.')
    st.subheader('Excelencia')
    st.write('Buscamos constantemente superar las expectativas y alcanzar la más alta calidad en cada proyecto que entregamos y siempre aspiramos a la grandeza en todo lo que emprendemos.')

with tab3:
    with st.container(border= True):
        st.header('Formulario de contacto')
        st.write('Póngase en contacto con nosotros a través de nuestro formulario y a la brevedad le responderemos:')
        
        with st.form('contacto'):
            name = st.text_input('Nombre')
            email = st.text_input('Correo electrónico')
            subject = st.text_input('Asunto')
            message = st.text_input('Mensaje')
            submit_bottom = st.form_submit_button("Enviar")

        if submit_bottom:
            new_df = pd.DataFrame([
                {
                    "nombre": name,
                    "correo": email,
                    "asunto": subject,
                    "mensaje": message
                    }]
                                    )
            updated_df = pd.concat([df, new_df], ignore_index= True)
            conn.update(worksheet= "clientes", data=updated_df)
            st.cache_data.clear()
            st.success("¡Pronto nos pondremos en contacto!")
                

    with st.container(border= True):
        st.header('Redes Sociales')
        st.page_link('https://www.linkedin.com/in/marco-espinoza-5365a1176/', label= 'LinkedIn', icon= '🔗')
    
# with tab4:
#     st.write("Nosotros trabajamos con las tecnologías más modernas del mercado")
#     st.write("+ Python")
#     st.write("+ R")
#     st.write("+ Streamlit")
#     with st.container(border = True):
#         python, rstudio, stream = st.columns(3)
#         with python:
#             st.image('.\imagenes\Python.svg.png', width= 100, use_column_width= "never")
#         with rstudio:
#             st.image('.\imagenes\studio.png', width= 100, use_column_width= "never")
#         with stream:
#             st.image('.\imagenes\streamlit.png', width= 100, use_column_width= "never")
    