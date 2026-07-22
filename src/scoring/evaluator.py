from src.scoring.salary_filter import salary_matches
from src.scoring.location_filter import location_matches
from src.scoring.title_filter import title_matches 
from src.scoring.keyword_filter import keyword_matches

def evaluate_job(job, settings):
    reasons = []

    if salary_matches(job, settings):
        reasons.append("Salary matches")
    else:
        reasons.append("Salary too low")

    if location_matches(job, settings):
        reasons.append("Location matches")
    else:
        reasons.append("Wrong location")
    if title_matches(job, settings):
        reasons.append("Title matches")
    else:
        reasons.append("Title doesn't match")

    matched_keywords = keyword_matches(job, settings)

    if matched_keywords:
        reasons.append(
            "Keywords matched: " + ", ".join(matched_keywords)
    )
    else:
     reasons.append("No preferred keywords found")  
    passed = (
        salary_matches(job, settings)
        and location_matches(job, settings)
        and title_matches(job, settings)
    )

    return passed, reasons