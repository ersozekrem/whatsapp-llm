import ollama

# Test if Ollama is working
print("Testing Ollama connection...")

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'Say hello in one sentence!'
        }
    ]
)

print("\nAI Response:")
print(response['message']['content'])
print("\n✅ Success! Ollama is working.")