from langchain_community.llms import Ollama

# Load Ollama model
llm = Ollama(model="llama3.2")  # You can use "llama2", "gemma", or any installed model

# Generate a response
response = llm.invoke("What is AI?")
print(response)
