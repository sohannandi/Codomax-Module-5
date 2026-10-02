"""AI Resume Analyzer — Module 5 mini project.

A command-line tool that analyzes a resume against a job description.
Currently uses a mock analysis function; designed to plug in a real LLM API.
"""

import os
import re
from typing import List, Set, Dict

# Optional: Uncomment and configure for real LLM usage
# Example for OpenAI:
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# Example for Gemini:
# import google.generativeai as genai
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_text_from_path(path: str) -> str:
    """Load text from a file; return empty string on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except (OSError, IOError):
        return ""

def extract_skills_mock(text: str) -> Set[str]:
    """
    Mock skill extraction: looks for keywords in a predefined skill set.
    Replace this with a real LLM call for production.
    """
    # A non-exhaustive skill dictionary for demonstration
    skill_keywords = {
        "programming": ["python", "java", "javascript", "typescript", "c++", "ruby", "go", "rust", "sql", "html", "css"],
        "data_science": ["machine learning", "deep learning", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "tableau", "power bi", "statistics"],
        "web_dev": ["react", "angular", "vue", "node.js", "express", "django", "flask", "rest", "graphql"],
        "cloud": ["aws", "azure", "gcp", "docker", "kubernetes", "terraform"],
        "soft": ["communication", "leadership", "teamwork", "problem solving", "project management", "agile", "scrum"]
    }

    found = set()
    text_lower = text.lower()
    for category, keywords in skill_keywords.items():
        for kw in keywords:
            # Simple word-boundary check (can be improved with regex)
            if re.search(rf"\\b{re.escape(kw)}\\b", text_lower):
                found.add(kw)
    return found

def analyze_resume_mock(resume_text: str, jd_text: str) -> Dict:
    """
    Perform mock analysis: extract skills, compute match/missing, suggest improvements.
    Returns a dictionary with structured results.
    """
    if not resume_text.strip():
        return {"error": "Resume text is empty."}
    if not jd_text.strip():
        return {"error": "Job description text is empty."}

    resume_skills = extract_skills_mock(resume_text)
    jd_skills = extract_skills_mock(jd_text)

    matching = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    extra = resume_skills - jd_skills

    match_score = len(matching) / len(jd_skills) if jd_skills else 0.0

    # Generate suggestions
    suggestions = []
    if missing:
        suggestions.append(f"Consider gaining experience in: {', '.join(sorted(missing))}.")
    if len(matching) < 3 and jd_skills:
        suggestions.append("Highlight transferable skills or relevant projects that align with the role.")
    if not extra:
        suggestions.append("Your resume shows strong alignment; consider adding quantifiable achievements.")
    else:
        suggestions.append(f"Your additional skills ({', '.join(sorted(extra))}) may be valuable for related roles.")

    return {
        "resume_skills": sorted(resume_skills),
        "jd_skills": sorted(jd_skills),
        "matching_skills": sorted(matching),
        "missing_skills": sorted(missing),
        "extra_skills": sorted(extra),
        "match_score": round(match_score, 2),
        "suggestions": suggestions
    }

def analyze_resume_llm(resume_text: str, jd_text: str) -> Dict:
    """
    Placeholder for real LLM analysis.
    Uncomment and implement one of the providers below.
    """
    # --- OPENAI EXAMPLE ---
    # try:
    #     prompt = f"""
    #     You are an expert career coach. Analyze the resume below against the job description.
    #     Provide:
    #     1. Skills extracted from the resume
    #     2. Skills required by the job description
    #     3. Matching skills
    #     4. Missing skills
    #     5. Improvement suggestions (bullet points)
    #     Format your answer as JSON with keys: resume_skills, jd_skills, matching_skills, missing_skills, suggestions (list of strings).
    #     Resume: \"\"\"{resume_text}\"\"\"
    #     Job Description: \"\"\"{jd_text}\"\"\"
    #     """
    #     response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[{"role": "user", "content": prompt}],
    #         temperature=0.2
    #     )
    #     content = response.choices[0].message["content"]
    #     # Expecting JSON; parse safely
    #     import json
    #     return json.loads(content)
    # except Exception as e:
    #     return {"error": f"LLM analysis failed: {e}"}
    #
    # --- GEMINI EXAMPLE ---
    # try:
    #     model = genai.GenerativeModel('gemini-pro')
    #     prompt = f"""
    #     Analyze the resume against the job description.
    #     Return JSON with keys: resume_skills (list), jd_skills (list), matching_skills (list), missing_skills (list), suggestions (list of strings).
    #     Resume: {resume_text}
    #     Job Description: {jd_text}
    #     """
    #     response = model.generate_content(prompt)
    #     import json
    #     return json.loads(response.text)
    # except Exception as e:
    #     return {"error": f"LLM analysis failed: {e}"}
    #
    # Fallback to mock if LLM not configured
    return analyze_resume_mock(resume_text, jd_text)

def main():
    print("=== AI Resume Analyzer (Module 5) ===\n")
    print("Choose input method:")
    print("1) Type/paste resume and job description")
    print("2) Load from sample files (data/sample_resume.txt, data/sample_jd.txt)")
    choice = input("Select 1 or 2: ").strip()

    if choice == "1":
        print("\n--- Enter resume text (end with an empty line) ---")
        resume_lines = []
        while True:
            line = input()
            if line == "":
                break
            resume_lines.append(line)
        resume_text = "\n".join(resume_lines)

        print("\n--- Enter job description (end with an empty line) ---")
        jd_lines = []
        while True:
            line = input()
            if line == "":
                break
            jd_lines.append(line)
        jd_text = "\n".join(jd_lines)

    elif choice == "2":
        resume_text = load_text_from_path("data/sample_resume.txt")
        jd_text = load_text_from_path("data/sample_jd.txt")
        if not resume_text:
            print("Warning: sample_resume.txt not found or empty.")
        if not jd_text:
            print("Warning: sample_jd.txt not found or empty.")
    else:
        print("Invalid choice.")
        return

    if not resume_text and not jd_text:
        print("No input provided. Exiting.")
        return

    # Use mock analysis (switch to LLM by commenting/uncommenting)
    result = analyze_resume_mock(resume_text, jd_text)
    # result = analyze_resume_llm(resume_text, jd_text)  # Uncomment to try real LLM

    if "error" in result:
        print(f"\nError: {result['error']}")
        return

    print("\n=== Analysis Results ===")
    print(f"Match Score: {result['match_score']*100:.0f}%")
    print(f"\nResume Skills ({len(result['resume_skills'])}): {', '.join(result['resume_skills']) or 'None'}")
    print(f"\nJob Description Skills ({len(result['jd_skills'])}): {', '.join(result['jd_skills']) or 'None'}")
    print(f"\nMatching Skills ({len(result['matching_skills'])}): {', '.join(result['matching_skills']) or 'None'}")
    print(f"\nMissing Skills ({len(result['missing_skills'])}): {', '.join(result['missing_skills']) or 'None'}")
    print(f"\nExtra Skills (in resume, not in JD): {', '.join(result['extra_skills']) or 'None'}")

    if result["suggestions"]:
        print("\n--- Suggestions ---")
        for i, s in enumerate(result["suggestions"], start=1):
            print(f"{i}. {s}")

    print("\nTip: To use a real LLM, obtain an API key, set it in .env, and uncomment the LLM section in app/main.py.")

if __name__ == "__main__":
    main()