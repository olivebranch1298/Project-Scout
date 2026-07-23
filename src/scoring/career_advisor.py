def career_advice(
    recommendation,
    resume_score,
    ats_score,
    company_fit_score,
    missing_skills,
):

    advice = []

    if "Apply" in recommendation:
        advice.append("This role is worth applying to.")

    elif "Maybe" in recommendation:
        advice.append("Apply if you're genuinely interested.")

    else:
        advice.append("Your time is probably better spent elsewhere.")

    if resume_score >= 90:
        advice.append("Your resume already aligns well.")

    if ats_score < 60:
        if missing_skills:
            advice.append(
                f"Consider adding these skills if you have them: {', '.join(missing_skills)}."
            )
        else:
            advice.append("No major ATS improvements are needed.")

    if company_fit_score >= 85:
        advice.append("This company aligns well with your preferences.")

    return advice
