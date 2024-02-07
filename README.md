# 명찰생성기

> Created at 2023
> Wrote by Denver, 높은뜻정의교회

## 주의사항

프로젝트 예시 제공 및 원활한 이해를 돕기 위해 목업 이미지들이 레포지토리에 포함되어 있습니다  
해당 이미지들은 보안 처리가 완료된 파일들로, 무단 복제, 사용 및 재배포를 엄금합니다

대상 파일: `/data/background.jpg` `/data/backgroundB.png` `team1_띵하준.png` `team1_명하준.png`

## 연락처

프로젝트 사용이나 사용방법 등에 대해서 궁금하신 게 있다면  
높은뜻정의교회 청소년부 명하준 혹은 `fe.dev.denver@gmail.com` 으로 연락 부탁드립니다

## 사용방법

### Directory Structure

```txt
.
├── README.md
├── data                    ## 데이터 디렉토리
│   ├── README.md
│   ├── background.jpg      # 배경 이미지
│   ├── backgroundB.jpg     # 배경 이미지2
│   └── participants.txt    # 참여자 명단(형식 후술)
├── fonts                   ## 폰트 디렉토리(내용 미포함)
│   ├── README.md
│   ├── BMDOHYEON_ttf.ttf
│   └── d2coding.ttc
├── makeNamecard.py         # 진입점(명찰생성기)
├── namecards               ## 생성된 명찰 저장
│   └── README.md
├── additionalNamecards     ## 추가생성용 디렉토리
└── tools                   ## 유틸리티
    ├── init_img.sh
    └── migrate.sh
```

### Git Ignored

- 폰트 파일들은 저작권 보호를 위해 깃에 올려놓지 않았습니다

  - 본 프로그램이 사용하는 폰트는 _배달의민족 도현체_ 와 _네이버 D2코딩 폰트_ 입니다

  - [배달의민족 폰트 공식 배포사이트](https://www.woowahan.com/fonts)

  - [네이버 D2 코딩폰트 레포지토리](https://github.com/naver/d2codingfont)

## How to Use

> 모든 설명은 arm architecture를 사용하는 맥북을 기준으로 작성되었습니다

1. 가상환경 구성: `python -m venv venv`

1. 가상환경 활설화: `source venv/bin/activate`

1. **필수 라이브러리 설치**

   - 한 번에 설치하기: `pip install -r requirements.txt`

   - 수동 설치하기

     - OpenCV: `pip install opencv-python`

     - Pillow: `pip install pillow`

     - NumPy: `pip install numpy`

1. 필요한 데이터 셋팅: **### 데이터 셋팅하기** 섹션 참고

1. 실행하기: `python makeNamecard.py`

### 데이터 셋팅하기

> `/data/` 폴더 하위에 들어가야할 파일들임

- 기본 명찰 배경 이미지를 `background.jpg`로 저장

- 스태프용 명찰 배경 이미지를 `backgroundB.jpg`로 저장

- `participants.txt` 파일을 형식에 맞게 입력

  - 아래와 같이, <팀|Int> <이름|Str> <역할|Str> <스태프인가?|Bool> <나이|Str>를 한 줄로 구성

    - 각 내용은 코드에서 `team` `name` `role` `isTeacher` `bod`의 변수로 나누어져 저장됨

  - 각 컬럼은 콤마(,)로 구분하되, 콤마 이후 공백이 없도록 입력

    예시:

    ```txt
    1,띵하준,스태프,True,99또래
    ```

### 데이터 셋팅과 관한 코드 수정하기

- 1 ~ 32번줄에 파일이름, 경로 등을 환경에 맞게 구성

- 중요 변수 내용 변경

  ```python
  bods = ["99또래", "98또래", "97또래", "00또래", "01또래"]
  roles = ["선생님", "간사님", "목사님", "전도사님", "스태프"]
  grades = ["예시1", "예시2", "예시3", "예시4", "예시5", "예시6"]
  ```

  - bods에 `participants.txt` 마지막 컬럼, 나이(bod)애 들어가는 내용들의 종류를 적기

    - isTeacher(스태프인가?) 컬럼이 True인 경우, 제외해도 무방함

  - bods 배열과 같은 크기로 grades 배열을 구성

    - 스태프가 아닌 경우, bods 배열에서 찾은 인덱스로 grades 내용을 명찰에 씀

      - ex: `1,기영욱,학생,False,98또래`는 isTeacher가 False이므로 명찰에 '예시2'가 적힘

    - 스태프인 경우, bod로 준 값을 그대로 씀

      - ex: `1,띵하준,스태프,True,99또래`는 isTeacher가 True이므로 명찰에 '선생님'이 적힘

    - roles 배열에 '스태프'로 취급할 역할을 나열하기

## 글자크기, 위치, 색깔 등 조정하기

> 좌표는 좌상단 (0, 0)을 기준으로 우측이 +x, 아래가 +y 이며, 단위는 픽셀(px)임

- 글자 색깔: `makeNamecard.py`의 50, 54, 59번째 줄 `textColor` 값을 변경

  - 순서대로 (R, G, B, Alpha) 값임

- 글자크기: 같은 파일 64 ~ 66번째 줄 변수들을 수정

  - `font`는 글자가 3글자 이하일 경우 기본크기(800), 4글자 이상일 경우 작은크기(720)으로 설정

    - 간혹 4글자 이상인 이름이 있어서 준비한 예외처리임

  - `smallFont`는 조(팀)을 표시하기 위한 작은 폰트임

  - `supersmallFont`는 역할을 표시하기 위한 가장 작은 폰트임

- 글자위치: 픽셀 단위로 조정이 필요함. 배경 이미지의 크기에 따라 잘 넣을 것

  - 71번줄 `x0`를 조정해서 시작 위치를 설정

    - else 문에는 4글자 이상일 경우 시작될 위치(더 앞이 되어야 함)로 설정

  - 74번줄 `xLen`에는 이름의 길이를 설정

    - 이 길이를 이용해서 글자와 글자 사이 간격, `xGap`이 자동 계산됨
