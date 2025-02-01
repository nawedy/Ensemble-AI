# Ensemble-AI Project Index

## Core Components
### API Gateway (`/api_gateway`)
```text
├── main.py               # Flask entrypoint (needs JWT auth)
├── requirements.txt      # Dependencies (add prometheus-client)
└── routes/
    ├── health.py         # Basic endpoint (needs metrics)
    └── [MISSING]        # auth.py, codegen.py from Phase 2.3
```

### Services (`/services`)
```text
coding/                  # Empty - Phase 2.1
math/                    # Empty - Phase 2.1  
reasoning/               # Empty - Phase 2.1
```

### Infrastructure
```text
docker/
├── docker-compose.yml    # Needs service definitions
├── Dockerfile.gateway    # Valid Python setup
└── Dockerfile.vscode     # Node.js base
```

## MVP Implementation Checklist

### Phase 1 Completion
✅ Basic API gateway scaffold  
✅ Docker foundation  
❌ OpenAPI specs  
❌ Wireframes

### Phase 2 Requirements
```text
1. [ ] Math Service (Wolfram Alpha integration)
2. [ ] Code Service (Codex/Copilot)  
3. [ ] Reasoning Service (GPT-4 + RAG)
4. [ ] VSCode Extension UI
5. [ ] API Gateway Enhancements
```

## Critical Path
1. Create service scaffolds with Docker support
2. Implement auth middleware
3. Add OpenAPI documentation
4. Set up CI/CD (GitHub Actions)