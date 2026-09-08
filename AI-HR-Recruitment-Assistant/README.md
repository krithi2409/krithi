# AI HR Recruitment Assistant

An AI-powered recruitment assistant for resume analysis, job analysis,
candidate-job matching, interview question generation and recruitment analytics.

## Key Agent Capabilities

- Resume Analysis Agent
- Job Description Analysis Agent
- Candidate Matching Agent
- Interview Assistant Agent
- Recruitment Memory Agent
- RAG document retrieval
- SQLite recruitment database
- Local LLM with Ollama

## Architecture

HR User -> Flask App -> Recruitment Orchestrator -> Specialized Agents
-> RAG / Tools / SQLite -> Ollama

## Installation

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Install/run Ollama and pull the model:
```bash
ollama pull llama3.2
ollama run llama3.2
```

Start:
```bash
python app.py
```

Open http://127.0.0.1:5000

## GitHub

```bash
git init
git add .
git commit -m "Initial AI HR Recruitment Assistant"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Note

This academic prototype is intended to assist HR professionals.
Final employment decisions should remain under human review and should
use job-relevant qualifications only.
