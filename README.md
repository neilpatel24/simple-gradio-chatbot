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