from src.search.job_factory import load_jobs
from src.utils.greeting import welcome
from src.config_loader import load_settings
from src.scoring.salary_filter import salary_matches
from src.scoring.location_filter import location_matches
from src.scoring.evaluator import evaluate_job
from src.scoring.resume_fit import resume_fit
from src.scoring.ats_fit import ats_fit
from src.profile_loader import load_profile
from src.scoring.skill_matcher import compare_skills


def main():
    welcome()

    settings = load_settings()
    profile = load_profile()
    jobs = load_jobs()

    results = []

    for job in jobs:
        passed, reasons = evaluate_job(job, settings)
        score = resume_fit(job, settings)
        ats_score = ats_fit(job, settings)
        matched, missing = compare_skills(job, profile)
        print("Matched Skills:", matched)
        results.append((score, job, passed, reasons))

        print(f"Resume Fit: {score}/100")
        print(f"ATS Fit: {ats_score}/100")

    print()

    results.sort(reverse=True)

    print("🏆 Ranked Jobs")
    print("----------------")

    for score, job, passed, reasons in results:
        print(f"{score}/100 - {job.company} - {job.title}")

if __name__ == "__main__":
    main()