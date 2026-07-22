from src.search.job_factory import load_jobs
from src.utils.greeting import welcome
from src.config_loader import load_settings
from src.scoring.salary_filter import salary_matches
from src.scoring.location_filter import location_matches
from src.scoring.evaluator import evaluate_job
from src.scoring.resume_fit import resume_fit


def main():
    welcome()

    settings = load_settings()

    print()
    print("User Settings")
    print(settings)

    jobs = load_jobs()

    print()

    for job in jobs:
        passed, reasons = evaluate_job(job, settings)
        score = resume_fit(job, settings)
        print(f"Resume Fit: {score}/100")
        if passed:
            print("✅", job.company)
        else:
            print("❌", job.company)

        for reason in reasons:
            print("   •", reason)

        print()


if __name__ == "__main__":
    main()