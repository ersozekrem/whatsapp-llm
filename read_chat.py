# Read WhatsApp chat file
print("Reading WhatsApp chat...\n")

# Open the chat file
with open('_chat.txt', 'r', encoding='utf-8') as f:
    messages = f.readlines()

# Show how many messages we found
print(f"✅ Found {len(messages)} lines in the chat\n")

# Show the first 10 messages
print("First 10 messages:")
print("-" * 50)
for i, message in enumerate(messages[:10]):
    print(message.strip())

print("-" * 50)
print(f"\nLast 10 messages:")
print("-" * 50)
for message in messages[-10:]:
    print(message.strip())

print("-" * 50)
print("\n✅ Successfully read the chat file!")