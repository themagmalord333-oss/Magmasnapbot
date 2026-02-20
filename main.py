import os
import time
import random
import asyncio
from threading import Thread
from flask import Flask
from pyrogram import Client, filters, idle
from neonize.client import NewClient
from neonize.events import MessageEv

# ---------------------------------------------------------
# 🌐 FLASK KEEP ALIVE (Render Web Server)
# ---------------------------------------------------------
web_app = Flask('')
@web_app.route('/')
def home(): return "ANYSNAP ULTIMATE IS RUNNING! 🚀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

# ---------------------------------------------------------
# ⚙️ CONFIGURATION
# ---------------------------------------------------------
API_ID = 37314366
API_HASH = "bd4c934697e7e91942ac911a5a287b46"
BOT_TOKEN = "8485202414:AAEEYv7_UjUR2DI4KN9l4bEKnsD9v0WGn7E"

tg_bot = Client("MagmaManager", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
wa_client = NewClient("magma_wa.db")

# --- 🔥 FULL RESTORED SPAM LIST ---
SPAM_MESSAGES = [
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘 𝗖𝗛𝗔𝗡𝗚𝗘𝗦 𝗖𝗢𝗠𝗠𝗜𝗧 𝗞𝗥𝗨𝗚𝗔 𝗙𝗜𝗥 𝗧𝗘𝗥𝗜 𝗕𝗛𝗘𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗔𝗨𝗧𝗢𝗠𝗔𝗧𝗜𝗖𝗔𝗟𝗟𝗬 𝗨𝗣𝗗𝗔𝗧𝗘 𝗛𝗢𝗝𝗔𝗔𝗬𝗘𝗚𝗜 🤖🙏🤔",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗨𝗠𝗠𝗬 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗞𝗢 𝗢𝗡𝗟𝗜𝗡𝗘 𝗢𝗟𝗫 𝗣𝗘 𝗕𝗘𝗖𝗛𝗨𝗡𝗚𝗔 𝗔𝗨𝗥 𝗣𝗔𝗜𝗦𝗘 𝗦𝗘 𝗧𝗘𝗥𝗜 𝗕𝗔𝗛𝗘𝗡 𝗞𝗔 𝗞𝗢𝗧𝗛𝗔 𝗞𝗛𝗢𝗟 𝗗𝗨𝗡𝗚𝗔 😎🤩😝😍",
    "{target} 𝗧𝗘𝗥𝗜 𝗚𝗙 𝗛𝗘 𝗕𝗔𝗗𝗜 𝗦𝗘𝗫𝗬 𝗨𝗦𝗞𝗢 𝗣𝗜𝗟𝗔𝗞𝗘 𝗖𝗛𝗢𝗗𝗘𝗡𝗚𝗘 𝗣𝗘𝗣𝗦𝗜",
    "{target} 𝗚𝗔𝗟𝗜 𝗚𝗔𝗟𝗜 𝗠𝗘 𝗥𝗘𝗛𝗧𝗔 𝗛𝗘 𝗦𝗔𝗡𝗗 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔𝗞𝗢 𝗖𝗛𝗢𝗗 𝗗𝗔𝗟𝗔 𝗢𝗥 𝗕𝗔𝗡𝗔 𝗗𝗜𝗔 𝗥𝗔𝗡𝗗 🤤🤣",
    "{target} 𝗔𝗕𝗘 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗢 𝗖𝗛𝗢𝗗𝗨 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗣𝗜𝗟𝗟𝗘 𝗞𝗨𝗧𝗧𝗘 𝗞𝗘 𝗖𝗛𝗢𝗗𝗘 😂👻🔥",
    "{target} 𝗧𝗘𝗥𝗜 𝗕𝗔𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗨𝗧 𝗠𝗘𝗜 𝗔𝗣𝗣𝗟𝗘 𝗞𝗔 𝟭𝟴𝗪 𝗪𝗔𝗟𝗔 𝗖𝗛𝗔𝗥𝗚𝗘𝗥 🔥🤩",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘𝗜 𝗕𝗔𝗧𝗧𝗘𝗥𝗬 𝗟𝗔𝗚𝗔 𝗞𝗘 𝗣𝗢𝗪𝗘𝗥𝗕𝗔𝗡𝗞 𝗕𝗔𝗡𝗔 𝗗𝗨𝗡𝗚𝗔 🔋 🔥🤩",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗘 𝗕𝗛𝗢𝗦𝗗𝗘 𝗠𝗘𝗜 𝗦𝗣𝗢𝗧𝗜𝗙𝗬 𝗗𝗔𝗟 𝗞𝗘 𝗟𝗢𝗙𝗜 𝗕𝗔𝗝𝗔𝗨𝗡𝗚𝗔 😍🎶🎶💥",
    "{target} 𝗠𝗔𝗗𝗔𝗥𝗖𝗛𝗢𝗗 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘 𝗚𝗛𝗨𝗧𝗞𝗔 𝗞𝗛𝗔𝗔𝗞𝗞𝗘 𝗧𝗛𝗢𝗢𝗞 𝗗𝗨𝗡𝗚𝗔 🤣🤣",
    "{target} 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗡 𝗞𝗜 𝗖𝗛𝗨𝗤 𝗠𝗘 𝗞𝗘𝗟𝗘 𝗞𝗘 𝗖𝗛𝗜𝗟𝗞𝗘 🍌🍌😍",
    "{target} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘 ✋ 𝗛𝗔𝗧𝗧𝗛 𝗗𝗔𝗟𝗞𝗘 👶 𝗕𝗔𝗖𝗖𝗛𝗘 𝗡𝗜𝗞𝗔𝗟 𝗗𝗨𝗡𝗚𝗔 😍",
    "{target} 𝗧𝗘𝗥𝗜 𝗕𝗘𝗛𝗘𝗡 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗘𝗜 𝗕𝗔𝗥𝗚𝗔𝗗 𝗞𝗔 𝗣𝗘𝗗 𝗨𝗚𝗔 𝗗𝗨𝗡𝗚𝗔𝗔 🌳🤢"
]

# --- 🎨 RESTORED ARTS ---
HACKER_ART = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿
"""
YOURMOM_ART = "🤱 *ANYSNAP VS YOUR MOM* 🤱\nTERI MAA MERI LUND PE! 🥵💋"

# ---------------------------------------------------------
# 📱 WHATSAPP COMMANDS & ANIMATIONS
# ---------------------------------------------------------
@wa_client.common_types(MessageEv)
def on_wa_message(client: NewClient, message: MessageEv):
    text = message.Message.conversation or message.Message.extendedTextMessage.text or ""
    chat_id = message.Info.MessageSource.Chat
    target = message.Info.PushName or "User"

    if text == ".help":
        menu = """🔥 *ANYSNAP ULTIMATE WA* 🔥
🚀 `.anysnap <count>` - Full Spam
🌹 `.rose` - Flower Bloom
🦋 `.butterfly` - Butterfly Art
🐱 `.cat` - Meow Animation
❤️ `.love` - Heart Animation
💻 `.hacker` - Hack System
🖕 `.fuck` - Fuck You
🤱 `.yourmom` - Mom Roast"""
        client.send_message(chat_id, menu)

    elif text.startswith(".anysnap"):
        try:
            count = int(text.split()[1]) if len(text.split()) > 1 else 10
            for _ in range(count):
                msg = random.choice(SPAM_MESSAGES).format(target=target)
                client.send_message(chat_id, msg)
                time.sleep(0.8)
        except: pass

    elif text == ".rose":
        for stage in ["🌱", "🌿", "🌷", "🌹 *FOR YOU!*"]:
            client.send_message(chat_id, stage); time.sleep(0.5)

    elif text == ".love":
        for heart in ["❤️", "🧡", "💛", "💚", "💙", "💜", "💖 *I LOVE YOU*"]:
            client.send_message(chat_id, heart); time.sleep(0.4)

    elif text == ".cat":
        for frame in ["🐈", "🐾", "🐈‍⬛", "🐱 *Meow!*"]:
            client.send_message(chat_id, frame); time.sleep(0.5)

    elif text == ".hacker":
        client.send_message(chat_id, f"💻 *HACKING...*\n```\n{HACKER_ART}\n```\n✅ *SYSTEM HACKED!*")

    elif text == ".yourmom":
        client.send_message(chat_id, YOURMOM_ART)

    elif text == ".fuck":
        client.send_message(chat_id, "🖕 *FUCK OFF!*")

# ---------------------------------------------------------
# 🤖 TELEGRAM LOGIN SYSTEM
# ---------------------------------------------------------
@tg_bot.on_message(filters.command("start") & filters.private)
async def tg_start(bot, message):
    await message.reply("🔥 **ANYSNAP HYBRID SYSTEM** 🔥\n\nWhatsApp Login ke liye apna number bhejein.\nExample: `+919876543210`")

@tg_bot.on_message(filters.text & filters.private)
async def tg_login(bot, message):
    phone = message.text.strip().replace("+", "")
    msg = await message.reply("🔄 OTP (Pairing Code) request kar raha hoon...")
    try:
        code = wa_client.request_pairing_code(phone)
        await msg.edit(f"✅ **PAIRING CODE:** `{code}`\n\nIse apne WhatsApp 'Link Devices' mein dalein.")
        if not wa_client.is_connected:
            wa_client.add_event_handler(MessageEv, on_wa_message)
            Thread(target=wa_client.connect, daemon=True).start()
    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")

# ---------------------------------------------------------
# 🚀 ADVANCED LAUNCHER (PYTHON 3.11+ FIX)
# ---------------------------------------------------------
async def main():
    # 1. Flask ko alag thread mein shuru karna
    Thread(target=run_web, daemon=True).start()
    
    # 2. Telegram Bot ko proper async loop mein start karna
    await tg_bot.start()
    print("✅ System Fully Online & Ready!")
    
    # 3. Bot ko zinda rakhna bina crash huye
    await idle()
    await tg_bot.stop()

if __name__ == "__main__":
    # Naye tareeke se event loop chalana jo Render par fail nahi hoga
    asyncio.run(main())