---

## 🤖 WhatsApp Auto-Responder Bot

Automatically reply to WhatsApp messages using AI based on your conversation history!

### Located in: `whatsapp-bot/`

### Requirements
- Node.js 18+
- Ollama running locally
- WhatsApp account

### Setup

**1. Install dependencies:**
```bash
cd whatsapp-bot
npm install
```
**2. Add your chat history file (_chat.txt) to the folder**

**3. Start the bot:**
```
bash
node bot.js
```

**4. Scan QR code with WhatsApp (Settings → Linked Devices → Link a Device)**

### Features
- 🤖 Automatically responds to incoming WhatsApp messages
- 🧠 Uses AI to generate responses based on your chat history
- 🔒 Runs locally - completely private
- 📱 Works with WhatsApp Web

### How It Works
1. Bot connects to WhatsApp via whatsapp-web.js
2. Listens for incoming messages
3. Sends message + chat history to local Ollama AI
4. Generates contextual response
5. Automatically replies

**Note:** Keep the terminal window open while bot is running. Press `Ctrl+C` to stop.

### Privacy & Security
- All data stays on YOUR computer
- No information is sent to external servers
- Chat histories are never uploaded to GitHub (protected by .gitignore)
- The AI model runs 100% locally via Ollama

**Built with ❤️ using Python, Node.js, Ollama, and Llama 3.2**
