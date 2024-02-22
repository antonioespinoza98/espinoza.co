import streamlit as st

st.set_page_config(page_title= 'Espinoza')

tab1, tab2, tab3, tab4 = st.tabs(['Nuestros servicios','Sobre nosotros','Contáctenos', 'Tecnologías'])

with tab1:
    st.header('Nuestros servicios')
    st.markdown('Nuestro enfoque integral pretende brindar un servicio integral con una fuerte influencia cuantitativa, junto con la tecnología más moderna del mercado.')
    st.markdown('+ Muestreo')
    st.markdown('+ Análisis de series temporales')
    st.markdown('+ Análisis de regresión')
    
with tab2: 
    # Quienes somos
    st.header('¿Quiénes somos?')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("B.Sc Marco Espinoza")
        st.image(".\imagenes\marco.jpeg")
        st.write("Graduado de Estadística de la Universidad de Costa Rica. Con dos años de experiencia laboral en la consultoria en datos.")
    with col2:
        st.subheader("M.Sc Humberto Espinoza")
        st.write("Con más de 30 años de experiencia en el área médica (...)")
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
    st.write('La disciplina es el cimiento sobre el cual construimos nuestro éxito. Nos comprometemos a mantenernos enfocados en nuestras metas y objetivos, incluso cuando los desafíos parezcan insuperables. A través de la disciplina, demostramos nuestra dedicación y determinación para alcanzar la excelencia en todo lo que hacemos.')
    st.subheader('Organización')
    st.write('La organización es la clave para la eficiencia y la efectividad. Nos esforzamos por mantener un entorno de trabajo ordenado y estructurado, donde cada tarea y proceso esté claramente definido y coordinado. Al priorizar la organización, optimizamos nuestro rendimiento y garantizamos resultados consistentes y confiables.')
    st.subheader('Excelencia')
    st.write('La excelencia es nuestro estándar. Buscamos constantemente superar las expectativas y alcanzar la más alta calidad en cada proyecto, producto o servicio que entregamos. Nos negamos a conformarnos con lo ordinario, y en su lugar, aspiramos a la grandeza en todo lo que emprendemos.')
with tab3:

    with st.form('contacto'):
        st.text_input('Su nombre')
        st.text_input('Su correo electrónico')
        
        st.form_submit_button("Enviar")
    
with tab4:
    st.write("Nosotros trabajamos con las tecnologías más modernas del mercado")
    st.markdown("+ Python")
    st.markdown("+ R")
    st.markdown("+ Streamlit")
    st.markdown("+ SPSS")
    with st.container(border = True):
        python, rstudio, stream = st.columns(3)
        with python:
            st.image('.\imagenes\Python.svg.png', width= 100, use_column_width= "never")
        with rstudio:
            st.image('.\imagenes\studio.png', width= 100, use_column_width= "never")
        with stream:
            st.image('.\imagenes\streamlit.png', width= 100, use_column_width= "never")
    