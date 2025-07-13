# 📥 YouTube Downloader para Termux

Este é um script em Python simples e funcional para baixar vídeos (`.mp4`) ou músicas (`.mp3`) do YouTube diretamente no seu **celular Android** usando **Termux**.

---

# 📥 YTMS - YouTube Downloader para Termux

Baixe vídeos (MP4) e músicas (MP3) do YouTube diretamente no seu Android usando Termux.

---

## ✅ Como usar

### 1. Instale os requisitos no Termux:

```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg wget -y
pip install pytube
termux-setup-storage

2. Baixe e execute o script:

wget https://raw.githubusercontent.com/Marconesds1/YTMS/main/YTMS.py
python YTMS.py


---

📁 Arquivos baixados

Os arquivos serão salvos automaticamente em:

/sdcard/Download


---

📌 Atalho opcional:

Adicione um comando curto para rodar sempre que quiser:

echo "alias ytms='python ~/YTMS.py'" >> ~/.bashrc
source ~/.bashrc

Depois basta digitar:

ytms


---

👨‍💻 Autor

Marcones
GitHub: @Marconesds1
Telegram: @marcones_ms
