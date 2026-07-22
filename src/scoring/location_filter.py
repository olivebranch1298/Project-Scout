def location_matches(job, settings):
    return job.location in settings["preferred_locations"]
