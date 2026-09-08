def calculate_candidate_score(required_skills, candidate_skills,
                              required_experience, candidate_experience):
    required = {s.strip().lower() for s in required_skills.split(",") if s.strip()}
    candidate = {s.strip().lower() for s in candidate_skills.split(",") if s.strip()}
    skill_score = (len(required & candidate) / len(required) * 70) if required else 0
    try:
        req, cand = float(required_experience), float(candidate_experience)
        exp_score = min(cand / req, 1) * 30 if req > 0 else 30
    except ValueError:
        exp_score = 0
    return round(skill_score + exp_score, 2)

def get_candidate_status(score):
    if score >= 75: return "Shortlisted"
    if score >= 50: return "Review"
    return "Rejected"
