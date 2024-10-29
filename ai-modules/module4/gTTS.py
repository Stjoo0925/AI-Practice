# pip install gTTS

# pip install soundfile

from gtts import gTTS
from io import BytesIO
import soundfile as sf

# 텍스트 입력 정의
input_text = "안녕하세요, gTTS 라이브러리를 사용하여 생성된 음성입니다."

# gTTS 객체 생성 (언어 설정: 한국어 "ko")
tts = gTTS(text=input_text, lang='ko')

# 바이트 스트림으로 음성 데이터를 생성
audio_bytes = BytesIO()
tts.write_to_fp(audio_bytes)
audio_bytes.seek(0)

# 바이트 데이터를 로컬에 저장
with open("gtts_output.mp3", "wb") as f:
    f.write(audio_bytes.read())

print("음성 파일이 'gtts_output.mp3'에 성공적으로 저장되었습니다.")
