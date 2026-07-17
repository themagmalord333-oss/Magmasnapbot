
<div align="center">

<img src="https://files.catbox.moe/6fjcnx.jpg" alt="Magma Logo" width="150" height="150" style="border-radius: 50%;">

<h1>🚀 MAGMA USERBOT MANAGER</h1>

<p>
<b>An advanced, high-performance Telegram Userbot Manager powered by Pyrogram and Python.</b>
</p>

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-v2.0+-red.svg?logo=telegram&logoColor=white)](https://docs.pyrogram.org/)
[![Flask](https://img.shields.io/badge/Flask-Keep%20Alive-lightgrey.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/themagmalord333-oss)
[![Telegram Community](https://img.shields.io/badge/Join-Community-blue.svg?logo=telegram)](https://t.me/MAGMAxRICH)

---

</div>

## 🔗 The Magma Ecosystem
This project is an essential part of the **Magma Ecosystem**. It is built to seamlessly integrate with our other powerful tools, including [Magmasting](https://github.com/themagmalord333-oss/Magmasting). Use them together to unlock the ultimate Telegram automation experience!

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Screenshots](#-screenshots)
- [Architecture Overview](#-architecture-overview)
- [Folder Structure](#-folder-structure)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration Guide (.env)](#-configuration-guide-env)
- [Commands Reference](#-commands-reference)
  - [Manager Bot Commands](#manager-bot-commands)
  - [Userbot Commands](#userbot-commands)
- [Web Server & Keep-Alive](#-web-server--keep-alive)
- [Performance & Security](#-performance--security)
- [Roadmap & Future Plans](#-roadmap--future-plans)
- [FAQ & Troubleshooting](#-faq--troubleshooting)
- [Contributing](#-contributing)
- [Support & Credits](#-support--credits)

---

## 💡 About the Project

**Magma Userbot Manager** is a scalable, session-based Telegram Userbot hosting platform. Instead of deploying individual userbot instances manually, users can simply start the main Manager Bot, provide their Pyrogram string session, and instantly deploy a powerful arsenal of userbot commands directly to their account.

### Why this project exists?
Setting up a Telegram userbot usually requires technical knowledge, server provisioning, and environment configuration. Magma Manager democratizes this by providing a unified host. It leverages memory-efficient dynamic client instantiation to run multiple userbots concurrently under a single Python process, complete with built-in Force-Subscribe authentication.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🛡️ **Dynamic Deployment** | Deploy userbots instantly via String Session without restarting the server. |
| 🔒 **Force-Subscribe System** | Gates usage behind mandatory channel and group membership. |
| 🚀 **High-Speed Execution** | Async/Await architecture utilizing Pyrogram's MTProto wrapper. |
| 🎨 **Rich Animations** | Built-in smart-edit ASCII arts and animated text sequences. |
| 🔨 **Raid & Admin Tools** | Ultra-fast mass banning, GC nuking, and tag-all systems with flood-wait handling. |
| 🎭 **Profile Cloning** | Instantly clone (and restore) user profiles including bio, name, and avatar. |
| 🌐 **Keep-Alive Server** | Integrated Flask server for 24/7 uptime on cloud platforms like Render/Koyeb. |

---

## 📸 Screenshots

<div align="center">
  <img src="https://files.catbox.moe/jf8s4d.jpg" alt="Project Screenshot" width="800" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <br>
  <i>Magma Manager in Action</i>
</div>

---

## 🏗 Architecture Overview

The system operates on a dual-layer architecture:
1. **The Controller (Manager Bot):** A standard Telegram Bot (authenticated via `BOT_TOKEN`) that handles onboarding, verifies Force-Subscribe compliance, and validates string sessions.
2. **The Clients (Userbots):** Dynamically generated in-memory Pyrogram `Client` instances that listen to commands prefixed with `.` specifically from the authenticated user's account (`filters.me`).

---

## 📁 Folder Structure

```text
MAGMA-USERBOT/
│
├── .env                  # Environment configurations (Secrets & Keys)
├── main.py               # Core application logic & bot handlers
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

```
## 🛠 Technologies Used
 * **Python 3.9+** - Core language
 * **Pyrogram** - MTProto API framework for Telegram
 * **Flask** - Lightweight WSGI web application framework
 * **Asyncio** - Asynchronous I/O loop management
 * **Python-dotenv** - Environment variable management
## 🚀 Getting Started
### Prerequisites
 * Python 3.9 or higher
 * A Telegram API ID and Hash (from my.telegram.org)
 * A Bot Token (from @BotFather)
 * A Pyrogram String Session (Generated via @Stingxsessionbot)
### Installation
 1. **Clone the repository**
   ```bash
   git clone [https://github.com/themagmalord333-oss/magma-userbot.git](https://github.com/themagmalord333-oss/magma-userbot.git)
   cd magma-userbot
   
   ```
 2. **Install dependencies**
   ```bash
   pip install pyrogram tgcrypto flask python-dotenv
   
   ```
 3. **Configure Environment Variables**
   Create a .env file in the root directory and configure it (see configuration guide below).
 4. **Run the Application**
   ```bash
   python main.py
   
   ```
## ⚙️ Configuration Guide (.env)
The .env file holds all sensitive and configurable data. Never commit this file to version control.
| Variable | Description | Example |
|---|---|---|
| PORT | Port for the Flask Keep-Alive server | 10000 |
| API_ID | Your Telegram API ID | 12345678 |
| API_HASH | Your Telegram API Hash | abcdef1234567890 |
| BOT_TOKEN | Token from BotFather for the Manager bot | 1234:ABCDef... |
| FORCE_CHANNEL_ID | Numeric ID of your Force Sub Channel | -1001234567890 |
| FORCE_CHANNEL_LINK | Invite link for the Force Sub Channel | https://t.me/+AbcDef |
| FORCE_GROUP | Username of the Force Sub Group (no @) | Anysnapsupport |
| OWNER_ID | Your Telegram User ID for special formatting | 8081343902 |
## 📜 Commands Reference
### Manager Bot Commands
These commands are sent directly to your Manager Bot in Private Messages.
| Command | Description |
|---|---|
| /start | Displays welcome message and connection instructions. |
| /add <session> | Authenticates and boots a new userbot instance using the provided Pyrogram session string. |
### Userbot Commands
Once a session is connected, these commands are run from the User's own account using the . prefix.
#### 🎭 Animations & Fun
 * .cat - Cute walking cat ASCII animation.
 * .rose - Blooming flower to rose animation.
 * .hacker - Terminal hacking terminal animation.
 * .error - System crash/fatal error animation.
 * .fuck - Middle finger loading animation.
 * .butterfly - Draws an ASCII butterfly.
 * .love - Colorful magic heart wave animation.
 * .yourmom - Mom roast animation (NSFW text).
 * .myson - "Don't talk to me or my son" ASCII art.
#### 🛠 Utility & Profile
 * .info <reply/id> - Fetches detailed user information, DC ID, and profile picture.
 * .clone <reply> - Copies target user's first name, last name, bio, and profile picture.
 * .back - Restores your original profile data from before the clone.
#### 🔨 Moderation & Raid
 * .anysnap <count> <reply/id> - Sends repeated spam messages to the target.
 * .aanysnap <reply> - Activates a global auto-reply for a specific user.
 * .tagall <msg> - Mentions everyone in the chat (bypasses standard limits via iteration).
 * .allban <id/username> - Mass bans all members in a group with a safe 0.5s delay.
 * .fastallban <id/username> - Aggressive mass ban with randomized 0.2s - 0.3s delays.
 * .end <id/username> - Full GC Nuke: Mass bans, changes title, and pins a tagged message to the owner.
 * .stop - Emergency stop for all running loops (Spam, Tagall, Massban, Auto-reply).
## 🌐 Web Server & Keep-Alive
To ensure the bot remains online when deployed on cloud services (like Render, Heroku, or Koyeb), the project integrates a lightweight **Flask Web Server**.
 * It binds to 0.0.0.0 on the port specified by the PORT env variable.
 * Exposes a / route returning "Magma Manager Bot is Running!".
 * Can be pinged by services like UptimeRobot or cron-job.org to prevent container hibernation.
## 🔒 Performance & Security
 * **Event Loop Patching:** Includes dynamic asyncio event loop handling to prevent RuntimeError: This event loop is already running in Python 3.14+ architectures.
 * **FloodWait Handling:** All iterative commands (spam, ban, smart-edit) are wrapped in try/except blocks specifically catching pyrogram.errors.FloodWait. The bot will automatically sleep for the required duration and resume.
 * **In-Memory Sessions:** Userbot clients are instantiated with in_memory=True, meaning session data is not written to the local disk of the server, securing user tokens against local file extraction.
## 🗺 Roadmap & Future Plans
 * [ ] Add Database integration (MongoDB) to persist user sessions across server restarts.
 * [ ] Implement a Web Dashboard to manage active userbot nodes.
 * [ ] Add Broadcast system for the Owner to message all connected users.
 * [ ] Introduce AFK (Away From Keyboard) module with auto-responders.
 * [ ] Implement multi-language support.
## ❓ FAQ & Troubleshooting
<details>
<summary><b>Why am I getting "Access Denied" when trying to /start?</b></summary>


You have not joined the mandatory Force Subscribe channel and group. Ensure you click the buttons provided by the bot and join them before sending /start again.
</details>
<details>
<summary><b>My Public Channel Link isn't working for Force Subscribe. Why?</b></summary>


Ensure your <code>FORCE_CHANNEL_ID</code> in the <code>.env</code> file is set to the numeric ID (starting with <code>-100</code>), not the @username. Furthermore, the Manager Bot must be an Admin in that channel to check member statuses.
</details>
<details>
<summary><b>The bot crashes with a FloodWait error.</b></summary>


The code is designed to catch Pyrogram <code>FloodWait</code> exceptions and <code>asyncio.sleep()</code> them out automatically. However, if you are spamming heavily with <code>.fastallban</code>, Telegram may temporarily restrict your account. Use with caution.
</details>
<details>
<summary><b>How do I stop a raid in progress?</b></summary>


Simply send <code>.stop</code> in any chat where your userbot is active. It resets all global state trackers (active_spams, tagall_running, active_bans).
</details>
## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
 1. Fork the Project
 2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
 3. Commit your Changes (git commit -m 'Add some AmazingFeature')
 4. Push to the Branch (git push origin feature/AmazingFeature)
 5. Open a Pull Request
## 📄 License
Distributed under the MIT License. See LICENSE for more information.
## 📞 Support & Credits
<div align="center">
**Made with ❤️ by MAGMA**
Telegram Owner

Telegram Community

GitHub
Connected Ecosystem: Magmasting
</div>
