from ollama_service import generate_response

def generate_interview_questions(job_title, candidate_skills):
    prompt = f"""You are an AI Interview Assistant.
Job: {job_title}
Candidate skills: {candidate_skills}
Generate exactly 10 questions:
4 technical, 3 experience-based, 2 problem-solving and 1 behavioral.
Keep questions job-related."""
    return generate_response(prompt)
