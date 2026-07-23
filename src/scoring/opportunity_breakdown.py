from config.user_profile import SCORING_WEIGHTS


def opportunity_breakdown(resume_score, ats_score, company_fit_score):

    resume_points = resume_score * SCORING_WEIGHTS["resume"]
    ats_points = ats_score * SCORING_WEIGHTS["ats"]
    company_points = company_fit_score * SCORING_WEIGHTS["company_fit"]

    return {
        "resume": resume_points,
        "ats": ats_points,
        "company_fit": company_points,
        "total": round(
            resume_points +
            ats_points +
            company_points
        ),
    }