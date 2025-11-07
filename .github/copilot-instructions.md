# Copilot Instructions: Helsinki Python MOOC 2025

## Project Overview

This is a personal learning repository for the **University of Helsinki Python Programming MOOC 2025**, a 14-part course divided into two sections:

- **Introduction to Programming** (Parts 01-07)
- **Advanced Course in Programming** (Parts 08-14)

Expected workload: ~10-20 hours/week per part.

## Repository Structure

```
helsinki/
├── README.md                    # Main progress tracker with course outline
├── Pipfile                      # Python dependencies (Python 3.9)
├── IntroductionToProgramming/
│   └── Part{NN}/
│       ├── slides/              # Course slides PDFs
│       └── section{NN}_topic/   # Sections organized by topic
│           └── exercises/       # Python exercise files
├── AdvancedCourse/              # Parts 08-14 (same structure)
│   └── Part{NN}/
│       ├── slides/
│       └── section{NN}_topic/
│           └── exercises/
└── .vscode/
    └── settings.json            # Peacock color customization
```

**Example structure:**

- `IntroductionToProgramming/Part01/section01_getting_started/exercises/01_emoticon.py`
- `IntroductionToProgramming/Part01/section05_conditional_statements/exercises/`

## Workflow Conventions

### Branch Strategy

- `main`: Stable progress checkpoint
- `part{NN}`: Working branch for each course part (e.g., `part01`, `part02`)
- Create a new branch when starting each part: `git checkout -b part01`

### Progress Tracking

- Update README.md checklist (`- [ ]` → `- [x]`) after completing each part
- Add notes under the relevant `### Part {NN}` section in README.md
- All learning notes stay in the top-level README.md (not in separate files)

### Organization Patterns

- Store course materials in `{Section}/Part{NN}/slides/`
- Exercises organized by topic: `{Section}/Part{NN}/section{NN}_topic_name/exercises/`
- Keep part numbers zero-padded (Part01, not Part1)
- Section names use snake_case (e.g., `section01_getting_started`, `section05_conditional_statements`)
- Sections: `IntroductionToProgramming/` (Parts 01-07), `AdvancedCourse/` (Parts 08-14)
- Python version: 3.9 (managed via Pipfile)

## Key Context for AI Agents

**This is a learning/study repository, not a software project.** When asked to help:

- Focus on explaining concepts, not just providing solutions
- Reference official course materials when relevant
- Suggest learning resources for Python fundamentals
- Help organize notes and track progress through the course structure
- Avoid over-engineering—keep solutions simple and educational
- This is for individual learning, not shared with study groups

**Common tasks:**

- Updating progress checklist in README.md
- Creating/organizing note sections for new parts
- Explaining Python concepts covered in the course
- Helping debug learning exercises (guide, don't solve)

## VS Code Configuration

The workspace uses the Peacock extension with teal theming (`#27ada1`) to visually distinguish this project.
