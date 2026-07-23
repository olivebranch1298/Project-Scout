# TODO (Sprint 15):
# Replace this rule-based keyword extractor with an LLM-based
# skill extraction engine. The current implementation only finds
# exact string matches from COMMON_SKILLS and will miss many
# equivalent or related skills.

COMMON_SKILLS = [
    "Python",
    "SQL",
    "AI",
    "Machine Learning",
    "Security",
    "Identity",
    "Infrastructure",
    "Kubernetes",
    "Terraform",
    "AWS",
    "Azure",
    "GCP",
    "Program Management",
    "Technical Program Management",
    "Automation",
    "Risk Management",
    "Trust & Safety",
]

def extract_skills(job):

    description = job.description.lower()

    found = []

    for skill in COMMON_SKILLS:
        if skill.lower() in description:
            found.append(skill)

    return found 