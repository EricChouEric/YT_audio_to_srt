# YouTube 字幕生成與校正工具

## 簡介
此專案包含兩個主要資料夾：

1. **YT_download_playlist**
   - 用於從 YouTube 播放清單下載影片音訊，將音訊轉為 `.wav` 格式，並使用 Whisper 模型生成初步的字幕檔案（`.srt`）。
   
2. **srt_correct_tool**
   - 提供一個簡單的圖形介面，協助使用者對 `.srt` 字幕檔進行人工精細校正。

## 使用說明

### 1. 環境需求
在開始之前，請確保已安裝以下環境：

- Python 3.7 或以上
- ffmpeg
- Whisper（medium 模型）
- 其他必要的 Python 套件（詳見下方安裝方式）

### 2. 安裝依賴

```bash
pip install -r requirements.txt
```

**注意：** 此專案需要安裝 Whisper medium 模型。可執行在Github上git clone whisper.cpp：

### 3. 資料夾功能

#### **YT_download_playlist**

1. 將 YouTube 播放清單的 URL 提供給工具。
2. 執行main.py將會：
   - 下載影片音訊並轉為 `.wav` 格式。
   - 利用 Whisper 模型將 `.wav` 音訊轉錄成初步字幕檔案（`.srt`）。
   - 將結果保存至指定目錄。

#### **srt_correct_tool**
1. 將初步生成的 `.srt` 檔案載入工具。
2. 使用圖形介面進行：
   - 時間軸的細調。
   - 字幕內容的修正。
   - 播放對應音訊片段進行核對。
3. 修正後的字幕可保存為新的 `.srt` 檔案。

### 4. 使用流程

#### 第一步：下載音訊並生成初步字幕
1. 將 YouTube 播放清單 URL 和whisper.cpp的位置添加到 `YT_download_playlist` 工具中。
2. 執行腳本，生成 `.wav` 檔案並轉錄為 `.srt` 字幕。

#### 第二步：字幕校正
1. 打開 `srt_correct_tool` 工具。
2. 載入第一步生成的 `.srt` 檔案與對應的 `.wav` 音訊檔案。
3. 在圖形介面中逐句校對與修正字幕。
4. 保存修正後的字幕檔案。

## 目錄結構
```
project_root/
├── YT_download_playlist/
│   ├── main.py
│   └── result/
│       ├── audio/
│       └── srt/
├── srt_correct_tool/
│   ├── srt_tool.py
│   ├── srt_tool.app
│   ├── capy.ico
└── README.md
```

## 注意事項
- **Whisper 模型**：預設使用 medium 模型，若需更高精度可切換至 large 模型。
- **音訊與字幕匹配**：在校正字幕時，請確保音訊檔案與字幕檔案命名一致。

## 開發者
若有任何問題，歡迎聯繫開發者或提交 Issue。
