markdown
# WhatsApp Chat AI Assistant

Ask questions about your WhatsApp chat history using a local AI model. Everything runs on your computer - completely private and offline!

## 🚀 Features

- Chat with AI about your WhatsApp conversation history
- 100% local and private - no data leaves your computer
- Uses Ollama with Llama 3.2 model
- Interactive Q&A interface
- Works completely offline

## 📋 Requirements

- Windows 11 (or Windows 10)
- Python 3.11+
- Ollama
- At least 4GB free RAM

## 🛠️ Installation

### 1. Install Ollama
Download and install from: https://ollama.ai/download

### 2. Download AI Model
ollama pull llama3.2

text

### 3. Install Python Package
pip install ollama

text

## 📱 How to Use

### 1. Export Your WhatsApp Chat
- Open WhatsApp on your phone
- Select a chat
- Tap the contact/group name → Export Chat → Without Media
- Transfer the `_chat.txt` file to your computer

### 2. Run the Assistant
python chat_assistant.py

text

### 3. Ask Questions!
Example questions:
- "What topics did we discuss?"
- "When did we talk about [topic]?"
- "Summarize this conversation"
- "What contact information was shared?"

Type `exit` to quit.

## 📁 Project Files

- `test_ollama.py` - Test Ollama connection
- `read_chat.py` - Read and display WhatsApp chat
- `chat_qa.py` - Basic Q&A with predefined question
- `chat_assistant.py` - Interactive chat assistant (main script)

## 🔒 Privacy

Your WhatsApp chat data stays on YOUR computer. The AI model runs locally through Ollama. No data is sent to the internet.

**Note:** Never commit your actual chat files (`_chat.txt`) to GitHub!

## ⚙️ How It Works

1. Reads your exported WhatsApp chat file
2. Sends the chat history + your question to the local Ollama AI
3. AI analyzes the conversation and provides answers
4. Everything happens on your machine

## 🤝 Contributing

Feel free to fork and improve this project!

## 📄 License

MIT License - feel free to use and modify!

---

Built with ❤️ using Python, Ollama, and Llama 3.2
