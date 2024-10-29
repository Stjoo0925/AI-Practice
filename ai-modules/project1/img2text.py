# 이미지를 텍스트로 변환해주는 모듈

# STEP 1: 필요한 모듈 임포트
import numpy as np
from fastapi import FastAPI, UploadFile, HTTPException
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import io

# FastAPI 인스턴스 생성
app = FastAPI()

# STEP 2: CLIPProcessor 및 모델 객체 생성
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 지원하지 않는 파일 형식 확인
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG are supported.")

    # STEP 3: 이미지 로드
    contents = await file.read()  # 이미지 파일을 바이트로 읽기
    image = Image.open(io.BytesIO(contents)).convert("RGB")  # 이미지를 PIL로 디코딩 후 RGB로 변환

    # STEP 4: CLIP 모델로 텍스트 예측
    # 샘플 텍스트 레이블
    texts = ["a photo of a dog", "a photo of a cat", "a photo of a person", "a photo of a car", "a photo of a tree"]

    # 이미지와 텍스트 레이블을 전처리
    inputs = processor(text=texts, images=image, return_tensors="pt", padding=True).to(device)

    # 모델 예측
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # 이미지-텍스트 간 유사도
    probs = logits_per_image.softmax(dim=1)  # 확률 계산

    # 가장 높은 확률을 가진 텍스트 선택
    predicted_text = texts[probs.argmax().item()]

    # 결과 반환
    return {"predicted_text": predicted_text}
