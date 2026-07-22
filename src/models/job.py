from dataclasses import dataclass


@dataclass
class Job:
    company: str
    title: str
    location: str
    work_arrangement: str
    salary: str
    requirements: str
    preferred_qualifications: str
    description: str
    url: str