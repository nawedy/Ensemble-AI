# MVP Implementation Plan

## 1. Service Scaffolding (Phase 2.1)
```python
# services/math/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve_equation():
    # Wolfram Alpha integration
    return "Math service stub"

# Similar for coding/reasoning services
```

## 2. API Gateway Enhancements
```python
# api_gateway/routes/auth.py
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def init_auth(app):
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
    jwt.init_app(app)
```

## 3. Docker Orchestration
```yaml
# docker/docker-compose.yml
services:
  math-service:
    build: ../services/math
    ports:
      - "5001:5000"
  # Add similar for other services
```

## 4. CI/CD Pipeline
```yaml
# .github/workflows/ci.yml
name: CI
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r api_gateway/requirements.txt
      - run: pytest api_gateway/tests/
```

Next Steps:
1. Implement service stubs
2. Add JWT authentication
3. Define Docker services
4. Write OpenAPI spec