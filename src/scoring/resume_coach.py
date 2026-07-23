def coach_resume(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if skill == "AI":
            suggestions.append(
                "Highlight AI or Generative AI projects."
            )

        elif skill == "SQL":
            suggestions.append(
                "Mention SQL experience in your Skills section."
            )

        elif skill == "Python":
            suggestions.append(
                "Include Python projects or automation work."
            )

        elif skill == "Security":
            suggestions.append(
                "Emphasize security or risk management experience."
            )

        elif skill == "Infrastructure":
            suggestions.append(
                "Highlight infrastructure or platform programs."
            )

        else:
            suggestions.append(
                f"Consider mentioning {skill} if you have experience."
            )

    if not suggestions:
        suggestions.append(
            "Your resume aligns well with this job."
        )

    return suggestions