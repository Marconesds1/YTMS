from pytube import YouTube
import os

def baixar_video(url, tipo):
    try:
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
    link = input("Cole o link do vídeo do YouTube: ")
    tipo = input("Baixar como MP3 ou MP4? ").strip().lower()
    baixar_video(link, tipo)
