def salary_matches(job, settings):
    salary = int(job.salary.replace("$", "").replace(",", ""))

    return salary >= settings["minimum_salary"]