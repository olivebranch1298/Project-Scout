def print_job_card(
    job,
    recommendation,
    opportunity,
    resume,
    ats,
    matched,
    missing,
    suggestions,
    resume_suggestions,
    reasons,
):
    print("=" * 60)

    print(job.company)
    print(job.title)
    print()

    print(f"Recommendation: {recommendation}")
    print(f"Opportunity Score: {opportunity}/100")
    print(f"Resume Fit: {resume}/100")
    print(f"ATS Fit: {ats}/100")

    print()

    print("Matched Skills:")
    print(matched if matched else "None")

    print()

    print("Missing Skills:")
    print(missing if missing else "None")

    print()

    print("Suggested Resume Keywords:")
    print(suggestions if suggestions else "None")

    print()

    print("Resume Suggestions:")

    if resume_suggestions:
        for suggestion in resume_suggestions:
            print(f"• {suggestion}")
    else:
        print("None")

    print()

    print("Why:")

    for reason in reasons:
        print(f"• {reason}")

    print("=" * 60)
    print()