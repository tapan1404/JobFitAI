def calculate_score(resume_data, job_title):
    # Pre-defined job skills (mock data — can expand later)
    job_skills_map = {
        "frontend developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
        "data scientist": ["Python", "Pandas", "Machine Learning", "Statistics", "SQL"],
        "backend developer": ["Python", "Django", "Flask", "SQL", "REST APIs"]
    }

    expected_skills = job_skills_map.get(job_title.lower(), [])
    resume_skills = resume_data.get("skills", [])

    # Normalize skills
    matched = [skill for skill in resume_skills if skill.lower() in [s.lower() for s in expected_skills]]
    match_percent = round((len(matched) / len(expected_skills)) * 100, 2) if expected_skills else 0
    missing = list(set(expected_skills) - set([s.lower() for s in resume_skills]))

    return {
        "match_percent": match_percent,
        "matched_skills": matched,
        "missing_skills": missing
    }
