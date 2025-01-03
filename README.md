# Project Workflow: Audio Translation and Subtitle Alignment

This README provides an overview of the workflow for translating audio and aligning subtitles using the provided pipeline. The system is designed to handle audio translation and synchronization with subtitles efficiently. Below is a breakdown of the process based on the included flowchart.

---

## Workflow Steps
- - ![image](https://github.com/EricChouEric/YT_subtitle_project/blob/main/img/Framework.png)
### 1. **Download Audio and Perform Rough Translation**
   - **Input:** Playlist or collection URL containing multiple video URLs.
   - **Process:**
     1. Extract audio from videos in the playlist (e.g., `Chinese_video_title.mp3`).
     2. Generate a hash value for each audio file to build a dictionary for subtitle alignment.
     3. Use the Whisper model to perform rough transcription and generate intermediate subtitle files (e.g., `Hash_1.srt`, `Hash_2.srt`).
     4. Cross-reference hash values with the dictionary to produce a refined subtitle file (e.g., `Subtitle1.srt`).
   - **Output:** Rough subtitle files.
   

---

### 2. **Subtitle Correction Using SRT Files and Audio**
   - **Input:**
     - Initial subtitle file (e.g., `Subtitle1.srt`).
     - Corresponding audio file (e.g., `Subtitle1.mp3`).
   - **Process:**
     1. Analyze time intervals and textual content from the subtitle file.
     2. Split the audio into segments corresponding to each subtitle line.
     3. Match audio segments with subtitle lines to improve accuracy.
     4. Provide a user interface for manual verification, where users can:
        - Load subtitle (`.srt`) and audio (`.mp3`) files.
        - Adjust timings and text alignment.
        - Play and save corrected subtitle files.
   - **Output:** Final corrected subtitle file.

---

## Key Components

- **Hashing System:**
  - Generates unique identifiers for audio segments to assist in dictionary-based subtitle refinement.

- **Whisper Model:**
  - Used for automatic transcription and initial subtitle generation.

- **Manual Adjustment Tool:**
  - Allows users to review, edit, and finalize subtitles.

---

## Usage

1. Provide the playlist or collection URL.
2. Run the pipeline to generate rough subtitles.
3. Use the manual adjustment tool to refine the subtitles.
4. Save the corrected subtitle files.

---

## Output

- Rough subtitles: `Hash.srt`
- Final subtitles: `Subtitle_corrected.srt`


---

## Future Improvements

- Enhance the Whisper model's accuracy for transcription.
- Automate more subtitle alignment processes to minimize manual adjustments.
- Expand compatibility with various audio and subtitle formats.

---

## Contact

For questions or suggestions, please contact the project team.

---
