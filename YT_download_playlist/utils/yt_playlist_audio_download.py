import yt_dlp
import os

class VideoDownloader:
    def __init__(self, playlist_url, audio_output='./result/audio', srt_output='./result/srt', subtitle_langs=['zh-Hant']):
        # 初始化設置
        self.playlist_url = playlist_url
        self.audio_output = audio_output
        self.srt_output = srt_output
        self.subtitle_langs = subtitle_langs
        
        # 創建目標資料夾
        if not os.path.exists(self.audio_output):
            os.makedirs(self.audio_output)
        if not os.path.exists(self.srt_output):
            os.makedirs(self.srt_output)
        
        # 設定 yt-dlp 選項
        self.ydl_opts = {
            'outtmpl': os.path.join(self.audio_output, '%(playlist_title)s/%(title)s.%(ext)s'),  # 儲存音頻檔案
            'format': 'bestaudio/best',  # 下載最佳音頻
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'writesubtitles': True,  # 嘗試下載字幕
            'subtitleslangs': self.subtitle_langs,  # 下載指定語言的字幕
            'subtitlesformat': 'srt',  # 設置字幕格式為srt
            'progress_hooks': [self.progress_hook],  # 監控下載進度的hook
        }

    def progress_hook(self, d):
        """下載進度監控"""
        if d['status'] == 'finished':
            print(f"Download complete: {d['filename']}")

    def download_playlist(self):
        """下載播放清單"""
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.playlist_url])

    def download(self):
        """啟動下載過程"""
        self.download_playlist()


if __name__ == '__main__':
    # 用來下載播放清單的URL
    playlist_url = 'https://youtube.com/playlist?list=PLQn99bzkJv9xkYTHFsBIsA0xgtVcQmGzG&si=8hwYWAS_WAZ_uwkF'  # 你可以替換成你的播放清單URL

    # 創建 VideoDownloader 實例並下載
    downloader = VideoDownloader(playlist_url)
    downloader.download()
