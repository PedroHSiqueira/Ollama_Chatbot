from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Responda a pergunta abaixo, em português:

aqui é o histórico de mensagens: {context}

Pergunta: {question}

Resposta: 
"""

# Expecifica o modelo de linguagem a ser utilizado
model = OllamaLLM(model="llama3")

#define o template da mensagem
prompt = ChatPromptTemplate.from_template(template)

#ligar prompt ao modelo
chain = prompt | model

#função para enviar a mensagem
def handle_conversation():
    context = ""
    print("Olá! seja bem-vindo, eu me chamo Len, e sou uma IA Chatbot!, escreva 'sair' para encerrar a conversa.")
    while True:
        question = input("Você: ")

        # Verifica se o usuário deseja sair
        if question.lower() == "sair":
            print("Len: Até mais!")
            break

        # Passa ao modelo de linguagem um prompt
        result = chain.invoke({"context": context, "question": question})
        print(f"Len: {result}")

        # Atualiza o contexto
        context += f"Você: {question}\nLen: {result}\n"

# Executa o Chatbot(Script)
if __name__ == "__main__":
    handle_conversation()