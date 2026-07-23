from config.user_profile import SCORING_WEIGHTS


def opportunity_score(resume_score, ats_score, company_fit_score):    

    """
    Overall opportunity score.

    Resume Fit is currently weighted more heavily because
    it better represents recruiter interest.

    Later we can add:
    - salary
    - posting age
    - company preference
    - remote preference
    """

    score = (
        resume_score * SCORING_WEIGHTS["resume"] +
        ats_score * SCORING_WEIGHTS["ats"] +
        company_fit_score * SCORING_WEIGHTS["company_fit"]
    )

    return round(score)