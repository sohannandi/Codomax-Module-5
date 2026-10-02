# Module 5 — AI Tools & Mini Project: AI Resume Analyzer

## Overview

This project explores AI productivity tools (ChatGPT, Gemini, Microsoft Copilot) and builds a simple AI-powered Resume Analyzer. The analyzer:
- Takes a resume and job description as input
- Uses an LLM (or a mock function) to extract skills, compute match, and suggest improvements
- Demonstrates prompt engineering and AI-assisted development

This satisfies Module 5 requirements:
1. Experiment with AI tools and document findings
2. Build a functional AI-powered mini project
3. Share learning and project on LinkedIn

## Project Structure

```text
Module-5-AI-Mini-Project/
├── app/
│   └── main.py                # Core application logic
├── data/
│   ├── sample_resume.txt      # Example resume (optional)
│   └── sample_jd.txt          # Example job description (optional)
├── screenshots/               # Placeholder for UI screenshots
├── ai_experiment_notes.md     # Notes on AI tool exploration
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Features

- **Input:** Accept resume text (string or file) and job description
- **AI Processing:** 
  - Mock analysis: keyword-based skill extraction & matching (replace with real LLM)
  - Placeholder for calling ChatGPT/Gemini API via environment variable
- **Output:** Structured results:
  - Skills found in resume
  - Skills required by job description
  - Matching skills
  - Missing skills
  - Improvement suggestions
- **Error Handling:** Validates input, handles missing files/API failures gracefully
- **Security:** No hard-coded secrets; uses `.env` for API keys (see `.env.example`)

## How the Mock Analysis Works

The current `analyze_resume()` function in `app/main.py` uses:
1. Skill keyword lists (hard-coded for demo)
2. Simple set operations to find matches/gaps
3. Heuristic suggestions based on missing skills

To use a real LLM:
1. Sign up for an API key (OpenAI, Gemini, etc.)
2. Add it to a `.env` file (see `.env.example`)
3. Uncomment the LLM call in `main.py` and implement the prompt

## Setup & Usage

### Prerequisites
- Python 3.7+
- (Optional) `openai` or `google-generativeai` packages if using real LLM

### Installation
```bash
# Clone this repository
git clone <your-repo-url>
cd Module-5-AI-Mini-Project

# Install dependencies (only needed for real LLM)
pip install -r requirements.txt
```

### Running the Demo (Mock Analysis)
```bash
python app/main.py
```

Follow the prompts to enter resume text and job description (or use sample files).

### Using a Real LLM (Optional)
1. Copy `.env.example` to `.env`
2. Add your API key (e.g., `OPENAI_API_KEY=sk-...`)
3. Uncomment the LLM section in `app/main.py`
4. Adjust the prompt and model as needed
5. Run `python app/main.py`

## AI Tool Experimentation Notes

See [ai_experiment_notes.md](ai_experiment_notes.md) for:
- Tools explored: ChatGPT, Gemini, Microsoft Copilot
- Prompts/workflows tried
- What was useful
- Limitations and verification performed

## Security

- Never commit API keys
- `.env` is listed in `.gitignore`
- Provide `.env.example` as a template
- Validate all inputs (file paths, empty strings)

## Sample Data

The `data/` folder contains sample resume and job description files for quick testing.

## Submission

- GitHub repository link: **[PASTE LINK AFTER PUSHING]**
- LinkedIn post link: **[PASTE LINK AFTER POSTING]**

## Next

Proceed to **Module 6: Final AI & ML Project** (you can extend this analyzer or build a new end-to-end application).