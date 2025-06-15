import gradio as gr
from transformers import pipeline

# Load a lightweight model (free-tier friendly)
model = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

def chat(message, history):
    response = model(message, max_length=100)[0]['generated_text']
    return response

# Create a ChatGPT-like interface
gr.ChatInterface(chat).launch()
