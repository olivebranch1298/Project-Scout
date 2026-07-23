def suggest_keywords(missing_skills):

    if len(missing_skills) == 0:
        return []

    return sorted(missing_skills)