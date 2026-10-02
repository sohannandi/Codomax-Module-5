# Module 5 — AI Tool Experimentation Notes

## Overview

This document records my exploration of three AI productivity tools:
- ChatGPT
- Google Gemini
- Microsoft Copilot

For each tool, I tested practical workflows: code generation, debugging, documentation, research assistance, brainstorming, and productivity.

---

## 1. ChatGPT

### Tasks tested
- Generate Python code for a resume analyzer
- Debug a loop that caused an infinite loop
- Write a README and user instructions
- Brainstorm project ideas and features

### Prompt / workflow
> "Build a Python command-line resume analyzer that extracts skills from a resume and compares them with a job description. Return a structured result with matching skills, missing skills, and suggestions."

### Result
ChatGPT produced a clean scaffold with:
- A `main.py` entry point
- Skill extraction using keyword matching
- Set operations for matching/missing skills
- A prompt template for an LLM API

### What was useful
- Very fast at scaffolding code
- Good at explaining trade-offs
- Helpful for writing documentation

### Limitations / verification
- The generated regex initially double-escaped word boundaries, which could miss matches. I verified by running the script and fixed it with a proper boundary pattern.
- I did not accept code blindly; I reviewed it for security (no API keys, safe file handling) and correctness.

---

## 2. Google Gemini

### Tasks tested
- Summarize a long resume
- Suggest missing skills for a job description
- Generate a JSON schema for the analysis output

### Prompt / workflow
> "Analyze the following resume against the job description. Return JSON with keys: resume_skills, jd_skills, matching_skills, missing_skills, suggestions."

### Result
Gemini returned a reasonable JSON structure with:
- Skills lists
- A confidence score
- Actionable suggestions

### What was useful
- Strong summarization
- Good at producing structured JSON

### Limitations / verification
- Sometimes the JSON was malformed (missing commas or trailing commas). I validated the output with `json.loads()` and asked it to retry when parsing failed.
- I compared its output against the mock analyzer to sanity-check the results.

---

## 3. Microsoft Copilot

### Tasks tested
- Explain a Python function
- Suggest a better name for a variable
- Write a unit test for `analyze_resume()`

### Prompt / workflow
> "Explain what this function does and suggest a clearer name for the variable `jd_skills`."

### Result
Copilot provided:
- A concise explanation
- A more descriptive variable name
- A basic test using `assert`

### What was useful
- Integrated well with the editor
- Fast at small refactorings

### Limitations / verification
- Suggestions were sometimes generic. I verified the refactor by running the program.
- I kept the final code decision myself rather than accepting every suggestion.

---

## 4. Cross-tool observations

| Capability | ChatGPT | Gemini | Copilot |
|------------|---------|--------|---------|
| Code generation | Excellent | Good | Good |
| Debugging | Excellent | Good | Good |
| Summarization | Good | Excellent | Moderate |
| Structured output | Good | Excellent | Moderate |
| Editor integration | Moderate | Moderate | Excellent |

### Key lessons
1. **AI accelerates scaffolding, not judgment.** I still reviewed every line of code.
2. **Prompt specificity matters.** Asking for JSON with an exact schema produced much better results.
3. **Always verify.** I ran the code, checked edge cases, and tested with empty input.
4. **Security first.** I never put API keys in code; I used environment variables and `.gitignore`.

---

## 5. Verification performed

- Ran the mock analyzer with sample input
- Tested empty resume / empty job description
- Checked that no secrets were hard-coded
- Confirmed `.env` is excluded from git
- Reviewed generated code for correctness before committing
