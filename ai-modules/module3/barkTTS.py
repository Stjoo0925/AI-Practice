# pip install git+https://github.com/suno-ai/bark.git

# Bark 라이브러리와 관련 모듈을 임포트합니다.
from bark import generate_audio
import numpy as np
import soundfile as sf

# 텍스트 입력을 정의합니다.
input_text = "안녕하세요, Bark 모델을 사용하여 음성을 생성합니다."

# 음성 데이터를 생성합니다.
audio_array = generate_audio(input_text)

# 생성된 음성을 로컬 파일로 저장합니다.
output_path = "bark_output.wav"
sf.write(output_path, audio_array, samplerate=24000)
print(f"음성 파일이 '{output_path}'에 성공적으로 저장되었습니다.")