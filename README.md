# NoExcuses

AI로 강화된 잔소리로 게으름을 박살내자!

<details>
<summary> 기술 시현 영상 </summary>
<div markdown="1">    
  
https://github.com/user-attachments/assets/fc7def39-daaf-400c-a3c9-dfe00cb73d94
  
</div>
</details>

### 프로젝트 시작
```
conda activate chatbot
cd client
npm run dev
```

## 🛠️ Tech Stacks
FE: React

BE: Flask, SQLite

ML: TensorFlow, PPO(Proximal Policy Optimization)

## 📂 Directory Structure

```
📦 NoExcuses
├─ 📂 client                         # React 프론트엔드 디렉토리
│  ├─ 📦 node_modules
│  ├─ 📂 public
│  │  └─ 📄 index.html
│  └─ 📂 src
│     ├─ 📄 App.js
│     ├─ 📄 index.js
│     └─ 📂 components
│        ├─ 📂 images
│        ├─ 📂 style
│        ├─ 📂 utils                 # 유틸리티 함수들을 모아둔 디렉토리
│        └─ 📂 views                 # 페이지 단위의 컴포넌트 디렉토리
│           └─ 📄 Chat.jsx           # 채팅 관련 메인 컴포넌트
│ 
├─ 🐍 app.py                         # Flask 백엔드 메인 애플리케이션
├─ 🐍 chat_model.py                  # ChatGPT API 연동 로직
├─ 🐍 rl_agent.py                    # 강화학습(Reinforcement Learning) 에이전트를 구현한 파일
├─ 📄 package.json                   # 프로젝트 의존성 및 스크립트 정의
├─ 📄 .env                           # 환경 변수 파일 (API 키 등)
├─ 📄 .gitignore
├─ 📄 LICENSE
└─ 📄 README.md 
```
