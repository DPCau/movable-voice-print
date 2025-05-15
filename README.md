# Movable Voice Print 活字乱刷术

<p align="center">
  <a href="./docs/README_en.md"><img src="https://img.shields.io/badge/English-0078D4?style=flat&logo=google-translate&logoColor=white" alt="English"></a>
  <a href="./README.md"><img src="https://img.shields.io/badge/中文-FF0000?style=flat&logo=google-translate&logoColor=white" alt="中文"></a>
</p>

## 🌟 项目简介  
本工具通过语音识别(Whisper)提取音频中每个单词/字的起止时间戳,按时间区间切割音频片段,再随机排列生成新音频.


## 🚀 核心功能  
1. **多语言词级分割**:依赖Whisper模型,支持中英日等100+语言,精准识别单词/字的时间区间().  
2. **无损音频重组**:基于原始音频片段随机排列,保留原发音人音色和语调.  
3. **自动化流程**:一键完成「语音识别→切割→重组」全流程,无需手动操作.  


## 📦 环境要求  
- **系统**:Windows/macOS/Linux  
- **依赖**:  
  - Python 3.8-3.10
  - PyTorch
  - Whisper
  - pydub


## 🛠️ 安装步骤  
1. **克隆项目**  
   ```bash  
   git clone https://github.com/DPCau/movable-voice-print.git
   ```  
2. **创建虚拟环境** 
   ```bash  
   uv venv --python 3.9
   source .venv/bin/activate
   ```

3. **安装Python依赖**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **安装FFmpeg**  
   - **Windows**:从[FFmpeg官网](https://ffmpeg.org/)下载,添加到系统环境变量.  
   - **macOS**:`brew install ffmpeg`  
   - **Linux**:`sudo apt-get install ffmpeg`  


## 📖 使用指南  
### 1. 准备输入音频  
- 支持格式:MP3/WAV音频格式.  
- 建议:音频时长≤30分钟,确保语音清晰(嘈杂环境可能影响识别精度).  

### 2. 运行脚本  
```python  
python main.py --input input_audio.mp3
```  

### 3. 可选参数  
| 参数          | 说明                                                                 |  
|---------------|----------------------------------------------------------------------|  
| `--input`     | 输入音频路径(必填)                                                 |  
| `--output`    | 输出音频路径(默认:output_audio.mp3)                               |  
| `--model`     | Whisper模型版本(可选:tiny/base/small/medium/large,默认:base)    |  
| `--language`  | 强制指定语言(如:zh/en/jp,默认:english),语言仅对切分得到文本有影响 |
| `--format`| 输出音频的格式(可选:mp3/wav,默认:mp3)|
| `--device`| 指定设备(可选:cpu/cuda,默认:cpu)|


## 📘 示例流程  
1. **输入音频**:  
   ```  
   input.mp3(内容:"[孙笑川]不要说废话我不喜欢别人说废话.")  
   ```  

2. **识别时间戳**:  
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

3. **随机重组后输出**:  
   ```  
   output_audio.mp3(内容:"[孙笑川]说要废话我废喜不说欢不人别话.") 
   ```  


## 🧪 精度与优化  
**语音识别精度**:  
推荐使用`medium`或`large`模型提升中文等语言的时间戳准确性.

## 📜 许可证  
MIT