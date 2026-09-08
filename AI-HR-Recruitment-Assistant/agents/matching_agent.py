from ollama_service import generate_response

def match_candidate_to_job(resume_text, job_description):
    prompt = f"""You are an AI Candidate Matching Agent.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Evaluate skill match, experience match, education match and project relevance.
Give Match Score out of 100, strengths, missing skills and recommendation:
Shortlist / Review / Reject.

Use only job-relevant qualifications. Do not consider protected characteristics."""
    return generate_response(prompt)
