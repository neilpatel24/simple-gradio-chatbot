# Simple Gradio Chatbot

This repository demonstrates a minimal Gradio-based chatbot that uses the OpenAI API. You can run it locally, dockerize it, and deploy to Hugging Face Spaces.

---

## 1. `app.py`
```python
import os
import gradio as gr
from openai import OpenAI

# Initialize OpenAI client (set your API key in environment)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define chatbot function
def chat_with_gpt(prompt, chat_history=[]):
    # Append user message
    chat_history = chat_history or []
    chat_history.append({"role": "user", "content": prompt})

    # Call OpenAI chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or your chosen model
        messages=chat_history
    )
    ai_message = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": ai_message})
    return ai_message, chat_history

# Build Gradio interface
demo = gr.Chatbot()
with gr.Blocks() as app:
    gr.Markdown("# 🦜🔗 Simple GPT Chatbot")
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type your message...")
        submit = gr.Button("Send")
    submit.click(
        fn=chat_with_gpt,
        inputs=[txt, chatbot],
        outputs=[chatbot, chatbot]
    )

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)
``` 

---

## 2. `requirements.txt`
```
openai
gradio
``` 

---

## 3. `Dockerfile`
```dockerfile
# Use official Python image
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py ./

# Expose port
EXPOSE 7860

# Launch the app
CMD ["python", "app.py"]
``` 

---

## 4. `README.md`
```markdown
# Simple Gradio Chatbot

A minimal chatbot UI powered by OpenAI's GPT models and Gradio.

## Setup

1. Clone the repo:
   ```bash
git clone <your-repo-url>
cd simple_gradio_chatbot
```  
2. Create a `.env` file with your API key:
   ```bash
export OPENAI_API_KEY="your_openai_key"
```  
3. Install dependencies:
   ```bash
pip install -r requirements.txt
```  
4. Run locally:
   ```bash
python app.py
```  

## Docker

Build and run the container:
```bash
docker build -t gradio-chatbot .
docker run -e OPENAI_API_KEY="$OPENAI_API_KEY" -p 7860:7860 gradio-chatbot
```

## Deploy to Hugging Face Spaces

1. Push this repo to a GitHub or directly import into a new Hugging Face Space.
2. Choose "docker" as the runtime; Spaces will build the Dockerfile automatically.
3. Set the `OPENAI_API_KEY` secret in the Space settings.
4. Your chatbot will be live at `https://<your-space-name>.hf.space`.
