import json

from src.parsers.google_parser import parse_google_job


def load_jobs():
    with open("data/jobs.json", "r") as file:
        jobs_data = json.load(file)

    for i, job in enumerate(jobs_data):
        print(f"Loaded {len(jobs_data)} jobs")

    return [parse_google_job(job) for job in jobs_data]