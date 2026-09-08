from database import get_candidates

def get_recruitment_memory():
    return [
        {"id": c[0], "name": c[1], "score": c[6], "status": c[7]}
        for c in get_candidates()
    ]

def get_shortlisted_candidates():
    return [c for c in get_candidates() if c[7] == "Shortlisted"]
