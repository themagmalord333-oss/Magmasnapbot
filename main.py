import os
import time
import random
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from neonize.client import NewClient
from neonize.events import MessageEv

# --- 🌐 RENDER KEEP ALIVE ---
app = Flask('')
@app.route('/')
def home(): return "ANYSNAP ULTIMATE IS ONLINE! 🚀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- ⚙️ CONFIGURATION ---
API_ID = 37314366
API_HASH = "bd4c934697e7e91942ac911a5a287b46"
BOT_TOKEN = "8485202414:AAEEYv7_UjUR2DI4KN9l4bEKnsD9v0WGn7E"

tg_bot = Client("MagmaManager", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
wa_client = NewClient("magma_wa.db")

# --- 🔥 FULL SPAM LIST RESTORED ---
SPAM_MESSAGES = [
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘 𝗖𝗛𝗔𝗡𝗚𝗘𝗦 𝗖𝗢𝗠𝗠𝗜𝗧 𝗞𝗥𝗨𝗚𝗔 🤖🙏🤔",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗞𝗢 𝗢𝗡𝗟𝗜𝗡𝗘 𝗢𝗟𝗫 𝗣𝗘 𝗕𝗘𝗖𝗛𝗨𝗡𝗚𝗔 😎🤩😝😍",
    "{target} 𝗧𝗘𝗥𝗜 𝗕𝗔𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗨𝗧 𝗠𝗘𝗜 𝗔𝗣𝗣🇱🇪 𝗞𝗔 𝟭𝟴𝗪 𝗪𝗔𝗟𝗔 𝗖𝗛𝗔𝗥𝗚𝗘𝗥 🔥🤩",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘🇮 𝗕𝗔𝗧𝗧𝗘𝗥𝗬 𝗟𝗔𝗚𝗔 𝗞𝗘 𝗣𝗢𝗪𝗘𝗥𝗕𝗔𝗡𝗞 𝗕𝗔𝗡𝗔 𝗗𝗨𝗡𝗚𝗔 🔋",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗘 𝗕𝗛𝗢𝗦𝗗𝗘 𝗠𝗘𝗜 𝗦𝗣𝗢𝗧𝗜𝗙𝗬 𝗗𝗔𝗟 𝗞𝗘 𝗟𝗢𝗙𝗜 𝗕𝗔𝗝𝗔𝗨𝗡𝗚𝗔 😍🎶",
    "{target} 𝗧𝗘𝗥𝗜 𝗕𝗔𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘𝗜 𝗕𝗔𝗥𝗚𝗔𝗗 𝗞𝗔 𝗣𝗘𝗗 𝗨𝗚𝗔 𝗗𝗨𝗡𝗚𝗔𝗔 🌳🤢",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘 ✋ 𝗛𝗔𝗧𝗧𝗛 𝗗𝗔𝗟𝗞𝗘 👶 𝗕𝗔𝗖𝗖𝗛𝗘 𝗡𝗜𝗞𝗔𝗟 𝗗𝗨𝗡𝗚𝗔 😍"
]

# --- 📱 WHATSAPP COMMANDS & ANIMATIONS ---
@wa_client.common_types(MessageEv)
def on_wa_message(client: NewClient, message: MessageEv):
    text = message.Message.conversation or message.Message.extendedTextMessage.text or ""
    chat_id = message.Info.MessageSource.Chat
    sender = message.Info.PushName or "User"

    # .help Command
    if text == ".help":
        menu = """🔥 *ANYSNAP ULTIMATE WA* 🔥

🚀 `.anysnap <count>` - Full Spam
🌹 `.rose` - Flower Bloom
🦋 `.butterfly` - Butterfly Art
🐱 `.cat` - Meow Animation
❤️ `.love` - Heart Animation
💻 `.hacker` - Hack System
🖕 `.fuck` - Fuck You
🤱 `.yourmom` - Mom Roast
ℹ️ `.info` - User Info"""
        client.send_message(chat_id, menu)

    # .anysnap Spam
    elif text.startswith(".anysnap"):
        try:
            count = int(text.split()[1]) if len(text.split()) > 1 else 10
            for _ in range(count):
                msg = random.choice(SPAM_MESSAGES).format(target=sender)
                client.send_message(chat_id, msg)
                time.sleep(0.7)
        except: pass

    # .rose Animation
    elif text == ".rose":
        for stage in ["🌱", "🌿", "🌷", "🌹 *FOR YOU!*"]:
            client.send_message(chat_id, stage)
            time.sleep(0.5)

    # .love Animation
    elif text == ".love":
        for heart in ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "💖 *I LOVE YOU*"]:
            client.send_message(chat_id, heart)
            time.sleep(0.4)

    # .cat Animation
    elif text == ".cat":
        for frame in ["🐈", "🐾", "🐈‍⬛", "🐱 *Meow!*"]:
            client.send_message(chat_id, frame)
            time.sleep(0.5)

    # .butterfly Art
    elif text == ".butterfly":
        client.send_message(chat_id, "🦋 *Flying...*")
        time.sleep(0.5)
        client.send_message(chat_id, "``` Ƹ̵̡Ӝ̵̨̄Ʒ ```")

    # .hacker Art
    elif text == ".hacker":
        client.send_message(chat_id, "💻 *HACKING...*")
        time.sleep(1)
        client.send_message(chat_id, "```[■■■■■■■■■□] 99%```")
        time.sleep(1)
        client.send_message(chat_id, "✅ *DATABASE HACKED!*")

    # .info Command
    elif text == ".info":
        info = f"""👤 *USER INFO*
📝 *Name:* {sender}
🆔 *ID:* `{chat_id.split('@')[0]}`
📱 *Device:* WhatsApp Userbot
🚀 *Powered By:* Magma Manager"""
        client.send_message(chat_id, info)

# --- 🤖 TELEGRAM OTP SYSTEM ---
@tg_bot.on_message(filters.command("start") & filters.private)
async def tg_start(bot, message):
    await message.reply("🔥 **ANYSNAP HYBRID BOT** 🔥\n\nWhatsApp Login ke liye apna number bhejein.\nExample: `+919876543210`")

@tg_bot.on_message(filters.text & filters.private)
async def tg_login(bot, message):
    phone = message.text.strip().replace("+", "")
    msg = await message.reply("🔄 OTP Request kar raha hoon...")
    try:
        code = wa_client.request_pairing_code(phone)
        await msg.edit(f"✅ **PAIRING CODE:** `{code}`\n\nIs code ko WhatsApp mein dalein. Bot active ho jayega!")
        if not wa_client.is_connected:
            wa_client.add_event_handler(MessageEv, on_wa_message)
            Thread(target=wa_client.connect).start()
    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    Thread(target=run_web).start()
    print("✅ System Online!")
    tg_bot.run()