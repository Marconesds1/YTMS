import os
from yt_dlp import YoutubeDL

def baixar_video(url, tipo):
    caminho = "/sdcard/Download"
    ydl_opts = {
        'outtmpl': os.path.join(caminho, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    if tipo == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif tipo == 'mp4':
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })
    else:
        print("❌ Tipo inválido. Use 'mp3' ou 'mp4'.")
        return

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(f"🔽 Baixando {tipo.upper()}...")
            ydl.download([url])
        print(f"✅ Download concluído! Arquivo salvo em: {caminho}")
    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")

if __name__ == "__main__":
    print("=== YouTube Download by Marcones_ms (yt-dlp) ===")
    link = input("Cole o link do vídeo do YouTube: ").strip()
    tipo = input("Baixar como MP3 ou MP4? ").strip().lower()
    baixar_video(link, tipo)
