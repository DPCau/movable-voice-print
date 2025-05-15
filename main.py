import argparse
import os
from audio_tools import AudioTools


def main():
    parser = argparse.ArgumentParser(
        description="Tool for randomly shuffling audio segments based on word-level timestamps",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--input", "-i", type=str, required=True,
                        help="Path to input audio file (required, supports mp3 and wav)")
    parser.add_argument("--model", "-m", type=str, default="base",
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size (affects recognition accuracy and speed)")
    parser.add_argument("--output", "-o", type=str, default="./output/output_audio.mp3",
                        help="Path to output audio file (default: ./output/output_audio.mp3)")
    parser.add_argument("--format", "-f", type=str, default="mp3",
                        choices=["mp3", "wav"],
                        help="Output format (only supports mp3/wav)")
    parser.add_argument("--device", "-d", type=str, default="cpu",
                        choices=["cpu", "cuda"],
                        help="Execution device (cpu or cuda, requires GPU for cuda)")
    parser.add_argument("--language", "-l", type=str, default="english",
                        help="Force specify audio language (e.g., chinese/english/japanese; auto-detect by default)")

    args = parser.parse_args()
    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file not found: {args.input}")
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    audio_tools = AudioTools()
    try:
        audio_tools.run(
            input_path=args.input,
            model_name=args.model,
            output_path=args.output,
            format=args.format,
            device=args.device,
            language=args.language
        )
    except Exception as e:
        print(f"Error occurred during execution: {str(e)}")
if __name__ == "__main__":
    main()