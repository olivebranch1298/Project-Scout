from src.scoring.keyword_filter import keyword_matches
from src.scoring.title_filter import title_matches


def ats_fit(job, settings):
    score = 0

    matched_keywords = keyword_matches(job, settings)
    score += len(matched_keywords) * 10

    if title_matches(job, settings):
        score += 30

    return min(score, 100)