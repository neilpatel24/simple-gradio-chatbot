import os
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

# Load environment variables from .env (if present)
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define chatbot function
def chat_with_gpt(prompt, chat_history=None):
    chat_history = chat_history or []
    chat_history.append({"role": "user", "content": prompt})

    # Call OpenAI chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )
    ai_message = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": ai_message})
    return ai_message, chat_history

# Build Gradio interface
demo = gr.Chatbot(type='messages')
with gr.Blocks() as app:
    gr.Markdown("# 🦜🔗 Simple GPT Chatbot")
    chatbot = gr.Chatbot(type='messages')
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type your message...")
        submit = gr.Button("Send")
    submit.click(
        fn=chat_with_gpt,
        inputs=[txt, chatbot],
        outputs=[txt, chatbot]
    )

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860, share=True)