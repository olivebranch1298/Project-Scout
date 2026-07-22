def title_matches(job, settings):
    job_title = job.title.lower()

    for title in settings["preferred_titles"]:
        if title.lower() in job_title:
            return True

    return False