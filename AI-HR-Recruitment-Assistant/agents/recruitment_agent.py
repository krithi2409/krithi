from agents.resume_agent import analyze_resume
from agents.job_agent import analyze_job_description
from agents.matching_agent import match_candidate_to_job
from agents.interview_agent import generate_interview_questions

def recruitment_agent(action, data):
    if action == "resume":
        return analyze_resume(data)
    if action == "job":
        return analyze_job_description(data)
    if action == "match":
        return match_candidate_to_job(data["resume"], data["job"])
    if action == "interview":
        return generate_interview_questions(data["job_title"], data["skills"])
    return "Unknown recruitment action."
