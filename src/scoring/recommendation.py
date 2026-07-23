def recommend(resume_score, ats_score):

    if resume_score >= 90 and ats_score >= 50:
        return "🟢 Strong Apply"

    elif resume_score >= 80:
        return "🟡 Apply"

    elif resume_score >= 70:
        return "🟠 Maybe"

    else:
        return "🔴 Skip"