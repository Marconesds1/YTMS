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

📥 Instalação no Termux

1. Instale os requisitos:

pkg update && pkg upgrade -y
pkg install python ffmpeg wget -y
pip install pytube
termux-setup-storage

2. Baixe o script:

wget https://raw.githubusercontent.com/Marconesds1/YTMS/main/YTMS.py

3. Execute:

python YTMS.py


---

⚙️ Como funciona?

Ele irá pedir o link do vídeo do YouTube.

Em seguida, pergunte se quer MP3 (áudio) ou MP4 (vídeo).

O arquivo será salvo em:
📁 /sdcard/Download



---

🔁 Atalho opcional (com alias):

echo "alias ytms='python ~/YTMS.py'" >> ~/.bashrc
source ~/.bashrc

Agora você pode rodar com apenas:

ytms


---

📝 Sugestão de README.md

Aqui está um modelo simples para colocar no seu repositório YTMS:

# 🎵 YTMS - YouTube Music & Video Downloader (Termux)

Baixe vídeos e músicas do YouTube diretamente no seu Android com Termux.

## 🚀 Instalação no Termux

```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg wget -y
pip install pytube
termux-setup-storage
wget https://raw.githubusercontent.com/Marconesds1/YTMS/main/YTMS.py
python YTMS.py

✅ Recursos

🎧 Baixa áudio em MP3

🎥 Baixa vídeo em MP4

📁 Salva diretamente em /sdcard/Download


📌 Atalho rápido

echo "alias ytms='python ~/YTMS.py'" >> ~/.bashrc
source ~/.bashrc

Depois, basta rodar:

ytms

⚠️ Uso Educacional

Este projeto é para fins educacionais. Respeite os direitos autorais.

👨‍💻 Autor

Marcones
🔗 GitHub: @Marconesds1
📱 Telegram: @marcones_ms

---
