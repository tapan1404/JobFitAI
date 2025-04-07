def get_job_match_score(resume_data, job_profile):
    job_keywords = {
        "Data Scientist": ["python", "machine learning", "statistics", "data analysis", "pandas", "numpy"],
        "Web Developer": ["html", "css", "javascript", "react", "node.js", "frontend", "backend"],
        "Android Developer": ["kotlin", "java", "android studio", "xml", "firebase"],
        "Software Engineer": ["c++", "java", "python", "data structures", "algorithms", "system design"],
        "DevOps Engineer": ["docker", "kubernetes", "aws", "jenkins", "linux", "ci/cd", "terraform"],
        "UI/UX Designer": ["figma", "adobe xd", "sketch", "wireframing", "prototyping", "user research"],
        "Cloud Engineer": ["aws", "azure", "gcp", "cloud infrastructure", "virtualization"],
        "Database Administrator": ["sql", "oracle", "mysql", "mongodb", "database management", "backup"],
        "AI/ML Engineer": ["deep learning", "tensorflow", "pytorch", "nlp", "cv", "python"],
        "Cybersecurity Analyst": ["network security", "vulnerability assessment", "firewall", "threat detection"],
        "Product Manager": ["agile", "scrum", "roadmap", "jira", "user stories", "market research"],
        "Business Analyst": ["requirement gathering", "excel", "sql", "power bi", "data analysis", "communication"]
    }

    required_skills = job_keywords.get(job_profile, [])
    resume_skills = [skill.lower() for skill in resume_data.get('skills', [])]

    matched_skills = list(set(required_skills).intersection(set(resume_skills)))
    missing_skills = list(set(required_skills) - set(matched_skills))

    score = int((len(matched_skills) / len(required_skills)) * 100) if required_skills else 0

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
