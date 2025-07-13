# 📥 YouTube Downloader para Termux

Este é um script em Python simples e funcional para baixar vídeos (`.mp4`) ou músicas (`.mp3`) do YouTube diretamente no seu **celular Android** usando **Termux**.

---

# 🎵 YTMS - YouTube Downloader com yt-dlp para Termux

Baixe músicas (MP3) e vídeos (MP4) do YouTube no Android via Termux usando `yt-dlp`.

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/Marconesds1/YTMS.git
cd YTMS

2. Instale as dependências

pkg update && pkg upgrade -y
pkg install python ffmpeg git -y
pip install yt-dlp
termux-setup-storage

3. Execute o script

python YTMS.py


---

📁 Onde os arquivos são salvos

Os downloads vão para:

/sdcard/Download


---

🛠️ Dica: criar um alias para facilitar

echo "alias ytms='python ~/YTMS/YTMS.py'" >> ~/.bashrc
source ~/.bashrc

Agora só digite:

ytms


---

⚠️ Aviso Legal

Use para conteúdo autorizado. Respeite direitos autorais.


---

👨‍💻 Autor

Marcones
GitHub: @Marconesds1
Telegram: @marcones_ms
