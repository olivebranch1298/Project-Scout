def analyze_skill_gap(job_skills, profile):

    matched = []
    missing = []

    profile_skills = profile["skills"]

    for skill in job_skills:
        if skill in profile_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing