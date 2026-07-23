from config.user_profile import USER_PROFILE

def company_fit(company_info):

    score = 100

    if company_info["priority"] != "High":
        score -= 10

    if USER_PROFILE["preferred_company_size"] == "Enterprise":
        if company_info["size"] != "Enterprise":
            score -= 15

    industry_match = False

    for preferred in USER_PROFILE["preferred_industries"]:
        if preferred.lower() in company_info["industry"].lower():
            industry_match = True
            break

    if not industry_match:
        score -= 10

    return score