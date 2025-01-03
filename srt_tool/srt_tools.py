import pysrt
import tkinter as tk
from pydub import AudioSegment
from pydub.playback import play           # 載入 pydub.playback 的 play 模組
from tkinter import filedialog

class SRTPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SRT Editor")

        self.srt_content = None
        self.text_entries = []

        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='black')  # 设置背景为黑色

        load_srt_button = tk.Button(self.root, text="Load srt File", command=self.load_srt_file, bg='green', fg='black')
        load_srt_button.pack()

        load_mp3_button = tk.Button(self.root, text="Load mp3 File", command=self.load_mp3_file, bg='blue', fg='black')
        load_mp3_button.pack()

        canvas = tk.Canvas(self.root, bg='black')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.table = tk.Frame(canvas, bg='black')
        self.table.pack()

        scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=canvas.yview, bg='black')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.create_window((0, 0), window=self.table, anchor=tk.NW)

        self.table.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.root.bind_all("<MouseWheel>", lambda event: self.scroll_table(event, canvas))

    def load_srt_file(self):
        srt_file_path = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])

        if srt_file_path:
            self.srt_content = pysrt.open(srt_file_path)
            self.display_srt_content(srt_file_path)

    def load_mp3_file(self):
        self.mp3_file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])


    def play_mp3(self, start, end):
        if hasattr(self, 'mp3_file_path'):
            mp3_audio = AudioSegment.from_mp3(self.mp3_file_path)
            start_time = self.calculate_milliseconds(start)
            end_time = self.calculate_milliseconds(end)
            audio_slice = mp3_audio[start_time:end_time]
            play(audio_slice)
            print(f"Playing audio from {start} to {end}")
        else:
            print("MP3 file not loaded yet. Load an MP3 file first.")

    def calculate_milliseconds(self, time):
        return (time.hours * 3600 + time.minutes * 60 + time.seconds) * 1000 + time.milliseconds

    def display_srt_content(self, file_path):
        for i, sub in enumerate(self.srt_content):
            time_label = tk.Label(self.table, text=f"{sub.start} --> {sub.end}", bg='black', fg='white')
            time_label.grid(row=i, column=0)

            text_entry = tk.Entry(self.table, width=40, bg='black', fg='white')
            text_entry.insert(tk.END, sub.text)
            text_entry.grid(row=i, column=1)

            save_button = tk.Button(self.table, text="Save", command=lambda idx=i, entry=text_entry, start=sub.start, end=sub.end, path=file_path: self.apply_changes(idx, entry, start, end, path), bg='green', fg='black')
            save_button.grid(row=i, column=2)

            play_srt_button = tk.Button(self.table, text="Play SRT", command=lambda start=sub.start, end=sub.end: self.play_mp3(start, end), bg='green', fg='black')
            play_srt_button.grid(row=i, column=3)

    def apply_changes(self, index, entry, start, end, file_path):
        self.srt_content[index].text = entry.get()
        self.srt_content[index].start = start
        self.srt_content[index].end = end

        self.srt_content.save(file_path, encoding='utf-8')
        # self.update_text_entries()

    # def update_text_entries(self):
    #     for i, sub in enumerate(self.srt_content):
    #         self.text_entries[i].delete(0, tk.END)
    #         self.text_entries[i].insert(tk.END, sub.text)

    def scroll_table(self, event, canvas):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def run(self):
        self.root.mainloop()

player = SRTPlayer()
player.run()


# pyinstaller --onefile srt_tools.py -w --icon=capy.ico