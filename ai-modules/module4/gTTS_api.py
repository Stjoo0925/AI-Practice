# 필요한 라이브러리 설치
# pip install gTTS
# pip install soundfile
# pip install "fastapi[standard]"

# step 1 : import module
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gtts import gTTS
from io import BytesIO
from fastapi.responses import StreamingResponse
import datetime

# step 2 : create inference object(instance)
# FastAPI 앱 초기화
app = FastAPI()

# step 3 : prepare data
# 텍스트 입력 모델 정의
class TextInput(BaseModel):
    text: str

# step 4 : inference
# TTS 변환 엔드포인트 정의
@app.post("/synthesize")
async def synthesize_text(input: TextInput):
    # 입력된 텍스트가 비어 있는지 확인
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="텍스트를 입력해야 합니다.")
    
    # gTTS 객체 생성 및 텍스트 변환
    tts = gTTS(text=input.text, lang='ko')
    
    # 바이트 스트림으로 음성 데이터를 저장
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)  # 스트림을 처음으로 되돌립니다.

    # step 5 : post processing
    # 로컬 파일에 저장
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"tts_output_{timestamp}.mp3"
    with open(output_filename, "wb") as f:
        f.write(audio_bytes.read())
    audio_bytes.seek(0)  # 다시 스트림 처음으로 이동하여 스트리밍 반환 준비

    # 파일 저장 경로 정보 출력
    print(f"음성 파일이 '{output_filename}'에 성공적으로 저장되었습니다.")
    
    # StreamingResponse로 음성 데이터를 반환
    return StreamingResponse(audio_bytes, media_type="audio/mp3")
