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
    st.header('¿Quiénes somos?')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("B.Sc Marco Espinoza")
        st.image(".\imagenes\marco.jpeg")
        st.write("Graduado de Estadística de la Universidad de Costa Rica. Con dos años de experiencia laboral en la consultoria en datos.")
    with col2:
        st.subheader("M.Sc Humberto Espinoza")
        st.write("Con más de 30 años de experiencia en el área médica (...)")
    
    
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
    