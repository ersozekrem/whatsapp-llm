import ollama

print("Loading your WhatsApp chat...\n")

# Read the chat file
with open('_chat.txt', 'r', encoding='utf-8') as f:
    chat_history = f.read()

print(f"✅ Loaded chat (length: {len(chat_history)} characters)\n")

# Function to ask questions about the chat
def ask_question(question):
    print(f"Question: {question}\n")
    print("AI is thinking...\n")
    
    prompt = f"""Here is a WhatsApp conversation:

{chat_history}

Based on this conversation, please answer the following question:
{question}

Answer:"""
    
    response = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    
    return response['message']['content']

# Ask a question
question = "What topics did we discuss in this conversation?"
answer = ask_question(question)

print("Answer:")
print(answer)