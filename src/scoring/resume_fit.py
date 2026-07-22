from src.scoring.keyword_filter import keyword_matches

def resume_fit(job, settings):
    score = 0

    if job.title in settings["preferred_titles"]:
        score += 40

    salary = int(job.salary.replace("$", "").replace(",", ""))

    if salary >= settings["minimum_salary"]:
        score += 30

    if (
        job.location in settings["preferred_locations"]
        or job.work_arrangement in settings["preferred_work_arrangements"]
    ):
        score += 20

    matched_keywords = keyword_matches(job, settings)
    score += len(matched_keywords) * 2

    return min(score, 100)