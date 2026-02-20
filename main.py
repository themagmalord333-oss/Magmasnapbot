import time
import random
from neonize.client import NewClient
from neonize.events import MessageEv
from neonize.types import Message

# --- CONFIGURATION & SESSION ---
client = NewClient("magma_wa_session.db")

# --- SPAM MESSAGES (Telegram Wale) ---
SPAM_MESSAGES = [
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘 𝗖𝗛𝗔𝗡𝗚𝗘𝗦 𝗖𝗢𝗠𝗠𝗜𝗧 𝗞𝗥𝗨𝗚𝗔...",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗞𝗢 𝗢𝗡𝗟𝗜𝗡𝗘 𝗢𝗟𝗫 𝗣𝗘 𝗕𝗘𝗖𝗛𝗨𝗡𝗚𝗔...",
    "{target} 𝗧𝗘𝗥𝗜 𝗕𝗔𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗨𝗧 𝗠𝗘𝗜 𝗔𝗣𝗣𝗟𝗘 𝗞𝗔 𝟭𝟴𝗪 𝗪𝗔𝗟𝗔 𝗖𝗛𝗔𝗥𝗚𝗘𝗥...",
    # (Aap baki ki list yahan copy-paste kar sakte hain)
]

# --- ASCII ARTS ---
HACKER_ART = "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁...\n(Full Hacker Art Here)"
YOURMOM_ART = "🤱 *ANYSNAP VS YOUR MOM* 🤱\nTERI MAA MERI LUND PE! 🥵"

@client.common_types(MessageEv)
def on_message(client: NewClient, message: MessageEv):
    text = message.Message.conversation or message.Message.extendedTextMessage.text or ""
    chat_id = message.Info.MessageSource.Chat
    sender_name = message.Info.PushName or "User"

    # .help Command
    if text == ".help":
        help_menu = """
🔥 *MAGMA WA USERBOT* 🔥

🌹 `.rose` - Rose Animation
💻 `.hacker` - System Hack
⚠️ `.error` - System Crash
🖕 `.fuck` - Fuck Art
🤱 `.yourmom` - Mom Roast
🚀 `.anysnap <count>` - Spam
"""
        client.send_message(chat_id, help_menu)

    # .anysnap (Spam)
    elif text.startswith(".anysnap"):
        try:
            count = int(text.split()[1]) if len(text.split()) > 1 else 5
            for _ in range(count):
                msg = random.choice(SPAM_MESSAGES).format(target=sender_name)
                client.send_message(chat_id, msg)
                time.sleep(0.8)
        except: pass

    # Animations & Arts
    elif text == ".rose":
        client.send_message(chat_id, "🌱")
        time.sleep(0.5)
        client.send_message(chat_id, "🌹 *FOR YOU!*")

    elif text == ".hacker":
        client.send_message(chat_id, "💻 *Hacking System...*")
        time.sleep(1)
        client.send_message(chat_id, f"```{HACKER_ART}```\n\n✅ *SYSTEM HACKED!*")

    elif text == ".fuck":
        client.send_message(chat_id, "🖕 *FUCK YOU!*")

    elif text == ".yourmom":
        client.send_message(chat_id, YOURMOM_ART)

# --- OTP LOGIN SYSTEM ---
def start_bot():
    if not client.is_connected:
        print("\n" + "="*40)
        phone = input("📞 WhatsApp Number (e.g. 919876543210): ")
        print("🔄 OTP Code Request kar raha hoon...")
        code = client.request_pairing_code(phone)
        print(f"\n🔥 LOGIN OTP: {code}")
        print("👉 WhatsApp -> Linked Devices -> Link with Phone Number mein dalo.")
        print("="*40 + "\n")

    client.add_event_handler(MessageEv, on_message)
    client.connect()

if __name__ == "__main__":
    start_bot()