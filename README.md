## :mag_right: 프로젝트 주제
수정,삭제할 때 비밀번호를 입력해야하는 게시글 REST API 서버 개발 <br>
과제 출처 : 띵스플로우


## :bulb: Stacks
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white"> 

## :pencil2: 요구사항 분석

- 게시글 글자수 제한
    - 제목 : 최대 20자 / 본문 : 최대 200자
    
- 게시글 비밀번호 생성
    - 비밀번호는 6자 이상, 숫자 1개 이상 입력
    - 게시글을 작성할 때, 비밀번호를 입력
    - 게시글을 수정할 때, 비밀번호를 입력
    - 게시글을 삭제할 때, 비밀번호를 입력
    
- 게시글 페이지 로드 (선택 주제)
   - 게시글이 20개가 넘어가면 새 페이지로 넘어간다.

## :gift_heart: new challenge
  - Django_framework의 hashpassword 를 이용해 봤다.
  - superuser를 사용하지 않고, 비밀번호를 생성해 게시글의 보안성을 높였다.
  - 제목, 본문 등 DB 입력에 대한 유효성 검사를 해보았다. 
    
    
## :triangular_ruler: API 정상동작 여부

### 게시글 작성

- 제목 최대 20자, 본문 최대 200자 , 작성자, 비밀번호를 입력
![create](https://user-images.githubusercontent.com/99165573/188929244-1031656f-8f7f-4bff-ae72-e201b0195925.jpg)

### 게시글 조회

- 게시물이 20개 넘어가면 페이지 1개 추가 

![list](https://user-images.githubusercontent.com/99165573/188929436-b2c17446-28de-4ee7-818b-c187b50ce003.jpg)
![list 2](https://user-images.githubusercontent.com/99165573/188929512-ad870d15-c0ac-43c7-b5f9-93fffd19724f.jpg)

### 게시글 수정

- 비밀번호를 입력하고 내용을 수정

![update](https://user-images.githubusercontent.com/99165573/188929605-d18fa0e0-ab6a-4729-8b3c-fb1e706bc2ec.jpg)

### 게시글 삭제

-비밀번호를 입력하고 내용을 삭제

![delete](https://user-images.githubusercontent.com/99165573/188929754-b8b520b7-c1d9-42a2-b3e3-07f3c5d7e5b4.jpg)

## :paperclip: 커밋 컨벤션 

-[emoji][태그 항목]:[ 커밋 내용]
  
- 태그 항목
  - Feature : 새로운 기능추가
  - Fix : 에러 해결
  - Docs : 문서 수정
  
## :100: 느낀점
  - django는 배워도 배워도 사용할 수 있는 기능이 끝도 없이 많다. 그래서 이번 프로젝트 또한 쓴 맛을 맛보았다.
    django의 공식 문서를 다시 한번 학습하는 시간을 가져야겠다. 

