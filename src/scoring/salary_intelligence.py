def salary_intelligence(job):

    company = job.company.lower()

    if company == "anthropic":
        return "$210k–260k"

    if company == "google":
        return "$180k–240k"

    return "Unknown"