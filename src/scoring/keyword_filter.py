def keyword_matches(job, settings):
    description = job.description.lower()

    matched_keywords = []

    for keyword in settings["keywords"]:
        if keyword.lower() in description:
            matched_keywords.append(keyword)

    return matched_keywords