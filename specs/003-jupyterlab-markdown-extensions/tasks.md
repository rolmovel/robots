# Tasks: JupyterLab Markdown Extensions

**Input**: Design documents from `/specs/003-jupyterlab-markdown-extensions/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No automated tests requested. Each user story includes a reproducible manual validation task.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Repository root**: `curso/`, `scripts/`, `specs/`
- Paths are relative to repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Ensure project structure and dependencies are ready for extension integration

- [X] T001 Add `jupyterlab-myst>=2.4` to curso/requirements.txt

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Verify the extension installs correctly and is operational before documenting

**⚠️ CRITICAL**: No user story validation can succeed until the extension is installed

- [X] T002 Verify `pip install -r curso/requirements.txt` succeeds with jupyterlab-myst in a clean venv
- [X] T003 Verify `jupyter labextension list` shows jupyterlab-myst as enabled after install

**Checkpoint**: Foundation ready - extension is installed and active

---

## Phase 3: User Story 1 - Visualizar Markdown con formato completo (Priority: P1) 🎯 MVP

**Goal**: Opening `.md` files in JupyterLab renders GFM content (tables, code blocks, lists, links) correctly

**Independent Test**: Open `curso/capitulo-00-fundamentos/README.md` in JupyterLab and verify tables, code blocks, and lists render with proper formatting

### Implementation for User Story 1

- [X] T004 [US1] Update specs/001-curso-inversion-openbb/quickstart.md to document jupyterlab-myst extension and Markdown viewing instructions
- [X] T005 [US1] Validate Markdown rendering: open a course README in JupyterLab and confirm GFM elements render correctly (tables, code blocks, task lists)

**Checkpoint**: User Story 1 is functional — Markdown files render with full GFM formatting in JupyterLab

---

## Phase 4: User Story 2 - Renderizar diagramas Mermaid (Priority: P2)

**Goal**: Mermaid code blocks in Markdown files render as visual SVG diagrams in JupyterLab

**Independent Test**: Create a `.md` file with a ````mermaid` flowchart block, open in JupyterLab, verify SVG diagram appears

### Implementation for User Story 2

- [X] T006 [US2] Create curso/ejemplo-mermaid.md with sample Mermaid diagrams (flowchart, sequence) for verification
- [X] T007 [US2] Validate Mermaid rendering: open curso/ejemplo-mermaid.md in JupyterLab and confirm diagrams render as SVG

**Checkpoint**: User Story 2 is functional — Mermaid diagrams render visually in JupyterLab Markdown viewer

---

## Phase 5: User Story 3 - Instalación automática en setup (Priority: P3)

**Goal**: Running `./scripts/setup_env.sh` installs the extension automatically with no manual steps

**Independent Test**: Run `./scripts/setup_env.sh python3.11 .venv-test` in a fresh directory and confirm `jupyter labextension list` shows jupyterlab-myst enabled

### Implementation for User Story 3

- [X] T008 [US3] Verify scripts/setup_env.sh installs jupyterlab-myst automatically (no script changes needed — it already installs curso/requirements.txt)
- [X] T009 [US3] Add jupyterlab-myst import check to .github/workflows/ci-install-check.yml verify step
- [X] T010 [US3] Validate end-to-end: run setup_env.sh from scratch and confirm JupyterLab starts with extensions active

**Checkpoint**: User Story 3 is functional — full setup automation verified

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and CI updates

- [X] T011 [P] Update specs/003-jupyterlab-markdown-extensions/quickstart.md with final verification results
- [X] T012 Run quickstart.md validation to confirm all steps are accurate

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - add pip package to requirements
- **Foundational (Phase 2)**: Depends on Phase 1 — verifies the install works
- **User Stories (Phase 3-5)**: All depend on Phase 2 completion (extension installed)
  - US1, US2, US3 can proceed in priority order (sequential)
  - US1 and US2 are independent of each other (could run parallel)
  - US3 validates the automation that covers US1+US2
- **Polish (Phase 6)**: Depends on all user stories being verified

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 - No dependency on other stories
- **User Story 2 (P2)**: Can start after Phase 2 - No dependency on US1 (same extension provides both capabilities)
- **User Story 3 (P3)**: Can start after Phase 2 - Validates the end-to-end automation

### Within Each User Story

- Documentation/examples before validation
- Validation confirms the story acceptance criteria

### Parallel Opportunities

- T004 and T006 can run in parallel (different files, different stories)
- T005 and T007 can run in parallel (different validation targets)
- T009 and T011 can run in parallel (different files)

---

## Parallel Example: User Stories 1 & 2

```bash
# After Phase 2 (extension installed), launch both stories in parallel:

# User Story 1:
Task T004: "Update quickstart docs for Markdown viewing"
Task T005: "Validate Markdown rendering"

# User Story 2 (parallel):
Task T006: "Create ejemplo-mermaid.md with sample diagrams"
Task T007: "Validate Mermaid rendering"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Add jupyterlab-myst to requirements.txt
2. Complete Phase 2: Verify installation works
3. Complete Phase 3: Validate Markdown rendering
4. **STOP and VALIDATE**: GFM Markdown renders in JupyterLab
5. Merge if ready — Mermaid and automation are incremental additions

### Incremental Delivery

1. T001-T003 → Extension installed and verified (foundation)
2. T004-T005 → Markdown GFM rendering confirmed (MVP!)
3. T006-T007 → Mermaid diagrams confirmed (enhancement)
4. T008-T010 → Automation and CI verified (completeness)
5. T011-T012 → Documentation polished (final)

### Single Developer Strategy

Execute sequentially in task ID order (T001 → T012). The whole feature is achievable in a single implementation session given the minimal code changes required.

---

## Notes

- This feature requires only 1 new pip dependency (`jupyterlab-myst>=2.4`)
- No code logic changes to notebooks or scripts
- The existing `setup_env.sh` already installs from `curso/requirements.txt` — no script modifications needed
- Research confirmed `jupyterlab-myst` provides BOTH Markdown and Mermaid rendering (single package)
