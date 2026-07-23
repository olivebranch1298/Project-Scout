def explain(score, ats_score, missing_skills):

    reasons = []

    if score >= 90:
        reasons.append("Excellent resume alignment.")
    elif score >= 80:
        reasons.append("Good resume alignment.")
    else:
        reasons.append("Resume could be stronger.")

    if ats_score >= 50:
        reasons.append("Strong ATS compatibility.")
    else:
        reasons.append("ATS score could be improved.")

    if len(missing_skills) == 0:
        reasons.append("No important skills missing.")
    else:
        reasons.append(
            f"Missing {len(missing_skills)} skill(s)."
        )

    return reasons