from ollama_service import generate_response

def analyze_job_description(job_description):
    prompt = f"""You are an AI Job Description Analysis Agent.
Analyze:
{job_description}
Identify job title, required skills, preferred skills, required experience,
education, responsibilities and important keywords."""
    return generate_response(prompt)
