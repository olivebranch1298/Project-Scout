from src.search.job_factory import load_jobs
from src.utils.greeting import welcome


def main():
    welcome()

    jobs = load_jobs()

    print()

    for job in jobs:
        print(job)
        print()


if __name__ == "__main__":
    main()