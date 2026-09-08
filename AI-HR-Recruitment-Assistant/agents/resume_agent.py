from ollama_service import generate_response

def analyze_resume(resume_text):
    prompt = f"""You are an AI Resume Analysis Agent.
Analyze this resume:
{resume_text}
Extract: candidate name, email, phone, technical skills, soft skills,
education, work experience, projects and certifications.
Use only information present in the resume. Return a clear structured summary."""
    return generate_response(prompt)
