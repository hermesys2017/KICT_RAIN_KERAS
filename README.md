# KICT Rain AI - 딥러닝 기반 강수량 예측 시스템

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![QGIS 3.40+](https://img.shields.io/badge/QGIS-3.40+-green.svg)](https://qgis.org/)

> 한국건설기술연구원(KICT) 및 HermeSys에서 개발한 레이더 데이터 기반 정량적 강수 예측 시스템

## 📋 목차

- [소개](#-소개)
- [주요 기능](#-주요-기능)
- [설치 방법](#-설치-방법)
- [사용 방법](#-사용-방법)
- [모델 버전](#-모델-버전)
- [프로젝트 구조](#-프로젝트-구조)
- [개발 환경 설정](#-개발-환경-설정)
- [라이선스](#-라이선스)

## 🌧️ 소개

KICT Rain AI는 딥러닝 모델을 활용하여 레이더 데이터로부터 최대 180분 앞의 강수 패턴을 예측하는 시스템입니다. QGIS 플러그인과 독립 실행형 Python 스크립트 두 가지 방식으로 사용할 수 있습니다.

### 주요 특징

- **다양한 모델 옵션**: Keras 표준 모델, TFLite 최적화 모델, 앙상블 모델 지원
- **QGIS 통합**: QGIS 플러그인으로 제공되어 공간 데이터 분석 워크플로우에 완벽 통합
- **독립 실행 가능**: QGIS 없이도 Python 스크립트로 모델 사용 가능
- **실시간 예측**: 레이더 합성영상(HSP) 데이터를 입력으로 실시간 강수량 예측

## ✨ 주요 기능

- ✅ 레이더 데이터(ASC 형식) 기반 강수량 예측
- ✅ 최대 180분 전방 예측
- ✅ 3가지 모델 버전 지원 (Ver1 Keras, Ver1 TFLite, Ver2 Ensemble)
- ✅ QGIS GUI 인터페이스 제공
- ✅ 배치 처리 지원
- ✅ 자동 의존성 설치

## 🚀 설치 방법

### 필수 요구사항

- Python 3.8 이상
- QGIS 3.40 이상 (플러그인 사용 시)

### 1. 저장소 클론

```bash
git clone https://github.com/hermesys2017/KICT_RAIN_KERAS.git
cd KICT_RAIN_KERAS
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

또는 개발 의존성 포함:

```bash
pip install -r requirements-dev.txt
```

### 3. QGIS 플러그인 설치 (선택사항)

1. QGIS를 실행합니다
2. `플러그인` > `플러그인 관리 및 설치`로 이동
3. `ZIP에서 설치` 탭 선택
4. `kict_rain_ai` 폴더를 압축하여 업로드
5. 플러그인 활성화

**참고**: 플러그인 최초 실행 시 필요한 패키지(tensorflow, gdown)가 자동으로 설치됩니다.

## 📖 사용 방법

### 방법 1: Python 스크립트로 사용

`main.py` 파일을 사용하여 모델을 직접 실행할 수 있습니다:

```python
from data import dataset
from model_oop import RainVer1Model, RainVer1TfliteModel, RainVer2Model

# 입력 파일 경로 설정
files = [
    "./datas/RDR_CMP_HSP_PUB_202208082320-525x625-1km.asc",
    "./datas/RDR_CMP_HSP_PUB_202208082330-525x625-1km.asc",
    "./datas/RDR_CMP_HSP_PUB_202208082340-525x625-1km.asc",
    "./datas/RDR_CMP_HSP_PUB_202208082350-525x625-1km.asc",
]

# Ver1 모델 사용
input_data = dataset(files)
model = RainVer1Model("./models/model-best_rec_180min_f.h5")
model.save_prediction_files(input_data, "output/ver1/")

# Ver2 앙상블 모델 사용
input_data = dataset(files)
model = RainVer2Model("./models")
model.save_prediction_files(input_data, "output/ver2/")

# Ver1 TFLite 모델 사용
input_data = dataset(files, is_ver1_tflite=True)
model = RainVer1TfliteModel("./models/model-best_rec_180min_f.tflite")
model.save_prediction_files(input_data, "output/ver1_tflite/")
```

실행:
```bash
python main.py
```

### 방법 2: QGIS 플러그인으로 사용

1. QGIS에서 플러그인 활성화
2. 툴바에서 KICT Rain AI 아이콘 클릭
3. GUI에서 입력 파일 선택
4. 모델 버전 선택
5. 예측 실행

## 🔧 모델 버전

### Ver1 - Keras 모델
- **파일 형식**: `.h5`
- **특징**: 표준 Keras/TensorFlow 모델
- **용도**: 높은 정확도가 필요한 경우

### Ver1 TFLite - 경량화 모델
- **파일 형식**: `.tflite`
- **특징**: TensorFlow Lite로 최적화된 경량 모델
- **용도**: 빠른 추론 속도가 필요한 경우

### Ver2 - 앙상블 모델
- **파일 형식**: 여러 `.tflite` 모델
- **특징**: 다중 모델 앙상블로 안정적인 예측
- **용도**: 최고의 예측 성능이 필요한 경우

## 📁 프로젝트 구조

```
KICT_RAIN_KERAS/
├── kict_rain_ai/          # QGIS 플러그인 소스
│   ├── kict_rain_ai.py    # 플러그인 메인 클래스
│   ├── kict_rain_ai_dialog.py  # UI 다이얼로그
│   ├── services/          # 모델 서비스 로직
│   ├── models/            # 학습된 모델 파일
│   └── test/              # 테스트 코드
├── main.py                # 독립 실행 스크립트
├── model_oop.py           # 모델 클래스 정의
├── data.py                # 데이터 전처리
├── requirements.txt       # Python 의존성
├── pyproject.toml         # 프로젝트 설정
└── README.md              # 프로젝트 문서
```

## 🛠️ 개발 환경 설정

### 코드 스타일

이 프로젝트는 [Ruff](https://github.com/astral-sh/ruff)를 사용하여 코드 스타일을 관리합니다:

```bash
# 코드 포맷팅
ruff format .

# 린팅
ruff check .
```

### 테스트 실행

```bash
cd kict_rain_ai
python -m pytest test/
```

### 플러그인 빌드

```bash
cd kict_rain_ai
make zip
```

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👥 개발자

- **한국건설기술연구원 (KICT)**
- **HermeSys**
  - Email: info@hermesys.co.kr
  - Website: http://www.hermesys.co.kr

## 🔗 링크

- [GitHub Repository](https://github.com/hermesys2017/KICT_RAIN_KERAS)
- [Issue Tracker](https://github.com/hermesys2017/KICT_RAIN_KERAS/issues)
- [QGIS Plugin Repository](https://plugins.qgis.org/)

## 📞 지원

문제가 발생하거나 질문이 있으시면 [이슈 트래커](https://github.com/hermesys2017/KICT_RAIN_KERAS/issues)에 등록해주세요.
