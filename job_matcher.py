from difflib import SequenceMatcher

job_keywords = {
    "Software Developer": ["programming", "software development", "algorithms", "debugging", "object-oriented"],
    "Data Scientist": ["data analysis", "machine learning", "statistics", "python", "data mining"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "UI", "responsive design"],
    "Backend Developer": ["API", "database", "server", "Node.js", "Python", "Java"],
    "Full Stack Developer": ["frontend", "backend", "React", "Node.js", "full stack", "API"],
    "DevOps Engineer": ["CI/CD", "Docker", "Kubernetes", "AWS", "infrastructure", "automation"],
    "Machine Learning Engineer": ["ML", "deep learning", "TensorFlow", "scikit-learn", "AI"],
    "Data Analyst": ["Excel", "SQL", "data visualization", "Tableau", "PowerBI"],
    "Android Developer": ["Java", "Kotlin", "Android Studio", "mobile development"],
    "iOS Developer": ["Swift", "iOS", "Xcode", "Objective-C", "iPhone"],
    "Cybersecurity Analyst": ["cybersecurity", "network security", "ethical hacking", "vulnerabilities"],
    "Cloud Engineer": ["AWS", "Azure", "cloud architecture", "deployment", "GCP"]
}

def get_job_match_score(resume_data, job_profile):
    required_skills = job_keywords.get(job_profile, [])
    resume_text = " ".join([
        str(resume_data.get("name", "")),
        str(resume_data.get("email", "")),
        " ".join(map(str, resume_data.get("skills") or [])),
        " ".join(map(str, resume_data.get("experience") or [])),
        " ".join(map(str, resume_data.get("education") or [])),
    ])

    matched_keywords = [skill for skill in required_skills if skill.lower() in resume_text.lower()]
    score = int((len(matched_keywords) / len(required_skills)) * 100) if required_skills else 0

    return {
        "score": score,
        "matched_keywords": matched_keywords,
        "required_keywords": required_skills
    }
