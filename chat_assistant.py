import ollama

print("="*60)
print("WhatsApp Chat Q&A - Powered by Local AI")
print("="*60)

# Read the chat file
with open('_chat.txt', 'r', encoding='utf-8') as f:
    chat_history = f.read()

print(f"\n✅ Loaded chat with Sergazy Abi\n")

# Function to ask questions
def ask_question(question):
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

# Interactive loop
print("You can now ask questions about your chat!")
print("Type 'exit' or 'quit' to stop\n")

while True:
    question = input("Your question: ")
    
    if question.lower() in ['exit', 'quit', 'bye']:
        print("\n👋 Goodbye!")
        break
    
    if question.strip() == "":
        continue
    
    print("\n🤖 AI is thinking...\n")
    answer = ask_question(question)
    print(f"Answer: {answer}\n")
    print("-"*60 + "\n")