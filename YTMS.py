from pytube import YouTube
import os

def corrigir_link(link):
    if "youtu.be/" in link:
        video_id = link.split("/")[-1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return link

def baixar_video(url, tipo):
    try:
        url = corrigir_link(url)
        yt = YouTube(url)
        print(f"\n🎵 Título: {yt.title}")
        print(f"⏱️ Duração: {yt.length // 60} minutos")

        caminho = "/sdcard/Download"

        if tipo == 'mp3':
            audio = yt.streams.filter(only_audio=True).first()
            print("🔽 Baixando áudio...")
            out_file = audio.download(output_path=caminho)
            base, ext = os.path.splitext(out_file)
            novo_arquivo = base + '.mp3'
            os.rename(out_file, novo_arquivo)
            print(f"✅ Música salva em: {novo_arquivo}")

        elif tipo == 'mp4':
            video = yt.streams.get_highest_resolution()
            print("🔽 Baixando vídeo...")
            video.download(output_path=caminho)
            print(f"✅ Vídeo salvo em: {caminho}")

        else:
            print("❌ Tipo inválido. Use 'mp3' ou 'mp4'.")

    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")

if __name__ == "__main__":
    print("=== YouTube Download by Marcones_ms ===")
    link = input("Cole o link do vídeo do YouTube: ").strip()
    tipo = input("Baixar como MP3 ou MP4? ").strip().lower()
    baixar_video(link, tipo)
