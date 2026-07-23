def suggest_resume_improvements(
    matched_skills,
    missing_skills,
    resume_score,
):
    suggestions = []

    if resume_score < 95:
        suggestions.append("Quantify achievements with metrics.")

    if missing_skills:
        suggestions.append(
            f"Highlight experience related to: {', '.join(missing_skills)}"
        )

    if not matched_skills:
        suggestions.append(
            "Tailor your resume more closely to this role."
        )

    if not suggestions:
        suggestions.append("Your resume is already well aligned.")

    return suggestions