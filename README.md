markdown
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
2. Add your chat history file (_chat.txt) to the folder

3. Start the bot:

bash
node bot.js
4. Scan QR code with WhatsApp (Settings → Linked Devices → Link a Device)

Features
🤖 Automatically responds to incoming WhatsApp messages
🧠 Uses AI to generate responses based on your chat history
🔒 Runs locally - completely private
📱 Works with WhatsApp Web
How It Works
Bot connects to WhatsApp via whatsapp-web.js
Listens for incoming messages
Sends message + chat history to local Ollama AI
Generates contextual response
Automatically replies
Note: Keep the terminal window open while bot is running. Press Ctrl+C to stop.
