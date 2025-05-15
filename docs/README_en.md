# Movable Voice Print

<p align="center">
  <a href="./README_en.md"><img src="https://img.shields.io/badge/English-0078D4?style=flat&logo=google-translate&logoColor=white" alt="English"></a>
  <a href="../README.md"><img src="https://img.shields.io/badge/中文-FF0000?style=flat&logo=google-translate&logoColor=white" alt="中文"></a>
</p>

## 🌟 Project Overview  
This tool uses speech recognition (Whisper) to extract word/character-level timestamps from audio, splits audio segments based on time intervals, then randomly reorganizes them to generate new audio.

## 🚀 Core Features  
1. **Multilingual Word Segmentation**: Powered by Whisper model, supports 100+ languages (Chinese/English/Japanese, etc.), precisely identifying word/character time intervals.  
2. **Lossless Audio Recomposition**: Randomly rearranges original audio fragments while preserving speaker's voice characteristics and intonation.  
3. **Automated Workflow**: One-click processing for full pipeline - "Speech Recognition → Splitting → Recomposition".  

## 📦 Requirements  
- **OS**: Windows/macOS/Linux  
- **Dependencies**:  
  - Python 3.8-3.10  
  - PyTorch  
  - Whisper  
  - pydub  

## 🛠️ Installation  
1. **Clone Repository**  
   ```bash  
   git clone https://github.com/DPCau/movable-voice-print.git  
   ```  
2. **Create Virtual Environment**  
   ```bash  
   uv venv --python 3.9  
   source .venv/bin/activate  
   ```  

3. **Install Python Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Install FFmpeg**  
   - **Windows**: Download from [FFmpeg Official](https://ffmpeg.org/), add to PATH.  
   - **macOS**: `brew install ffmpeg`  
   - **Linux**: `sudo apt-get install ffmpeg`  

## 📖 Usage Guide  
### 1. Prepare Input Audio  
- Supported Formats: MP3/WAV  
- Recommendation: ≤30min duration, clear speech (background noise may reduce accuracy).  

### 2. Run Script  
```python  
python main.py --input input.mp3  
```  

### 3. Optional Parameters  
| Parameter       | Description                                                                 |  
|-----------------|-----------------------------------------------------------------------------|  
| `--input`       | Input audio path (required)                                                 |  
| `--output`      | Output path (default: output_audio.mp3)                                     |  
| `--model`       | Whisper model size (options: tiny/base/small/medium/large, default: base)   |  
| `--language`    | Force language detection (e.g., zh/en/jp, default: english). Affects text splitting only. |  
| `--format`      | Output format (options: mp3/wav, default: mp3)                             |  
| `--device`      | Compute device (options: cpu/cuda, default: cpu)                            |  

## 📘 Example Workflow  
1. **Input Audio**:  
   ```  
   input.mp3 (Content: "[Sun Xiaochuan]不要说废话我不喜欢别人说废话.<Don't talk nonsense. I hate people talking nonsense.>")  
   ```  

2. **Timestamp Recognition**:  
   ```json  
   [
      {"text": "不要", "start": 0.0, "end": 0.26}, 
      {"text": "说", "start": 0.26, "end": 0.5}, 
      {"text": "废", "start": 0.5, "end": 0.68}, 
      {"text": "话", "start": 0.68, "end": 0.84}, 
      {"text": "我不", "start": 0.84, "end": 1.14}, 
      {"text": "喜欢", "start": 1.14, "end": 1.48}, 
      {"text": "别", "start": 1.48, "end": 1.72}, 
      {"text": "人", "start": 1.72, "end": 1.82}, 
      {"text": "说", "start": 1.82, "end": 1.98}, 
      {"text": "废", "start": 1.98, "end": 2.18}, 
      {"text": "话", "start": 2.18, "end": 2.42}
   ]
   ```  

3. **Recomposed Output**:  
   ```  
   output_audio.mp3 (Content: "[Sun Xiaochuan] 说要废话我废喜不说欢不人别话.")  
   ```  

## 🧪 Accuracy & Optimization  
**Speech Recognition Accuracy**:  
Recommend using `medium` or `large` models for better timestamp accuracy in Chinese and other languages.

## 📜 License  
MIT