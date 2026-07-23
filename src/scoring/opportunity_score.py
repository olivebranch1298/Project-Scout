def opportunity_score(resume_score, ats_score):
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
        resume_score * 0.7 +
        ats_score * 0.3
    )

    return round(score)