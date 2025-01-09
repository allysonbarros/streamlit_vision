# Image to Text App

This Streamlit application generates a story based on the description of an uploaded image using the Groq API.

## Features

- Upload an image (jpg, jpeg, png)
- Generate a description of the image using Groq's Vision model
- Generate a story based on the image description
- Download the generated story as a text file

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/allysonbarros/streamlit_vision.git
    cd streamlit_vision
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your Groq API Key in the sidebar.

4. Upload an image and generate a description.

5. Generate a story based on the description and download it as a text file.

## Credits

Created with ❤️ by Allyson Barros

Follow me on [LinkedIn](https://www.linkedin.com/in/allysonbarros/) | [GitHub](https://github.com/allysonbarros/)