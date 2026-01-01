# 📜 CONSTITUTION.md
Hackathon II — Spec-Driven Cloud-Native AI Todo System

## 1. Purpose & Philosophy

This repository implements Hackathon II: The Evolution of Todo using Spec-Driven Development and AI-Native Architecture.

The system evolves from a simple in-memory CLI to a cloud-native, event-driven, AI-powered Todo platform, without manual coding.
The engineer's role is system architect, not syntax writer.

**Golden Rule:**
❌ No handwritten application code
✅ All code is generated via Claude Code from validated specs

## 2. Core Principles

**Spec is the Source of Truth**
All behavior, APIs, schemas, and flows originate from /specs.

**AI-Native by Design**
AI agents are first-class citizens using MCP tools, not wrappers.

**Stateless & Cloud-Ready**
All services are horizontally scalable and restart-safe.

**Progressive Evolution**
Each phase builds on the previous without breaking contracts.

**Production-Grade Defaults**
Security, auth, observability, and scalability are mandatory.

## 3. Development Constraints (Non-Negotiable)

❌ Manual code writing is forbidden

❌ Ad-hoc changes outside specs are forbidden

✅ Specs must be refined until Claude Code produces correct output

✅ Every feature must have a corresponding spec

✅ Generated code must match the spec exactly

Violating these rules invalidates the submission.

## 4. Supported Phases

| Phase | Scope | Outcome |
|-------|-------|---------|
| I | Console App | In-memory Python Todo |
| II | Web App | Full-stack, authenticated CRUD |
| III | AI Chatbot | MCP-powered conversational Todo |
| IV | Local K8s | Docker + Helm + Minikube |
| V | Cloud Native | Kafka + Dapr + Managed K8s |

## 5. Repository Structure

```
.
├── .spec-kit/
│   └── config.yaml
├── specs/
│   ├── overview.md
│   ├── architecture.md
│   ├── features/
│   ├── api/
│   ├── database/
│   └── ui/
├── frontend/
│   └── CLAUDE.md
├── backend/
│   └── CLAUDE.md
├── CLAUDE.md
├── CONSTITUTION.md
└── README.md
```

## 6. Technology Constitution

### Phase-Aligned Stack (Version-Compatible)

#### Core
- Python ≥ 3.13
- Node.js ≥ 20 LTS
- TypeScript ≥ 5.4
- UV for Python dependency management

#### Frontend
- Next.js ≥ 16 (App Router)
- React ≥ 19
- Tailwind CSS
- OpenAI ChatKit

#### Backend
- FastAPI
- SQLModel
- Neon Serverless PostgreSQL
- Better Auth (JWT)

#### AI & Agents
- OpenAI Agents SDK
- Official MCP SDK
- Claude Code
- Spec-Kit Plus

#### Cloud & DevOps
- Docker
- Kubernetes
- Helm
- Minikube
- kubectl-ai
- kagent

#### Event-Driven (Phase V)
- Kafka (Redpanda / Strimzi)
- Dapr (Pub/Sub, State, Jobs, Secrets)

## 7. Specification Governance

### Spec Categories

| Folder | Responsibility |
|--------|----------------|
| /specs/features | User-visible behavior |
| /specs/api | REST & MCP contracts |
| /specs/database | Schema & indexes |
| /specs/ui | Components & pages |

### Spec Rules
- Specs must be deterministic
- Specs must include acceptance criteria
- Specs must be referenceable using @specs/...
- Specs evolve — code regenerates

## 8. Authentication & Security Constitution

- Authentication is mandatory from Phase II onward
- JWT is the only trust mechanism
- Backend never trusts frontend state
- User isolation is enforced at:
  - API level
  - Database query level
  - MCP tool level
- Environment variables are the only configuration source.

## 9. AI Agent & MCP Rules

- Agents must not mutate state directly
- All mutations go through MCP tools
- MCP tools are:
  - Stateless
  - Idempotent where possible
  - Database-backed
- Agents confirm actions in natural language

## 10. Cloud-Native & Scalability Guarantees

- Services must be restart-safe
- Horizontal scaling must not break behavior
- Kubernetes manifests are Helm-driven
- Infrastructure changes are spec-driven
- Event handling is asynchronous in Phase V

## 11. Observability & Reliability

- Failures must be explicit
- Errors must be user-friendly
- Logs must be structured
- Events must be auditable (Kafka)

## 12. Bonus-Readiness

This architecture explicitly supports:
- Reusable Intelligence (Agent Skills)
- Cloud-Native Blueprints
- Urdu language support
- Voice commands
- Multi-client real-time sync

No rewrites required.

## 13. Enforcement

If a conflict exists between:
- Code and Spec → Spec wins
- README and Spec → Spec wins
- Assumption and Spec → Spec wins

## 14. Final Statement

This project is not a Todo app.
It is a reference implementation of AI-Native, Spec-Driven, Cloud-Scale software engineering.

Write specs.
Refine intent.
Let agents build.
