시작하기
=======

Mu를 사용하여 설치하기
--------------------

요구 사항
~~~~~~~~~

Windows 또는 macOS 컴퓨터 (`Mu 에디터`_\ 가 설치됨).

.. _Mu 에디터: https://github.com/roboticsware/mu/releases/latest

MicroPython 모드 선택
~~~~~~~~~~~~~~~~~~~~

Mu를 열고 왼쪽 상단의 **모드(Mode)** 버튼을 클릭합니다. **ESP32**\ 를 선택하고 **확인(OK)**\ 을 클릭합니다.

.. image:: /images/mu-select-mode-esp32.jpg
    :alt: Mu 에디터에서 ESP32 모드 선택

Mu에서 espzero 설치하기
~~~~~~~~~~~~~~~~~~~~~~

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
-----------------------

Mu의 파일 관리자를 사용하여 ``espzero_lib`` 폴더 안에 ``espzero`` 라이브러리를 ESP32로 복사하여 설치할 수 있습니다.

**파일(Files)** 버튼을 클릭하여 파일 관리자를 엽니다.

.. image:: /images/mu-files-button.jpg
    :alt: Mu에서 파일(Files) 버튼 클릭

Mu의 **컴퓨터의 파일(Files on your computer)** 창에서 ``espzero_lib`` 폴더 안에 있는 ``espzero`` 폴더를 찾습니다. 해당 항목을 **장치의 파일(Files on your device)** 창으로 드래그 앤 드롭합니다.

.. image:: /images/mu-drag-and-drop.jpg
    :alt: Mu에서 컴퓨터의 espzero를 장치로 드래그 앤 드롭
