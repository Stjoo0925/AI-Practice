# rust 다운로드

# pip install git+https://github.com/myshell-ai/MeloTTS.git

# 필요한 모듈을 임포트합니다.
from melotts import MeloTTS
import soundfile as sf
import numpy as np

# MeloTTS 모델 초기화
tts = MeloTTS(model_name="myshell-ai/MeloTTS-Korean")

# 텍스트 입력 정의
input_text = "안녕하세요, 이것은 MeloTTS 모델을 사용한 TTS 예제입니다."

# 텍스트를 음성으로 변환
audio_data = tts.synthesize(input_text)

# 오디오 데이터를 float32 형식으로 변환하여 저장
output_path = "meloTTS_output.wav"
sf.write(output_path, audio_data, samplerate=24000, format="WAV")
print(f"음성 파일이 '{output_path}'에 성공적으로 저장되었습니다.")

# 선행 설치 프로그램이 너무 많아 포기