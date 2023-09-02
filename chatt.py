import openai
import streamlit as st

# Mettez à jour votre clé API OpenAI ici
openai_api_key = "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"

# Configurez la clé API OpenAI
openai.api_key = openai_api_key

# Définissez le titre de votre application Streamlit
st.title("💬 Chatbot")

# Initialisez la liste des messages si elle n'existe pas déjà
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Comment puis-je vous aider?"}]

# Affichez les messages existants
for msg in st.session_state.messages:
    st.text(f"{msg['role']}: {msg['content']}")

# Ajoutez une entrée pour l'utilisateur
user_input = st.text_input("Votre message:")
if user_input:
    # Ajoutez le message de l'utilisateur à la liste
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Obtenez la réponse du chatbot
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    
    # Récupérez la réponse du chatbot
    bot_message = response.choices[0].message["content"]
    
    # Ajoutez la réponse du chatbot à la liste
    st.session_state.messages.append({"role": "assistant", "content": bot_message})
    
    # Affichez la réponse du chatbot
    st.text(f"Assistant: {bot_message}")
