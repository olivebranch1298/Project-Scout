def compare_skills(job, profile):

    matched = []
    missing = []

    description = job.description.lower()

    for skill in profile["skills"]:

        if skill.lower() in description:
            matched.append(skill)

    return matched, missing