# 🚐 여차저차
![onealog](https://www.career.go.kr/cnet/prototype/SmartEditorImgDownload.do?fileDown=2019/02/25/09/f92.JPG)

### 📢 4라져버릴조
### 프로젝트명 : 여차저차
### **여**(행)**차**(박)(레)**저차**(림)

---

⏲️ Development time

2024.05.10(금) ~ 2023.05.

- 아이디어 공유
- 와이어프레임 및 SA문서 작성
- READ.ME 작성
- 기능구현
- 발표

🧑‍🤝‍🧑 Development Team: Team-4
- 이한별 :
- 김예은 : 좋아요 및 팔로우 기능 구현
- 정윤기 : 게시판 CRUD
- 진성길 :

💻 Development Environment
- Programming Language :   <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 

- Web Framework :  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">  

- Front-End Framework : <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">


- Database : <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">

- IDE : <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">

- Version Control : 
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

- Communication : <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">




---

⚙️ Technology Stack
- Frontend : HTML
- Backend : Django
- Idea Brainstorming Tools and Environments : Slack, Zep, Notion, figma

---

📝 Project Architecture
- S.A. 노션 : https://www.notion.so/4-S-A-6ffaa44bbef34eff908b8180a7e25ccc

### ERD
![onealog](https://teamsparta.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F83c75a39-3aba-4ba4-a792-7aefe4b07895%2F31273314-d745-414f-8455-fa4a17a52701%2FUntitled.png?table=block&id=5e722b2a-8d40-40ef-bf27-1ef5db20ed56&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=2000&userId=&cache=v2)   

- 시연영상 : 아직없음

---

📌 Key Features

#### 1. Article CRUD
- 사용자는 게시글을 작성하고, 읽고, 업데이트하고, 삭제할 수 있습니다.
- 권한: 인증된 사용자만 게시글 CRUD 작업을 수행할 수 있습니다.
#### 2. Comment CRUD
- 사용자는 게시글에 대한 댓글을 작성, 조회, 업데이트 및 삭제할 수 있습니다.
댓글은 각 글의 세부정보 페이지 하단에 표시됩니다.
- 권한: 권한이 있는 사용자만 댓글을 작성하거나 편집할 수 있습니다.
#### 3. Like Feature
- 사용자는 게시글에 좋아요를 누를 수 있습니다.
- 권한: 인증된 사용자만 가능합니다.
#### 4. Search Functionality
- 사용자는 제목, 내용 또는 작성자 이름으로 게시글을 검색할 수 있습니다.
검색 결과는 검색 결과 페이지에 표시됩니다.
#### 5. Token-Based Authentication
- 토큰 기반 인증은 가입, 로그인 및 프로필 액세스 중에 안전한 사용자 인증을 보장하는 데 사용됩니다.

---

✒️ API


| Endpoint | Description | Method | 설명 |
| --- | --- | --- |  --- |
| /api/index/ | 메인화면 | GET |
| /api/users/ | 회원가입 | POST | 아이디 , 비밀번호,  입력하여 회원 가입을 진행하고 User DB에 저장됨 |
| /api/users/login/ |	로그인 | POST | 아이디 , 비밀번호를 입력하면  User DB를 확인하여 refresh key와 access key를 발급함
| /api/users/logout/	| 로그아웃 | POST |	refresh key를 입력하면 blacklisted 처리되어 로그아웃 됨
| /api/users/token/refresh/ | 토큰 재발급 | POST |토큰이 만료되면 토큰을 재발급, 다시 로그인 할 수 있도록 해줌
| follow/str:username/ |팔로우 |GET, POST |GET 요청에 팔로우, 팔로워 정보를 조회.  POST 요청에 username를 팔로우, 이미 팔로우인 경우 언팔로우
| /api/articles/ |게시글 |POST/ GET+pagination |GET 요청에  목록을 페이지네이션을 구현해 일부만 노출. POST 요청에 제목, 내용, 타입을 입력한 게시글 작성
| /api/articles/<int: pk>/comments/ |댓글작성 |POST | 게시글  int: pk의 댓글 작성(로그인 필요)
| /api/users/<str: username>/	| 프로필 확인, 프로필 수정| GET/PUT | GET 요청으로 str: username의 상세 정보를 출력 (이름,팔로워 수 등 / PUT 요청으로 username의 유저 상세 정보 수정)
| /api/article/<int: pk>/ | 게시글 상세 페이지, 게시글 수정, 삭제 | GET, PUT, DELETE | GET 요청으로 int: pk의 게시글 상세 페이지 확인. PUT 요청으로 int: pk의 게시글 수정(본인이 쓴 글만). DELETE 요청으로 int: pk의 게시글 삭제(본인이 쓴 글만)
/api/articles/<int: pk>/likes | 게시글 좋아요 | POST | ManyToManyField 로 테이블을 만들고 좋아요를 누를시  Likes DB에 저장 한번더 누를 시 Likes DB 삭제 |

