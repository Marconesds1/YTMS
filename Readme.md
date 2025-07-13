# 📥 YouTube Downloader para Termux

Este é um script em Python simples e funcional para baixar vídeos (`.mp4`) ou músicas (`.mp3`) do YouTube diretamente no seu **celular Android** usando **Termux**.

---

## 📌 Requisitos

Antes de usar o script, você precisa instalar alguns pacotes no Termux:

```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg wget -y
pip install pytube
termux-setup-storage
