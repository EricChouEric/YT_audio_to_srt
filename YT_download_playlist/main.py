from utils.wavtosrt import AudioToSrt
from utils.yt_playlist_audio_download import VideoDownloader



if __name__ == '__main__':
    # 用來下載播放清單的URL
    playlist_url = 'https://youtube.com/playlist?list=PLQn99bzkJv9xkYTHFsBIsA0xgtVcQmGzG&si=8hwYWAS_WAZ_uwkF'  # 你可以替換成你的播放清單URL

    #whisper.cpp path
    whiserper_path = '../whisper.cpp'

    # 創建 VideoDownloader 實例並下載
    downloader = VideoDownloader(playlist_url)
    downloader.download()

    #convert to srt
    srt_tools = AudioToSrt()
    srt_tools.excute()

