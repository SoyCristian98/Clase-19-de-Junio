import streamlit as st
import utils


st.set_page_config(page_title="ChatBot Básico",
                    page_icon="💎",
                    layout="wide")

st.title("ChatBot Básico 166")


#historial / guardar en cache el historial de las entradas de los usuarios

if "history" not in st.session_state: 
    st.session_state.history = []

#Contexto

if "context" not in st.session_state:
    st.session_state.context = []

#Construimos el espacio, emisor-mensaje - ciclo que se repite constantemente

for sender, msg in st.session_state.history:
    if sender == "Tú":
        st.markdown(f'**💡🌪️{sender}:**{msg}')
    else:
        st.markdown(f'**💎{sender}:**{msg}')

#Si no hay entrada
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

#Procesamiento de la entrada
def send_msg():
    user_input = st.session_state.user_input.strip()
    if user_input: 
        tag = utils.predict_class(user_input)
        st.session_state.context.append(tag)
        response = utils.get_response(tag, st.session_state.context)
        st.session_state.history.append(('Tú', user_input))
        st.session_state.history.append(('Bot', response))
        st.session_state.user_input = ""


#Creamos el campo de texto
st.text_input("Escribe tu mensaje:",
                key="user_input",
                on_change=send_msg )



