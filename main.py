from src.search.job_factory import load_jobs
from src.utils.greeting import welcome
from src.config_loader import load_settings
from src.scoring.evaluator import evaluate_job
from src.scoring.resume_fit import resume_fit
from src.scoring.ats_fit import ats_fit
from src.profile_loader import load_profile
from src.parsers.skill_extractor import extract_skills
from src.scoring.skill_gap import analyze_skill_gap
from src.scoring.recommendation import recommend
from src.scoring.salary_filter import salary_matches
from src.scoring.location_filter import location_matches
from src.scoring.skill_matcher import compare_skills
from src.scoring.explanation import explain

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
        recommendation = recommend(score, ats_score)

        job_skills = extract_skills(job)

        matched_job_skills, missing_job_skills = analyze_skill_gap(
            job_skills,
            profile
        )
        reasons = explain(
            score,
            ats_score,
            missing_job_skills
        )
        results.append(
            (
                score,
                ats_score,
                recommendation,
                job,
                passed,
                reasons,
            )
        )

        print(f"Resume Fit: {score}/100")
        print(f"ATS Fit: {ats_score}/100")
        print("Recommendation:", recommendation)
        print("Job Skills:", job_skills)
        print("Qualified:", matched_job_skills)
        print("Missing:", missing_job_skills)
        print("Explanation:")
        for reason in reasons:
            print(".", reason )

    results.sort(reverse=True)

    print("🏆 Ranked Jobs")
    print("----------------")

    for score, ats_score, recommendation, job, passed, reasons in results:
        print(
            f"{recommendation} | "
            f"Resume {score}/100 | "
            f"ATS {ats_score}/100 | "
            f"{job.company} | "
            f"{job.title}"
        )


if __name__ == "__main__":
    main()