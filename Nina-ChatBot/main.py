import gradio as gr
from langchain_community.llms import Ollama
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools import Tool
import requests

# Load Ollama LLM
llm = Ollama(model="llama3.2")

# Function to handle user input
def chatbot_response(user_input):
    response = llm.invoke(user_input)
    return response

# Create Gradio UI
interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs="text",
    title="AI Chatbot with Ollama & LangChain",
    description="Ask me questions or get the latest Bitcoin price!"
)

# Run the app
interface.launch(share=True)
