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
from src.scoring.keyword_suggestions import suggest_keywords
from src.scoring.opportunity_score import opportunity_score
from src.utils.job_card import print_job_card
from src.scoring.resume_suggestions import suggest_resume_improvements
from src.scoring.prioritize_resume import prioritize_resume
from src.scoring.prioritize_resume import prioritize_resume
from src.scoring.resume_coach import coach_resume
from src.scoring.company_intelligence import company_intelligence
from src.scoring.salary_intelligence import salary_intelligence
from src.scoring.company_fit import company_fit 
from src.scoring.opportunity_breakdown import opportunity_breakdown
from src.scoring.career_advisor import career_advice
from src.tracker.jobs import add_job
from datetime import date

def main():
    welcome()

    settings = load_settings()
    profile = load_profile()
    jobs = load_jobs()

    results = []

    for job in jobs:

        #Evaluate the job
        passed, reasons = evaluate_job(job, settings)

        #Calculate scores
        score = resume_fit(job, settings)
        ats_score = ats_fit(job, settings)

        company_info = company_intelligence(job) 
        company_fit_score = company_fit(company_info)

        overall_score = opportunity_score(
            score,
            ats_score,
            company_fit_score,
        )   

        breakdown = opportunity_breakdown(
            score,
            ats_score,
            company_fit_score,
        )

        salary = salary_intelligence(job)

        #Figure out recommendation
        recommendation = recommend(overall_score, ats_score)


        #Extract skills
        job_skills = extract_skills(job)

        #Compare skills
        matched_job_skills, missing_job_skills = analyze_skill_gap(
            job_skills,
            profile
        )

        #Provide career advice and suggestions based on the scores and missing skills
        advice = career_advice(
            recommendation,
            score,
            ats_score,
            company_fit_score,
            missing_job_skills
        )

        #Resume Suggestions
        resume_suggestions = coach_resume(
            missing_job_skills
        )

        #Prioritize the resume
        high_priority, medium_priority, low_priority = prioritize_resume(
            resume_suggestions
        )

        keyword_suggestions = suggest_keywords(
          missing_job_skills
       ) 
        reasons = explain(
            score,
            ats_score,
            missing_job_skills
        )
        results.append(
            (
                overall_score,
                score,
                ats_score,
                recommendation,
                job,
                passed,
                reasons,
            )
        )

        print_job_card(
            job,
            recommendation,
            overall_score,
            breakdown,
            advice,
            score,
            ats_score,
            matched_job_skills,
            missing_job_skills,
            keyword_suggestions,
            resume_suggestions,
            reasons,
            company_info,
            company_fit_score,
            salary,
)
        
        job_record = {
            "company": job.company,
            "title": job.title,
            "date_scored": str(date.today()),
            "recommendation": recommendation,
            "opportunity": overall_score,
            "resume_fit": score,
            "ats_fit": ats_score,
            "company_fit": company_fit_score,
            "salary": salary,
            "matched_skills": matched_job_skills,
            "missing_skills": missing_job_skills,
            "status": "Wishlist",
        }

        add_job(job_record)
        
    results.sort(reverse=True)

    print("🏆 Ranked Jobs")
    print("----------------")

    for overall_score, score, ats_score, recommendation, job, passed, reasons in results:
        print(
            f"{recommendation} | "
            f"Opportunity {overall_score}/100 | "
            f"Resume {score}/100 | "
            f"ATS {ats_score}/100 | "
            f"{job.company} | "
            f"{job.title}"
        )


if __name__ == "__main__":
    main()