<!--
Sync Impact Report
Version change: 0.0.0 -> 1.0.0
List of modified principles:
- [PRINCIPLE_1_NAME] -> Specification-Driven Development
- [PRINCIPLE_2_NAME] -> AI-Native Implementation
- [PRINCIPLE_3_NAME] -> Incremental Phase Evolution
- [PRINCIPLE_4_NAME] -> Stateless & Cloud-Native
- [PRINCIPLE_5_NAME] -> Clear Separation of Concerns
- [PRINCIPLE_6_NAME] -> Explicit Interface Boundaries
Added sections:
- Phase-Specific Requirements
- Constraints & Invariants
- Folder Structure Standards
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md (✅ updated)
- .specify/templates/spec-template.md (✅ updated)
- .specify/templates/tasks-template.md (✅ updated)
Follow-up TODOs: None
-->

# AI-Native Todo Application Constitution

## Core Principles

### I. Specification-Driven Development
All features and changes MUST originate from written specifications (specs). Specs are the absolute source of truth for the system's behavior and requirements. No implementation should exist without a corresponding spec.

### II. AI-Native Implementation
AI agents are the primary implementers of the codebase. Humans act as architects, providing guidance, reviewing output, and ensuring alignment with the project vision. No manual code edits should occur outside of AI-generated output.

### III. Incremental Phase Evolution
The project evolves through five distinct phases (Console -> Web -> AI/MCP -> K8s -> Cloud-Native). History and specifications MUST be preserved across phases, with each phase building upon the foundations and specs of the previous one.

### IV. Stateless & Cloud-Native
Starting from Phase II, all backend services MUST remain stateless. The system design should prioritize cloud-native principles, ensuring horizontal scalability and resilience.

### V. Clear Separation of Concerns
There must be a strict separation between UI, API, agent, tools, and infrastructure. Each component should have a clearly defined responsibility and interact with others only through established interfaces and contracts.

### VI. Explicit Interface Boundaries
Agent interactions must occur only through defined MCP tools. Services must not bypass defined interfaces (e.g., direct DB access by an agent is prohibited in Phase III+).

## Phase-Specific Requirements

### Phase Architecture
1. **Phase I (Console)**: Python CLI, in-memory storage, pure spec-to-code workflow.
2. **Phase II (Web)**: JS Frontend, Python Backend, JWT Auth, REST API.
3. **Phase III (AI/MCP)**: Chat interaction, MCP server, tool-only agent access, persistent DB.
4. **Phase IV (K8s)**: Containerization, Local K8s deployment, Helm/Manifests.
5. **Phase V (Cloud)**: Cloud deployment, Event-driven (Dapr/Kafka), Async processing, Decoupled services.

## Constraints & Invariants
- **No Phase Skipping**: Phases must be completed sequentially (1 through 5).
- **No Phase Collapsing**: Each phase must have its own implementation and artifacts.
- **No Hardcoded Secrets**: Use environment variables and secret management from the start.
- **No Persistence in Phase I**: Storage remains in-memory only for the console application.

## Folder Structure Standards
Each phase (phase-1 to phase-5) MUST contain:
- `specs/`: Current feature specifications.
- `specs/history/`: Historical versions of specifications.
- `plans/`: Implementation plans and architectural decisions.
- `tasks/`: Testable task lists.
- `implementation/`: The actual codebase.
- `README.md`: Phase-specific documentation.

## Governance
This constitution supersedes all other development practices in this project. Amendments require a version bump and a Sync Impact Report. All PRs and tasks must be validated against these principles.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
