
---

## 기능 1: GET /api/profile

### RED 단계 (Human)
```
블로그/포트폴리오 프로젝트에 JSON API를 추가하려고 해.
첫 번째 기능으로 GET /api/profile 엔드포인트를 만들 거야.
다음 테스트가 실패하는 RED 상태가 되도록 테스트 코드만 먼저 작성해줘:
- GET /api/profile → 200
- Content-Type이 application/json
- 응답에 name 필드가 있고, 그 값이 profile.json의 name과 같아야 함
```

### GREEN 단계 (AI)
```
위 테스트가 통과하도록 GET /api/profile API를 구현해줘.
data/profile.json을 읽어서 JSON으로 반환하면 돼.
Flask blueprint로 api 모듈을 만들고 url_prefix는 /api로 해줘.
```

---

## 기능 2: GET /api/projects

### RED 단계 (Human)
```
두 번째 API 기능: GET /api/projects
프로젝트 목록을 JSON 배열로 반환하는 엔드포인트야.
RED 테스트 조건:
- GET /api/projects → 200
- 응답이 배열이고, 각 항목에 title, description 필드가 있어야 함
테스트만 추가해줘 (아직 구현 X).
```

### GREEN 단계 (AI)
```
test_api_projects_returns_list 테스트가 통과하도록 
GET /api/projects 엔드포인트를 구현해줘.
data/projects.json을 로드해서 그대로 JSON으로 반환하면 돼.
```

---

## 기능 3: GET /api/projects/<id>

### RED 단계 (Human)
```
세 번째 API: GET /api/projects/<id> - 프로젝트 상세 조회
RED 테스트:
1. GET /api/projects/1 → 200, 해당 프로젝트 JSON (id, title, description 포함)
2. GET /api/projects/999 → 404 (존재하지 않는 id)
테스트 코드만 작성해줘.
```

### GREEN 단계 (AI)
```
GET /api/projects/<id> API를 구현해줘.
projects.json에서 id로 항목을 찾아서 반환하고, 없으면 404를 반환해줘.
projects.json에 id 필드를 추가해야 하면 추가해줘.
```

---

## 기능 4: GET /api/notes

### RED 단계 (Human)
```
네 번째 API: GET /api/notes - 노트/블로그 목록
data/notes.json에 id, title, content, date 구조로 노트가 있어.
RED 테스트:
- GET /api/notes → 200
- 응답이 배열이고, 각 항목에 title, content 필드가 있어야 함
테스트만 추가해줘.
```

### GREEN 단계 (AI)
```
GET /api/notes 엔드포인트를 구현해줘.
data/notes.json 파일이 없으면 샘플 데이터로 생성해주고, 
로드해서 JSON 배열로 반환하는 API를 만들어줘.
```

---

## 기능 5: GET /api/notes/<id>

### RED 단계 (Human)
```
다섯 번째 API: GET /api/notes/<id> - 노트 상세 조회
RED 테스트:
1. GET /api/notes/1 → 200, id/1인 노트의 title, content 포함
2. GET /api/notes/999 → 404
테스트 코드만 작성해줘.
```

### GREEN 단계 (AI)
```
GET /api/notes/<id> API를 구현해줘.
notes.json에서 id로 노트를 찾아 반환하고, 없으면 404를 반환해줘.
api blueprint의 projects/<id> 구현 패턴을 참고해서 만들어줘.
```

---

## 통합 요청 (선택)

### 한 번에 RED 테스트 5개
```
JSON API에 5개 기능을 TDD로 추가하려고 해.
다음 5개 엔드포인트에 대한 RED 테스트를 tests/test_api.py에 작성해줘:
1. GET /api/profile - 프로필 JSON
2. GET /api/projects - 프로젝트 목록
3. GET /api/projects/<id> - 프로젝트 상세 (404 포함)
4. GET /api/notes - 노트 목록
5. GET /api/notes/<id> - 노트 상세 (404 포함)
아직 구현하지 말고 테스트만 먼저 작성해서 RED 상태로 만들어줘.
```

### 한 번에 GREEN 구현
```
tests/test_api.py의 JSON API 테스트 5개가 모두 통과하도록 구현해줘.
blueprints/api.py를 만들고 app.py에 등록해줘.
data/notes.json이 없으면 생성하고, projects.json에 id 필드를 추가해줘.
```

---

## 제출 시 참고

- **RED**: 사람(Human)이 스펙을 정의하고 실패하는 테스트를 먼저 작성
- **GREEN**: AI가 테스트를 통과하도록 최소한의 코드를 구현
- 실제 과제에서는 위 프롬프트를 그대로 또는 수정해서 Cursor/ChatGPT 등에 입력한 뒤, 대화 기록과 함께 제출하면 됩니다.
