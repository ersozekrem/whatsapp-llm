const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const ollama = require('ollama').default;
const fs = require('fs');

console.log('Starting WhatsApp AI Bot...\n');

// Read chat history
let chatHistory = '';
try {
    chatHistory = fs.readFileSync('_chat.txt', 'utf-8');
    console.log('✅ Loaded chat history\n');
} catch (error) {
    console.log('⚠️  No chat history file found. Bot will reply without context.\n');
}

// Initialize WhatsApp client
const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

client.on('qr', (qr) => {
    console.log('📱 Scan this QR code:\n');
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('✅ WhatsApp AI Bot is ready!\n');
});

// AI Response Function
async function generateResponse(messageText, senderName) {
    const prompt = `You are responding to a WhatsApp message. Here is your previous conversation history:

${chatHistory}

Someone named ${senderName} just sent you: "${messageText}"

Based on your conversation history and the message, write a natural, friendly response. Keep it brief and conversational like a WhatsApp message.

Response:`;

    try {
        const response = await ollama.chat({
            model: 'llama3.2',
            messages: [{ role: 'user', content: prompt }],
        });
        
        return response.message.content;
    } catch (error) {
        console.error('Error generating AI response:', error);
        return 'Sorry, I had trouble processing that message.';
    }
}

// Listen for messages
client.on('message', async (message) => {
    console.log(`📩 Message from ${message.from}:`);
    console.log(`   "${message.body}"\n`);
    
    // Don't reply to group chats or yourself
    if (message.from.includes('@g.us') || message.fromMe) {
        return;
    }
    
    console.log('🤖 AI is thinking...');
    
    // Generate AI response
    const aiResponse = await generateResponse(message.body, message.from);
    
    console.log(`💬 AI Response: "${aiResponse}"\n`);
    
    // Send reply
    await message.reply(aiResponse);
    
    console.log('✅ Reply sent!\n---\n');
});

process.on('SIGINT', async () => {
    console.log('\n⏹️  Shutting down...');
    await client.destroy();
    process.exit(0);
});

client.initialize();