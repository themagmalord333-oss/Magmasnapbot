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
