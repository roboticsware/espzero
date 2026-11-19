변경 이력 (Change log)
======================

.. currentmodule:: espzero

0.0.8 - 2026-11-20
------------------
+ SSD1306 및 SH1106 I2C 디스플레이를 지원하는 ``OLED`` 클래스 도입
+ OLED 화면에 10종류 감정을 출력하는 로봇 표정(``show_face``) 및 시선 추적(``look_at``) 기능 추가
+ OLED 로봇 표정 8종 벡터 그래픽 다이어그램(``oled_robot_faces.svg``) 제작 및 레시피 반영
+ PC/노트북 마이크로 음성을 인식해 ESP32 스마트카를 무선 제어하는 **AI 음성 (AI Voice)** 섹션 신설
+ Mu 에디터 내장 온라인 플래셔([ESP Online Flasher]) 및 오프라인 플래셔 가이드 보강
+ Mu 에디터 환경과 일반 Python 에디터(VS Code, Thonny, mpremote) 환경을 명확히 구분한 패키지 설치 가이드
+ 초음파(HC-SR04P 3.3V) 및 LCD(PCF8574 레벨 시프터 연동) 회로도를 안전한 3.3V 기준으로 전면 개편
+ Freenove ESP32-S3 WROOM CAM (N16R8) 카메라 간섭 방지 안전 핀맵 기준 고해상도 SVG 회로도 제공
+ 문서 인덱스에 PyPI 최신 패키지 버전 배지 및 ReadTheDocs 빌드 상태 배지 연동
+ 한국어, 영어, 우즈베크어 문서에 버전별 히스토리 관리를 위한 ``changelog.rst`` 신설

0.0.7 - 2026-11-17
------------------
+ YOLO 모델 설치 가이드 및 WiFi YOLO 자율주행차 레시피 추가
+ 논블로킹 스트리밍 및 WiFi 지원을 포함한 ``vision.py`` 모듈 고도화
+ 단독 배터리 구동 ``main.py`` 자동 실행 및 야외 핫스팟 연동 팁 추가
+ 한국어 및 우즈베크어 문서 전면 동기화

0.0.6 - 2026-11-16
------------------
+ 카메라 비전 모듈 및 관련 RST 문서 추가
+ Freenove ESP32-S3 WROOM CAM 공식 핀 별칭 및 보드 메타데이터 추가
+ ESP32-S3용 NeoPixelLED 색상 설정기(setter) 및 핀 유효성 검증 강화
+ Sphinx 다국어(ko, en, uz) 문서 빌드 환경 구축

0.0.5 - 2026-11-15
------------------
+ CapTouch 정전식 터치 센서 문서 추가
+ ESP32-S3 / ESP32-C3용 내장 온도 센서(``esp_temp_sensor`` / ``mcu_temperature``) 버그 수정
+ ReadTheDocs 설정 및 링크 개선

0.0.3 - 2026-11-14
------------------
+ 스테퍼 모터(``Stepper``) 및 ``I2cLcd`` / ``GpioLcd`` 디스플레이 제어 기능 포팅
+ ``DistanceSensor`` 측정 단위를 센티미터(cm)로 통일
+ ESP32 38핀 NodeMCU 프로필 및 제한 핀(RESTRICTED_PINS) 안전 보호망 추가

0.0.2 - 2026-11-13
------------------
+ 내장 LED 별칭 ``esp_led`` 및 커스텀 소프트웨어 스케줄러 추가
+ NodeMCU V3 Lolin (ESP8266) 보드 프로필 지원 추가
+ MicroPython 호환성 및 패키지 임포트 구조 개선

0.0.1 - 2026-11-12
------------------
+ ESP32 및 ESP8266 피지컬 컴퓨팅을 위한 espzero 라이브러리 최초 릴리즈
