def prioritize_resume(resume_suggestions):

    high = []
    medium = []
    low = []

    for suggestion in resume_suggestions:

        text = suggestion.lower()

        if "ai" in text or "security" in text or "infrastructure" in text:
            high.append(suggestion)

        elif "sql" in text or "python" in text:
            medium.append(suggestion)

        else:
            low.append(suggestion)

    return high, medium, low