import os
import shutil
import glob
from collections import namedtuple

class AudioToSrt:
    def __init__(self, whisper_path):
        self.audio_path = './result/audio/' + os.listdir('./result/audio/')[-1]
        self.audio_path_list = glob.glob(self.audio_path + '/*')  # 確保匹配檔案
        self.whisper_path = whisper_path

        self.nametuple_path = []
        self.excep_file = []

        self.build_name_tuple()

    def build_name_tuple(self):
        """
        建立包含目錄、名稱及哈希值的 namedtuple 列表。
        """
        Path = namedtuple('Path', ['dir', 'name', 'hash'])

        for full_path in self.audio_path_list:
            dir, name = os.path.split(full_path)
            basename = os.path.splitext(name)[0]
            hash_value = hash(basename)  # 使用 hash() 計算名稱的哈希
            self.nametuple_path.append(Path(dir=dir, name=basename, hash=hash_value))

    def get_hash_path(self, file_type):
        """
        根據哈希值生成新路徑。
        """
        return [os.path.join(path.dir, f"{path.hash}{file_type}") for path in self.nametuple_path]

    def get_name_path(self, file_type):
        """
        根據名稱生成新路徑。
        """
        return [os.path.join(path.dir, f"{path.name}{file_type}") for path in self.nametuple_path]

    def check_input(self, value):
        """
        檢查輸入的值是否為字串。
        """
        if not isinstance(value, str):
            raise ValueError("輸入的值必須是字串")
        return value

    def rename(self, mode=None):
        """
        根據模式重命名檔案：'n2h' 或 'h2n'。
        """
        self.check_input(mode)

        # 檢查模式並選擇對應的檔案類型
        if mode == 'n2h':
            file_type = '.wav'
            paths_pair = zip(self.get_name_path(file_type), self.get_hash_path(file_type))
        elif mode == 'h2n':
            file_type = '.srt'
            paths_pair = zip(self.get_hash_path(file_type), self.get_name_path(file_type))
        else:
            raise ValueError("輸入值必須為 'n2h' 或 'h2n'")

        # 使用單一循環進行重命名
        for old_path, new_path in paths_pair:
            os.rename(old_path, new_path)

    def convert_to_srt(self):
        """
        將音頻檔案轉換為字幕檔案。
        """
        for p in self.get_hash_path('.wav'):
            try:
                os.system('{}/main -m {}/models/ggml-medium.bin -l zh -o{} -f {}'.format(self.whisper_path, 'srt', p))
                os.rename(p, p+'.srt')
                os.rename(f'{p}.srt', f'{p.split('.wav')[0]}.srt')
            except Exception as e:
                self.excep_file.append(f"{p}: {str(e)}")

        # 儲存異常檔案至 log.txt
        with open('log.txt', 'w', encoding='utf-8') as file:
            for item in self.excep_file:
                file.write(f"{item}\n")

        print("資料已儲存至 log.txt")                           

    def convert_to_16HZ(self):
        for p in self.get_hash_path('.wav'):
            p1 = p.split('.wav')[0]
            try:
                os.system('ffmpeg -i {}.wav -ar 16000 -ac 1 -c:a pcm_s16le {}_.wav'.format(p1, p1))
                os.remove(p)
                os.rename(f'{p1}_.wav', f'{p1}.wav')
            except Exception as e:
                print(e)

    def move_srt(self):
        file_name = os.listdir('./result/audio/')[-1]
        if not os.path.exists(f'./result/srt/{file_name}'):
            os.mkdir(f'./result/srt/{file_name}')
        for p in glob.glob(os.path.join(self.audio_path, '*.srt')):
            shutil.move(p, p.replace('audio', 'srt'))

    def excute(self):
        self.rename(mode='n2h')
        self.convert_to_16HZ()
        self.convert_to_srt()
        self.rename(mode='h2n') 
        self.move_srt()





if __name__ == '__main__':
    pass
