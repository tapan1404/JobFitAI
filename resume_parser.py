from pyresparser import ResumeParser
import nltk
nltk.data.path.append('./nltk_data')

# Dictionary of required skills for various job profiles
job_profile_skills = {
    "data scientist": {"python", "machine learning", "data analysis", "statistics", "pandas", "numpy"},
    "frontend developer": {"html", "css", "javascript", "react", "redux"},
    "backend developer": {"python", "django", "flask", "sql", "api"},
    "fullstack developer": {"html", "css", "javascript", "react", "nodejs", "express", "mongodb", "sql"},
    "software engineer": {"c++", "java", "python", "dsa", "oops", "problem solving"},
    # Add more profiles and skills as needed
}

def parse_resume(filepath):
    data = ResumeParser(filepath).get_extracted_data()
    return data

def score_resume(resume_data, job_profile):
    resume_skills = set(map(str.lower, resume_data.get("skills", [])))
    required_skills = job_profile_skills.get(job_profile.lower(), set())

    if not required_skills:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "message": f"No skill template found for job profile '{job_profile}'"
        }

    matched_skills = resume_skills & required_skills
    missing_skills = required_skills - resume_skills
    score = int(len(matched_skills) / len(required_skills) * 100)

    return {
        "score": score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "message": "Score calculated successfully"
    }
