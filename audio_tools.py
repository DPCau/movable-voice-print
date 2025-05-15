import whisper
from pydub import AudioSegment
import random


class AudioTools:
    def __get_word_timestamps(self ,audio_path, model_name="base", device="cpu", language="english"):
        # options: tiny/base/small/medium/large
        if model_name not in ["tiny", "base", "small", "medium", "large"]:
            raise ValueError("Invalid model name")

        model = whisper.load_model(model_name, device=device)
        result = model.transcribe(
            audio_path,
            word_timestamps=True,
            fp16=False,
            language=language,
        )
        words = []
        sentence = []
        for segment in result["segments"]:
            for word in segment["words"]:
                words.append({
                    "text": word["word"],
                    "start": word["start"],
                    "end": word["end"]
                })
                sentence.append(word["word"])
        return words

    def __split_audio_by_timestamps(self ,audio_path, timestamps):
        audio = AudioSegment.from_file(audio_path)

        segments = []
        for ts in timestamps:
            start_ms = int(ts["start"] * 1000)
            end_ms = int(ts["end"] * 1000)
            segment = audio[start_ms:end_ms]
            segments.append(segment)
        return segments
    
    def __shuffle_and_concat_segments(self, segments, output_path="./output/output_audio.mp3", format='mp3'):
        if format not in ["mp3", "wav"]:
            raise ValueError("Invalid format. Supported formats are 'mp3' and 'wav'.")
        random.shuffle(segments)
        new_audio = AudioSegment.empty()
        for seg in segments:
            new_audio += seg
        new_audio.export(output_path, format=format)
        print(f"audio save at: {output_path}")

    def run(self, input_path, model_name="base", output_path="./output/output_audio.mp3", format="mp3", device="cpu", language="english"):
        words = self.__get_word_timestamps(input_path, model_name, device, language)
        segments = self.__split_audio_by_timestamps(input_path, words)
        self.__shuffle_and_concat_segments(segments, output_path, format)
        print("done!")