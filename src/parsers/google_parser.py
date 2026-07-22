from src.models.job import Job


def parse_google_job(job_data):
    return Job(
        company=job_data["company"],
        title=job_data["title"],
        location=job_data["location"],
        work_arrangement=job_data["work_arrangement"],
        salary=job_data["salary"],
        requirements=job_data["requirements"],
        preferred_qualifications=job_data["preferred_qualifications"],
        description=job_data["description"],
        url=job_data["url"],
    )