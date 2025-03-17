from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms.ollama import Ollama

# Initialize Ollama LLM
llm = Ollama(model="llama3.2")

# Create a conversational memory
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(llm=llm, memory=memory)

# Start chatting
print(conversation.invoke("Who discovered gravity?"))
print(conversation.invoke("And when did that happen?"))
