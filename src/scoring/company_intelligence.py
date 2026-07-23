def company_intelligence(job):

    company = job.company.lower()

    if company == "anthropic":
        return {
            "size": "1,000+ employees",
            "type": "Private",
            "industry": "AI Safety",
            "priority": "High"
        }

    if company == "google":
        return {
            "size": "180,000+ employees",
            "type": "Public",
            "industry": "Technology",
            "priority": "High"
        }

    return {
        "size": "Unknown",
        "type": "Unknown",
        "industry": "Unknown",
        "priority": "Normal"
    }