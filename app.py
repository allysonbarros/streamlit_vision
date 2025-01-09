import streamlit as st
from streamlit_theme import st_theme
from PIL import Image
from groq import Groq
import base64

# Código principal do aplicativo Streamlit
st.title("Image to Text App")
st.write("This app generates a story based on the description of an image.")

# Solicita a chave da API da OpenAI
st.sidebar.title("Settings")
GROQ_API_KEY = st.sidebar.text_input("Enter your Groq API Key", type="password")

# Adicionando os créditos no rodapé da Sidebar
st.sidebar.markdown("---")
st.sidebar.title("Credits")
theme = st_theme()

if theme and theme.get('base') == "dark":
    logo = Image.open("assets/logo-white.png")
else:
    logo = Image.open("assets/logo.png")

st.sidebar.image(logo, width=200)
st.sidebar.write("Created with ❤️ by Allyson Barros")
st.sidebar.write("Follow me on [LinkedIn](https://www.linkedin.com/in/allysonbarros/) | [GitHub](https://github.com/allysonbarros/)")


# Configura a chave da API da OpenAI globalmente
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

    # Função para codificar a imagem em base64
    def encode_image(image_bytes):
        return base64.b64encode(image_bytes.read()).decode('utf-8')

    # Função para gerar história
    def generate_story(scenario):
        try:

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Gere uma história com base no texto: {scenario}.",
                    }
                ],
                model="llama-3.3-70b-versatile",
            )

            return chat_completion.choices[0].message.content
        except Exception as e:
            st.error(f"Erro ao gerar a história: {e}")
            return ""

    # Permite ao usuário fazer upload de uma imagem
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Codifica a imagem carregada
        base64_image = encode_image(uploaded_file)

        # Solicita a descrição da imagem ao modelo OpenAI Vision
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Descreva o que você vê na imagem."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                },
                            },
                        ],
                    }
                ],
                model="llama-3.2-11b-vision-preview",
            )

            description = chat_completion.choices[0].message.content
            st.text_area("Image Description", description, height=300)
        except Exception as e:
            st.error(f"Error: {e}")

        if st.button("Generate Story"):
            # Gera uma história com base na descrição da imagem
            story = generate_story(description)
            if story:
                st.text_area("Generated Story", story, height=300)  # Mostra a história gerada

                # Gera um arquivo .txt da história
                with open("generated_story.txt", "w") as text_file:
                    text_file.write(story)

                # Botão para baixar o arquivo .txt
                with open("generated_story.txt", "rb") as file:
                    st.download_button(label="Download Story as Text File", data=file, file_name="generated_story.txt")
