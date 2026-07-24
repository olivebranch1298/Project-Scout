import json
from pathlib import Path

JOBS_FILE = Path("data/tracked_jobs.json")


def load_jobs():
    """Load all tracked jobs from disk."""

    if not JOBS_FILE.exists():
        return []

    with open(JOBS_FILE, "r") as f:
        return json.load(f)

def save_jobs(jobs):
    """Save all tracked jobs to disk."""

    JOBS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(JOBS_FILE, "w") as f:
        json.dump(jobs, f, indent=4)

def add_job(job_record):
    """Add a new job record to the tracker if it doesn't already exist."""

    jobs = load_jobs()

    for i, job in enumerate(jobs):
        if (
            job["company"] == job_record["company"]
            and job["title"] == job_record["title"]
        ):
            
            jobs[i] = job_record
            save_jobs(jobs)
            return

    jobs.append(job_record)
    save_jobs(jobs)