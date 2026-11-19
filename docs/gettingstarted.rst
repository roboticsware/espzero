시작하기
========

이 가이드는 초보자를 위한 **Mu 에디터 환경**뿐만 아니라 개발자 및 자동화를 위한 **mpremote / pip 명령줄 도구**를 사용하여 ESP32에 ``espzero`` 라이브러리를 설치하는 전체 방법을 안내합니다.

명령줄 도구로 설치하기 (CLI)
----------------------------

터미널이나 명령 프롬프트(CMD, PowerShell)에서 작업하는 경우 다음 도구를 사용하여 간편하게 설치할 수 있습니다.

mpremote로 보드에 직접 설치
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mpremote``\ 는 MicroPython 공식 명령줄 관리 도구로, PC에 연결된 보드와 직렬(USB) 통신하여 별도의 파일 복사 프로그램 없이 라이브러리를 다운로드하고 기기에 설치(MIP)해 줍니다.

1. **mpremote 설치 (PC 터미널)**:
   
   .. code-block:: bash

       pip install mpremote

2. **espzero 라이브러리 보드 설치**:
   
   ESP32 보드를 PC의 USB 포트에 연결한 상태에서 아래 명령어를 실행합니다. 기기 내부의 ``/lib`` 폴더에 ``espzero``\ 가 자동으로 설치됩니다:

   .. code-block:: bash

       mpremote mip install espzero

.. tip::
    ESP32 보드가 여러 개 연결되어 있거나 포트를 수동 지정해야 하는 경우, ``mpremote connect COMx mip install espzero`` (Windows) 또는 ``mpremote connect /dev/ttyUSB0 mip install espzero`` (macOS/Linux) 형태로 지정할 수 있습니다.

PC 개발 환경을 위한 pip 설치 (자동 완성/린팅)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VS Code, PyCharm 등 데스크톱 IDE에서 코드 작성 시 함수 및 클래스 자동 완성(IntelliSense)과 타입 검사를 사용하려면 PC 환경에도 설치합니다:

.. code-block:: bash

    pip install espzero

Mu를 사용하여 설치하기
----------------------

요구 사항
~~~~~~~~~

Windows 또는 macOS 컴퓨터 (`Mu 에디터`_\ 가 설치됨).

.. _Mu 에디터: https://github.com/roboticsware/mu/releases/latest

MicroPython 모드 선택
~~~~~~~~~~~~~~~~~~~~~

Mu를 열고 왼쪽 상단의 **모드(Mode)** 버튼을 클릭합니다. **ESP32**\ 를 선택하고 **확인(OK)**\ 을 클릭합니다.

.. image:: /images/mu-select-mode-esp32.jpg
    :alt: Mu 에디터에서 ESP32 모드 선택

자동 설치 (패키지 매니저)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
    **인터넷 연결 필요**: 패키지 매니저를 통해 온라인(PyPI/MIP)에서 최신 라이브러리를 검색하고 다운로드하므로, 컴퓨터가 인터넷에 연결되어 있어야 합니다.

Mu에서 espzero를 설치하려면 **패키지(Packages)**\ 를 클릭합니다.

.. image:: /images/mu-packages-button.jpg
    :alt: Mu에서 패키지 버튼 클릭

`espzero`\ 를 검색하고 **검색(Search)**\ 을 클릭합니다.

.. image:: /images/mu-search-espzero.jpg
    :alt: Mu 패키지 관리자에서 espzero 검색

**설치(Install)**\ 를 클릭하여 패키지를 다운로드하고 장치에 설치합니다.

.. image:: /images/mu-install-package.jpg
    :alt: Mu 패키지 관리자에서 설치 클릭

수동 설치 (드래그 앤 드롭)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mu의 파일 관리자를 사용하여 ``espzero_lib`` 폴더 안에 ``espzero`` 라이브러리를 ESP32로 복사하여 설치할 수 있습니다.

**파일(Files)** 버튼을 클릭하여 파일 관리자를 엽니다.

.. image:: /images/mu-files-button.jpg
    :alt: Mu에서 파일(Files) 버튼 클릭

Mu의 **컴퓨터의 파일(Files on your computer)** 창에서 ``espzero_lib`` 폴더 안에 있는 ``espzero`` 폴더를 찾습니다. 해당 항목을 **장치의 파일(Files on your device)** 창으로 드래그 앤 드롭합니다.

.. image:: /images/mu-drag-and-drop.jpg
    :alt: Mu에서 컴퓨터의 espzero를 장치로 드래그 앤 드롭
